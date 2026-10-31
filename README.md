# Last Draw

**High noon. One bell. Don't flinch.**

A tiny pixel-art western duel about reflexes. Two gunslingers face each other on main street.
Wait for the bell, then draw. Shoot too early and you lose. Shoot too late and you lose too.

### ▶ [Play it in your browser on itch.io](https://charlesonthewave.itch.io/last-draw)

Free, keyboard only.

![Title screen](materialy/zrzuty/01-ekran-tytulowy.png)

<p>
  <img src="materialy/zrzuty/02-ready.png" alt="Waiting for the bell" width="49%">
  <img src="materialy/zrzuty/03-po-strzale.png" alt="After the shot" width="49%">
</p>

This is my first game. I made it to learn the whole path from an idea on paper to a game anyone
can play online.

## How to play

| Key | What it does |
|---|---|
| 1 / 2 | Title screen: choose 1 Player or 2 Players |
| Space | 1 Player: shoot |
| A / L | 2 Players: left / right player shoots |
| R | Next round / play again |
| Esc | Back to the title screen |

**1 Player.** Five outlaws, each one faster than the last. You have two lives for the whole run:
lose once and you face the same outlaw again, lose twice and it's game over. Your best reaction
time is saved.

| # | Outlaw | | Draws in |
|---|---|---|---|
| 1 | Slow Joe | *"Drunk since noon. Still dangerous."* | 0.60 s |
| 2 | Dusty Pete | *"Never lost a duel. Never fought one either."* | 0.48 s |
| 3 | Rattlesnake Rosa | *"Bites before you see her move."* | 0.38 s |
| 4 | Deacon Graves | *"Reads your last rites while you draw."* | 0.30 s |
| 5 | The Undertaker | *"Already measured you for a coffin."* | 0.24 s |

Each outlaw's time varies by up to 0.03 s, so no two duels are the same.

**2 Players.** One keyboard, first to three wins. A false start gives the round to your opponent.
If both shoot in the same frame, it's a draw and the round is replayed.

## How it works

Made with **Godot 4.7** and **GDScript**. It uses the Compatibility renderer, so it runs in a web
browser.

- **Every screen is a scene.** `menu.tscn` is the title screen, `duel.tscn` is 1 Player,
  `duel_2p.tscn` is 2 Players. Each scene has one script that runs it.
- **A duel has three states:** `ready` → `fire` → `done`. After "Ready..." a timer waits a random
  2 to 6 seconds, then the game switches to `fire`, rings the bell and notes the time. Your
  reaction time is the gap between that moment and your key press. A key press during `ready`
  is a false start.
- **The computer opponent is just a timer.** When the bell rings, it starts its own countdown
  (its reaction time from the table above). If you haven't shot when it runs out, you lose.
- **2 Players is judged once per frame.** Both keys are collected first and checked together in
  `_process`, so two presses in the same frame are a fair draw, not a win for whichever key
  event the computer happened to read first.
- **Animation from one sprite sheet.** `kowboj.png` ("cowboy") has 16 frames: standing, shooting
  (1-4), falling (5-8) and a growing puddle (9-15). A Tween steps through the frames: the winner
  shoots, the loser falls.
- **Music survives scene changes.** `music.gd` is an autoload, a node Godot creates once at
  start and keeps between scenes. Before a duel the music fades out and only the wind is left.
  After the shot there is 1.5 s of silence for the echo, then the music comes back.
- **Parallax title screen.** Three layers (rocks, cacti, buildings) scroll at different speeds,
  which the eye reads as depth, like the view from a train window.
- **Best time** is saved to `user://record.txt`.

## Art and sound pipeline

Two Python scripts in `narzedzia/` ("tools") build the game's art and sound, so every change can
be repeated from scratch:

- `sklej_grafike.py` ("assemble graphics", needs Pillow) cuts the asset packs into the street
  background, adds a black outline to the cowboy, draws the tumbleweed and the puddle pixel by
  pixel, turns the title into pixel art and makes the itch.io cover.
- `zrob_dzwieki.py` ("make sounds", standard library only) synthesizes the 8-bit sound effects
  the way the NES did it: pulse and triangle waves, noise, and volume in 16 steps. Bell, gunshot
  with echo, wind with a whistle.

Run them from the repository root, e.g. `python -P narzedzia/sklej_grafike.py`.

## Project structure

Folder names and notes are in Polish, my native language. The game itself is in English.

```
godot/              the Godot project (open project.godot)
  assets/           art, sound and music: original packs and generated files
  menu.*            title screen
  duel.*            1 Player duel
  duel_2p.*         2 Players duel
  music.gd          background music (autoload)
  krzak.gd          rolling tumbleweed
  tlo_tytulowe.gd   parallax title background
  zrzuty.gd         F12 screenshot (works only when run from the editor)
narzedzia/          Python scripts for art and sound, fonts
materialy/          cover and screenshots for itch.io
GDD.md              game design: what is in the first version and what is not
PLAN.md             the plan, step by step
ASSETY.md           every asset with its author and license
```

## How I made it

- I started with a short design doc (`GDD.md`) with a firm "not in the first version" list,
  so the scope didn't keep growing.
- The whole game was built with grey rectangles first. Art and sound came at the end.
- Small steps: each one was something I could test in a few minutes. A step was committed only
  after I played it and it worked.
- The design, the decisions and the testing are mine. The code was written together with
  Claude, an AI coding assistant.

## Run from source

1. Install [Git LFS](https://git-lfs.com) before cloning. Art and sound are stored with LFS.
2. Open `godot/project.godot` in Godot 4.7 and press F5.

## Credits

- Cowboy sprite: [LinkNinja](https://linkninja.itch.io/pixelart-cowboy)
- Western tileset "YEEHAW!": [CURSED OFFERINGS](https://cursed-offerings.itch.io/yeehaw)
- Music "Lasso Lady": congusbongus, CC0 ([OpenGameArt](https://opengameart.org/content/lasso-lady-seamless-loop))
- Fonts: [Rye](https://fonts.google.com/specimen/Rye) by Nicole Fally and
  [Silkscreen](https://fonts.google.com/specimen/Silkscreen) by Jason Kottke (SIL Open Font License)
- Sound effects, tumbleweed, puddle and title screen: made for this game

The art, music and fonts belong to their authors and are used under their licenses
(details in `ASSETY.md`).

The original art packs are in `godot/assets/linkninja/` and `godot/assets/yeehaw/` only so the
project can be opened and rebuilt. **If you want to use them, please download them from the
authors' pages linked above.**
