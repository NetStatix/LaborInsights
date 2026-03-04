import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
load_dotenv()
import os
BASE_DIR = os.getenv("BASE_DIR")

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)
lang = st.session_state.get('lang', 'HY').lower()  

translations = {

"hy": {
    "page_title": " Մակարդակների վերլուծություն",

    "level_distribution_title": "Մակարդակների բաշխվածություն",

        "level_bar_title": "Մակարդակների բաշխվածության գրաֆիկ",

        "level_column_missing": "'level' սյունակը բացակայում է տվյալների մեջ։",

        "level_analysis_title": " Մակարդակների վերլուծություն",

        "analysis_for_level": "Տեսեք համապատասխան վերլուծությունը `{level}` մակարդակի համար",

        "student_oecd_comparison_title": "📉 Հայաստանում և OECD երկրներում student-level աշխատատեղերի համեմատական վերլուծություն",

        
        "student_intern_armenia": "Մակարդակների վերլուծության արդյունքում պարզ է դարձել, որ Հայաստանի աշխատաշուկայում student և internship մակարդակով աշխատատեղերի առաջարկը զգալիորեն սահմանափակ է։",
        "student_intern_oecd": "**{total_jobs}** ակտիվ աշխատատեղերից ընդամենը **{student_intern_jobs}**–ում է նշվում student կամ internship մակարդակը, ինչը կազմում է ընդամենը **{percentage:.1f}%**:",
        "student_intern_conclusion": "Համեմատության համար՝ OECD (Տնտեսական համագործակցության և զարգացման կազմակերպություն) երկրների միջին ցուցանիշը կազմում է մոտ **18%**, իսկ որոշ զարգացած տնտեսություններում այն հասնում է **55-60%**։",

        "top_10_industries": "Թոփ 10 Ինդուստրիաներ",
        "top_10_industries_title": "Թոփ 10 Ինդուստրիաները <<{level}>> մակարդակի համար",
        "industry_missing_warning": "❗ 'industry' սյունակը բացակայում է։",

        "top_10_categories_title": "Թոփ 10 աշխատանքային կատեգորիաներ",
        "category_missing_warning": "❗ 'category' սյունակը բացակայում է։",

        "top_10_jobs_title": " Թոփ 10 Հաստիքներ",
        "top_10_jobs_for_level": "Թոփ 10 Հաստիքները <<{level}>> մակարդակի համար",
        "name_missing_warning": "❗ 'name' սյունակը բացակայում է։",
        "no_data_for_level": "Տվյալներ չկան այս մակարդակ համար։",

        "top_10_job_categories_title": "Թոփ 10 մասնագիտական ուղղվածություններ",
        "top_10_job_categories_chart_title": "Թոփ 10 մասնագիտական ուղղվածությունները <<{level}>> մակարդակի համար",
        "jobcategory_missing": "❗ 'jobcategorybyfirst' սյունակը բացակայում է տվյալների մեջ։",

        "select_level_info": "Ընտրել մակարդակը համապատասխան վերլուծությունը դիտելու համար ․",
        "top_10_categories_for_level": "Թոփ 10 Կատեգորիաներ <<{level}>> մակարդակի համար",

        "select_level": "Ընտրել մակարդակը",
        "top_categories_by_level": "<<{level}>> մակարդակի թոփ 10 job կատեգորիաները",
        "no_data": "Տվյալներ չկան այս մակարդակի համար։",

        "importance_title": "📊 Մակարդակների վերլուծության կարևորությունը",
        "importance_p1": "Մակարդակների վերլուծությունը թույլ է տալիս խորությամբ պատկերացում կազմել հայկական աշխատաշուկայի կառուցվածքի և դինամիկայի մասին։ Տվյալների համադրումը պարզ է դարձնում, թե որ ուղղություններում մեծ պահանջարկ կա սկսնակ մասնագետների նկատմամբ, և որտեղ առավելություն ունեն փորձառու աշխատակիցները։",
        "importance_p2": "Այս պատկերացումները օգնում են՝",
        "employers_line": "գործատուներին ձևավորել արդյունավետ մարդկային ռեսուրսների ռազմավարություն՝ թիրախային հավաքագրում և վերապատրաստում իրականացնելու համար,",
        "professionals_line": "մասնագետներին գնահատել իրենց կարիերայի աճի հնարավորությունները և պլանավորել զարգացումը՝ շուկայի պահանջներին համապատասխան։",
        "final":"Այս մոտեցումը ստեղծում է աշխատաշուկայի ավելի թափանցիկ և արդյունավետ միջավայր՝ աջակցելով թե՛ կազմակերպություններին, թե՛ մասնագետներին։"
},
"en": {
  "page_title": "Levels Analysis",

  "level_distribution_title": "Level distribution",
  "level_bar_title": "Level distribution chart",
  "level_column_missing": "The 'level' column is missing from the data.",

  "level_analysis_title": "Level analysis",
  "analysis_for_level": "See the relevant analysis for the `{level}` level",

  "student_oecd_comparison_title": "📉 Comparative analysis of student-level job openings: Armenia vs OECD",

  "student_intern_armenia": "The analysis shows that student and internship-level opportunities in Armenia are significantly limited.",
  "student_intern_oecd": "Out of **{total_jobs}** active jobs, only **{student_intern_jobs}** mention a student or internship level, which is just **{percentage:.1f}%**.",
  "student_intern_conclusion": "For comparison, the average in OECD (Organisation for Economic Co-operation and Development) countries is around **18%**, and in some advanced economies it reaches **55–60%**.",

  "top_10_industries": "Top 10 industries",
  "top_10_industries_title": "Top 10 industries for the `{level}` level",
  "industry_missing_warning": "❗ The 'industry' column is missing.",

  "top_10_categories_title": "Top 10 job categories",
  "category_missing_warning": "❗ The 'category' column is missing.",

  "top_10_jobs_title": "Top 10 job titles",
  "top_10_jobs_for_level": "Top 10 job titles for the `{level}` level",
  "name_missing_warning": "❗ The 'name' column is missing.",
  "no_data_for_level": "No data for this level.",

  "top_10_job_categories_title": "Top 10 occupational directions",
  "top_10_job_categories_chart_title": "Top 10 occupational directions for the `{level}` level",
  "jobcategory_missing": "❗ The 'jobcategorybyfirst' column is missing from the data.",

  "select_level_info": "Select a level to view the corresponding analysis.",
  "top_10_categories_for_level": "Top 10 categories for the `{level}` level",

  "select_level": "Select level",
  "top_categories_by_level": "Top 10 job categories for the `{level}` level",
  "no_data": "No data for this level.",

  "importance_title": "📊 Why level analysis matters",
  "importance_p1": "Level analysis helps build a deep understanding of the structure and dynamics of Armenia’s labor market. Comparing data reveals where demand for entry-level talent is high and where experienced professionals have the advantage.",
  "importance_p2": "These insights help:",
  "employers_line": "employers design effective HR strategies for targeted hiring and training,",
  "professionals_line": "professionals assess their growth opportunities and plan development aligned with market needs.",
  "final": "This approach creates a more transparent and efficient labor market, supporting both organizations and professionals."
},
"ru": {
  "page_title": "Аналитика уровней",

  "level_distribution_title": "Распределение уровней",
  "level_bar_title": "График распределения уровней",
  "level_column_missing": "В данных отсутствует столбец 'level'.",

  "level_analysis_title": "Аналитика уровней",
  "analysis_for_level": "Посмотрите соответствующий анализ для уровня `{level}`",

  "student_oecd_comparison_title": "📉 Сравнительный анализ вакансий уровня student: Армения vs OECD",

  "student_intern_armenia": "Анализ показывает, что вакансии уровня student и стажировок в Армении существенно ограничены.",
  "student_intern_oecd": "Из **{total_jobs}** активных вакансий только в **{student_intern_jobs}** указан уровень student или internship — это всего **{percentage:.1f}%**.",
  "student_intern_conclusion": "Для сравнения, средний показатель в странах ОЭСР (Организация экономического сотрудничества и развития) — около **18%**, а в ряде развитых экономик достигает **55–60%**.",

  "top_10_industries": "Топ-10 отраслей",
  "top_10_industries_title": "Топ-10 отраслей для уровня `{level}`",
  "industry_missing_warning": "❗ В данных отсутствует столбец 'industry'.",

  "top_10_categories_title": "Топ-10 категорий вакансий",
  "category_missing_warning": "❗ В данных отсутствует столбец 'category'.",

  "top_10_jobs_title": "Топ-10 должностей",
  "top_10_jobs_for_level": "Топ-10 должностей для уровня `{level}`",
  "name_missing_warning": "❗ В данных отсутствует столбец 'name'.",
  "no_data_for_level": "Нет данных для этого уровня.",

  "top_10_job_categories_title": "Топ-10 профессиональных направлений",
  "top_10_job_categories_chart_title": "Топ-10 профессиональных направлений для уровня `{level}`",
  "jobcategory_missing": "❗ В данных отсутствует столбец 'jobcategorybyfirst'.",

  "select_level_info": "Выберите уровень, чтобы посмотреть соответствующий анализ.",
  "top_10_categories_for_level": "Топ-10 категорий для уровня `{level}`",

  "select_level": "Выберите уровень",
  "top_categories_by_level": "Топ-10 категорий вакансий для уровня `{level}`",
  "no_data": "Нет данных для этого уровня.",

  "importance_title": "📊 Важность анализа уровней",
  "importance_p1": "Анализ уровней помогает глубже понять структуру и динамику рынка труда Армении. Сопоставление данных показывает, где высокий спрос на начинающих специалистов, а где преимущество у опытных.",
  "importance_p2": "Эти инсайты помогают:",
  "employers_line": "работодателям выстраивать эффективную HR-стратегию для таргетированного найма и обучения,",
  "professionals_line": "специалистам оценивать возможности карьерного роста и планировать развитие в соответствии с потребностями рынка.",
  "final": "Такой подход делает рынок труда более прозрачным и эффективным, поддерживая и организации, и специалистов."
}
}


