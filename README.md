<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SuchLuukie/virtual-assistant">
  </a>

<h3 align="center">Athena Virtual Assistant</h3>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
# About The Project

Athena Virtual Assistant is my personal attempt at recreating larger more widely known virtual assistant's (I.E, Alexa, Siri, Google Assistant)
First of all I'd like to point out that this repository contains both the client side and server side of the project.
I decided on dividing the two so I could also host my personal portfolio website with it. Another benefit is that it's more scaleable and will allow people to try it out when I host it.

### Technical Details
Athena uses keyword replacement to prepare input for the intent classification (ML).
Once a function has been derived from the input, depending on the function it will call an API or library to get for instance the weather.



### Built With

* [Flask](https://flask.palletsprojects.com/en/2.1.x/) (Server side)
* [Sklearn](https://scikit-learn.org/stable/) (Server Side)

* [Tkinter](https://docs.python.org/3/library/tkinter.html) (Client Side)
* [Speech Recognition](https://pypi.org/project/SpeechRecognition/) (Client Side)
* [gTTS](https://pypi.org/project/gTTS/) (Client Side)
