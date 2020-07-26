# Automated Backups
Will be able to backup my files to my external hard drive whenever the script is run
Features:
  ## Detect changes in files and save/alert accordingly
    Save previous state of drive to compare to, without brute forcing the entirety of the whole drive on backup
      Possible to use checksums or similar to save state without taking space
    Update file containing list of repeat names and/or files to be manually sorted
      If multiple identical files, delete redundant files on both input and backup
  ## Encrypt and compress files
    Lossless compression
    Password based encryption
  ## Ability to select backup location
    Possible Google Drive integration?
