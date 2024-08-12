# **Witty Devices**

## **Site Overview**

[View the live project here.](https://witty-devices-91c5d0b3a8c2.herokuapp.com/)


Welcome to Witty Devices, your trusted source for the latest in smart home technology and security solutions. We offer a carefully curated range of products that combine innovation with convenience, helping you create a safer, smarter, and more efficient living space. Whether you're looking to upgrade your home security with intelligent cameras and alarms or seeking advanced automation systems to simplify daily tasks, Witty Devices has everything you need to transform your home into a modern, connected sanctuary. Explore our collection and experience the future of home technology today.

![Website responsiveness](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/amiresponsive.jpg?raw=true)

## Table of contents

- [**Witty Devices**](#witty-devices)
  - [**Site Overview**](#site-overview)
  - [Table of contents](#table-of-contents)
  - [**Planning stage**](#planning-stage)
    - [**Target Audiences:**](#target-audiences)
    - [**User Stories:**](#user-stories)
    - [**Site Aims:**](#site-aims)
    - [**How Will This Be Achieved:**](#how-will-this-be-achieved)
    - [**Design:**](#design)
    - [**Custom Models:**](#custom-models)
    - [**Wireframes:**](#wireframes)
    - [**Color Scheme:**](#color-scheme)
    - [**Typography:**](#typography)
    - [**Technologies Used:**](#technologies-used)
      - [**Design Tools**](#design-tools)
      - [**Front-End**](#front-end)
      - [**Back-End**](#back-end)
  - [**Current Features Common to all pages**](#current-features-common-to-all-pages)
    - [**Header Element**](#header-element)
    - [**Footer**](#footer)
  - [**Individual Page Content features**](#individual-page-content-features)
    - [**Home Page Content**](#home-page-content)
    - [**All Products Page Content**](#all-products-page-content)
    - [**All Smart Security Page Content**](#all-smart-security-page-content)
    - [**All Smart Home Tech Page Content**](#all-smart-home-tech-page-content)
    - [**Our Blog Page Content**](#our-blog-page-content)
    - [**Newsletter Page Content**](#newsletter-page-content)
    - [**Account Page Content**](#account-page-content)
    - [**Sign In Page Content**](#sign-in-page-content)
    - [**Join Page Content**](#join-page-content)
    - [**Checkout Page Content**](#checkout-page-content)
    - [**Privacy Policy Page Content**](#privacy-policy-page-content)
    - [**Refunds and Returns Page Content**](#refunds-and-returns-page-content)
    - [**Terms and Conditions Page Content**](#terms-and-conditions-page-content)
    - [**404 Error Page Content**](#404-error-page-content)
  - [**Future Enhancements**](#future-enhancements)
  - [**Testing Phase**](#testing-phase)
    - [**Testing During Development**](#testing-during-development)
      - [**Manual Testing**](#manual-testing)
      - [**User Story Testing**](#user-story-testing)
      - [**Functionality Testing**](#functionality-testing)
      - [**Solved and Known Bugs**](#bugs)
    - [**Testing After Development**](#testing-after-development)
      - [**Validators**](#validators)
      - [***HTML*** - https://validator.w3.org/nu/](#html---httpsvalidatorw3orgnu)
      - [***CSS*** - https://jigsaw.w3.org/css-validator/](#css---httpsjigsaww3orgcss-validator)
      - [***JSHint*** - https://jshint.com/](#jshint---httpsjshintcom)
      - [***Python linter*** - https://pep8ci.herokuapp.com/](#pythonlinter---httpspep8ciherokuappcom)
      - [**PageSpeed Insights**](#pagespeed-insights)
  - [**Deployment**](#deployment)
  - [**Credits**](#credits)
    - [**General reference:**](#general-reference)
    - [**Content:**](#content)

## **Planning stage**

### **Target Audiences:**

- **Homeowners** looking to upgrade their living spaces with the latest smart security systems and home automation technology.
- **Tech-savvy individuals** interested in integrating cutting-edge devices into their homes for enhanced convenience and control.
- **Young professionals** who value efficiency and seek to streamline their daily routines with smart home gadgets.
- **Parents** wanting to ensure the safety of their families with advanced home security solutions.
- **DIY enthusiasts** eager to customize and optimize their homes using smart devices.
- **Elderly people or caregivers** searching for smart home products that offer convenience, safety, and remote monitoring features.
- **Real estate developers or property managers** aiming to increase the value and appeal of their properties by incorporating modern smart technology.


### **User Stories:**

- As a user of the website, I want to easily navigate through Witty Devices' selection of smart security products, so I can quickly find the best system to protect my home and purchase it with confidence.

- As a user of the website, I want to see detailed product descriptions, so I can make informed decisions about which smart home devices will best suit my needs.

- As a user of the website, I want a seamless and secure checkout process, so I can complete my purchases without hassle and trust that my payment information is safe.

- As a user of the website, I want to find product recommendations and guides, so I can discover the latest smart home trends.

- As a user of the website, I want to see a clean, responsive design that works well on both desktop and mobile, so I can browse and shop for smart devices wherever I am.

- As a user of the website, I want to filter products by features, price, and compatibility, so I can efficiently find exactly what I need without sifting through irrelevant items.

- As a user of the website, I want to be able to subscribe to a newsletter so I can be informed whenever new products come in stock.

### **Site Aims:**

- Simplify Navigation: The website aims to provide an intuitive and user-friendly interface that allows users to effortlessly browse and find the smart security and home tech products they need.

- Offer Comprehensive Information: The website aims to feature detailed product descriptions, helping users make well-informed purchasing decisions.

- Ensure a Smooth Checkout Process: The website aims to deliver a seamless, secure, and hassle-free checkout experience, giving users peace of mind while completing their purchases.

- Provide Guidance: The website aims to offer helpful guides, tutorials, and product recommendations, ensuring users can easily discover and install the latest smart home devices.

- Optimize Mobile Experience: The website aims to deliver a clean, responsive design that functions flawlessly across all devices, enabling users to shop for smart devices on the go.

- Facilitate Efficient Product Search: The website aims to implement advanced filtering and search options, allowing users to quickly find products based on category, price, and rating, tailored to their specific needs.

- Implement a newsletter: The website aims to add a newsletter subscription, so that user can be alerted when a new line of product gets added.

### **How Will This Be Achieved:**

- Simplify Navigation: The website will achieve this by implementing a clear and organized menu structure, intuitive category listings, and a robust search function. Key sections like smart security and home tech will be prominently displayed for easy access.

- Offer Comprehensive Information: The website will provide detailed product pages that include in-depth descriptions, high-quality images and specifications as well as ratings for the products.

- Ensure a Smooth Checkout Process: The website will feature a streamlined checkout process with minimal steps, a payment option, and strong encryption to secure user data.

- Provide Guidance: The website will host a dedicated blog section with guides, smart home tips and new technologies that are constantly being released.

- Optimize Mobile Experience: The website will be built using responsive design principles, ensuring it adapts seamlessly to any screen size. Mobile-specific features, such as touch-friendly navigation and quick access buttons, will enhance the user experience on smartphones and tablets.

- Facilitate Efficient Product Search: The website will implement advanced filtering and sorting options, allowing users to search by categories such as price, brand, features, and compatibility.

- Implement a newsletter: The website will have a dedicated newsletter section, where users can enter their name and their email address to be added to the newsletter database.

### **Design:**
 * The database model or ERD(entity relationship diagram) was created to visualise the connection between models within the project. The diagram was created using Drawsql.app, here is the link to the diagram: [https://drawsql.app/teams/razvan-1/diagrams/witty-devices]

![Schema design](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/schema.jpg?raw=true)

### **Custom Models:**

The custom models made for this project were:

#### Our Blog:
The blog has functionality to add posts(as a admin/superuser) that have a title, a text body, a button to click that will expand the entire blog post in a new page where users can also comment on the blog post as well as delete their own comment.

**Blog Post Model Database Fields:**
- id: bigint
- post_title : varchar
- content: text
- author : varchar
- date_published: date
- comment: text
- comment_author: varchar
- comment_date: date


#### Newsletter:
The newsletter section's functionality is to allow users to input, in a form, their name and email address, to be added to the newsletter subscription.

**Newsletter Model Database Fields:**
- id: bigint
- name: varchar
- email: varchar
- date_subscribed: date

### **Wireframes:**

- Mobile Wireframes:
  - Home page

![Home page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/home-mobile.jpeg?raw=true)
  - All Products page
  
![All Products page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/products-mobile.jpeg?raw=true)
  - Products detail page
  
![Products detail page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/description-mobile.jpeg?raw=true)
  - Our Blog page
  
![Our Blog page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/blog-mobile.jpeg?raw=true)
  - Newsletter page
  
![Newsletter page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/newsletter-mobile.jpeg?raw=true)
  - Account page
  
![Account page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/account-mobile.jpeg?raw=true)
  - Checkout page
  
![Checkout page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/checkout-mobile.jpeg?raw=true)
  - Sign In page
  
![Sign In page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/signin-mobile.jpeg?raw=true)
  - Join page
  
![Join page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/join-mobile.jpeg?raw=true)

- Desktop Wireframes:
  - Home page

![Home page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/home-desktop.jpeg?raw=true)
  - All Products page
  
![All Products page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/products-desktop.jpeg?raw=true)
  - Products detail page
  
![Products detail page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/description-desktop.jpeg?raw=true)
  - Our Blog page
  
![Our Blog page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/blog-desktop.jpeg?raw=true)
  - Newsletter page
  
![Newsletter page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/newsletter-desktop.jpeg?raw=true)
  - Account page
  
![Account page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/account-desktop.jpeg?raw=true)
  - Checkout page
  
![Checkout page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/checkout-desktop.jpeg?raw=true)
  - Sign In page
  
![Sign In page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/signin-desktop.jpeg?raw=true)
  - Join page
  
![Join page](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/wireframes/join-desktop.jpeg?raw=true)

### **Color Scheme:**

 The color palette was created using [https://coolors.co/]

![Color Palette](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/palette.jpg?raw=true)


I also created this color contrast grid using [https://contrast-grid.eightshapes.com/](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23000000%2C%20Black%0D%0A%23212529%0D%0A%23FFFFFF%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp), to check the contrast scored and ensure the text remains visible across the entire website and that the site is accessible to everyone.

![Color Contrast Grid](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/contrastgrid.jpg?raw=true)

### **Typography:**

I decided on using a Google font named Barlow. It features rounded, slightly condensed letterforms with a clean, geometric aesthetic. Barlow’s design is inspired by the visual style of Californian road signs, combining functionality with a friendly, approachable look.

![Typography](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/font.jpg?raw=true)

### **Technologies Used:**

* Cloud developer platform from [Gitpod](https://www.gitpod.io/).
* IDE integrated into Gitpod from [Visual Studio Code](https://code.visualstudio.com/).
* Debugging assisted by [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/).
* Version control integrated into Gitpod from [Git](https://git-scm.com/).

### **Design Tools:**

* Icon library and toolkit from [Font Awesome 5](https://fontawesome.com/).
* Favicon created on [favicon.cc](https://www.favicon.cc/).
* Showcasing the site on different devices by [Bytes](https://ui.dev/amiresponsive)
* Paint from [Microsoft](https://apps.microsoft.com/store/detail/paint/9PCFS5B6T72H?hl=en-us&gl=us)
* ERD by [drawsql.app](https://drawsql.app/)

### **Front-End:**

- ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) as the base for markup text.
- ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) for custom styling the site.
- ![Javascript](https://img.shields.io/badge/logo-javascript-blue?logo=javascript&logoColor=f5f5f5)
    - [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) for JavaScript functionality.
- ![jQuery 3.4.1](https://img.shields.io/static/v1?label=jQuery&message=3.4.1&color=0769AD&logo=jquery&logoColor=ffffff)
    - [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
- ![Bootstrap 4.6](https://img.shields.io/static/v1?label=Bootstrap&message=4.6&color=ee6e73)
    - [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Used as the front-end framework for layout and design.
- ![Stripe API](https://img.shields.io/static/v1?label=Stripe&message=API&color=008CDD&logo=stripe&logoColor=ffffff)
    - [Stripe API](https://stripe.com/docs/api?lang=python) - Used to make secured payments.
- ![Amazon AWS S3](https://img.shields.io/static/v1?label=Amazon%20AWS&message=S3&color=232F3E&logo=amazon%20aws)
    - [Amazon AWS S3](https://aws.amazon.com/) - Used to store static files and media folders and files.

### **Back-End:**

- ![Python](https://img.shields.io/static/v1?label=Python&message=3.12.2&color=blue&logo=python&logoColor=ffffff)
    - [Python 3.12.2](https://www.python.org/) is a high-level, general-purpose programming language.
- ![Django](https://img.shields.io/static/v1?label=Django&message=3.2.25&color=092E20&logo=django)
    - [Django 3.2.25](https://docs.djangoproject.com/en/3.2/) - Used as my Python web framework.
- ![Heroku](https://img.shields.io/static/v1?label=Heroku&message=PaaS&color=430098&logo=heroku)
    - [Heroku](https://www.heroku.com) is used as *"Platform as a Service"* (PaaS) for app hosting.

### **Validation and Evaluation:**

* HTML validation from [W3C](https://validator.w3.org/#validate_by_input).
* CSS validation from [Jigsaw (W3C)](https://jigsaw.w3.org/css-validator/).
* Python validation from [CI Python Linter](https://pep8ci.herokuapp.com/).
* Javascript validation from [JSHint](https://jshint.com/).
* Web page quality improvements assisted by [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)


## **Current Features Common to all pages**

### **Header Element**

* The navigation bar appears on all pages.
* In the left corner there is the logo of the website.
* Contains links to the Home, All Products, Smart Security, Smart Home Tech, Our Blog, Newsletter, Account(which is togglable and opens links to Join and Sign In) and Shopping Bag for quick navigation around the website. 
* On mobile the navbar transforms into a togglable hamburger button.

![Header Desktop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/header-desktop.jpg?raw=true)

![Header Mobile](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/header-mobile.jpg?raw=true)

## **Footer**

* Placed at the bottom of the page, it includes links to Our Policies, Contact Details as well as links to all social media accounts.
* The footer includes a copyright notice at the bottom and has the same dark background as the promotional banner under the navbar. The footer also includes a function that automatically updates the date.

![Footer Destkop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/footer-desktop.jpg?raw=true)

![Footer Mobile](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/footer-mobile.jpg?raw=true)

## **Individual Page Content features**

### **Home Page Content:**

* The homepage contains the background and a button, a short heading and a Shop Now button that takes you to the All Products page.
  
![Home Desktop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/home-desktop.jpg?raw=true)

![Home Mobile](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/home-mobile.jpg?raw=true)

### **All Products Page Content:**

* The All Products page contains all the products from both sections, the smart security products and the smart home tech products.

![All Products Desktop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/allproducts-desktop.jpg?raw=true)

### **All Smart Security Page Content:**

* The All Smart Security Page contains products from the Smart CCTV Cameras, Smart Doorbells and Smart Baby Monitors pages. The page includes also 3 buttons at the top of the page to allow the user to filter by which category they want.

![All Smart Security Desktop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/security-desktop.jpg?raw=true)

### **All Smart Home Tech Page Content:**

* The All Smart Security Page contains products from the Smart Heating, Smart Lighting, Smart Plugs and Smart Speakers pages. The page includes also 4 buttons at the top of the page to allow the user to filter by which category they want.

![All Smart Home Tech Desktop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/hometech-desktop.jpg?raw=true)

### **Our Blog Page Content:**

* The Our Blog page contains multiple articles posted by the admin of the website. Every article has just a short preview and a button that the user can press to be redirected to the full article. On the full article page, the user can leave comments as well as delete their own comment.

![Our Blog](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/blog.jpg?raw=true)

### **Newsletter Page Content:**

* The Newsletter page contains a form that users can fill to subscribe to the website's newsletter. The form has a field for name and another field for users to input their email address, as well as a subscribe button.

![Newsletter](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/newsletter.jpg?raw=true)

### **Checkout Page Content:**

* The Checkout page contains a form that users can fill with their details(name and email address), delivery details(phone number, street, town or city, county, country and postcode) and payment information. The page also displays the order summary where the users can see the products they added to their shopping bag, total price, delivery price and grand total. At the bottom of the page there are 2 buttons, one takes the user back to the shopping bag to update it and the other button completes the order.

![Checkout](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/checkout.jpg?raw=true)

### **Account Page Content:**

* If the user is not logged in, the page will not allow you to go to the account page. When the user is logged in, the page displays a form where they can update their default delivery info, and a section where they can see their previous orders.
  
![Account section](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/account.jpg?raw=true)


### **Sign In Page Content:**

* The page displays a form for the user to login.

![Sign In Desktop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/login-desktop.jpg?raw=true)

![Sign In Mobile](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/login-mobile.jpg?raw=true)

### **Join Page Content:**

* The page displays a form for the user to register a new account.

![Join Desktop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/signup-desktop.jpg?raw=true)

![Join Mobile](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/signup-mobile.jpg?raw=true)

### **Privacy Policy Page Content:**

* The Privacy Policy was generated from Termsfeed and sets out how Witty Devices collects, stores and manages the customer's data. The Privacy Policy page can be accessed from anywhere on the site via the footer area, Our Policies column.

* Witty Devices is a fictitious ecommerce store created for educational purposes only. Witty Devices is not a real store and the privacy policy is not legally binding.

### **Refunds and Returns Page Content:**

* The Refunds and Returns policy was generated from Termsfeed and sets out how Witty Devices collects, stores and manages the customer's data. Refunds and Returns page can be accessed from anywhere on the site via the footer area, Our Policies column.

* Witty Devices is a fictitious ecommerce store created for educational purposes only. Witty Devices is not a real store and the Refunds and Returns policy is not legally binding.

### **Terms and Conditions Page Content:**

* The Terms and Conditions policy was generated from Termsfeed and sets out how Witty Devices collects, stores and manages the customer's data. The Terms and Conditions page can be accessed from anywhere on the site via the footer area, Our Policies column.

* Witty Devices is a fictitious ecommerce store created for educational purposes only. Witty Devices is not a real store and the Terms and Conditions policy is not legally binding.

### **404 Error Page Content**

* The page displays a message to inform the user that the page that they were looking for is unavailable.
* Under the message displayed, there is a button that sends the user back to the Home page.

![404 Error](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/404error.jpg?raw=true)


## **Future Enhancements**

* Add special offers and discounted items.
* Send out a real newsletter email to users that subscribed.
* Allow users to add to cart straight from the products page, not having to click on each individual product and then add to cart.
* Allow users to register/login with a social media account.
* Allow users to leave reviews on the product page.

***
## **Testing Phase**

### **Testing During Development**

During the development process, I have been constantly testing the website in the following ways:

1. Manually testing each element of the page for responsiveness and accesibility via a live server opened using GitPod.

2. Published the page via GitHub pages and shared with friends and family to receive feedback.

3. Made use of Developer Tools from different Internet browsers, to continuously identify and troubleshoot any problems I encountered.

#### **Manual Testing**

**Principles:**

1. **Exploratory Testing:** Manual testing is excellent for exploratory testing, where testers actively explore the application to discover unforeseen issues and usability problems.

2. **User Experience (UX) Testing:** Manual testers can assess the application's user-friendliness, usability, and overall user experience, providing valuable insights.

3. **Ad Hoc Testing:** In situations where test cases aren't well-defined or documented, manual testers can perform ad hoc testing to identify issues.

4. **Non-Functional Testing:** Tests related to subjective criteria like aesthetics, layout, and overall look and feel are often better suited for manual testing.

**When to Deploy Manual Testing:**

- **Usability Testing:** To evaluate the user interface and overall user experience.
- **Exploratory Testing:** When new features are introduced or when test cases are not yet well-defined.
- **Complex Test Scenarios:** For intricate and multi-step test cases where human intuition is required.
- **Non-Functional Testing:** Assessing subjective aspects like aesthetics, accessibility, and human factors.

* While testing the website, I have used 4 different browsers to make sure that it is cross-compatible. The desktop browsers I have used for the tesing were:

  - Firefox
  - Google Chrome
  - Microsoft Edge
  - DuckDuckGo

- I have also asked other people to test the website, using their personal iPhones and Macbooks using Safari, since I don't have access to these devices. To which they reported that they have not encountered any bugs.

#### **Automated Testing**

**Principles:**

1. **Repeatability:** Automated tests can be executed repeatedly without any variation in their steps and expected outcomes.

2. **Consistency:** Automated tests perform the same steps and checks each time, eliminating human errors and ensuring consistent results.

3. **Efficiency:** Automated tests can run quickly and efficiently, covering a large number of test cases in a short time.

4. **Regression Testing:** Automated tests are particularly useful for regression testing, where previously tested functionality is retested to ensure that new changes have not introduced defects.

5. **Data-Driven Testing:** Automation allows for data-driven testing, where tests are executed with different sets of data to verify various scenarios.

6. **Continuous Integration/Continuous Deployment (CI/CD):** Automated tests can be integrated into the CI/CD pipeline, allowing for immediate feedback on code changes and ensuring that only high-quality code is deployed.

**When to Deploy Automated Testing:**

- **Regression Testing:** Automated tests are ideal for regularly checking existing functionality after code changes.
- **Highly Repetitive Tests:** Tasks like data validation, login/logout procedures, and API testing can be automated for efficiency.
- **Load and Performance Testing:** Automated tools can simulate a large number of users to test system performance under heavy loads.
- **Cross-Browser and Cross-Platform Testing:** Automated frameworks can be used to test web applications on different browsers and platforms.

Automated testing can be a powerful tool for catching bugs early on and ensuring that the application is working as expected. While I fully acknowledge the benefits of automated testing and the value it adds to the overall development process, due to time constraints, implementing and maintaining Jest for automated testing was not possible.

#### **User Story Testing**

During my manual testing, I have tested every user story, to ensure that the needs of the users are met.

- As a user of the website, I want to easily navigate through Witty Devices' selection of smart security products, so I can quickly find the best system to protect my home and purchase it with confidence.

  * All users can easily access the smart security products from the navbar, by clicking on the smart security option and the navigating to all smart security products: 

  ![Story1](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/story1.jpg?raw=true)

![All Smart Security Desktop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/security-desktop.jpg?raw=true)

- As a user of the website, I want to see detailed product descriptions, so I can make informed decisions about which smart home devices will best suit my needs.

  * All users are able to see detailed product descriptions after clicking on a product from the category they are interested in:

  ![Story2](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/story2.jpg?raw=true)

- As a user of the website, I want a seamless and secure checkout process, so I can complete my purchases without hassle and trust that my payment information is safe.

  * The checkout process has been simplified, so that all users can easily checkout in a secure manner. The Checkout page contains a form that users can fill with their details(name and email address), delivery details(phone number, street, town or city, county, country and postcode) and payment information. The page also displays the order summary where the users can see the products they added to their shopping bag, total price, delivery price and grand total.

  ![Story3](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/checkout.jpg?raw=true)

- As a user of the website, I want to find product recommendations and guides, so I can discover the latest smart home trends.

  * All users can find product recommendations or guides in the Our Blog section of the website.

  ![Our Blog](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/blog.jpg?raw=true)

  ![Story4](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/story4.jpg?raw=true)

- As a user of the website, I want to see a clean, responsive design that works well on both desktop and mobile, so I can browse and shop for smart devices wherever I am.

  * The website has been designed with a responsive mobile first mindset, so that it works perfectly on both mobile devices and desktops.

  ![Story5](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/amiresponsive.jpg?raw=true)

- As a user of the website, I want to filter products by features, price, and compatibility, so I can efficiently find exactly what I need without sifting through irrelevant items.

  * In each products page, the users can find a sort button so that they can sort by name, price, category and rating, both ascending and descending. Users also can select from the navbar the option to show all products by category, price or rating.

  ![Story6a](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/story6a.jpg?raw=true)

  ![Story6b](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/story6b.jpg?raw=true)

- As a user of the website, I want to be able to subscribe to a newsletter so I can be informed whenever new products come in stock.

  * All users are able to subscribe to Witty Devices' newsletter by accessing the Newsletter section of the website from the navbar and filling in the form to subscribe.

  ![Story7](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/readme/newsletter.jpg?raw=true)

#### **Functionality testing**

* Home Page and Navbar:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Witty Devices | User heads to: https://witty-devices-91c5d0b3a8c2.herokuapp.com/ | Witty Devices Home Page is loaded | ✔ |
| Witty Devices Logo | Click | User is redirected to the Home Page | ✔ |
| Search bar | Click on the search button while search bar is empty | User is redirected to All Products page, all products are displayed and toast message:"You didn't enter any search criteria!", appears | ✔ |
| Search bar | Click on the button while typing something non-existent within search bar | User is redirected to Products page while none of products are displayed but a short message is displayed:"0 Products found for "random search word"" | ✔ |
| Search bar | Click on the button while "camera" is present in the search bar | User is redirected to Products page, while 4 products are displayed as they have the word "camera" present in: name, description, brand or category fields of the product, as well as a short message saying: "4 Products found for "camera"" | ✔ |
| Search bar | Click on the button while any word in the: name, description, brand, or category fields of the product is present in the search bar | User is redirected to the Products page and the product/s are displayed with the apropriate short message | ✔ |
| My Account/Not-Authenticated | Click | Drop down menu opens with 2 options: Join and Sign In | ✔ |
| My Account/Authenticated/User | Click | Drop down menu opens with 2 options: Account and Sign Out | ✔ |
| My Account/Authenticated/Admin | Click | Drop down menu opens with 3 options: Product Management, Account and Sign Out | ✔ |
| Shopping Bag/Not-Empty | Click | User is redirected to the shopping bag page and products present in the shopping bag are displayed | ✔ |
| Shopping Bag/Empty | Click | User is redirected to the shopping bag page and a short message,"Your bag is empty.", is displayed | ✔ |
| All Products | Click | Drop-down menu opens with the available options | ✔ |
| All Products > Any available option | Click | User is redirected to the products page sorted according to the chosen option | ✔ |
| Smart Security | Click | Drop-down menu opens with the available options | ✔ |
| Smart Security > Any available option | Click | User is redirected to the products page sorted according to the chosen option | ✔ |
| Smart Home Tech | Click | Drop-down menu opens with the available options | ✔ |
| Smart Home Tech > Any available option | Click | User is redirected to the products page sorted according to the chosen option | ✔ |
| Our Blog | Click | User is redirected to the blog page. | ✔ |
| Newsletter | Click | User is redirected to the newsletter page | ✔ |

* Footer:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Privacy Policy | Click | User is redirected to the Privacy Policy page | ✔ |
| Refunds and Returns | Click | User is redirected to the Refunds and Returns page | ✔ |
| Terms and Conditions | Click | User is redirected to the Terms and Conditions page | ✔ |
| Contact Email Address | Click | User's email app opens and automatically adds the Witty Devices email address to the recipient field.| ✔ |
| Contact Phone Number | Click | User's phone app opens and automatically adds the Witty Devices phone number in the keypad field.| ✔ |
| Social Network Icons | Click | New tab opens and the user is redirected to the chosen site | ✔ |

* Authentication:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Join/Invalid Form | Click | A short message will pop up depending on the scenario, saying: "Please fill out this field.", "Please lengthen this text to 4 characters or more(you are currently using x characters)." | ✔ |
| Join/Form Valid/Email in use already | Click | A message pops up saying: "A user is already registered with this email address." | ✔ |
| Join/Form Valid | Click | User is redirected to the VERIFY YOUR E-MAIL ADDRESS page and a short toast message pops up saying: "Confirmation email sent to testmail@test.com." | ✔ |
| Confirmation Email/Confirmation Link | Click | User is redirected to the CONFIRM EMAIL ADDRESS page. There is a confirm button to click  | ✔ |
| Confirm Button | Click | User gets redirected to the Sign In page and a short toast message pops up saying: "You have confirmed testmail@test.com." | ✔ |
| Join Page/Back to Sign In Button | Click | User gets redirected to the Sign In Page | ✔ |
| Join Page/Sign In Link | Click | User gets redirected to the Sign In Page | ✔ |
| Sign In Page/Sign Up Link | Click | User gets redirected to the Sign Up Page | ✔ |
| Sign in Page/ Home button | Click | User gets redirected to the Home Page | ✔ |
| Sign In/Form Invalid/Sign In Button | Click | A short message pops up saying: "The email address and/or password you specified are not correct." | ✔ |
| Sign In/Form Valid/Sign In Button | Click | User gets redirected to the Home page and toast message pops up saying: "Successfully signed in as XXX." | ✔ |
| Sign In Page/Forgot Password Link | Click | User gets redirected to the Password Reset Page | ✔ |
| Password Reset Page/Back to Login Button | Click | User gets redirected to the Sign In Page | ✔ |
| Password Reset Page/Form Empty/Reset My Password Button | Click | A short message pops up saying: "Pleas fill out this field." | ✔ |
| Password Reset Page/Form(Email) Invalid/Reset My Password Button | Click | A short message pops up saying: "The email address is not assigned to any user account" | ✔ |
| Password Reset Page/Form Valid/Reset My Password Button | Click | Password Reset Page is rendered with the message: "We have sent you an email. Please contact us if you do not receive it within a few minutes." | ✔ |
| Sign Out Page/Cancel Button | Click | User gets redirected to the Home page | ✔ |
| Sign Out Page/Sign Out Button | Click | User gets redirected to the Home page and a short toast message pops up saying: "You have signed out." | ✔ |

* Product Management:

- This feature is available only for admins.

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| My Account/Product Management | Click | User gets redirected to the Product Management Page | ✔ |
| Product Management Page/Cancel Button | Click | User gets redirected to the All Products Page | ✔ |
| Product Management Page/Form Invalid/Add Product Button | Click | A short message will pop up saying: "Please fill out this field." | ✔ |
| Product Management Page/Form Valid/Add Product Button | Click | User gets redirected to the added product page and a short toast message pops up saying: "Successfully added product!" | ✔ |
| Non-Admin User inserts /delete/ before the product number in the address bar | Enter | User gets redirected to the Home Page, and a small toast message pops up saying: "Sorry, only store owners can do that!" | ✔ |
| Non-Admin User inserts /edit/ before the product number in the address bar | Enter | User gets redirected to the Home Page, and a small toast message pops up saying: "Sorry,only store owners can do that!" | ✔ |

* Account:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Account| Click | User gets redirected to the Account page | ✔ |
| Account Page/Edit Any field/Update Information Button | Click | User gets redirected to the same page and a short toast message pops up saying: "Profile updated successfully" | ✔ |
| Account Page/Order History/Order Number | Click | User gets redirected to the Thank You page and a short toast message pops up saying: "This is a past confirmation for order number 3DK675DB88A34A9788FB10A15112J8PM. A confirmation email was sent on the order date." | ✔ |
| Thank You Page/Back to Account Button | Click | User gets redirected to the Account Page | ✔ |
| Account/Sign Out | Click | User gets redirected to the Sign Out Page | ✔ |

* Shopping Bag:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Shopping Bag Icon In Navbar | Click | User is redirected to the Shopping Bag Page | ✔ |
| Shopping Bag Icon/Page Empty | Click | The page is rendered with a message: "Your bag is empty." | ✔ |
| Qty Button Minus/Number of item is 1 | Click | The (-) button is disabled as the number of items is 1 | ✔ |
| Arrow Down Button | Click | The (🔽) button is disabled as the number of items is 1 | ✔ |
| Qty Button Plus/Number of item is 99 | Click | The (+) button is disabled as the number of items is 99 | ✔ |
| Arrow Up Button | Click | The (🔼) button is disabled as the number of items is 99 | ✔ |
| Qty Button Minus or Plus/Number of items from 2-98 | Click | The (-) and (+) buttons are decreasing/increasing the number of items | ✔ |
| Arrow Down or Up Buttons/Number of items from 2-98 | Click | The (🔽) and (🔼) buttons are decreasing/increasing the number of items | ✔ |
| Update Button | Click | The Shopping Bag Page gets refreshed, number of items updated, and a short toast message pops up saying: "Updated Product Name quantity to 1" | ✔ |
| Remove Button | Click | The Shopping Bag page gets refreshed, the desired item is removed, and a short toast message pops up saying: "Removed Product Name from your bag" | ✔ |
| Keep Shopping Button | Click | User gets redirected to the All Products Page | ✔ |
| Secure Checkout Button | Click | User gets redirected to the Checkout Page | ✔ |

* Checkout:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Checkout Page/Form Invalid/Complete Order Button | Click | A short field message pops up saying: "Please fill out this field." | ✔ |
|Checkout Page/Form Valid But Payment Details/Complete Order Button  | Click | A short message will pop up saying: "Your card number is incomplete.", "Your card's expiration date is incomplete.", "Your card's expiration date is in the past.", "Your card's security code is incomplete.", "Your postal code is incomplete." | ✔ |
| Checkout Page/Form Valid and Payment Details/Complete Order Button | Click | User gets redirected to the Thank You Page, a short toast message pops up saying: "Order successfully processed! Your order number is DVF58D184D034C10BA9D3162AC5C289T. A confirmation email will be sent to test@gmail.com." | ✔ |
| Thank You Page/Checkout Other Products Button | Click | User gets redirected to the All Products Page | ✔ |
| Checkout Page/Not-Authenticated User/Create an account Link | Click | User gets redirected to the Sign Up Page | ✔ |
| Checkout Page/Not-Authenticated User/Login Link | Click | User gets redirected to the Sign In Page | ✔ |
| Checkout Page/Save this delivery information to my profile Checked/Complete Order Button | Click | User Personal details and Delivery details are getting saved to user My Profile Page | ✔ |

* Products:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Sort by Filtering... | Click | The page gets refreshed and sorted as desired and clicked | ✔ |
| Image of the product | Click | User gets redirected to the Product Detail Page | ✔ |
| Badge Icon under the pricture | Click | User gets redirected to the Products page but rendered items are those of the clicked badge(category)  | ✔ |
| Add to Bag Button | Click | The Page gets refreshed and a short toast message pops up saying: "Added Product Name to your bag" | ✔ |
| Edit Button(Admins Only) | Click | Admin gets redirected to the Product Management Page, a short toast alert message pops up saying: "You are editing Product Name" | ✔ |
| Delete Button(Admins Only) | Click | The Products page is refreshed and a short toast message pops up saying: "Product: Product Name has been deleted!" | ✔ |
| Scroll Down | Scroll | User scrolls down the page, Back to the top Button appears | ✔ |
| Back to the Top Button | Click | The Page gets scrolled back to the top | ✔ |

* Product Detail:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Product Detail Page/ Arrow back Button(⬅) | Click | User gets redirected to the previous page | ✔ |
| Product Image | Click | New tab opens with the S3 bucket address | ✔ |
| Badge Icon under the pricture | Click | User gets redirected to the Products page but rendered items are those of the clicked badge(category)  | ✔ |
| Edit Button(Admins Only) | Click | Admin gets redirected to the Product Management Page, a short toast alert message pops up saying: "You are editing Product Name" | ✔ |
| Delete Button(Admins Only) | Click | The Products page is refreshed and a short toast message pops up saying: "Product: Product Name has been deleted!" | ✔ |
| Keep Shopping Button | Click | User gets redirected to the All Products Page | ✔ |
| Add to Bag Button | Click | The Page gets refreshed and a short toast message pops up saying: "Added Product Name to your bag" | ✔ |
| Heart Icon | Click | The Products is added to the Wishlist, a short toast message pops up saying: "Product Name added to Wishlist!" | ✔ |
| Sign in to review Link/Non-Authenticated User | Click | User gets redirected to the Sign In Page | ✔ |
| Submit Review Button/Review Form Invalid | Click | A short field message pops up saying: "Please fill out this field" | ✔ |
| Submit Review Button/Review Form Valid | Click | A short toast message pops up saying: "Thank you! Review submitted." | ✔ |
| Update Review Button/Review Form Invalid | Click | A short field message pops up saying: "Please fill out this field" | ✔ |
| Update Review Button/Review Form Valid | Click | A short toast message pops up saying: "Thanks! Your review has been updated." | ✔ |

* Our Blog:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Our Blog | Click | User gets redirected to the Our Blog page | ✔ |
| Our Blog/Read More button | Click | User gets redirected to the article page | ✔ |
| Our Blog/Read More button/Go Back button | Click | User gets redirected to the main Blog page | ✔ |
| Our Blog/Read More button/Submit Comment button | Click | User adds a comment underneath the article page and the page gets refreshed | ✔ |
| Our Blog/Read More button/Submit Comment button/Delete button | Click | User deletes his own comment and the page gets refreshed | ✔ |

* Newsletter:

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Newsletter | Click | User gets redirected to the Newsletter page | ✔ |
| Subscribe Now Button Invalid | Click | A short field message pops up saying: "Please fill out this field" | ✔ |
| Subscribe Now Button Invalid/Same Email address | Click | A short field message pops up when using an email address that has been used before saying: "Subscriber with this Email already exists." | ✔ |
| Subscribe Now Button Valid | Click | A short toast message pops up saying: "You have successfully subscribed" | ✔ |

* Privacy Policy: 

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Privacy Policy Page/Back to Home Page Button | Click | User gets redirected to the Home Page | ✔ |
| Privacy Policy Page/Privacy Policy Generator Link | Click | User gets redirected to the: https://www.termsfeed.com/privacy-policy-generator/ | ✔ |
| Privacy Policy/TermsFeed Cookies website Link | Click | User gets redirected to the: https://www.termsfeed.com/blog/cookies/#What_Are_Cookies | ✔ |
| Privacy Policy Page/https://witty-devices-91c5d0b3a8c2.herokuapp.com/ Link | Click | User gets redirected to the Home Page of Witty Devices site | ✔ |

* Returns and Refunds: 

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Returns and Refunds Page/Back to Home Page Button | Click | User gets redirected to the Home Page | ✔ |
| Returns and Refunds Page/Returns and Refunds Generator Link | Click | User gets redirected to the: https://www.termsfeed.com/return-refund-policy-generator/ | ✔ |
| Returns and Refunds Page/https://witty-devices-91c5d0b3a8c2.herokuapp.com/ Link | Click | User gets redirected to the Home Page of Witty Devices site | ✔ |

* Terms and Conditions: 

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Terms and Conditions Page/Back to Home Page Button | Click | User gets redirected to the Home Page | ✔ |
| Terms and Conditions Page/Terms and Conditions Generator Link | Click | User gets redirected to the: https://www.termsfeed.com/terms-conditions-generator/ | ✔ |
| Terms and Conditions Page/https://witty-devices-91c5d0b3a8c2.herokuapp.com/ Link | Click | User gets redirected to the Home Page of Witty Devices site | ✔ |

* All the links, buttons and forms work as expected, with no errors.

#### **Solved and Known Bugs:**

* Solved bugs: 

    - An early bug encountered was when opening a blog article, it would not appear fully, but this was immediately fixed with some custom css.

    ![Solved Bug](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/bug1.jpg?raw=true)


* Known bugs:

    - An existing bug that I am still working on is with the footer not sticking to the bottom on some pages on the desktop view(on mobile it still looks fine). The affected pages are the 404 page and the Empty Shopping Bag page.

    ![Known Bug](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/bug2.jpg?raw=true)


### **Testing After Development**

#### **Validators**

#### ***HTML*** - <https://validator.w3.org/nu/>

- All pages return no error.

![HTML results](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/HTMLvalidator.jpg?raw=true)

#### ***CSS*** - <https://jigsaw.w3.org/css-validator/>

- All pages tested, no issues found.

![CSS results](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/CSSvalidator.jpg?raw=true)

![CSS validator badge](https://jigsaw.w3.org/css-validator/images/vcss)

#### ***JSHint*** - <https://jshint.com/>

![JSHint results](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/jshint.jpg?raw=true)

#### ***Python linter*** - <https://pep8ci.herokuapp.com/>

![Python linter results](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/PYTHONvalidator.jpg?raw=true)

#### **PageSpeed Insights**

- All PageSpeed Insights tests have been made while in incognito mode to avoid any browser extensions interference.
- I have asked several people to run these tests from their own devices as well, and they were getting similar scores.

![PageSpeed Insights Desktop](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/PageSpeedDesktop.jpg?raw=true)

![PageSpeed Insights Mobile](https://github.com/RazvanTr10/Witty-Devices/blob/main/documentation/testing/PageSpeedMobile.jpg?raw=true)
***

## **Deployment**

### Making a Local Clone to create project

- Find the GitHub Repository.
- Click the green **Code** button.
- Copy the **.git link** shown.
- In Gitpod, change the directory to the location you would like the cloned directory to be located.
- Type **git clone**, and paste the link you copied in step 3.
- Press Enter to have the local clone created.


A live version of the site is deployed to [Heroku](https://www.heroku.com/) and can be found here: [Witty Devices](https://witty-devices-91c5d0b3a8c2.herokuapp.com/).

### PostgreSQL database from Code Institute

- ElephantSQL free database is shutting down, so I went with the database Code Institute provided for the students.
- To make the database for the project, the steps are next:
    - First go to [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/), enter your email address and click submit.

    - Your database will be generated automatically and you will receive an email with all the information about your database.

    - Within the email, you will have a link to the dashboard of the created database. Here you can see all of the needed information about your database or delete them if you'd like to. After you click the **Info** button, a list with all the needed information will pop up.


### Heroku Deployment

#### Preparation

- Before the deployment, the following steps were taken to prepare the application for the deployment on Heroku:

- The setting **DEBUG** in the settings.py has to be set to **FALSE**. 
- It was achieved by the next lines:
- Within **settings.py**:
    ````
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
          import env
    ````
    ````
      DEBUG = 'DEVELOPMENT' in os.environ
    ````
- Within **env.py**:
    ````
      os.environ["DEVELOPMENT"] = 'False'
    ````
- Allow Heroku as host: In **settings.py** add **ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']**
- All the dependencies were stored in the requirements.txt file with the command **pip3 freeze --local > requirements.txt**.
- The start command for the application **web: gunicorn witty_devices.wsgi:application** was stored in a Procfile.

#### Deployment

* Go to [Heroku](https://id.heroku.com/login), create account if you don't have and log in.

* Head to the dashboard and click **New**, then **Create new app**

* Give your app a name and select the region. After that click on **Create app**.

* Go to the **Settings** tab which you can find at the top of the Heroku page and under the **Config Vars** set your Key/Value Pairs.

    ````
    ENVIRONMENT=
    SECRET_KEY=
    DATABASE_URL=
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    EMAIL_HOST_USER=
    EMAIL_HOST_PASS=
    STRIPE_PUBLIC_KEY=
    STRIPE_SECRET_KEY=
    STRIPE_WH_SECRET=
    USE_AWS=
    ````

* Go to the **Deployment** tab at the top of the Heroku page and under **Deployment method** click on **GitHub**. After that, under the **Deployment method** section there is the **Connect to GitHub** section where you need to find your repository and then click **Connect**. Under the **Connect to GitHub** section you can find the **Automatic deploys** section, and here click on **Enable Automatic Deploys**.

### Amazon - AWS Hosting

- For this project I used [AWS](https://aws.amazon.com) to store media and static files online.

- Create an AWS account and log in. Once you are on the **AWS Management Console** page, follow these next steps:

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name) and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

````shell
	[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
````

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click `Add Statement`
	- Click `Generate Policy`
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Version": "2012-10-17",
      "Id": "Policy111111111111",
      "Statement": [
				{
					"Sid": "Stmt11111111111",
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::bucket-name/*"
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click `Save`.
- From the **Access Control List (ACL)** section, click **Edit** and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled**.


#### IAM

From the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
- Suggested Name: **manage-witty-devices** (manage + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the **AmazonS3FullAccess** policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::bucket-name",
						"arn:aws:s3:::bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Suggested Name: **witty-device-policy** (site name-policy)
	- Click **Create Policy**.
- From **User Groups**, click your **manage-witty-devices**.
- Click **Attach Policy**.
- Search for the policy you've just created ("witty-devices-policy") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: **wittydevices-staticfiles-user** (site name + staticfiles-user)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: **manage-wity-devices**
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- **AWS_ACCESS_KEY_ID** = **Access key ID**
	- **AWS_SECRET_ACCESS_KEY** = **Secret access key**

#### Final Setup

- The **DISABLE_COLLECTSTATIC** within Heroku Config Vars can be removed now, as AWS will handle the static files from now on.
- Within you **S3** Bucket, create a new folder called **media**.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe

- Stripe's API is used to handle payments. To setup Stripe follow next steps:

  - Create if you don't have and Log In to a Stripe account.
  - In the Stripe Dashboard -> **Get your test API keys.**
  - Add your **STRIPE_PUBLIC_KEY** and **STRIPE_SECRET_KEY** to your env.py, connect to your settings.py using your environment variables and then enter them into your project's Heroku Config Vars.
  - Including Stripe's Webhooks creates a failsafe if a customer exits the page during payment authorisation. In Stripe's Dashboard -> **Developers** -> **Webhooks** -> **Add Endpoint**: 'herokuapp url/checkout/wh'
  -  Choose **Retrieve all events** -> **Add Endpoint**.
  -  Add new key **STRIPE_WH_SECRET** to env.py, settings.py and Heroku Config Vars as before.


### Google Mail API

- Setup a Gmail Account that will be used to hold and store the emails for your project.
- Log In and navigate to **Settings** -> **See All Settings** -> **Accounts and Import** -> **Other Google Account settings**
- Activate 2-Step Verification
- Once verified access **App Passwords** -> enter a name for the password.(e.g. Django-Project Name)
- Click **Create** -> copy the 16 digit password that is generated.
- In your **settings.py** add the following Email Settings:
````
# Sending Emails
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'wittydevices@gmail.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
````  
- Add `EMAIL_HOST_PASS`, `EMAIL_HOST_USER` to your Heroku Config Vars.


## **Credits**

### **General reference:**

Heroku deployment instructions from Code Institute video tutorial

Readme styling from Tim Nelson's project [Unicorn Attractor](https://github.com/TravelTimN/ci-milestone05-fsfw)

Markdown Cheatsheet from [Adam Pritchard](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#html)

### **Content:**

- **Background** photo by <a href="https://unsplash.com/@jakubzerdzicki?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Jakub Żerdzicki</a> on <a href="https://unsplash.com/photos/a-laptop-computer-sitting-on-top-of-a-table-_0T3hgs3lig?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

- Descriptions of products were created by using [ChatGPT](https://chatgpt.com/)

- Images of products have either been created by using AI tools or taken from [Temu](https://temu.com), but modified as to not have any copyright infringement.