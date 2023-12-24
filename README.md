<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="[https://github.com/othneildrew/Best-README-Template](https://github.com/younis-alx/Moodify/edit/main/README.md)">
    <img src="frontend/public/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Moodify</h3>

  <p align="center">Moodify is an application to perform sentiment analysis on a given tweet/replies to estimate the mood of the text using natural language processing (NLP) technique used to determine the sentiment or emotional tone expressed in a piece of text. It involves scraping tweet and replies, analyzing text data to identify and categorize the sentiment as positive, negative, or neutral. </p>
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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![moodify gif (1)](https://github.com/younis-alx/Moodify/assets/126336909/d09a78fc-793b-4c30-bfab-b8b89220cd7d)

Moodify is an application to perform sentiment analysis on a given text to estimate the mood of the text using natural language processing (NLP) technique used to determine the sentiment or emotional tone expressed in a piece of text. It involves analyzing text data to identify and categorize the sentiment as positive, negative, or neutral.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

#### Project backend:
- aiohttp==3.9.1
- flasgger==0.9.7.1
- Flask==3.0.0
- Flask_Cors==4.0.0
- jmespath==1.0.1
- pandas==2.1.4
- python-dotenv==1.0.0
- Requests==2.31.0
- scipy==1.11.4
- setuptools==69.0.2
- textblob==0.17.1
- transformers==4.21.2
- tweepy==4.14.0
  
#### Project Frontend
- react
- tremor
- shadcn/ui
- mui-x
- tailwindCSS





<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To set the project locally you will need the following

### Prerequisites

* npm
  ```sh
  npm install npm@latest -g && npx tailwind init -p && npx shadcn-ui@latest init && npx shadcn-ui@latest init  &&
  npm install uuid @mui/x-charts @mui/icons-material @frontsource/roboto @mui/styled-engine-sc styled-components
  @emotion/react @emotion/styled react-router-dom &&
  npm install -D tailwindcss postcss autoprefixer @heroicon/react@1.0.6 &&
  npm install -g create-vite && npm create vite@latest frontend
  
  
  ```


### Installation

Installing and setting up clone.

1. Clone the repo
   ```sh
   git clone https://github.com/younis-alx/Moodify
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `.env` Note: apikey uses a rotater class to rotate between apikeys, **Can be used with one apikey.**
   ```python
  
    X_API_KEY="apikey1,apikey2"
    X_API_HOST='host'
    THRESHOLD=0.3
    HUGGINGFACE_API_KEY=''
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project can parse tweet replies using the URL and perform sentiment analysis on all replies and returns all useful visualizations and summaries 

![Screenshot 2023-12-20 143600](https://github.com/younis-alx/Moodify/assets/126336909/4ed5799c-7910-4b99-95cc-29c5a572c27e)

![image](https://github.com/younis-alx/Moodify/assets/126336909/e149b36b-81c9-4f13-a393-e35366a41526)

![image](https://github.com/younis-alx/Moodify/assets/126336909/b22faff4-4a6d-4e1b-b065-7d371fac780b)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Younis ahmed - [@swe_younis](https://twitter.com/swe_younis) 

<!-- Project Link: -->
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!--## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p> 



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links 
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
-->
