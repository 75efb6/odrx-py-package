## Installation

```bash
pip install odrx-py git+https://github.com/unclem2/rosu-pp-py.git
```

## API Wrapper

### Quick Start

```python
from odrx_py import AsyncODRXAPIClient

# Initialize client
client = AsyncODRXAPIClient()

# Get user by ID
user = await client.get_user_fromid(12345)

# Get beatmap
beatmap = await client.get_beatmap_fromid(1234567)

# Get leaderboard
leaderboard = await client.get_leaderboard(type="pp")

# Get top scores for a user
top_scores = await client.get_top_scores(12345)
```

### Methods

#### User Methods
- `get_user_fromid(user_id)` - Fetch user by ID
- `get_user_fromusername(username)` - Fetch user by username

#### Beatmap Methods
- `get_beatmap_fromid(map_id)` - Fetch beatmap by ID
- `get_beatmap_frommd5(md5)` - Fetch beatmap by MD5 hash
- `get_beatmap_leaderboard_fromid(map_id)` - Get leaderboard for beatmap by ID
- `get_beatmap_leaderboard_frommd5(md5)` - Get leaderboard for beatmap by MD5

#### Score Methods
- `get_top_scores(user_id)` - Get top 100 scores for user
- `get_recent_score(user_id, offset)` - Get recent scores with optional offset
- `get_scores_uid_beatmap_fromid(user_id, map_id)` - Get user scores on beatmap by ID
- `get_scores_uid_beatmap_frommd5(user_id, md5)` - Get user scores on beatmap by MD5
- `get_scores_uname_beatmap_fromid(username, map_id)` - Get user scores by username on beatmap ID
- `get_scores_uname_beatmap_frommd5(username, md5)` - Get user scores by username on beatmap MD5

#### Leaderboard & Whitelist
- `get_leaderboard(type, country)` - Get global leaderboard (type: "pp" or "score")
- `get_whitelist()` - Get whitelisted beatmaps
- `whitelist_add_fromid(map_id)` - Add beatmap to whitelist by ID (requires key)
- `whitelist_add_frommd5(md5)` - Add beatmap to whitelist by MD5 (requires key)

### Authentication

For whitelist operations, provide your whitelist key:

```python
client = AsyncODRXAPIClient(whitelist_key="your_key_here")
```

## Performance Calculator

### Quick Start

```python
from odrx_py.performance import PPCalculator
from pathlib import Path

# Initialize Path of the beatmap
beatmap = Path(__file__).parent / "resources" / "beatmap.osu"

# Initialize calculator
calculator = PPCalculator(beatmap, mods=[{"acronym": "RX"}])

# Get the pp number/calculate
calculator.calculate_performance()
```

### Class / Methods
- `PPCalculator(beatmap, mods, n300, n100, n50, misses, combo)` - Initializes the Calculator class giving it the required data.

- `calculate_performance()` - Calculates the performance points.

### Mod Format

#### Normal mods
```python
mods = [{
    "acronym": "(insert mod name)"
}]
```

#### Speed modifier
```python
mods = [{
    "acronym": "CS",
    "settings": {
        "rateMultiplier": 1.0
    }
}]
```

#### StrEnum of all Mods (src/enums/mods.py)
```python
from enum import StrEnum

class Mods(StrEnum):
  Relax = "RX"
  DifficultyAdjust = "DA"
  NightCore = "NC"
  CustomSpeed = "CS"
  DoubleTime = "DT"
  Hidden = "HD"
  FlashLight = "FL"
  ShitMod = "RE" # REZ
  WindUp = "WU"
  Precise = "PR"
  HardRock = "HR"
  HalfTime = "HT"
  AutoPilot = "AP"
  WindDown = "WD"
  ApproachDifferent = "AD"
  Auto = "AT"
  Easy = "EZ"
  FreezeFrame = "FR"
  Mirror = "MR"
  Muted = "MU"
  NoFail = "NF"
  Random = "RD"
  ScoreV2 = "V2"
  SmallCircle = "SC"
  SuddenDeath = "SD"
  Perfect = "PF"
  Traceable = "TC"
  Synesthesia = "SY"
  NoMod = "NM"
```