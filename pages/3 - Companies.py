import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from dotenv import load_dotenv
load_dotenv()
import os
BASE_DIR = os.getenv("BASE_DIR")
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)
lang = st.session_state.get('lang', 'HY').lower()  # Վերցնում ենք session_state-ից

translations = {
    "hy":  {
        "companies_title": "Ընկերությունների/գործատուների  վերլուծություն",
        

    "employers_title": " Հայաստանում ամենախոշոր գործատուները և նրանց ազդեցությունը",
        'about':"Ստորև ներկայացված է հայկական աշխատաշուկայի առաջատար գործատուների թափուր հաստիքների քանակը.",
        "leading_text": """Հայաստանի աշխատաշուկայում առաջատար գործատուներն են՝  
- 🟦 **SoftConstruct**  
- 🟨 **Digitain**  

 Այս տեխնոլոգիական հսկաները ոչ միայն զբաղեցնում են առաջատար դիրքեր շուկայում , այլև հանդես են գալիս որպես խոշոր գործատուներ ՝ միավորելով մեծ թվով մասնագետների և ընդգրկելով տարբեր ոլորտներ ։""",

        "industry_distribution": "Ոլորտային բաշխվածություն",
        "industry_text": """Ըստ մեր վերլուծության՝ այս երկու ընկերությունները միասին ընդգրկում են հետևյալ ոլորտները՝  
- 🎮 **iGaming / Betting**  
- 💻 **IT & Software Development**  
- 🧠 **AI & Data Analysis**  
- 📞 **Customer Support**  
- 📢 **Marketing & Business Operations**  

""",
        "conclusion_title":"Եզրակացություն",
        "conclusion": "📌 **Եզրակացություն**",
        "conclusion_text": """✅ **SoftConstruct** և **Digitain** ընկերությունները հայկական աշխատաշուկայում  բացում են բազմաթիվ հնարավորություններ, հատկապես հետևյալ խմբերի համար՝  
- 📚 Ուսանողներ / սկսնակ մասնագետներ  
- 🧑‍💻 Ծրագրավորողներ, QA, Data Analysts  
- 🧑‍💼 Մարքեթինգի, օպերացիոն կառավարման մասնագետներ  

Այս ոլորտների բազմազանությունը նպաստում է ոչ միայն զբաղվածությանը, այլև  Հայաստանի տեխնոլոգիական իմիջի ամրապնդմանը համաշխարհային մակարդակում։""",


        "top10_employers_title": "Հայաստանի TOP 10 Գործատուները ըստ աշխատանքների քանակի",

        "banks_paragraph": """
📌 Հայաստանի աշխատաշուկայի թոփ 10 գործատուների շարքում կարևոր տեղ են զբաղեցնում հայկական բանկերը։ Սա վկայում է նրանց կարևոր դերի և նշանակության մասին։ Բանկերը ոչ միայն հանդիսանում են խոշոր գործատուներ, այլև ակտիվ ներդրում են կատարում երիտասարդ մասնագետների զարգացման գործում։ Շատ բանկեր կազմակերպում են ուսանողական թրեյնինգներ և պրակտիկ ծրագրեր, որոնք ստեղծում են արդյունավետ հնարավորություններ կարիերան նոր սկսողների համար։

Հայկական բանկերի դերը աշխատաշուկայի զարգացման գործում անգնահատելի է․ նրանք ոչ միայն ապահովում են կայուն աշխատատեղեր, այլև նպաստում երկրի տնտեսական աճին և մասնագիտական կարողությունների շարունակական զարգացմանը։
""",

        "select_company_box": "Ընկերությունների գնահատումը ըստ տարբեր ցուցանիշների",
        "select_name":"Ընտրել ընկերություն ․",
        "company_industries_categories": "Ընկերության ինդուստրիաներ և կատեգորիաներ",
        "industry_distribution": "🏢 Ինդուստրիաների բաշխվածություն",
        "category_distribution": "📂 Կատեգորիաների բաշխվածություն",
        "select_job_skills": "🔎 Ընտրել աշխատանք պահանջվող հմտությունները տեսնելու համար ․",
        "job_label": "Հաստիք ․",
        "job_required_skills": "📝 {job} աշխատանքի պահանջվող հմտություններ",
        "skill_column": "Հմտություն",
        "count_column": "Քանակ",
        "skills_chart_title": "Պահանջվող հմտությունների բաշխվածություն {job} աշխատանքի համար",
        "level_distribution": "Մակարդակների բաշխվածություն ",
        "top_10_prof_skills": "🛠️ Թոփ 10 մասնագիտական հմտություններ ",
        "skills_table": "📋 Հմտությունների աղյուսակ ",
        "no_prof_skills": "Այս կազմակերպության համար մասնագիտական հմտությունների տվյալներ չկան։",
        "top_10_soft_skills": "💼 Թոփ 10 փափուկ (անհատական) հմտություններ " ,
        "no_soft_skills": "Այս կազմակերպության համար փափուկ հմտությունների տվյալներ չկան։",
        "no_level_data":"Այս ընկերության մակարդակի վերաբերյալ տվյալներ չկան",
        "top_10_jobs": "Ընդհանուր մասնագիտական ուղղվածություն ունեցող մասնագետների ցանկը ըստ ընտրված կազմակերպության ",
        "no_jobcategory_data": "Այս կազմակերպության համար jobcategorybyfirst տվյալներ չկան։",
        "jobcategory_column_missing": "❗ 'jobcategorybyfirst' սյունակը բացակայում է տվյալների մեջ։",
        "work_time_distribution": "🕒 Աշխատաժամանակի տեսակները ",
        "employment_term_distribution": "📄 Աշխատանքային պայմանների տեսակները ",

    },
"en": {
  "companies_title": "Employers / companies analysis",

  "employers_title": "Largest employers in Armenia and their impact",
  "about": "Below is the number of open positions for Armenia’s leading employers.",
  "leading_text": "The leading employers in Armenia’s labor market are:\n- 🟦 **SoftConstruct**\n- 🟨 **Digitain**\n\nThese technology giants not only hold leading positions in the market, but also act as major employers, bringing together large teams across different domains.",

  "industry_distribution": "🏢 Industry distribution",
  "industry_text": "According to our analysis, these two companies together span the following industries:\n- 🎮 **iGaming / Betting**\n- 💻 **IT & Software Development**\n- 🧠 **AI & Data Analysis**\n- 📞 **Customer Support**\n- 📢 **Marketing & Business Operations**\n",

  "conclusion_title": "Conclusion",
  "conclusion": "📌 **Conclusion**",
  "conclusion_text": "✅ **SoftConstruct** and **Digitain** open numerous opportunities in Armenia’s labor market, especially for:\n- 📚 Students / entry-level specialists\n- 🧑‍💻 Developers, QA, Data Analysts\n- 🧑‍💼 Marketing and operations professionals\n\nThis diversity not only boosts employment, but also strengthens Armenia’s technological image globally.",

  "top10_employers_title": "TOP 10 employers in Armenia by number of jobs",

  "banks_paragraph": "📌 Armenian banks occupy an important place among the top 10 employers. This highlights their crucial role and impact. Banks are not only major employers but also actively invest in the development of young specialists. Many banks run student trainings and internship programs that create effective opportunities for those starting their careers.\n\nThe role of Armenian banks in labor-market development is invaluable: they provide stable jobs and contribute to economic growth and continuous skill development in the country.",

  "select_company_box": "Company evaluation by different indicators",
  "select_name": "Select a company:",
  "company_industries_categories": "Company industries and categories",
  "category_distribution": "📂 Category distribution",
  "select_job_skills": "🔎 Select a job to see its required skills:",
  "job_label": "Job:",
  "job_required_skills": "📝 Required skills for {job}",
  "skill_column": "Skill",
  "count_column": "Count",
  "skills_chart_title": "Distribution of required skills for {job}",
  "level_distribution": "Level distribution",
  "top_10_prof_skills": "🛠️ Top 10 professional skills",
  "skills_table": "📋 Skills table",
  "no_prof_skills": "No professional skill data for this company.",
  "top_10_soft_skills": "💼 Top 10 soft (personal) skills",
  "no_soft_skills": "No soft-skill data for this company.",
  "no_level_data": "No level data available for this company.",
  "top_10_jobs": "List of general occupational categories for the selected company",
  "no_jobcategory_data": "No jobcategorybyfirst data for this company.",
  "jobcategory_column_missing": "❗ The 'jobcategorybyfirst' column is missing in the data.",
  "work_time_distribution": "🕒 Work time types",
  "employment_term_distribution": "📄 Employment term types"
},
"ru": {
  "companies_title": "Аналитика работодателей / компаний",

  "employers_title": "Крупнейшие работодатели в Армении и их влияние",
  "about": "Ниже показано количество открытых позиций у ведущих работодателей Армении.",
  "leading_text": "Лидеры рынка труда Армении:\n- 🟦 **SoftConstruct**\n- 🟨 **Digitain**\n\nЭти технологические гиганты не только удерживают лидирующие позиции на рынке, но и являются крупными работодателями, объединяя большие команды в разных направлениях.",

  "industry_distribution": "🏢 Отраслевое распределение",
  "industry_text": "По нашему анализу эти две компании вместе охватывают следующие направления:\n- 🎮 **iGaming / Betting**\n- 💻 **IT и разработка ПО**\n- 🧠 **AI и анализ данных**\n- 📞 **Поддержка клиентов**\n- 📢 **Маркетинг и бизнес-операции**\n",

  "conclusion_title": "Вывод",
  "conclusion": "📌 **Вывод**",
  "conclusion_text": "✅ **SoftConstruct** и **Digitain** создают множество возможностей на рынке труда Армении, особенно для:\n- 📚 Студентов / начинающих специалистов\n- 🧑‍💻 Разработчиков, QA, Data Analysts\n- 🧑‍💼 Специалистов по маркетингу и операционному управлению\n\nЭто разнообразие не только повышает занятость, но и укрепляет технологический имидж Армении на мировом уровне.",

  "top10_employers_title": "ТОП-10 работодателей Армении по числу вакансий",

  "banks_paragraph": "📌 Армянские банки занимают важное место среди топ-10 работодателей. Это подчёркивает их ключевую роль и влияние. Банки не только являются крупными работодателями, но и активно инвестируют в развитие молодых специалистов. Многие банки проводят студенческие тренинги и программы практик, создавая эффективные возможности для начала карьеры.\n\nРоль армянских банков в развитии рынка труда бесценна: они обеспечивают стабильные рабочие места и способствуют экономическому росту и непрерывному развитию профессиональных компетенций в стране.",

  "select_company_box": "Оценка компаний по различным показателям",
  "select_name": "Выберите компанию:",
  "company_industries_categories": "Отрасли и категории компании",
  "category_distribution": "📂 Распределение категорий",
  "select_job_skills": "🔎 Выберите должность, чтобы увидеть требуемые навыки:",
  "job_label": "Должность:",
  "job_required_skills": "📝 Требуемые навыки для {job}",
  "skill_column": "Навык",
  "count_column": "Количество",
  "skills_chart_title": "Распределение требуемых навыков для {job}",
  "level_distribution": "Распределение уровней",
  "top_10_prof_skills": "🛠️ Топ-10 профессиональных навыков",
  "skills_table": "📋 Таблица навыков",
  "no_prof_skills": "Для этой компании нет данных о профессиональных навыках.",
  "top_10_soft_skills": "💼 Топ-10 soft-skills (личных навыков)",
  "no_soft_skills": "Для этой компании нет данных о soft-skills.",
  "no_level_data": "Для этой компании нет данных по уровням.",
  "top_10_jobs": "Список обобщённых профессиональных направлений для выбранной компании",
  "no_jobcategory_data": "Для этой компании нет данных jobcategorybyfirst.",
  "jobcategory_column_missing": "❗ В данных отсутствует столбец 'jobcategorybyfirst'.",
  "work_time_distribution": "🕒 Типы рабочего времени",
  "employment_term_distribution": "📄 Типы условий занятости"
},
}

