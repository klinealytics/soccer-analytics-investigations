#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared helpers for loading data and soccer analytics investigations."""

from mplsoccer import Sbopen
import pandas as pd
import pathlib

parser = Sbopen()

# StatsBomb competitions with full 360 coverage (checked Nov 8, 2026)
MENS_TOURNAMENTS_360 = {
    'World Cup 2022': (43, 106),
    'Euro 2020': (55, 43),
    'Euro 2024': (55, 282),
}

WOMENS_TOURNAMENTS_360 = {
    "Women's World Cup 2023": (72, 107),
    "Women's Euro 2022": (53, 106),
    "Women's Euro 2025": (53, 315),
}

def load_events(competition_id, season_id, cache_dir='data'):
    """Load all events for one competition-season, from cache if saved."""

    # load events from cache if available, otherwise download and save
    cache = pathlib.Path(cache_dir) / f'events_{competition_id}_{season_id}.pkl'
    if cache.exists():
        df_events = pd.read_pickle(cache)
        print('Loaded events from cache', flush=True)
    else:
        df_match = parser.match(competition_id, season_id)
        n = len(df_match)
        events = []
        for i, match_id in enumerate(df_match['match_id'], start=1):
            events.append(parser.event(match_id)[0])
            # printing progress report every 20 matches for sanity check
            if i % 20 == 0 or i == n:
                print(f'{i}/{n} matches loaded', flush=True)
        df_events = pd.concat(events, ignore_index=True)
        cache.parent.mkdir(parents=True, exist_ok=True)
        df_events.to_pickle(cache)
        print(f'Saved events to {cache}', flush=True)
    return df_events
    
def load_many(tournaments):
    """Load and combine events for several tournaments, labelled by name."""
    frames = []
    for name, (comp_id, season_id) in tournaments.items():
        df = load_events(comp_id, season_id)
        df['tournament'] = name
        frames.append(df)
    
    events = pd.concat(frames, ignore_index=True)
    events['tournament'].value_counts()
    return events