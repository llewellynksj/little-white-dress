# Little White Dress

## Testing File

![Image of website across different devices](readme_assets/responsive-dark.webp)

[Visit the  live website here](https://little-white-dress-ad94e830edef.herokuapp.com/)

<br>

## Contents

### [Testing](#testing-1)
- [Function Testing](#function-testing)
- [User Story Testing](#user-story-testing)
- [Lighthouse](#lighthouse)
- [Validator Testing](#validator-testing)
- [Bugs](#bugs)

<br>

----

<br>

## Testing
Testing was performed across a range of devices, including:
- MacBook Air M1
- Nothing Phone (1)
- iPhone 15 Plus

### **Function Testing**

| Page | Test | Successfully Completed |
| :----| :---| :----------------------:|
| All | Logo text links back to homepage | Yes |
| All | Navigation links go to relevant page | Yes |
| All | Navigation menu remains fixed at top of page on scroll | Yes |
| All | Social media icons in footer link to external sites, opening in new tabs | Yes |
| All | Call to action buttons link to relevant page | Yes |
| All | External links open to correct page and in a new tab | Yes |
| All | Images and text flex responsively | Yes |
| Contact | Form submits | Yes |
| Contact | Submitted form sends email | Yes |
| Register | Form creates new user | Yes |
| Login | Registered user can login successfully | Yes |
| Logout | Registered user can logout | Yes |
| Logout | Message is displayed on logout | Yes |
| Products/Profile | Favourited items are saved and appear on User's profile page | Yes |
| My Appointments | Booked appointments are visible to the User | Yes |
| Book Appointment | Form submits successfully | Yes |
| Book Appointment | Date that falls on a store closed day cannot be booked | Yes |
| Book Appointment | Date in the past cannot be booked | Yes |
| Book Appointment | A date and time that already exists in the database cannot be booked | Yes |
| My Appointments | Booked appointments can be rescheduled and cancelled | Yes |
| My Recommendations | Recommendations added by User are displayed | Yes |
| My Recommendations | Recommendations added by User can be amended and deleted | Yes |
| Add Recommendation | Form submits successfully | Yes |


<br>

### **User Story Testing**

| Client Goal | Solution | Tested & Successfully Completed |
| :----| :---| :----------------------:|
| As site admin I want to be able to upload and remove any dress products from the site | Using the Product model database this is possible via the admin portal | Yes |
| As a site admin I want to be able to view any enquiries sent via the website contact form | Enquiries sent via the contact form are accessible via the admin portal and are also emailed to the store's gmail address | Yes |
| As site admin I want to be able to view any bookings by customers to come and try on dresses | Using the Appointment model database this is accessed via the admin portal | Yes |
| As site admin I want to be able to amend any bookings by customers to come and try on dresses | Using the Appointment model database this is accessed via the admin portal | Yes |
| As site admin I want to be able to cancel any bookings by customers to come and try on dresses | Using the Appointment model database this is accessed via the admin portal | Yes |
| The website should create a strong brand identity | Through thought out use of colours, fonts and imagery | Yes |
| The website should be responsive across different devices | Using devtools and test users this was tested across a range of devices | Yes |

<br>

| First Time Visitor Goal | Solution | Tested & Successfully Completed |
| :----| :---| :----------------------:|
| As a first time user I want to browse available wedding dresses | Users can look at the dresses via the 'All Styles' button or by choosing a category | Yes |
| As a first time user I want to book an appointment to try on dresses | Various call to action buttons direct the User to register/login to book an appointment | Yes |
| As a first time user I want to save my favourite dresses so I can refer back to them later | Each product has a 'Favourite' button on their product details page. If a User is not registered they will be directed to register first | Yes |
| As a first time user I want to be able to contact the store | Address, phone and email are provided as well as a contact form | Yes |
| As a first time user I want to be able to filter my search by dress style and price | Due to time constraints this feature was not implemented but is planned for a future deploment | No |
| As a first time user I want to view details about the dress such as price and available sizes | The individual product detail page lists all necessary information | Yes |
| As a first time user I want to be able to find recommendations for other wedding services in the bridal community | A sample of recommendations are given on the homepage. If a User is not registered and wants to see more recommendations they are directed to first login | Yes |

<br>

| Returning Visitor Goal | Solution | Tested & Successfully Completed |
| :----| :---| :----------------------:|
| As a returning user I want to see my favourite dresses | When a User clicks on the Favourite button this is saved to their Profile until they remove it | Yes |
| As a returning user I want to view any current bookings I have to try on dresses | The 'My Appointments' page displays any current appointment bookings | Yes |
| As a returning user I want to amend any current bookings I have to try on dresses | Accessed via the 'My Appointments' page | Yes |
| As a returning user I want to cancel any current bookings I have to try on dresses | Accessed via the 'My Appointments' page | Yes |
| As a returning user I want to be able to post recommendations for other wedding services to the bridal community | Registered Users can do this via the Community section | Yes |

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

![Screenshot of WC3 testing for ]()
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