html_content = f"""
<div style='
    background: linear-gradient(90deg, #0f172a 0%, #64748b 100%);
    padding: 2rem;
    border-radius: 15px;
    margin-top: 2rem;
    color: white;
    font-size: 1rem;
    line-height: 1.6; 
    text-align: center;
'>
    <h2 style='color: white;font-size :1.8rem'>{translations[lang]["companies_title"]}</h2>
    
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)


@st.cache_data
def load_data(path=f"{BASE_DIR}data/All.xlsx"):
    df = pd.read_excel(path)
    df.columns = [col.lower() for col in df.columns]  
    return df

df = load_data()

st.markdown("""
<style>
.subheader-companies{
  font-size: 30px;        
  font-weight: 700;
  color: #d8e2eb;
  line-height: 1.2;
  margin: .25rem 0 1rem 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(f"### {translations[lang]['employers_title']}")
st.markdown(f"###### {translations[lang]['about']}")


top_companies = (
    df['company']
      .dropna()
      .astype(str)
      .str.strip()
      .replace('', None)
      .dropna()
      .value_counts()
      .nlargest(10)
      .rename_axis('company')
      .reset_index(name='job_count')
)

if top_companies.empty:
    st.info("Տվյալներ չեն գտնվել `company` սյունակում։")
else:
    fig_line = go.Figure()

    fig_line.add_trace(go.Scatter(
        x=top_companies['company'],
        y=top_companies['job_count'],
        mode="lines+markers",
        line=dict(color="#f59e0b", width=4),  # orange
        marker=dict(size=8, color='white', line=dict(width=2, color='#f59e0b')),
        name="Jobs Posted",
        hovertemplate="<b>%{x}</b><br>Jobs: %{y}<extra></extra>",
    ))

    for i, row in top_companies.iterrows():
        fig_line.add_annotation(
            x=row['company'],
            y=row['job_count'],
            text=str(row['job_count']),
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1.5,
            arrowcolor="#f59e0b",
            font=dict(color="white", size=14),
            bgcolor="rgba(0,0,0,0.35)",
            bordercolor="#f59e0b",
            borderwidth=1,
            ay=-20  
        )

    fig_line.update_layout(
        paper_bgcolor="#1E1E2F",
        plot_bgcolor="#1E1E2F",
        font=dict(color="white"),
        margin=dict(t=60, b=60, l=50, r=30),
        height=420,
        xaxis=dict(
            title=None,
            tickangle=-30,
            categoryorder="array",
            categoryarray=top_companies['company'].tolist(),
            showgrid=False
        ),
        yaxis=dict(
            title=None,
            rangemode="tozero",
            gridcolor="rgba(255,255,255,0.12)",
            zerolinecolor="rgba(255,255,255,0.25)"
        ),
        hovermode="x unified"
    )

    st.plotly_chart(fig_line, use_container_width=True)

with st.container():
    st.markdown(f"#### {translations[lang]['leading_text']}")

    st.markdown("---")

with st.container():
    st.markdown(f"#### {translations[lang]['industry_distribution']}")
    st.markdown(translations[lang]['industry_text'])
    st.markdown("---")

with st.success(translations[lang]['conclusion']):
    st.markdown(translations[lang]['conclusion_text'])


st.markdown("---")
  
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
        {translations[lang]["banks_paragraph"]}

    """,
    unsafe_allow_html=True
)

st.markdown("---")

company_names = df['company'].dropna().unique()
with st.container():
    st.markdown(
    f"""
    <div style='
        background-color:#e6f2ff;
        padding:10px;
        border-radius:10px;
        border:1px solid #cce0ff;
        margin-bottom:10px;'>
        <h4 style='color:#003366;margin-bottom:10px;'>{translations[lang]["select_company_box"]}</h4>

    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown(translations[lang]["select_name"])
    selected_company = st.selectbox("Ընկերություն", sorted(company_names), key="company_select", label_visibility="collapsed")

company_df = df[df['company'] == selected_company]

import plotly.graph_objects as go
import plotly.graph_objects as go

with st.container():
    st.markdown("---")
    st.subheader(translations[lang]["company_industries_categories"])
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"##### {translations[lang]['industry_distribution']}")
        if 'industry' in company_df.columns:
            industry_counts = company_df['industry'].dropna().value_counts().reset_index()
            industry_counts.columns = ['Industry', 'Count']
            if not industry_counts.empty:
                fig_industry = go.Figure(
                    data=[go.Bar(
                        x=industry_counts['Count'],
                        y=industry_counts['Industry'],
                        orientation='h',
                        marker=dict(color='darkblue ')
                    )]
                )
                fig_industry.update_layout(
                    paper_bgcolor='black',
                    plot_bgcolor='black',
                    font=dict(color='white'),
                    xaxis=dict(color='white', gridcolor='blue'),
                    yaxis=dict(color='white', gridcolor='green'),
                    title="Distribution of industries"
                )
                st.plotly_chart(fig_industry, use_container_width=True)
            else:
                st.info("Այս ընկերության համար ինդուստրիայի տվյալներ չկան։")
        else:
            st.warning("«industry» սյունակը բացակայում է։")

    with col2:
        st.markdown(f"##### {translations[lang]['category_distribution']}")
        if 'category' in company_df.columns:
            category_counts = company_df['category'].dropna().value_counts().reset_index()
            category_counts.columns = ['Category', 'Count']
            if not category_counts.empty:
                fig_category = go.Figure(
                    data=[go.Bar(
                        x=category_counts['Count'],
                        y=category_counts['Category'],
                        orientation='h',
                        marker=dict(color='darkblue')
                    )]
                )
                fig_category.update_layout(
                    paper_bgcolor='black',
                    plot_bgcolor='black',
                    font=dict(color='white'),
                    xaxis=dict(color='white', gridcolor='blue'),
                    yaxis=dict(color='white', gridcolor='green'),
                    title="Distribution of categories"
                )
                st.plotly_chart(fig_category, use_container_width=True)
            else:
                st.info("Այս ընկերության համար կատեգորիայի տվյալներ չկան։")
        else:
            st.warning("«category» սյունակը բացակայում է։")

   
