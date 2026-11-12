<!-- Q: I accidentally deleted the uploads folder on our production server. About 2,000 user images are gone. What now? -->

**Stop writes to the affected disk now, then look for a backup or snapshot before you try any recovery tool.** New writes can overwrite the deleted files' blocks, and installing a recovery tool on the same volume does the same.

1. **Limit writes.** Put the site in maintenance mode, or stop the app so users can't upload. If the uploads folder lived on its own volume, unmount it or remount it read-only.
2. **Check for backups.** Look in this order:
   - Cloud snapshots (AWS EBS, DigitalOcean, GCP, Hetzner)
   - Host-level backups (your provider's panel, or Time Machine or rsnapshot on a self-managed box)
   - A copy in S3 or other object storage, if the app mirrors uploads there
   - Another server, such as staging, a replica or a CDN origin cache
3. **Restore into a new location.** Mount the snapshot as a new volume, or restore to `/tmp/restore`. Then copy the files back. Don't restore over the live disk.
4. **If there is no backup, try file recovery.** Take a disk image first, or attach the volume to a second machine. Run `extundelete` (ext3/ext4) or `photorec` against the image, not the live disk. Success is uncertain. On ext4 it often fails because the journal zeroes the file metadata. Images (JPEG/PNG) are the best case because `photorec` recovers them by file signature, though it loses the original filenames.
5. **Rebuild what you can.** Your database probably still holds the image paths or URLs. Check for copies in CDN caches, email attachments or user devices.

Once you're stable, add automated daily backups of the uploads folder and a delete guard (object storage with versioning, or a read-only mount for the app user).

What is your setup: cloud provider, filesystem, and were the uploads on local disk or object storage? With that I can give exact commands.
