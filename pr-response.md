# PR Response Doc — CineLog Watchlist Feature

## AI Usage

<!-- Fill in at the end — how you used AI tools during this project -->

## Comment 1 — Rename

**What I did:**
Renamed the function `save_to_watchlist()` to `add_to_watchlist()` inside `services/watchlist_service.py` to preserve the codebase's strict `verb_to_noun` naming convention. I also updated the import statement and route invocation within `routes/watchlist.py`.

**How I verified:**
I performed a project-wide search (`grep` / Find in Files) for `save_to_watchlist` across the entire codebase repository. The search confirmed that the only occurrences were located within `services/watchlist_service.py` and its direct routing call site inside `routes/watchlist.py`, ensuring no dangling references remain.

## Comment 2 — Deduplication

**What I did:**
Added a database query check to `add_to_watchlist()` that checks if a `WatchlistEntry` with the given `user_id` and `film_id` already exists. If found, it explicitly raises a newly defined custom exception, `AlreadyInWatchlistError`.

**How I verified:**
I verified this logic by reviewing how `services/collection_service.py` handles duplicate entries through `AlreadyInCollectionError`. This defensive structure safely arrests duplicate operations before database commits execute.

## Comment 3 — Missing test

**What I did:**
**How I verified:**

## Comment 4 — Default visibility

**My position:**
**Reasoning:**
**Tradeoff acknowledged:**

## Comment 5 — Sort order

**My position:**
**Reasoning:**
**Engagement with reviewer's point:**

## Comment 6 — Rebase

**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description

<!-- Written at the end — feature overview, design decisions, manual testing steps -->
