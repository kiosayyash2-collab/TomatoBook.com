# tentang project
nama project:
jenis project: aplikasi produktifitas berbasis browser
Bahasa pemrograman: JS,HTML,CSS,PHP,SQL,Python(dengan api tambahan)
Version: 1.0

# server side
|--Cpanel
|-- server/ # PHP application and database access
| |-- public/ # The only directory exposed by the web server
| | `-- api/
| | |-- health.php
| | |-- tasks.php
| | |-- sessions.php
| | `-- settings.php
| |-- src/ # Private PHP code; outside public web root
| | |-- Config/Database.php
| | |-- Controllers/
| | |-- Services/
| | |-- Repositories/
| | |-- Validation/
| | `-- bootstrap.php
| |-- database/
| | |-- migrations/
| | `-- seeds/
| |-- tests/
| |-- storage/logs/
| |-- .env.example
| |-- composer.json # Optional PHP dependency manifest
| `-- README.md
|
`-- extension/ # Optional future browser extension
 |-- manifest.json
 |-- popup.html
 |-- popup.js
 `-- popup.css