st.markdown(
    f"""
    <div style='
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
        text-align: center;
        font-size: 3rem;
        line-height: 1.6;
    '>
        <h1 style='color: white;font-size:2rem'>{translations[lang]["page_title"]}</h1>
    </div>
    """,
    unsafe_allow_html=True
)

def wrap_title(text: str, width: int = 24) -> str:
    words = str(text).split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            if cur:
                lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return "<br>".join(lines)


@st.cache_data
def load_data(path=f"{BASE_DIR}data/All.xlsx"):
    df = pd.read_excel(path)
    df.columns = [col.lower() for col in df.columns]
    return df

df = load_data()

allowed_levels = ['Student', 'Junior', 'Mid level', 'Senior', 'Not defined']

if 'level' in df.columns:
    level_df = df[df['level'].isin(allowed_levels)]

    level_counts = (
        level_df['level']
        .value_counts()
        .reindex(allowed_levels, fill_value=0)
        .reset_index()
    )
    level_counts.columns = ['Levels', 'Color']

    st.markdown(f"#### {translations[lang]['level_distribution_title']}")

    st.dataframe(level_counts, hide_index=True, use_container_width=True)


    fig = px.bar(
        level_counts,
        x="Levels",
        y="Color",
        color="Color",
        color_continuous_scale="viridis",
        title="",
        text="Color"
    )
    fig.update_layout(
        xaxis_title=None,
        yaxis_title="Open Positions (number)",
        title_x=0.3,
        height = 500,
        title_text = ""
    )
    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning(f"❗ {translations[lang]['level_column_missing']}")

