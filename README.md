# Little White Dress

Little White Dress (LWD) is a website developed as part of a Portfolio Project for my Full Stack Software Development course delivered by Code Institute. The idea was born out of a real-world need; a close friend who is a wedding planner with a dream to open their own wedding dress store.

A visitor to the LWD website can easily browse the products on sale, make a booking to attend the store and try on dresses, and join a community of brides who share recommendations.

![Image of ]()

[Visit the  live website here]()

<br>

## Contents
----

### [User Experience (UX)](#user-experience-ux-1)
- [Purpose](#purpose)
- [User Stories](#user-stories)
  - [First Time Visitors](#first-time-visitor-goals)
  - [Returning Visitors](#returning-visitor-goals)
  - [Frequent Users](#frequent-visitor-goals)

### [Design](#design-1)
- [Colour Scheme](#colour-scheme)
- [Typography](#typography)
- [Imagery](#imagery)
- [Wireframes](#wireframes)

### [Database and Logic](#database-and-logic-1)
- [User Journey](#user-journey)
- [Epics](#epics)
- [Kanban Board](#kanban-board)
- [Database](#database)

### [Project Structure](#project-structure-1)
- [Apps](#apps)
  - [Product](#products)
  - [Customer](#customer)
  - [Contact](#contact)
  - [Recommendations](#recommendations)
  - [Appointment](#appointment)


### [Features](#features-1)
- [Existing Features](#existing-features)
  - [Homepage](#homepage)
  - [Next page](#next_page)
- [Accessibility](#accessibility)
- [Future Features](#future-features)

### [Technologies](#technologies-1)

### [Version Control](#version-control-1)

### [Deployment](#deployment-1)

### [Testing](#testing-1)
- [Function Testing](#function-testing)
- [User Story Testing](#user-story-testing)
- [Lighthouse](#lighthouse)
- [Validator Testing](#validator-testing)
- [Bugs](#bugs)

### [Credits](#credits-1)
- [Resources](#resources)
- [Acknowledgements](#acknowledgements)

<br>

----

<br>

## User Experience (UX)
### **Purpose**

As the Little White Dress website has been created for a business *idea*, the UX and UI have been developed closely with the prospective business owner's input throughout. A strong brand identity has been central to decisions around typography, imagery, and colours to create a feeling of sophisticated luxury but with a welcoming warmth.

The main purposes of the webpage is to provide visitors with the ability to view products for sale, book appointments, and join a community of other brides.

The site has been built with a mobile-first responsive design. The needs of the user and the brand identity have been kept at the forefront of the design process.

<br>

### User Stories
### **Client Goals**
- As site admin I want to be able to upload and remove any dress products from the site
- As a site admin I want to be able to view any enquiries sent via the website contact form
- As site admin I want to be able to view any bookings by customers to come and try on dresses
- As site admin I want to be able to amend any bookings by customers to come and try on dresses
- As site admin I want to be able to cancel any bookings by customers to come and try on dresses
- The website should create a strong brand identity
- The website should be responsive across different devices

<br>

### **First Time Visitor Goals** 
- As a first time user I want to browse available wedding dresses
- As a first time user I want to book an appointment to try on dresses
- As a first time user I want to save my favourite dresses so I can refer back to them later
- As a first time user I want to be able to contact the store
- As a first time user I want to be able to filter my search by dress style and price
- As a first time user I want to view details about the dress such as price and available sizes
- As a first time user I want to be able to find recommendations for other wedding services in the bridal community


<br>

### **Returning Visitor Goals**
- As a returning user I want to see my favourite dresses
- As a returning user I want to view any current bookings I have to try on dresses
- As a returning user I want to amend any current bookings I have to try on dresses
- As a returning user I want to cancel any current bookings I have to try on dresses
- As a returning user I want to be able to post recommendations for other wedding services to the bridal community


<br>


----

## Design
### **Colour Scheme**
The colour scheme for this site has been kept fairly simple with just a couple of really key shades. This is in keeping with the sophisticated and clean brand identity.

The main colour (F4E9E5) was selected as it reflects the soft feminine feel that relates to being 'bridal'.


The colour palette was created using the [Coolors](https://coolors.co/) website.

![Image of colour palette](readme_assets/coolor_palette.webp)

<br>

### **Typography**
All fonts were sourced from [Google Fonts](https://fonts.google.com/)
#### Logo
The font used for the logo is 'Julius Sans One'

![Image of the Little White Dress logo](readme_assets/lwd_logo.webp)

#### Web Content
The font used for the body content throughout the site is called 'Crimson Text'


<br>

### **Imagery**
All images were sourced from [Adobe Stock](https://stock.adobe.com/uk/) and [iStock Photo](https://www.istockphoto.com/), with the exception of the owner image on the contact page. This image is a personal image belonging to Samantha Landy, who gave permission for it's use on this site.

Images have been specifically chosen to be in keeping with the brand identity. They are light, clean and professional.

The Favicon was also deisnged in this way and has been generated using the website colour #F4E9E5 and the logo font 'Julius Sans One'. It was created on [Favicon.io](https://favicon.io/).

![Image of Favicon](readme_assets/favicon.webp)

<br>

### **Wireframes**
[Balsamiq Wireframing Software](https://balsamiq.com/) was used to create the wireframes.
<details>
<summary>Homepage</summary>

![Wireframe image of homepage design](readme_assets/index1.webp)

<br>

![Wireframe image of homepage design](readme_assets/index2.webp)
</details>

<details>
<summary>About</summary>

![Wireframe image of about page design](readme_assets/about.webp)
</details>

<details>
<summary>Contact</summary>

![Wireframe image of contact page design](readme_assets/contact.webp)
</details>

<details>
<summary>Products</summary>

![Wireframe image of products page design](readme_assets/products.webp)
</details>

<details>
<summary>Product Details</summary>

![Wireframe image of product details page design](readme_assets/product_detail.webp)
</details>

<details>
<summary>Profile</summary>

![Wireframe image of profile page design](readme_assets/profile.webp)
</details>

<details>
<summary>Appointments</summary>

![Wireframe image of appointments page design](readme_assets/appointments.webp)
</details>

<br>


For a full PDF of all wireframes (mobile, tablet, desktop) click [here](readme_assets/wireframes_all.pdf).

----

## Database and Logic

Careful consideration was taken in the planning stages of this project. Initial user journeys were mapped out for both the admin and general user. From these an ER Diagram was created.

### **User Journey**
![Image of user journey map](readme_assets/lwd_user_journey.webp)

<br>

![Image of admin journey map](readme_assets/lwd_admin_journey.webp)

<br> 

### **Database**
![Image of entity relationship diagram](readme_assets/lwd_erd.webp)

<br>

### **Epics**
![Image of epics chart](readme_assets/lwd_epics.webp)

### **Kanban Board**
A Kanban approach was used to keep track of the flow of the project. Once User Stories were set up in the Project they were assigned to EPICs and began the project journey in the 'ToDo' column. As development progressed these moved through 'In Progress' to finally 'Done'. An additional column was added 'Unable to implement' for any features that were not successfully completed.

[You can visit the project board here](https://github.com/users/llewellynksj/projects/5/views/1)

Below is an example part way through the site build:

![Image of kanban project hub from Github](readme_assets/kanban.webp)

----

## Project Structure
### **Apps:**
Little White Dress has a total of 5 Apps. These are:
* Product
* Customer
* Contact
* Recommendations
* Appointment

These are outlined with their corresponding models below.

#### PRODUCT

  * Holds the database for any products displayed on the website
  * Displays the homepage and various product views
  * Adds liked products to customer record

Models:

![Product Model](readme_assets/product.webp)

![Category Model](readme_assets/category.webp)
<br>

#### CUSTOMER

  * Holds the database for all customer profiles
  * Displays the customer profile pages and all update pages related to the user
  * Holds the templates for all customer and user related pages including registration

Models:

![Customer Model](readme_assets/customer.webp)

<br>

#### CONTACT

  * Holds the database for the store's contact details and for any enquiries made via the contact form
  * Displays the contact page

Models:

![Contact Detail Model](readme_assets/contact_detail.webp)

![Enquiry Model](readme_assets/enquiry.webp)

<br>

#### RECOMMENDATIONS

  * Holds the database for all recommendations made in the brides community section of the website
  * Displays all recommendations including specific recommendations to logged in users
  * Enables CRUD functionality:
    - Create a Recommendation
    - Read all community Recommendations
    - Update and amend own Recommendations
    - Delete own Recommendations

Models:

![Recommendation Model](readme_assets/recommendation.webp)

<br>

#### APPOINTMENT

  * Holds the database for all appointments that are made
  * Displays the appointment booking and confirmation pages
  * Enables CRUD functionality:
    - Create an Appointment
    - Read/view all booked Appointments
    - Update and reschedule Appointments
    - Delete/cancel Appointments

Models:

![Appointment Model](readme_assets/appointment.webp)

----

## Features
### **Existing Features**


<br>

### **Accessibility**
In addition to being best practice, having an accessible website is extremely high on the list of requirements for the target audience. Close attention has been paid to the following in order to ensure the site is as accessible as possible:
- Clear and simple font styling, avoiding any cursive or calligraphic scripts.
- Contrasting colour scheme, but avoiding colours that are too bold.
- Use of semantic HTML
- Ensuring all images have an alt description for screen readers or where the image cannot be loaded. Also ensuring that these are as descriptive as possible.

<br>

### **Future Features**
In the future there are features and developments that it would be useful to consider adding to create an even better user experience of this website. They include:

- 

<br>

----

## Technologies
### **Languages Used**
This website has been written in .

<br>

**Frameworks, Libraries and Programs Used**
- 

<br>

----

## Version Control
Version control has been maintained using Git. The code written for this website has been updated via regular commits to Github. These serve as a record of development and changes made.

The commit history can be viewed [here]()

<br>

----

## Deployment

<br>

----

## Testing
Testing was performed across a range of devices, including:
- 

### **Function Testing**

| Page | Test | Successfully Completed |
| :----| :---| :----------------------:|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


<br>

### **User Story Testing**

| Client Goal | Solution | Tested & Successfully Completed |
| :----| :---| :----------------------:|
|   |  |  |
|   |  |  |
|   |  |  |
|   |  |  |
|   |  |  |

<br>

| First Time Visitor Goal | Solution | Tested & Successfully Completed |
| :----| :---| :----------------------:|
|   |  |  |
|   |  |  |
|   |  |  |
|   |  |  |

<br>

| Returning Visitor Goal | Solution | Tested & Successfully Completed |
| :----| :---| :----------------------:|
|  |  |  |
|  |  |  |
|  |  |  |

<br>

| Frequent Visitor Goal | Solution | Tested & Successfully Completed |
| :----| :---| :----------------------:|
|  |  |  |
|  |  |  |
|  |  |  |

<br>

### **Lighthouse**

For Mobile Devices
<details>
<summary>Homepage</summary>

![Screenshot of Lighthouse testing for homepage on mobile devices](readme_assets/lighthouse/homepage_mobile.webp)
</details>
<details>
<summary>All Products</summary>

![Screenshot of Lighthouse testing for All Products on mobile devices](readme_assets/lighthouse/all_styles_mobile.webp)
</details>
<details>
<summary>Category Products</summary>

![Screenshot of Lighthouse testing for Category Products on mobile devices](readme_assets/lighthouse/category_mobile.webp)
</details>
<details>
<summary>Product Detail</summary>

![Screenshot of Lighthouse testing for Product Detail on mobile devices](readme_assets/lighthouse/product_detail_mobile.webp)
</details>
<details>
<summary>About</summary>

![Screenshot of Lighthouse testing for About Us on mobile devices](readme_assets/lighthouse/about_mobile.webp)
</details>
<details>
<summary>Contact</summary>

![Screenshot of Lighthouse testing for Contact Us on mobile devices](readme_assets/lighthouse/contact_mobile.webp)
</details>
<details>
<summary>Register</summary>

![Screenshot of Lighthouse testing for Registration on mobile devices](readme_assets/lighthouse/register_mobile.webp)
</details>
<details>
<summary>Login</summary>

![Screenshot of Lighthouse testing for Login on mobile devices](readme_assets/lighthouse/login_mobile.webp)
</details>
<details>
<summary>Profile</summary>

![Screenshot of Lighthouse testing for Profile on mobile devices](readme_assets/lighthouse/profile_mobile.webp)
</details>
<details>
<summary>Settings</summary>

![Screenshot of Lighthouse testing for Settings on mobile devices](readme_assets/lighthouse/settings_mobile.webp)
</details>
<details>
<summary>Recommendations</summary>

![Screenshot of Lighthouse testing for Community Recommendations on mobile devices](readme_assets/lighthouse/community_mobile.webp)
![Screenshot of Lighthouse testing for My Recommendations on mobile devices](readme_assets/lighthouse/my_recs_mobile.webp)
![Screenshot of Lighthouse testing for Add Recommendation on mobile devices](readme_assets/lighthouse/add_rec_mobile.webp)
</details>
<details>
<summary>Appointments</summary>

![Screenshot of Lighthouse testing for My Appointments on mobile devices](readme_assets/lighthouse/my_appointments_mobile.webp)
![Screenshot of Lighthouse testing for Book Appointment on mobile devices](readme_assets/lighthouse/book_appt_mobile.webp)
</details>
<br>

For Desktop
<details>
<summary>Homepage</summary>

![Screenshot of Lighthouse testing for homepage on desktop](readme_assets/lighthouse/homepage_desktop.webp)
</details>
<details>
<summary>All Products</summary>

![Screenshot of Lighthouse testing for All Products on desktop](readme_assets/lighthouse/all_styles_desktop.webp)
</details>
<details>
<summary>Category Products</summary>

![Screenshot of Lighthouse testing for Category Products on desktop](readme_assets/lighthouse/category_desktop.webp)
</details>
<details>
<summary>Product Detail</summary>

![Screenshot of Lighthouse testing for Product Detail on desktop](readme_assets/lighthouse/product_detail_desktop.webp)
</details>
<details>
<summary>About</summary>

![Screenshot of Lighthouse testing for About Us on desktop](readme_assets/lighthouse/about_desktop.webp)
</details>
<details>
<summary>Contact</summary>

![Screenshot of Lighthouse testing for Contact Us on desktop](readme_assets/lighthouse/contact_desktop.webp)
</details>
<details>
<summary>Register</summary>

![Screenshot of Lighthouse testing for Registeration on desktop](readme_assets/lighthouse/register_desktop.webp)
</details>
<details>
<summary>Login</summary>

![Screenshot of Lighthouse testing for Login on desktop](readme_assets/lighthouse/login_desktop.webp)
</details>
<details>
<summary>Profile</summary>

![Screenshot of Lighthouse testing for Profile on desktop](readme_assets/lighthouse/profile_desktop.webp)
</details>
<details>
<summary>Settings</summary>

![Screenshot of Lighthouse testing for Settings on desktop](readme_assets/lighthouse/settings_desktop.webp)
</details>
<details>
<summary>Recommendations</summary>

![Screenshot of Lighthouse testing for Community Recommendations on desktop](readme_assets/lighthouse/community_desktop.webp)
![Screenshot of Lighthouse testing for My Recommendations on desktop](readme_assets/lighthouse/my_recs_desktop.webp)
![Screenshot of Lighthouse testing for Add Recommendation on desktop](readme_assets/lighthouse/add_rec_desktop.webp)
</details>
<details>
<summary>Appointments</summary>

![Screenshot of Lighthouse testing for My Appointments on desktop](readme_assets/lighthouse/my_appointments_desktop.webp)
![Screenshot of Lighthouse testing for Book Appointment on desktop](readme_assets/lighthouse/book_appt_desktop.webp)
</details>

<br>

### **Validator Testing**
HTML
<details>
<summary>Homepage</summary>

![Screenshot of WC3 testing for homepage]()
</details>
<details>
<summary>Dates Page</summary>

![Screenshot of WC3 testing for next page]()
</details>
<details>

<br>

CSS
<details>
<summary>Stylesheet</summary>

![Screenshot of W3C Jigsaw testing for CSS Stylesheet]()
</details>

  <br>

### **Bugs**
  
  | Raised by | Bug | Solution |
  | :---      | :---| :---     |
  |  |  |  |
  |  |  |  |
  |  |  |  |
  |  |  |  |
  |  |  |  |
  |  |  |  |

<br>

----

## Credits
### **Resources**
- 

<br>

### **Acknowledgements**
