# Turtle Humanoid Worker Game

## Video

![Video](video_2.gif)

## Description

This is a [Turtle graphics](https://docs.python.org/3/library/turtle.html)
game.<br />
You control the humanoid that works in a factory.<br />

## Background

Program is developed with VSCode and written in Python.<br />
Install VSCode, python 3 and required libraries.<br />
Run main.py in the src folder to start the program.<br />

## Instructions

The factory products appear to the pick up point in one of three<br />
different crate sizes via a heavy duty lift.<br />
The crate can be collected using left and right arrow keys.<br />
The screen continues infinitely to both directions and crate is<br />
picked up automatically as well as released to the drop point.<br />
Different size crates are to be delivered to the corresponding unloading<br />
platforms where another lift hoists them upstairs beyond the screen view.<br />
A bigger crate weighs more and slows down the walking speed.

## Ohjeet

Tehtaassa valmistetut tuotteet tulevat noutopisteelle kollissa jonakin<br />
kolmesta eri kokovaihtoehdosta tavarahissin kautta.<br />
Kollin voi noutaa käyttämällä nuolinäppäimiä vasemmalle ja oikealle.<br />
Kuvaruutu jatkuu molempiin suuntiin loputtomasti ja kollin nosto<br />
tapahtuu automaattisesti kuten myös alaslasku lähetyspisteelle.<br />
Eri kokoiset kollit toimitetaan eri lastauslaitureille, joissa<br />
toinen hissi nostaa ne yläkertaan kuvaruudun ulkopuolelle.<br />
Suurempi kolli painaa enemmän ja hidastaa kävelyvauhtia.

## N.B.

Running all tests at once might take a few minutes to complete.<br />
Call Humanoid create_measurement_grid() to show grid.<br />
'humanoid_speed' will change to "slow" when set to "default".<br />

## Testing

You can run individual unit tests from src folder in the terminal with:<br />
python -m unittest .\test\test_background.py<br />
python -m unittest .\test\test_box.py<br />
python -m unittest .\test\test_constants.py<br />
python -m unittest .\test\test_game.py<br />
python -m unittest .\test\test_helpers.py<br />
python -m unittest .\test\test_humanoid.py<br />
python -m unittest .\test\test_info.py<br />
python -m unittest .\test\test_surface.py<br />

Or all at once from src folder with:
python -m unittest

## Changelog

**[0.0.9] - Sep 10. 2025:**<br />
_- Added background._<br />

**[0.0.10] - Sep 12. 2025:**<br />
_- Added lifts._<br />
_- Added boxes._<br />

**[0.0.11] - Sep 14. 2025:**<br />
_- Added lift movement._<br />

**[0.0.12] - Sep 16. 2025:**<br />
_- Added box movement along y-axis._<br />

**[0.0.13] - Sep 18. 2025:**<br />
_- Added box movement along x-axis._<br />

**[0.0.14] - Sep 24. 2025:**<br />
_- Completed game engine._<br />

**[1.0.0] - Sep 25. 2025:**<br />
_- Initial release._<br />

**[1.0.1] - Sep 29. 2025:**<br />
_- Replaced Initial release with patched version._<br />

**[1.0.2] - Sep 30. 2025:**<br />
_- Game documentation and unit tests._<br />

**[1.0.3] - Oct 2. 2025:**<br />
_- Released the game._<br />