#-------------------------------------------------------------------------------------------------------------
st.markdown("---")

st.markdown("""
<style>
.subheader-text{
  font-size: 30px;        
  font-weight: 700;
  color: #d8e2eb;
  line-height: 1.2;
  margin: .25rem 0 1rem 0;
}
</style>
""", unsafe_allow_html=True)

job_counts = df['name'].value_counts(dropna=True)

st.markdown(f"<div class='subheader-text'> {translations[lang]['student_oecd_comparison_title']}</div>", unsafe_allow_html=True)

total_jobs = df['name'].count() 

student_intern_jobs = df[df['level'].str.lower().isin(['student', 'internship'])]['name'].count()

percentage = (student_intern_jobs / total_jobs) * 100
total_jobs = df['name'].count()
student_intern_jobs = df[df['level'].str.lower().isin(['student', 'internship'])]['name'].count()
percentage = (student_intern_jobs / total_jobs) * 100

LANG_LABEL_TO_CODE = {"Հայերեն": "hy", "English": "en", "Русский": "ru"}

def _current_lang_code() -> str:
    raw = (
        st.session_state.get("lang_code")
        or st.session_state.get("lang")
        or st.session_state.get("language")
        or "hy"
    )
    code = LANG_LABEL_TO_CODE.get(raw, raw)  
    if code not in translations:
        code = "en" if "en" in translations else next(iter(translations.keys()))
    return code

