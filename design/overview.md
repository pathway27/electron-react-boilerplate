Oh I just finished Assassin's Creed 2 on my PC, let me buy 3.
Three days later, playing on PC, what I already own Assassin Creed 3 on PS3 as part of PSN+?!

## Features

See the month/year's upcoming games in our calender. Hyped games will take precedence. Granular to day level
Scan your computer for games to add to your collection.
Add any folder, on your computer, with DRM free/backup games to add to your collection.
Manage any and every Platform (plugins?), show duplicates and relationships (collections/series, offspins, re-master, remakes).

Manage all the games you own; digital and physical with a modern UI and PICTURESSS!

Scraping game information
Server to sync user collections
Website to access game information anywhere

App to scan physical games with barcode

## Software Stack

Need to be a desktop app which is easy to style.
Web over a cross-platform toolkit

Electron JS with React (ES6)
Why?
  - I want to learn React

sqlite3 (Preferably, but need design) or PouchDB?
Do we need a model framework? No. Are you sure?, this is a very data heavy application.

Docker to manage basically all microservers
Add kubernetes to scale (or is docker swarm enough?)

Electron - Desktop App - MIT
  Electron React Boilerplate - MIT
React - Front End <- Refactor common
React Native - Mobile - MIT
CouchDB - Database - Apache-2.0
PouchDB - Apache 2.0
Scrapy - Scraper - MIT-ish

Phoenix - Server Shit - MIT

Javascript
Python
Elixir

# Hardware Stack

Linux with Docker installed.

Potential Vendors
  - Hetzner
  - AWS
  - Google
  - Bluemix
  - Azure
  - OVH
  - Find more on lowendbox

How to know specs. we need?


# TODOS

SQL/Data Design
View Design - Discordant (Discord inspired UI, gray and whites with colors)
Skeleton
Rough estimates on how much data; what data on each page;
Fetch this years full calender worth of games from any and all APIs I can.
Abstract way to fetch data from either SQL or pouchDB then run benchmarks

Some way to queue tasks of scanning/updating platform/folders

Updating Database server (with diff/git)

Icons

Localizations

# Goal

I think Discord is missing this and should absorb us.
So then what license?