with st.container():
    st.markdown("---")
    st.subheader(translations[lang]["top_10_jobs"])

    if 'jobcategorybyfirst' in company_df.columns:
        top_jobs = (
            company_df['jobcategorybyfirst']
            .dropna()
            .astype(str)
            .value_counts()
            .nlargest(10)
            .reset_index()
        )
        top_jobs.columns = ['Job Category', 'Color']

        if not top_jobs.empty:
            fig_job_cat = px.bar(
                top_jobs,
                x='Job Category',
                y='Color',
                color='Color',
                color_continuous_scale='sunsetdark',
                title="Distribution of professional directions"
            )
            fig_job_cat.update_layout(
                xaxis_title="Profession",
                yaxis_title="Open Positions (number)",
                paper_bgcolor='black',
                plot_bgcolor='black',
                font=dict(color='white')
            )
            st.plotly_chart(fig_job_cat, use_container_width=True)
        else:
            st.info(translations[lang]["no_jobcategory_data"])
    else:
        st.warning(translations[lang]["jobcategory_column_missing"])


with st.container():
    st.markdown("---")
    st.subheader(translations[lang]["select_job_skills"])

    if 'name' in company_df.columns:
        jobs_list = sorted(company_df['name'].dropna().unique())
        selected_job = st.selectbox(translations[lang]["job_label"], jobs_list)

        job_data = company_df[company_df['name'] == selected_job]

        skill_cols = [f'professional_skills_{i}' for i in range(1, 11)]
        skills = []

        for _, row in job_data.iterrows():
            for col in skill_cols:
                skill = row.get(col)
                if pd.notna(skill) and skill.strip():
                    skills.append(skill.strip())

        if skills:
            unique_skills = sorted(set(skills))

            st.markdown(
                f"""
                <div style='
                    background-color:#e6f7ff;
                    padding:15px;
                    border-radius:8px;
                    border:1px solid #99d6ff;
                    margin-bottom:10px;'>
                    <h5 style='color:#004466;font-size: 0.8rem'>📝  {translations[lang]["job_required_skills"].format(job=selected_job)}</h5>
                </div>
                """,
                unsafe_allow_html=True 
            )

            # Տպում ենք միայն հմտությունները որպես աղյուսակ
            skill_df = pd.DataFrame(unique_skills, columns=[translations[lang]["skill_column"]])
            st.dataframe(skill_df, use_container_width=True, hide_index=True)

        else:
            st.info(f"❗ Հմտությունների տվյալներ չկան՝ {selected_job} աշխատանքի համար։")
    else:
        st.warning("❗ Աշխատանքների սյունակը բացակայում է տվյալների մեջ։")

