from pathlib import Path
import streamlit as st
from PIL import Image

# ---- PATH SETTINGS ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd() 
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Lucas_Morais_-_Software_Engineer.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
recommendation_letter = current_dir / "assets" / "recommendation_letter.pdf"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Lucas Morais"
PAGE_ICON  = "	:male-technologist:"
NAME = "Lucas Morais"
DESCRIPTION = """Crafting robust backend solutions with Node.js/NestJs, developing data-driven solutions, and guiding web development projects."""
EMAIL = "lucas.ecomp2012@gmail.com"
SOCIAL_MEDIA = {
  "Kaggle": "https://www.kaggle.com/lmorais",
  "Github": "https://github.com/gordinh",
  "Linkedin": "https://www.linkedin.com/in/eulucasmorais/",
  "Gitlab": "https://gitlab.com/lucasmorais93",
}

SOCIAL_MEDIA_ICONS = {
  "Linkedin": "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg",
  "Kaggle": "https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png",
  "Github": "https://img.icons8.com/material-outlined/48/000000/github.png",
  "Gitlab": "https://images.ctfassets.net/xz1dnu24egyd/1IRkfXmxo8VP2RAE5jiS1Q/ea2086675d87911b0ce2d34c354b3711/gitlab-logo-500.png",
}

PROJECTS = {
  "📊 Introduction do Data Analysis with Pandas": "http://tinyurl.com/7d57hye7",
  "📉 Stock Trend Prediction" : "http://bit.ly/38",
  "🏀 NBA Data Analysis": "http://tinyurl.com/533njpmn",
  "📝 To-do app": "https://todoist.streamlit.app/"
}

st.set_page_config(PAGE_TITLE, PAGE_ICON)

with open(css_file) as f:
  st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
  PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
  st.image(profile_pic, width=250)

with col2:
  st.title(NAME)
  st.write(DESCRIPTION)
  st.write("")
  st.download_button(
    label="	📜 Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
  )
  st.write("📫 ", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    html_link = f'<a href="{link}"><img src="{SOCIAL_MEDIA_ICONS[platform]}" alt="{platform}" width="20"> {platform}</a>'
    cols[index].write(html_link, unsafe_allow_html=True)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write("""
- ✅ Extensive experience in building and maintaining robust backend solutions using Python, Node.js, and NestJs.
- ✅ Proficient in managing and optimizing Google Cloud Platform resources for efficient operations.
- ✅ Skilled in orchestrating and monitoring Kubernetes clusters for seamless deployment and management.
- ✅ Strong background in DevOps practices, including migration of databases and services to cloud platforms like Oracle and Google Cloud.
- ✅ Tech leadership capabilities demonstrated through designing solution architectures and overseeing development team sprints.
- ✅ Expertise in integrating third-party services and building communication solutions using TypeScript and Google Cloud functions.
- ✅ Hands-on experience in web scraping for data collection and utilization of Apache Beam with Google Dataflow for ETL system development.
- ✅ Proven track record of problem-solving and initiative-taking in various projects and environments.
""")


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
  """
- 💻 Backend Development: Node.js, NestJs, Express
- ☁️  Cloud Platforms: Google Cloud Platform (GCP), Oracle Cloud
- 🐳 Containerization and Orchestration: Kubernetes, Docker
- 🗃️ Database Management: Postgres, MySQL, Oracle
- 🔄 Data Processing and ETL: Apache Beam, Google Dataflow
- 🤝 Integration Services: Third-party API integration, Google Cloud functions
- 🕸️ Web Scraping: Python (Beautiful Soup, Scrapy)
- 📊 Statistical Analysis: Python (NumPy, SciPy), Excel
- 📜 Version Control: Git
- ⚙️ DevOps: Continuous Integration/Continuous Deployment (CI/CD), Monitoring (Kubernetes, Prometheus)
"""
)

# --- WORK HISTORY ---
st.write("#")
st.write("🚧", "**Software Engineer | AdMobilize**")
st.write("09/2016 - 01/2024")
st.write(
  """
At AdMobilize i was able to work in a lot of stacks, being my first experience in a
work environment and learning the necessary responsibilities for development of API's,
SaaS, microservices, GCP Stack, taking the firsts steps on CI/CD, Google Kubernetes, ETL,
Apache Beam, Big Query. 
AdMobilize is a machine intelligence company making sense of the physical world.
- ▶️ Creating solutions in backend for dashboard (NodeJS)
- ▶️ Helped manage Google Cloud Platform resources
- ▶️ Developed distributed data pipelines in Python and integrating with third-parties
services for ETL systems
- ▶️ Helped mantain Kubernetes Services, improving GKE integration with CI/CD,
monitoring clustes and API's, managing pods deployments
"""
)

# --- JOB 2 ---
st.write("#")
st.write("🚧", "**DevOps | Paynow do Brasil**")
st.write("09/2021 - 09/2022")
st.write(
  """
At Paynow i've been working as a DevOps developer using Oracle Cloud and Google Cloud
solutions, responsibly for setting and monitoring the migration to Kubernetes solution.
At Paynow, I've been working as a DevOps developer utilizing Oracle Cloud and Google
Cloud solutions. I was responsible for orchestrating and monitoring Kubernetes clusters
in Oracle Cloud .
- ▶️ Orchestrate Kubernetes Clusters in Oracle Cloud and Google Cloud
- ▶️ Migrated databases/services to Oracle Cloud
- ▶️ Migrated databases/services to Google Cloud
- ▶️ Monitored applications in Kubernetes Clusters
- ▶️ Monitored and criated ssl certificates with Kubernetes, Istio and Certbot for applications
"""
)


# --- JOB 3 ---
st.write("#")
st.write("🚧", "**Tech Lead | Reedcod Reconquista de Crédito**")
st.write("07/2022 - Present")
st.write(
  """
At Reedcod, I had the opportunity to work on various fronts, both in web development
and team management, as well as direct client interaction. Reedcod is a consultancy
and solutions development company with a primary focus on the financial sector. We
offer solutions for credit recovery, performance management tools for businesses, and
solutions for various commercial enterprises.
Some of the key responsibilities and roles I undertook included:
- ▶️ Developing debt management solutions
- ▶️ Creating a performance management platform
- ▶️ Integrating with ERPs
- ▶️ Planning and overseeing development team sprints (1-5)
- ▶️ Designing solution architectures
- ▶️ Developing APIs using NestJS
- ▶️ Projecting and budgeting solution costs for clients
"""
)


# --- JOB 4 ---
st.write("#")
st.write("🚧", "**Software Engineer | WAO! Shop**")
st.write("05/2021 - 02/2023")
st.write(
  """
At WAO! Shop I was able to develop integration solutions with third-parties services. WAO!
Shop was a e-commerce platform, so my role there was to help building integrations with
Whatsapp + SMS services (Keybe and MessageBird), delivery partners (Liftit, Quick, TTP
and Webpack) and also with Zoho Inventory/Invoicing.  All the integrations services were
built with TS and solutions like pubsub and google cloud functions for communication
between all services and external services.

I have also worked with Python to create a web scraper for collecting data from Yahoo
Finance. Additionally, I utilized Apache Beam with Google Dataflow to build an ETL
system that supported our fraud analytics.
"""
)


# --- PROJECTS & ACCOMPLISHMENTS ---
st.write("#")
st.subheader("Projects  & Accomplishments")
st.write('---')
for project, link in PROJECTS.items():
  st.write(f"[{project}]({link})")