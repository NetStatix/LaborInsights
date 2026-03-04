import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
import os
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = os.getenv("BASE_DIR")
st.set_page_config(
    page_title="Աշխատանքների Վերլուծություն | Հայկական Աշխատաշուկա",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)

lang = st.session_state.get('lang', 'HY').lower()  

translations = {
    "hy": {
        "page_title": "Աշխատանքների Վերլուծություն | Հայկական Աշխատաշուկա",
         "page_description": """
            <div class="custom-header-content">
                <h1>Աշխատանքների/հաստիքների վերլուծություն</h1>
            </div>
        """,


        "section_title": "Ընտրված աշխատանքի համապարփակ վերլուծություն",

        "select_job": "Ընտրել աշխատանք ․",

        "job_title": "Աշխատանքի անվանում",

            "company_count": "կազմակերպություն",

        "companies_for_job": "Կազմակերպություններն ըստ ընտրված աշխատանքի",

        "industries_for_job": "Ինդուստրիաներն ըստ ընտրված աշխատանքի",
        "categories_for_job": "Կատեգորիաներն ըստ ընտրված աշխատանքի",

        "skills": "հմտություն",

        "required_skills": "Պահանջվող մասնագիտական հմտություններ",

        "level_distribution": "Մակարդակների բաշխվածություն {} աշխատանքի համար",

        "no_levels": "Լեվելների տվյալներ չկան այս աշխատանքի համար։",

        "no_data": "Այս աշխատանքի վերաբերյալ տվյալներ չգտնվեցին։",
        "separator": "---",

        "top_10_jobs": "Թոփ 10 մասնագետներն ըստ թափուր հաստիքների",

        "job_analysis_summary": """
Վերլուծության արդյունքները ցույց են տալիս, որ Հայաստանի աշխատաշուկայում այս պահին առավել պահանջված հաստիքներն են հաշվապահությունը և վաճառքի կառավարումը (Sales Management)։ Այս փաստը ընդգծում է երկու հիմնական միտում․

📊 Հաշվապահություն – մնում է առանցքային ոլորտ, որը ապահովում է ընկերությունների ֆինանսական կայունությունն ու թափանցիկությունը։ Այն առաջարկում է մասնագիտական աճի լայն հնարավորություններ և երկարաժամկետ, կայուն կարիերայի կառուցման ուղի։

🤝 Վաճառքի կառավարում – կարևոր դեր է խաղում վաճառքների աճի, հաճախորդների հետ հարաբերությունների կառավարման և շուկայի ընդլայնման գործընթացում։ Այս ոլորտը բացում է լայն հնարավորություններ ինչպես սկսնակների, այնպես էլ փորձառու մասնագետների համար։

Ընդհանուր առմամբ, այս երկու հաստիքների բարձր պահանջարկը վկայում է, որ հայաստանյան աշխատաշուկան մեծ կարևորություն է տալիս ֆինանսական վերահսկողությանը և վաճառքների զարգացմանը։ Դրանք հանդիսանում են երկրի տնտեսության աճի և կայուն զարգացման հիմնական շարժիչ ուժերը։
""",

        "job_title": "Աշխատանքի անվանում",

        "open_positions": "Բաց հաստիքներ",

        "top_15_general_jobs": "Թոփ ընդհանուր մասնագիտական ուղղվածություն ունեցող մասնագետները",

      
        "missing_jobcategory_column": "'jobcategorybyfirst' սյունը բացակայում է տվյալների մեջ։",
 
        "top_industries_by_open_positions": "Թոփ 10 ինդուստրիաներն ըստ հաստիքների",
        "top_categories_by_open_positions": "Թոփ 10 աշխատանքային կատեգորիաներն ըստ հաստիքների",
        "industry_column_missing": "❗ 'industry' սյունակը բացակայում է տվյալների մեջ։",
        "category_column_missing": "❗ 'category' սյունակը բացակայում է տվյալների մեջ։",
        

    },
    "en": {
  "page_title": "Jobs Analysis | Armenian Labor Market",
  "page_description": "<div class=\"custom-header-content\"><h1>Jobs/Positions Analysis</h1></div>",

  "section_title": "Comprehensive analysis for the selected job",
  "select_job": "Select a job:",
  "job_title": "Job title",

  "company_count": "Company",
  "companies_for_job": "Companies for the selected job",
  "industries_for_job": "Industries for the selected job",
  "categories_for_job": "Categories for the selected job",

  "skills": "Skill",
  "required_skills": "Required professional skills",

  "level_distribution": "Level distribution for the {} job",
  "no_levels": "No level data for this job.",
  "no_data": "No data found for this job.",
  "separator": "---",

  "top_10_jobs": "Top 10 specialists by open positions",

  "job_analysis_summary": "The analysis shows that, at the moment, the most in-demand roles in Armenia are Accounting and Sales Management. This highlights two key trends:\n\n📊 **Accounting** – remains a core function that ensures companies’ financial stability and transparency. It offers broad opportunities for professional growth and a clear path to a long-term, stable career.\n\n🤝 **Sales Management** – plays a crucial role in revenue growth, customer relationship management, and market expansion. The field provides wide opportunities for both entry-level and experienced professionals.\n\nOverall, the high demand for these two roles indicates that the Armenian labor market places strong emphasis on financial control and sales development—key drivers of the country’s economic growth and sustainable development.",

  "open_positions": "Open positions",
  "top_15_general_jobs": "Top general occupational categories",

  "missing_jobcategory_column": "The 'jobcategorybyfirst' column is missing from the data.",

  "top_industries_by_open_positions": "Top 10 industries by positions",
  "top_categories_by_open_positions": "Top 10 job categories by positions",
  "industry_column_missing": "❗ The 'industry' column is missing from the data.",
  "category_column_missing": "❗ The 'category' column is missing from the data."
},
"ru": {
  "page_title": "Аналитика вакансий | Рынок труда Армении",
  "page_description": "<div class=\"custom-header-content\"><h1>Аналитика вакансий/должностей</h1></div>",

  "section_title": "Комплексный анализ выбранной должности",
  "select_job": "Выберите должность:",
  "job_title": "Название должности",

  "company_count": "Компания",
  "companies_for_job": "Компании по выбранной должности",
  "industries_for_job": "Отрасли по выбранной должности",
  "categories_for_job": "Категории по выбранной должности",

  "skills": "Навык",
  "required_skills": "Требуемые профессиональные навыки",

  "level_distribution": "Распределение уровней для должности {}",
  "no_levels": "По этой должности нет данных по уровням.",
  "no_data": "Данные по этой должности не найдены.",
  "separator": "---",

  "top_10_jobs": "Топ-10 специалистов по числу открытых позиций",

  "job_analysis_summary": "Анализ показывает, что на данный момент наиболее востребованы в Армении направления — бухгалтерия и управление продажами. Это подчёркивает две ключевые тенденции:\n\n📊 **Бухгалтерия** — остаётся ключевой областью, обеспечивающей финансовую устойчивость и прозрачность компаний. Она предлагает широкие возможности профессионального роста и путь к долгосрочной стабильной карьере.\n\n🤝 **Управление продажами** — играет важную роль в росте выручки, управлении отношениями с клиентами и расширении рынка. Направление открывает широкие возможности как для начинающих, так и для опытных специалистов.\n\nВ целом высокая востребованность этих двух направлений свидетельствует о том, что рынок труда Армении придаёт большое значение финансовому контролю и развитию продаж — ключевым драйверам экономического роста и устойчивого развития страны.",

  "open_positions": "Открытые позиции",
  "top_15_general_jobs": "Топ обобщённых профессиональных направлений",

  "missing_jobcategory_column": "В данных отсутствует столбец 'jobcategorybyfirst'.",

  "top_industries_by_open_positions": "Топ-10 отраслей по числу позиций",
  "top_categories_by_open_positions": "Топ-10 категорий по числу позиций",
  "industry_column_missing": "❗ В данных отсутствует столбец 'industry'.",
  "category_column_missing": "❗ В данных отсутствует столбец 'category'."
},
}

