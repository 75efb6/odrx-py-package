## Installation

```bash
pip install odrx_py
```

## Quick Start

```python
from odrx_py import APIClient

# Initialize client
client = APIClient()

# Get user by ID
user = await client.get_user_fromid(12345)

# Get beatmap
beatmap = await client.get_beatmap_fromid(1234567)

# Get leaderboard
leaderboard = await client.get_leaderboard(type="pp")

# Get top scores for a user
top_scores = await client.get_top_scores(12345)
```

## API Methods

### User Methods
- `get_user_fromid(user_id)` - Fetch user by ID
- `get_user_fromusername(username)` - Fetch user by username

### Beatmap Methods
- `get_beatmap_fromid(map_id)` - Fetch beatmap by ID
- `get_beatmap_frommd5(md5)` - Fetch beatmap by MD5 hash
- `get_beatmap_leaderboard_fromid(map_id)` - Get leaderboard for beatmap by ID
- `get_beatmap_leaderboard_frommd5(md5)` - Get leaderboard for beatmap by MD5

### Score Methods
- `get_top_scores(user_id)` - Get top 100 scores for user
- `get_recent_score(user_id, offset)` - Get recent scores with optional offset
- `get_scores_uid_beatmap_fromid(user_id, map_id)` - Get user scores on beatmap by ID
- `get_scores_uid_beatmap_frommd5(user_id, md5)` - Get user scores on beatmap by MD5
- `get_scores_uname_beatmap_fromid(username, map_id)` - Get user scores by username on beatmap ID
- `get_scores_uname_beatmap_frommd5(username, md5)` - Get user scores by username on beatmap MD5

### Leaderboard & Whitelist
- `get_leaderboard(type, country)` - Get global leaderboard (type: "pp" or "score")
- `get_whitelist()` - Get whitelisted beatmaps
- `whitelist_add_fromid(map_id)` - Add beatmap to whitelist by ID (requires key)
- `whitelist_add_frommd5(md5)` - Add beatmap to whitelist by MD5 (requires key)

## Authentication

For whitelist operations, provide your whitelist key:

```python
client = APIClient(whitelist_key="your_key_here")
```