def t(key: str, **kwargs) -> str:
    code = _current_lang_code()
    txt = translations.get(code, {}).get(key) or translations.get("en", {}).get(key) or key
    try:
        return txt.format(**kwargs) if kwargs else txt
    except KeyError:
        return txt



st.markdown(t("student_intern_armenia"))

st.markdown(t(
    "student_intern_oecd",
    total_jobs=total_jobs,
    student_intern_jobs=student_intern_jobs,
    percentage=percentage,  
))

st.markdown(t("student_intern_conclusion"))

st.markdown("---")
#---------------------------------------------------------------------------------------------------------------
st.markdown(f"<div class='subheader-text'> {translations[lang]['level_analysis_title']}</div>", unsafe_allow_html=True)

st.markdown(translations[lang]["select_level_info"])


levels = ['Student', 'Junior', 'Mid level', 'Senior', 'Not defined']

cols = st.columns(5)

active_level = None
for idx, level in enumerate(levels):
    if cols[idx].button(level):
        active_level = level

if active_level:
    st.markdown(f"---\n#### {translations[lang]['analysis_for_level'].format(level=active_level)}")

    level_df = df[df["level"] == active_level]

    if not level_df.empty:
        st.markdown(f"<div class='subheader-text'> {translations[lang]['top_10_industries']}</div>", unsafe_allow_html=True)
        

        if "industry" in level_df.columns:
            industry_counts = (
                level_df["industry"]
                .dropna()
                .value_counts()
                .head(10)
                .reset_index()
            )
            industry_counts.columns = ["Industry", "Color"]

            title_wrapped1 = wrap_title(translations[lang]["top_10_industries_title"].format(level=active_level), width=24)


            fig_industry = px.bar(
                industry_counts,
                x="Industry",
                y="Color",
                color="Color",
                color_continuous_scale="teal",
                text="Color",
                title=title_wrapped1
            )
            fig_industry.update_layout(
                xaxis_title=None,
                yaxis_title="Open Positions (number)",
                title_x=0.3,
                height = 600

            )
            fig_industry.update_traces(textposition="outside")

            st.plotly_chart(fig_industry, use_container_width=True)

        else:
            st.warning(translations[lang]["industry_missing_warning"])

        st.markdown("---")

        st.markdown(f"<div class='subheader-text'> {translations[lang]['top_10_categories_title']}</div>", unsafe_allow_html=True)
        

        if "category" in level_df.columns:
            category_counts = (
                level_df["category"]
                .dropna()
                .value_counts()
                .head(10)
                .reset_index()
            )
            category_counts.columns = ["Category", "Color"]
            title_wrapped2 = wrap_title(translations[lang]["top_10_categories_for_level"].format(level=active_level), width=24)

            fig_category = px.bar(
                category_counts,
                x="Category",
                y="Color",
                color="Color",
                color_continuous_scale="plasma",
                text="Color",
                title = title_wrapped2,
                
            )
            fig_category.update_layout(
                xaxis_title=None,
                yaxis_title="Open Positions (number)",
                title_x=0.3,
                height = 600

            )
            fig_category.update_traces(textposition="outside")

            st.plotly_chart(fig_category, use_container_width=True)

        else:
            st.warning(translations[lang]["category_missing_warning"])


        st.markdown("---")
        #---------------------------------------------------------------------------------------------------

        st.markdown(f"### {translations[lang]['top_10_jobs_title']}")

        if "name" in level_df.columns:
            job_counts = (
                level_df["name"]
                .dropna()
                .value_counts()
                .head(10)
                .reset_index()
           )
            job_counts.columns = ["Job Title", "Color"]  

            title_wrapped3 = wrap_title(
                translations[lang]["top_10_jobs_for_level"].format(level=active_level),
                width=24
            )

            fig_jobs = px.bar(
                job_counts,
                x="Job Title",                 
                y="Color",                     
                color_continuous_scale="viridis",
                text="Color",
                title=title_wrapped3
            )

            fig_jobs.update_traces(
                textposition="outside",
                textfont_size=12,
                marker_line_color="white",
                marker_line_width=1,
                showlegend=False
            )

            fig_jobs.update_layout(
                coloraxis_showscale=False,            
                xaxis=dict(
                    title=translations[lang].get("job_column", ""),
                    tickangle=-25,
                    tickfont=dict(size=12),
                    automargin=True,
                    categoryorder="total descending", 
                    gridcolor="rgba(255,255,255,0.1)"
                ),
                yaxis=dict(
                    title=translations[lang].get("open_positions_column", "Open Positions(number)"),
                    gridcolor="rgba(255,255,255,0.12)",
                    zerolinecolor="rgba(255,255,255,0.25)"
                ),
                margin=dict(t=60, b=120, l=70, r=30),
                title_x=0.3,
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
                height = 550
            )

            st.plotly_chart(fig_jobs, use_container_width=True)
        else:
            st.warning(translations[lang]["name_missing_warning"])


        st.markdown("---")

        #---------------------------------------------------------------------------------------------------
        st.markdown(f"### {translations[lang]['top_10_job_categories_title']}")

        if "jobcategorybyfirst" in level_df.columns:
            jobcat_counts = (
                level_df["jobcategorybyfirst"]
                .dropna()
                .value_counts()
                .head(10)
                .reset_index()
            )
            jobcat_counts.columns = ["Job title", "Color"]  

            title_wrapped4 = wrap_title(
                translations[lang]["top_10_job_categories_chart_title"].format(level=active_level),
                width=24
            )

            fig_jobcat = px.bar(
                jobcat_counts,
                x="Job title",                 
                y="Color",                     
                color="Color",
                color_continuous_scale="cividis",
                text="Color",
                title=title_wrapped4
            )

            fig_jobcat.update_traces(
                textposition="outside",
                textfont_size=12,
                marker_line_color="white",
                marker_line_width=1,
                showlegend=False
            )

            fig_jobcat.update_layout(
                coloraxis_showscale=False,           
                xaxis=dict(
                    title=None,
                    tickangle=-25,
                    tickfont=dict(size=12),
                    automargin=True,
                    categoryorder="total descending", 
                    gridcolor="rgba(255,255,255,0.1)"
                ),
                yaxis=dict(
                    title="Open Positions (number)",
                    gridcolor="rgba(255,255,255,0.12)",
                    zerolinecolor="rgba(255,255,255,0.25)"
                ),
                margin=dict(t=60, b=120, l=70, r=30),
                title_x=0.3,
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
                height = 550
            )

            st.plotly_chart(fig_jobcat, use_container_width=True)
        else:
            st.warning("❗ 'jobcategorybyfirst' սյունակը բացակայում է տվյալների մեջ։")

        st.markdown("---")


    else:
        st.warning(translations[lang]["no_data_for_level"])




