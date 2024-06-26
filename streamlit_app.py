import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Dheeraj Gambhir, Senior Manager- Quality Engineering.
''')

image = Image.open('DG.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- 17+ years of experience in Quality Management with a soundtrack record of delivering test solutions globally. Proven ability to meet deadlines, coordinate work, implement automated solutions, and test strategies. Having effective leadership, negotiating and communication skills. 
- Spearheading a high-performing QA team, ensuring the delivery of top-notch software products.
- Possessed in-depth understanding of product architecture and its impact on feature and system testing.
- Proficient in utilizing a wide range of programming languages and frameworks, including Java, JavaScript, C#, Selenium, Appium, TestNG, and Cucumber.
- Experience in designing Automation Framework using open-source tools and possess extensive experience with DevOps technologies such as AzureDevOps, Docker, Terraform, and Jenkins.
- Spearheaded successful cloud migration projects and developed a long-term QA vision to implement industry best practices.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://softwaretestingjournal.com/" target="_blank">Dheeraj Gambhir</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications-and-awards">Certifications And Awards</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**M.Sc. in Computer Science**','2002-2006')


#####################
st.markdown('''
## Work Experience
''')

txt('**Sr. Manager - Quality Engineering (SDET) at Tavant**','2006-Present')
st.markdown('''
- Ensure test automation is followed and test scripts are executed on a nightly basis by deploying continuous integration model. Understand how all elements of the application ecosystem work together and developing QA approaches that fit the overall strategy.
- Actively takes part in the talent hiring process as well as help employees to plan and develop their career path.
- Coordinate and administrate all products test activities, ensuring day-to-day delivery of testing operations of QA team of 20- 25 members.
- Set and reflect on OKR on an annual basis to ensure productivity strategically matches the organization's direction.
''')

#####################
st.markdown('''
## Certifications And Awards
''')
txt('**Certifications**','')
st.markdown('''
- Microsoft Azure Fundamentals (AZ -900)
- Prince 2 Foundation and Practitioner Certified
- ISTQB Certified Professional (ITB)
- CSTM Certified Professional (GAQM)
''')

txt('**Awards**','')
st.markdown('''
- Tavant Excellence Award for Customer Focus in 2022.
- Shining Star Award for conducting various QE trainings in 2021.
- Tavant Excellence Award for Agility in 2013.
- Spot Award for leading API automation CoE in 2020.
''')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Java`, `C#`, `JavaScript`')
txt3('Database', '`MySQL`, `Oracle`')
txt3('Version Controlling', '`Github`, `Bitbucket`')
txt3('Automation', '`Selenium`, `Playwright`, `RestAssured`, `RestSharp`, `TestNG`,`JUnit`, `AzureDevOps`,`Postman`, `Karate`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/dheerajgambhir/')
txt2('Twitter', 'https://twitter.com/dheerajgambhir')
txt2('GitHub', 'https://github.com/dgambhir01')

