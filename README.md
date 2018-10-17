# Nxs-backup with some extensions

This version allows:
- external SMTP (SSL, TLS) mail sending
- s3fs access configuration and custom s3 endopoints
- successful jobs execution email
- pip installation (pip install https://github.com/Sovetnikov/nxs-backup/archive/master.zip)


```yaml
main:
  server_name: nxs-backup

  admin_mail: admin@mail.com
  client_mail:
  - client@mail.com
  # Success email reports for client and admin
  send_success_reports: yes

  mail_from: admin@mail.com
  level_message: error

  block_io_read: ''
  block_io_write: ''
  blkio_weight: ''
  general_path_to_all_tmp_dir: /var/nxs-backup

  cpu_shares: ''

  log_file: /dev/stdout

  # SMTP sending config section
  smtp_server: smtp.yandex.ru
  smtp_port: 465
  smtp_ssl: yes # smtp_tls also supported
  smtp_user: smtp_user
  smtp_password: smtp_password

  smtp_timeout: 60
jobs:
  - job: desc-files
    type: desc_files
    tmp_dir: /var/nxs-backup/files/desc/dump_tmp

    sources:
    - target:
      - /app/data
      excludes:
      - CACHE
      gzip: yes

    - storage: s3
      enable: yes

      backup_dir: /backup

      bucket_name: 'bucket_name'
      # s3 bucket access settings
      access_key_id: 'access_key_id'
      secret_access_key: 'secret_access_key'
      s3fs_opts: '-o url=https://<external_endpoint> -o use_path_request_style'

      store:
        days: 5
        weeks: 2
        month: 6
```