def _lang_code() -> str:
    raw = (
        st.session_state.get("lang_code") 
        or st.session_state.get("lang")   
        or "hy"
    )
    code = LANG_LABEL_TO_CODE.get(raw, raw)
    return code if code in translations else "en"

def _t(k: str) -> str:
    code = _lang_code()
    return translations.get(code, {}).get(k) or translations.get("en", {}).get(k, k)

def render_level_importance_block():
    html = f"""
<div style="
    background: linear-gradient(90deg, #0f172a 0%, #64748b 100%);
    padding: 2rem;
    border-radius: 15px;
    margin-top: 2rem;
    color: white;
    font-size: 1rem;
    line-height: 1.6;">
  <h3 style="margin: 0 0 .75rem 0;">{_t("importance_title")}</h3>
  <p style="margin: 0 0 .75rem 0;">{_t("importance_p1")}</p>
  <p style="margin: 0 0 .75rem 0;">{_t("importance_p2")}</p>
  <ul style="margin: .25rem 0 0 1.2rem;">
    <li>{_t("employers_line")}</li>
    <li>{_t("professionals_line")}</li>
  </ul>
  <p style="margin: 0 0 .75rem 0;">{_t("final")}</p>
</div>
"""
    st.markdown(html, unsafe_allow_html=True)

render_level_importance_block()