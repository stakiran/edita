# edita
basic text editing skill TA(Time Attack) with your text editor.

![edita_demo](https://user-images.githubusercontent.com/23325839/58016061-b87b0b00-7b37-11e9-846d-5c5c5bd1b982.gif)

## Requirement
- Python 3.6+

## Installation
- Get edita.py with `git clone` etc.
- Get wordlist `google-10000-english.txt` from [first20hours/google-10000-english - GitHub](https://github.com/first20hours/google-10000-english)

## Start game
(1) Open two window(e.g. console window and editor window) beforehand.

(2) Do `python edita.py -w google-10000-english.txt`

(3) Play the game with open edita.temp with your editor.

## How to play

### Rule
Initial status.

```
activated avg characteRistic rea
ction organizations starsmerchan
t turner om chronic protective i
nspection Nfl population disAppo
inted mesa cancelled Fossil reac
hes blanket IncluSion sig haven 
priority insTrument menus abando
ned ht owner tt carol reynolds f
are gaYS matrix hurt retro ss ex
tending pending motorS digest ke
```

**Your mission is to edit all upper case to lower**.

In this case, editing targets are like this:

```
activated avg characteRistic rea
                      ^
ction organizations starsmerchan
t turner om chronic protective i
nspection Nfl population disAppo
          ^                 ^
inted mesa cancelled Fossil reac
                     ^
hes blanket IncluSion sig haven 
            ^    ^
priority insTrument menus abando
            ^
ned ht owner tt carol reynolds f
are gaYS matrix hurt retro ss ex
      ^^
tending pending motorS digest ke
                     ^
```

Therefore the correct is like this:

```
activated avg characteristic rea
ction organizations starsmerchan
t turner om chronic protective i
nspection nfl population disappo
inted mesa cancelled fossil reac
hes blanket inclusion sig haven 
priority instrument menus abando
ned ht owner tt carol reynolds f
are gays matrix hurt retro ss ex
tending pending motors digest ke
```

### Hit
If you think you complete all editing, do save on your editor.

If wrong, you cannot pass yet and increase `x` char.

```
$ python edita.py -w google-10000-english.txt
==== edita.py ====
Stage.01:x
```

```
$ python edita.py -w google-10000-english.txt
==== edita.py ====
Stage.01:xx
```

```
$ python edita.py -w google-10000-english.txt
==== edita.py ====
Stage.01:xxx
```

If correct, you can pass and go to next stage.

```
==== edita.py ====
Stage.01:xxxxx
         23.28 sec.
Stage.02:
```

### Clear
If clear all stages, display your total time.

```
$ python edita.py -w google-10000-english.txt
==== edita.py ====
Stage.01:xxxxxx
         82.28 sec.
Stage.02:x
         35.75 sec.
Stage.03:xx
         33.94 sec.
         ----
   Total:151.97 sec.
```

## Configuration

### Game control
`-x`, `-y`, `-c` and `-r` option.

For example: `python edita.py -w google-10000-english.txt -x 10 -y 5 -c 3 -r 5`

`-x` and `-y` means text size.

```
    X
<-------->
dIstrict g   A
aTes docum   |
EntEd wrIt   | Y
ings hunte   |
r women be   V
```

`-c` means game count(If `-c 3`, total 3 games like this).

```
$ python edita.py -w google-10000-english.txt -x 10 -y 5 -c 3 -r 5
==== edita.py ====
Stage.01:
         9.78 sec.
Stage.02:
         20.11 sec.
Stage.03:
         10.56 sec.
         ----
   Total:40.45 sec.
```

`-r` means replacing count(If `-r 5`, there are total 5 targets like this).

```
dIstrict g 
 ^
aTes docum 
 ^
EntEd wrIt 
^  ^    ^
ings hunte 
r women be 
```

### Wordlist
`-w (wordlist-filepath)` option.

This file must be 1 word per 1 line format and all characters must be lower alphabet.

## License
[MIT License](LICENSE)

## Author
[stakiran](https://github.com/stakiran)