with st.container():
    st.markdown("---")
    st.subheader(f"🧱 {translations[lang]['level_distribution']}")


    if 'level' in company_df.columns:
        level_counts = company_df['level'].dropna().value_counts().reset_index()
        level_counts.columns = ['Level', 'Open Positions (number)']
        if not level_counts.empty:
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("##### 🎯 Pie Chart")
                fig_pie = px.pie(
                    level_counts,
                    names="Level",
                    values="Open Positions (number)",
                    hole=0.4,
                    color_discrete_sequence=px.colors.qualitative.Set3
                )
                st.plotly_chart(fig_pie, use_container_width=True)

            with col2:
                st.markdown("##### 📊 Bar Chart")
                fig_bar = px.bar(
                    level_counts,
                    x="Level",
                    y="Open Positions (number)",
                    color="Open Positions (number)",
                    color_continuous_scale="viridis",
                )
                st.plotly_chart(fig_bar, use_container_width=True)

            st.dataframe(level_counts, use_container_width=True, hide_index=True)

        else:
            st.info("Այս կազմակերպության համար լեվելների տվյալներ չկան։")
    else:
        st.warning("❗ 'level' սյունակը բացակայում է տվյալների մեջ։")

with st.container():
    st.markdown("---")
    st.subheader(translations[lang]["top_10_prof_skills"])


    professional_cols = [f'professional_skills_{i}' for i in range(1, 11)]
    professional_skills = []

    for col in professional_cols:
        if col in company_df.columns:
            professional_skills += company_df[col].dropna().astype(str).tolist()

    professional_skills = [s for s in professional_skills if s.strip() != ""]

    if professional_skills:
        skill_counts = Counter(professional_skills)
        skill_df = (
            pd.DataFrame(skill_counts.items(), columns=['Hard Skill', 'Color'])
            .sort_values(by='Color', ascending=False)
            .head(10)
        )

        col1, col2 = st.columns(2)

        with col1:
            fig_top_skills = px.bar(
                skill_df,
                x='Hard Skill',
                y='Color',
                color='Color',
                color_continuous_scale='plasma',
            )
            st.plotly_chart(fig_top_skills, use_container_width=True)

        with col2:
            st.markdown("##### " + translations[lang]["skills_table"])
            st.dataframe(skill_df, hide_index=True, use_container_width=True)

    else:
        st.info(translations[lang]["no_level_data"])
 
