<!-- Q: 사내 관리자 페이지에 역할 기반 권한(관리자/편집자/뷰어)을 추가하는 구현 계획을 써줘. 백엔드는 Django야. -->

**Django 내장 Group + Permission으로 구현하는 걸 추천해요.** 역할 3개는 Group 3개로 충분하고, 별도 Role 모델은 필요 없어요. 가정: 지금 페이지는 Django admin이거나 `View` 기반 커스텀 뷰예요. 다르면 알려 주세요.

## 역할별 권한

| 역할 | view | add | change | delete |
|---|---|---|---|---|
| 뷰어 | O | X | X | X |
| 편집자 | O | O | O | X |
| 관리자 | O | O | O | O (+ 사용자·그룹 관리) |

## 구현 단계

1. **그룹 생성 (데이터 마이그레이션)**
   - `accounts/migrations/000X_create_role_groups.py`에서 `Viewer`, `Editor`, `Admin` 그룹을 만들어요.
   - 앱별 모델 권한을 `Permission`에서 조회해 `group.permissions.set(...)`으로 연결해요.
   - 권한은 `post_migrate` 시점에 생성돼요. 그래서 마이그레이션에서 `create_permissions`를 먼저 호출하거나, `post_migrate` 시그널로 그룹을 만들어요.
   - 권한 매핑은 `ROLE_PERMISSIONS = {"Viewer": ["view"], "Editor": ["view","add","change"], ...}` 같은 dict 한 곳에 모아요.

2. **Django admin 적용**
   - `ModelAdmin`의 `has_view/add/change/delete_permission`이 이미 모델 권한을 확인해요. 그래서 그룹만 맞으면 대부분 끝나요.
   - 직원 계정은 `is_staff=True`가 필요해요. `is_superuser`는 관리자 1~2명에게만 주세요. 슈퍼유저는 모든 권한 검사를 우회해요.
   - 뷰어가 폼에서 값을 바꾸지 못하도록, 필요하면 `get_readonly_fields`에서 `has_change_permission`을 확인해요.

3. **커스텀 뷰 적용 (해당 시)**
   - 클래스 뷰는 `PermissionRequiredMixin`과 `permission_required = "app.change_item"`을 써요.
   - 함수 뷰는 `@permission_required(..., raise_exception=True)`를 써요.
   - 템플릿의 버튼은 `{% if perms.app.change_item %}`로 숨겨요. 단, 이건 화면 처리일 뿐이에요. 실제 차단은 서버 뷰가 해요.

4. **역할 할당 UI**
   - 사용자 수정 화면에서 그룹을 하나만 고르게 해요. `UserAdmin`을 상속해 `filter_horizontal` 대신 단일 선택 필드를 쓰면 돼요.
   - 사용자·그룹 모델의 change 권한은 `Admin` 그룹에만 주세요. 그렇지 않으면 편집자가 자기 역할을 올릴 수 있어요.

5. **API가 있으면 (DRF)**
   - `DjangoModelPermissions`를 상속한 클래스를 기본값으로 설정해요. GET에도 view 권한을 요구하려면 `perms_map`을 오버라이드해야 해요. 기본값은 GET에 권한을 요구하지 않아요.

6. **테스트**
   - 역할 × 동작 매트릭스를 `pytest.mark.parametrize`로 만들어요. 예: `("viewer", "POST", "/admin/app/item/add/", 403)`.
   - 마이그레이션 후 각 그룹의 권한 집합이 기대값과 같은지도 검증해요.

7. **배포**
   - 기존 사용자를 먼저 그룹에 매핑하는 스크립트를 만들어요. 매핑 전에 배포하면 권한이 사라져서 접근이 막힐 수 있어요.
   - 변경 이력은 `django-simple-history`나 `LogEntry`로 남겨요. 권한 변경 감사에 필요해요.

## 확인할 점

- 행 단위 권한이 필요해요? 예를 들어 "자기 팀 데이터만 수정"이면 모델 권한만으로는 부족해요. 그때는 `django-guardian`이나 `get_queryset` 필터를 추가해야 해요.
- 역할이 나중에 더 늘어날 가능성이 있어요? 그렇다면 지금 구조(Group)가 그대로 확장돼요.

다음 단계로 현재 프로젝트 구조(admin인지 커스텀 뷰인지, 앱 목록)를 알려 주시면 1번의 마이그레이션 코드를 바로 써 드릴게요.