page_description = translations.get(lang, {}).get("page_description", "")

st.markdown("""
    <style>
    .custom-header-content {
        background: linear-gradient(135deg, #003366, #6699CC);
        color: white;
        text-align: center;
        padding: 2rem;
        margin-bottom: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .custom-header-content h1 {
        margin-bottom: 1rem;
        font-size: 2rem;
    }

    .custom-header-content p {
        font-size: 1.1rem;
        margin: 0 auto;
        max-width: 700px;
    }

    .stApp {
        padding: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(page_description, unsafe_allow_html=True)



@st.cache_data
def load_data(path=f"{BASE_DIR}data/All.xlsx"):
    df = pd.read_excel(path)
    df.columns = [col.lower() for col in df.columns]
    return df

df = load_data()

total_jobs = len(df)

skill_columns = [f"professional_skills_{i}" for i in range(1, 11)]

all_skills = pd.Series(df[skill_columns].values.ravel())
top_skill = all_skills.value_counts().idxmax()

top_level = df['level'].value_counts().idxmax()

card_style = """
<style>
.card-container {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
}
.card {
    flex: 1;
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(135deg, #2b5876, #4e4376);
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    color: white;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
}
.card h2 {
    margin: 0;
    font-size: 32px;
    text-align: center;
}
.card p {
    margin: 5px 0 0;
    font-size: 20px;
    opacity: 0.9;
    text-align: center; 
}
</style> 
"""

card_html = f"""
<div class="card-container">
    <div class="card">
        <h2>{total_jobs}</h2>
        <p>All Jobs</p>
    </div>
    <div class="card">
        <h2>{top_skill}</h2>
        <p>Top Skill</p>
    </div>
    <div class="card">
        <h2>{top_level}</h2>
        <p>Top Level</p>
    </div>
</div>
"""

st.markdown(card_style + card_html, unsafe_allow_html=True)

#_----------------------------------------------
job_counts = df['name'].dropna().value_counts()

st.markdown(f"### {translations[lang]['section_title']}")

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
import re
import pandas as pd
import streamlit as st
import plotly.express as px

import os
BASE_DIR = os.getenv("BASE_DIR")
opts = (
    df[["name", "normalized_title"]]
    .dropna(subset=["name", "normalized_title"])
    .drop_duplicates()
    .sort_values("name")
)
raw_selected = st.selectbox(translations[lang]["select_job"], opts["name"].tolist())

selected_job = opts.loc[opts["name"] == raw_selected, "normalized_title"].iloc[0]

left_norm  = df["normalized_title"].fillna("").astype(str).str.strip().str.casefold()
right_norm = str(selected_job).strip().casefold()
mask_norm  = left_norm.eq(right_norm)

keyword = str(selected_job).strip().split()[0].lower() if selected_job else ""
pattern = r"\b" + re.escape(keyword) + r"\b" if keyword else r"$a^"

mask_raw = df["name"].fillna("").astype(str).str.casefold().str.contains(pattern)

job_df = df[mask_norm | mask_raw].copy()

for col in ["industry", "category", "level", "company"]:
    if col in job_df.columns:
        job_df[col] = job_df[col].astype(str).str.strip()

if job_df.empty:
    st.info(translations[lang]["no_data"])
else:
    industries = job_df["industry"].dropna().unique()
    categories = job_df["category"].dropna().unique()
    levels     = job_df["level"].dropna().unique()
    companies  = job_df["company"].dropna().unique()

    level_counts = (
        job_df["level"].value_counts().rename_axis("Level").reset_index(name="Count")
    )

    card_style = """
    <div style='background-color:#1e1e2f;padding:15px;border-radius:12px; max-height:250px; overflow-y:auto; margin-bottom:20px;'>
        <h4 style='color:#58a6ff;'>{title}</h4>
        <p style='color:white;font-size:18px;'>{content}</p>
    </div>
    """

    st.markdown(card_style.format(
        title=translations[lang]["job_title"],
        content=f"<b>{selected_job}</b>"
    ), unsafe_allow_html=True)

    companies_text = (
        f"{len(companies)} {translations[lang]['company_count']}<br><br>" +
        "<br>".join(sorted(map(str, companies)))
    ) if len(companies) else "—"
    st.markdown(card_style.format(
        title=translations[lang]["companies_for_job"], content=companies_text
    ), unsafe_allow_html=True)

    industries_text = (f"{len(industries)} — " + ", ".join(sorted(map(str, industries)))) if len(industries) else "—"
    st.markdown(card_style.format(
        title=translations[lang]["industries_for_job"], content=industries_text
    ), unsafe_allow_html=True)

    categories_text = (f"{len(categories)} — " + ", ".join(sorted(map(str, categories)))) if len(categories) else "—"
    st.markdown(card_style.format(
        title=translations[lang]["categories_for_job"], content=categories_text
    ), unsafe_allow_html=True)

    skill_cols = [c for c in [f"professional_skills_{i}" for i in range(1, 11)] if c in job_df.columns]
    skills = (
        pd.Series(job_df[skill_cols].values.ravel("K"))
        .dropna().astype(str).str.strip()
    )
    skills = skills[skills.ne("")].drop_duplicates().tolist()
    skills_text = (f"{len(skills)} {translations[lang]['skills']}<br><br>" + "<br>".join(skills)) if skills else "—"
    st.markdown(card_style.format(
        title=translations[lang]["required_skills"], content=skills_text
    ), unsafe_allow_html=True)

    if not level_counts.empty:
        fig_levels = px.bar(
            level_counts,
            x="Level", y="Count",
            color="Count", text="Count",
            color_continuous_scale="Blues",
            title=None
        )
        fig_levels.update_traces(textposition="outside", showlegend=False)
        fig_levels.update_layout(
            coloraxis_showscale=False,
            xaxis_title=None,
            yaxis_title="Open Positions (number)",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            margin=dict(t=20, b=60, l=60, r=20),
            height=460
        )
        st.plotly_chart(fig_levels, use_container_width=True)
    else:
        st.info(translations[lang]["no_levels"])


st.markdown("---")  


st.markdown(f"### {translations[lang]['top_10_jobs']}")

top_jobs = job_counts.head(10).reset_index()
top_jobs.columns = ['Job Title', 'Color']

fig_top_jobs = px.bar(
    top_jobs,
    x='Job Title',                  
    y='Color',                     
    color='Color',
    color_continuous_scale='Viridis',
    text='Color',
    title="Distribution of jobs"
)

fig_top_jobs.update_traces(
    textposition='outside',
    textfont_size=12,
    marker_line_color='white',
    marker_line_width=1
)

fig_top_jobs.update_layout(
    coloraxis_showscale=False,    
    xaxis=dict(
        title=None,        
        tickangle=-25,
        tickfont=dict(size=12),
        automargin=True
    ),
    yaxis=dict(
        title="Open Positions (number)",          
        gridcolor='rgba(255,255,255,0.1)',
        zerolinecolor='rgba(255,255,255,0.25)'
    ),
    margin=dict(t=50, b=100, l=70, r=30),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    title_x=0.3
)

st.plotly_chart(fig_top_jobs, use_container_width=True)


st.markdown(
    f"""
    <div style="
        background: linear-gradient(90deg, #0f172a 0%, #64748b 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        color: white;
        font-size: 1rem;
        line-height: 1.6;
    ">
    {translations[lang]["job_analysis_summary"]}
   
    """,
    unsafe_allow_html=True
)
# -------------------------
st.markdown("---")  

st.markdown(f"### {translations[lang]['top_15_general_jobs']}")

if "jobcategorybyfirst" in df.columns:
    category_counts = (
        df["jobcategorybyfirst"]
        .dropna()
        .astype(str).str.strip()
        .replace("", None).dropna()
        .value_counts()
        .head(15)
        .reset_index()
    )
    category_counts.columns = ["Job Category", "Color"]

    fig_job_category = px.bar(
        category_counts,
        x="Job Category",                 
        y="Color",                        
        color="Color",
        color_continuous_scale="Cividis",
        text="Color",
        title="Distribution of jobs"
    )

    fig_job_category.update_traces(
        textposition="outside",
        textfont_size=12,
        marker_line_color="white",
        marker_line_width=1,
        showlegend=False
    )

    fig_job_category.update_layout(
        coloraxis_showscale=False,       
        xaxis=dict(
            title=None,
            tickangle=-25,
            tickfont=dict(size=12),
            automargin=True,
            gridcolor="rgba(255,255,255,0.1)"
        ),
        yaxis=dict(
            title="Open Positions (number)",
            gridcolor="rgba(255,255,255,0.12)",
            zerolinecolor="rgba(255,255,255,0.25)"
        ),
        margin=dict(t=50, b=120, l=70, r=30),
        height=600,
        title_x=0.3,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(fig_job_category, use_container_width=True)
else:
    st.warning(f"❗ {translations[lang]['missing_jobcategory_column']}")


#------------------------------------------------------------------------
st.markdown("---")  

st.markdown(f"### {translations[lang]['top_industries_by_open_positions']}")

if "industry" in df.columns:
    industry_counts = (
        df["industry"]
        .dropna()
        .value_counts()
        .head(10)
        .reset_index()
    )
    industry_counts.columns = ["Industry", "Open Positions"]

    fig_industry_pie = px.pie(
        industry_counts,
        names="Industry",
        values="Open Positions",
        hole=0.35,
        title='Distribution of industries',
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig_industry_pie.update_traces(
        textinfo="percent",
        textposition="inside",
        pull=[0.05] * len(industry_counts),
        marker=dict(line=dict(color="#000000", width=1))
    )

    fig_industry_pie.update_layout(
        margin=dict(t=50, b=100, l=30, r=30),
        title_x=0.3,
        height=600,
        legend=dict(
            orientation="h",          
            y=-0.2,                   
            x=0.5,
            xanchor="center",
            font=dict(size=13)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white", size=14)
    )

    st.plotly_chart(fig_industry_pie, use_container_width=True)
else:
    st.warning(translations[lang]["industry_column_missing"])
# -------------------------
st.markdown("---") 

st.markdown(f"### {translations[lang]['top_categories_by_open_positions']}")


if "category" in df.columns:
    category_counts = (
        df["category"]
        .dropna()
        .value_counts()
        .head(10)
        .reset_index()
    )
    category_counts.columns = ["Category", "Color"]

    fig_category_bar = px.bar(
        category_counts,
        x="Category",
        y="Color",
        color="Color",
        color_continuous_scale="Teal",
        text="Color",
        title="Distribution of categories"
    )
    fig_category_bar.update_layout(
        xaxis_title=None,
        yaxis_title="Open Positions (number)",
        title_x=0.3,
        margin=dict(t=25, b=50, l=50, r=50),
        width = 1200,
        height = 600
    )
    fig_category_bar.update_traces(textposition="outside")

    st.plotly_chart(fig_category_bar, use_container_width=True)
else:
    st.warning(translations[lang]["category_column_missing"])


# -------------------------      