with st.container():
    st.markdown("---")
    st.subheader(translations[lang]["top_10_soft_skills"])


    personal_cols = [f'personal_skills_{i}' for i in range(1, 11)]
    personal_skills = []

    for col in personal_cols:
        if col in company_df.columns:
            personal_skills += company_df[col].dropna().astype(str).tolist()

    personal_skills = [s for s in personal_skills if s.strip() != ""]

    if personal_skills:
        skill_counts = Counter(personal_skills)
        skill_df = (
            pd.DataFrame(skill_counts.items(), columns=['Soft Skill', 'Color'])
            .sort_values(by='Color', ascending=False)
            .head(10)
        )

        col1, col2 = st.columns(2)

        with col1:
            fig_top_personal = px.bar(
                skill_df,
                x='Soft Skill',
                y='Color',
                color='Color',
                color_continuous_scale='magma',
            )
            fig_top_personal.update_layout(
                xaxis_title="Soft Skill",
                yaxis_title="Number",
                title_x=0.5,
            )
            st.plotly_chart(fig_top_personal, use_container_width=True)

        with col2:
            st.markdown("##### " + translations[lang]["skills_table"])
            st.dataframe(skill_df, hide_index=True, use_container_width=True)

    else:
        st.info(translations[lang]["no_soft_skills"])

if not company_df.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"##### {translations[lang]['work_time_distribution']}")
        time_counts = company_df['time'].dropna().value_counts()
        if not time_counts.empty:
            fig_time = px.bar(
                time_counts,
                x=time_counts.index,
                y=time_counts.values,
                labels={"x": "aaaa", "y": "Number"},
                color_discrete_sequence=["#3399ff"]
            )
            st.plotly_chart(fig_time, use_container_width=True)
        else:
            st.info("Տվյալներ չկան այս բաժնում։")

    with col2:
        st.markdown(f"##### {translations[lang]['employment_term_distribution']}")
        term_counts = company_df['employment term'].dropna().value_counts()
        if not term_counts.empty:
            fig_term = px.bar(
                term_counts,
                x=term_counts.index,
                y=term_counts.values,
                labels={"x": "Աշխատանքային պայման", "y": "Number"},
                color_discrete_sequence=["#66cc99"]
            )
            st.plotly_chart(fig_term, use_container_width=True)
        else:
            st.info("Տվյալներ չկան այս բաժնում։")

