# @44.o0 Instagram Reels Automation

A completely separate Railway automation for the Instagram account **@44.o0**.

This repository is **not** the existing first Instagram automation and must use its own Railway service, volume, Telegram bot, environment variables, database, posting history, schedules, logs and backups.

## Designed behavior

- Instagram account: `@44.o0`
- Instagram User ID: `28428666546764974`
- Source Drive folder: `1QREdguUC-VAZ-Me_kPbbJ1u3xjc-jf6K`
- 2 Reels/day at `13:00` and `20:30` Asia/Kolkata
- Fixed initial inventory; new Drive files are ignored until manual `/rescan`
- Recursively inventories `.mp4` and `.mov` videos from subfolders
- Finishes one folder before moving to the next
- Natural numeric filename/folder ordering
- Google Drive file ID is the duplicate-protection identity
- Persistent SQLite state on a Railway Volume
- Fully automatic official Instagram API publishing
- Railway public HTTPS URL temporarily serves only the active Reel to Meta
- Temporary Reel deleted from Railway after every attempt
- Three automatic attempts with bounded backoff
- `UNCERTAIN` is separate from `FAILED`; ambiguous `media_publish` outcomes are never automatically retried
- Permanent failed list after three attempts; queue then continues
- Deterministic controlled caption rotation with no runtime AI
- Rotating meme / weird-explainer / engagement caption packs and hashtag packs
- Separate owner-only Telegram bot with inline submenus and slash commands
- Recovery ZIP sent to Telegram every 48 hours; no backup archive retained on Railway
- 72-hour Instagram Insights snapshot and Telegram report for every posted Reel
- `/top` leaderboard from stored 72-hour analytics

## Railway environment variables

Add secrets in **Railway → Service → Variables**. Never commit tokens to GitHub.

Required:

```text
DRIVE_FOLDER_ID=1QREdguUC-VAZ-Me_kPbbJ1u3xjc-jf6K
INSTAGRAM_USER_ID=28428666546764974
INSTAGRAM_ACCESS_TOKEN=<add securely in Railway>
TELEGRAM_BOT_TOKEN=<second bot token>
TELEGRAM_OWNER_ID=<your Telegram numeric user ID>
PUBLIC_BASE_URL=https://<this-new-service>.up.railway.app
```

Recommended / defaults:

```text
AUTOMATION_TIMEZONE=Asia/Kolkata
REEL_POST_TIMES=13:00,20:30
MAX_ATTEMPTS=3
BACKUP_INTERVAL_HOURS=48
ANALYTICS_DELAY_HOURS=72
INSTAGRAM_API_VERSION=v25.0
INSTAGRAM_SHARE_TO_FEED=true
REELS_DATA_DIR=/data
```

Generate a Railway public domain for this **new service**, then put the exact `https://...` value in `PUBLIC_BASE_URL`.

## Railway Volume

Attach a new Railway Volume to this service and mount it at:

```text
/data
```

Persistent state:

```text
/data/44o0_state.sqlite3
```

Temporary downloads are stored under `/data/tmp` only while needed and are deleted after the attempt. Startup also removes stale temporary files left by an interrupted process.

## Telegram controls

Main controls are available from `/panel` using inline submenus.

Slash commands:

```text
/panel
/status
/next
/stats
/queue
/history
/failed
/skipped
/uncertain
/top
/config
/health
/logs
/logs today
/logs posted
/logs failed
/logs uncertain
/logs errors
/pause
/resume
/postnow
/skip
/skip REEL_ID
/unskip REEL_ID
/retry REEL_ID
/rescan
/backup
/help
```

`/postnow` consumes the next Reel immediately but does **not** remove or move the next scheduled 13:00/20:30 slot. If another post is already running, it is rejected instead of queueing a second publisher.

## Failure states

- `PENDING` — eligible for automatic posting.
- `POSTED` — successfully published and permanently excluded from the queue.
- `FAILED` — three real attempts failed; listed by `/failed` and skipped automatically.
- `SKIPPED` — manually skipped; `/unskip ID` restores its original queue position.
- `UNCERTAIN` — the publish request may have succeeded but the response was ambiguous. Automatic retry is blocked to prevent duplicate Reels.

If the service dies before `media_publish`, the Reel safely returns to `PENDING`. If it dies while `media_publish` is in flight, it becomes `UNCERTAIN` on startup.

## Backups

Every 48 hours the second Telegram bot sends a ZIP containing:

- a consistent SQLite snapshot
- CSV inventory/history export
- JSON inventory/history export
- non-secret recovery configuration

Tokens and other secrets are intentionally excluded. The ZIP is deleted locally after Telegram delivery.

## First deployment sequence

1. Deploy this repository as a **new Railway service**.
2. Attach a **new volume** at `/data`.
3. Generate a **new Railway public domain** for this service.
4. Add the environment variables above, including the already-verified second-account Instagram token.
5. Create/use the **separate Telegram bot** and set its token + your numeric Telegram user ID.
6. Deploy/redeploy.
7. The first successful startup creates the fixed Drive inventory and sends a Telegram startup report.
8. Use `/panel`, `/health`, `/stats` and `/next` to verify the queue before leaving automatic posting enabled.

Do not point this service at the database, volume, Telegram bot, Railway service, or environment variables of the first automation.
