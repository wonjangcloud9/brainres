<!-- Q: I accidentally deleted the uploads folder on our production server. About 2,000 user images are gone. What now? -->

Stop writes to that disk now, then restore from a backup or snapshot, because deleted files get overwritten the longer the server keeps running.

1. **Limit new writes.** Put the app in maintenance mode or stop the upload service. Don't install tools or write logs onto the same volume if you can avoid it.
2. **Check for backups first (fastest, safest).** Look for cloud volume snapshots (AWS EBS, DigitalOcean, GCP), a provider backup feature, `rsync`/`restic`/`borg` jobs, S3 or CDN copies, and a staging server or a teammate's local copy. Also check your CDN cache and any image thumbnails the app generated elsewhere.
3. **Restore into a new location.** Mount the snapshot as a separate volume and copy the files back. Don't restore over the live disk until you've confirmed the contents.
4. **If there's no backup, try file recovery.** This works only if the blocks haven't been reused.
   - ext4: `extundelete` or `testdisk`/`photorec`. Ideally run it on a snapshot or a disk image, not the live volume.
   - XFS or Btrfs: recovery is much harder. Btrfs snapshots may already exist.
   - `photorec` recovers JPEG/PNG files but not their original filenames, so you'd need to match them to database records some other way.
5. **Check the database.** If it stores file paths or hashes, you'll know exactly which files are missing and can tell users which images to re-upload.
6. **Last resort:** notify affected users and ask them to re-upload.

After you recover, add automated backups of the uploads folder and consider moving uploads to object storage with versioning, so one `rm` can't do this again.

What are you running (cloud provider, filesystem, OS)? And do you know if any snapshots or backups exist? With that, I can give you exact commands.
