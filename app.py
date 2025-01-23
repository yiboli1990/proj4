Below is a concise summary of the main points and discussion threads in the transcript:
	1.	Upcoming Meeting With Brian (Monday)
	•	The speakers are planning to update Brian on several topics, including AI guardrails (previously discussed), final adjustments to the ETSC framework, and an introduction of a “pro reject” approach and systematic consumer testing.
	•	They also want to bundle together updates around MRM, ETSC, and ETP commitments to provide a cohesive “end state” picture.
	2.	AI Topics & T/Risk Coordination
	•	There is friction regarding how T/Risk and second-line teams process reviews and the perception that second-line processes are slowing down AI initiatives.
	•	T/Risk appears to be deferring some steps or waiting until after MRM reviews to avoid repetitive rework.
	•	The team notes that developers (and others) sometimes blame risk/control functions for delays, but emphasize that T/Risk is independent and has its own process.
	•	The group considers having a direct conversation with T/Risk (possibly with “Car”) to clarify procedures and reduce miscommunication—ideally in person rather than via email.
	3.	New Detection Model for T2
	•	There is a mention of a new AI-related detection model with shorter latency (around one second).
	•	The plan is to pilot it for bankers and eventually expand it for GS or broader usage.
	•	It would be “preventative” rather than “detective,” checking documents in real time.
	4.	Transformer Model for Short-Term Trading Signals
	•	A separate team is building a transformer-based model to generate trading signals over very short windows (e.g., ten seconds).
	•	Discussion centers on how MRM or second-line could effectively validate or test these kinds of real-time models, which can be challenging with fast market data.
	•	There is a question of whether this transformer approach qualifies as “GI/AI” given it is presumably much smaller scale than large language models (LLMs).
	5.	Buyback Trade and MMLat Update
	•	Brief reference to a new client-related buyback trade (about 500 million EUR) with some discontinuities in payoff.
	•	Possible plan to mention this to Brian if relevant, though it may be more detail than he needs.
	6.	FRAC Breaches and New Workflow Tool
	•	They discuss persistent FRAC (Framework for Risk Appetite Compliance) breaches and the firm’s protocol for addressing them (e.g., obtaining new committed dates, root-cause explanations).
	•	A new “breach action plan protocol” and workflow tool from risk engineering might soon be mandatory.
	•	Concern is raised that this new process was built primarily with market risk in mind and might be too cumbersome or less relevant for non-financial risk.
	•	They note it will require some scrutiny to ensure it makes sense for their specific use cases before they adopt it.
	7.	Regulatory Exam (Michaela / Next Steps)
	•	The team wants clarity on how aggressively to respond to exam feedback from regulators.
	•	They sense the regulatory examination team might be split: some think the current approach is adequate, others believe more thorough documentation is required.
	•	They plan to see if they can glean more information informally during upcoming meetings (e.g., an MRM “conclave”).
	•	They also discuss whether scheduling time directly with Michaela after some internal alignment might be beneficial.
	8.	General Approach & Next Steps
	•	The speakers plan to provide Brian with a summary of all these points: AI guardrails, ETSC framework, T/Risk coordination, FRAC breaches, CCR updates, and possible buyback trade updates.
	•	They will also flag any overhead or headcount concerns if new processes (e.g., the FRAC workflow tool) become mandatory.
	•	They consider setting up a timeline for year-end tasks (e.g., internal sign-offs, next regulatory discussions) and ensure they coordinate well with leadership and exam teams.

Overall, the conversation focuses on preparing for an upcoming leadership update (with Brian), addressing AI model governance (especially T/Risk interactions), dealing with repeated FRAC breaches, and strategizing regulatory engagements and next steps.












Summary of the Meeting
	1.	Overall Exam Objective and Process
	•	The Federal Reserve exam focused on assessing the firm’s Model Risk Management (MRM) framework and practices, including governance, model development, model validation, and ongoing monitoring procedures.
	•	The examiners conducted transaction testing to evaluate how well the firm executes its MRM procedures in practice.
	•	The exam occurred virtually between September 20, 2024, and November 15, 2024.
	2.	Key Conclusion: Generally Satisfactory but One MRA Issued
	•	Examiners concluded that most components of the firm’s MRM framework are “generally satisfactory.”
	•	However, the exam identified a control deficiency in the validation framework for “in-use” models. This deficiency may impede the firm’s ability to confirm that models remain appropriately calibrated and fit for purpose over time.
	•	As a result, an MRA (Matter Requiring Attention) is being issued regarding weaknesses in the model validation controls framework.
	3.	Details of the MRA
	•	Deficiency in Qualitative Assessments: Although the firm uses both qualitative and quantitative tools to assess model performance, there is insufficient documentation or substantiation for qualitative assessments, except in cases that trigger additional validation or remediation.
	•	Limited Evidence of Qualitative Reviews: During quarterly and annual reviews, examiners saw little evidence that qualitative assessments had actually been performed or documented.
	•	Infrequent Revalidations: A significant proportion of models have not been revalidated over recent years, raising safety and soundness concerns—particularly for higher-risk models that are not automatically subject to periodic revalidation.
	•	Remediation Required by December 31, 2025: The firm must enhance its MRM practices so that both quantitative and qualitative assessments are adequately and consistently supported, especially in quarterly/annual reviews for higher-risk models.
	4.	Clarifications on Revalidation Frequency
	•	The Federal Reserve does not mandate specific revalidation intervals in the guidance. However, the examiners emphasized the importance of confirming that models remain fit for purpose on a regular basis.
	•	The MRA focuses on ensuring ongoing, evidence-based checks rather than dictating a particular revalidation schedule.
	5.	Observations on the Apple Card CECL Model (Model 2381)
	•	While these issues are not new findings (they were already noted in a previous ACL exam), examiners reiterated concerns regarding:
	1.	Model Development: Issues in regression inputs, regression-output evaluation, and insufficient model-fit testing.
	2.	Model Documentation: Limitations and compensating controls were not prominently highlighted, and documentation did not meet MRM standards.
	3.	Model Validation: Validators did not sufficiently justify use of the same approach for Apple Card and the Apple Card monthly installment product. Excessive use of time dummy variables raised concerns about overfitting, which was not challenged by validators.
	4.	Ongoing Monitoring: Thresholds are set such that red performance is only triggered if both the Apple Card model and an alternative model underperform—this dependency might mask issues.
	•	Supervisory findings related to this model remain open from the previous ACL exam, so no new formal findings are being issued here. However, the examiners encouraged continued remediation and deeper engagement if needed.
	6.	Next Steps
	•	The firm plans to review the final exam letter in detail and then discuss with the Federal Reserve examiners how best to address the MRA.
	•	Examiners will continue quarterly monitoring; during these updates, the firm can raise any questions about the MRA or other related issues.

Overall, the meeting emphasized the importance of comprehensive and well-documented qualitative assessments, alongside quantitative monitoring, to ensure all models in use remain appropriately calibrated and truly fit for their intended purpose—particularly in rapidly changing market or business environments.






Below is a structured, detailed summary of the conversation. It reflects the key points, the context surrounding each, and the follow-up actions or concerns raised during the discussion.

1. Upcoming Meeting with Brian (MRM Exit Meeting)
	•	Schedule Confirmation: There is an MRM (Model Risk Management) exit meeting planned with Brian on Monday (or possibly Tuesday).
	•	Agenda Items:
	•	Regulatory Updates: The team wants to finalize and present various regulatory updates, including Basel-related developments and some second collateral allocator issues.
	•	AI Updates:
	•	Recent internal “guardrail” approvals.
	•	Governance process changes for AI usage.
	•	Overview of AI initiatives in production and a forward-looking view (next quarter or two).

2. AI Initiatives and Business Use Cases
	•	Large Language Models (LLMs): There is a mention of a “long list” of large LLM-based tools that will impact more models soon.
	•	Generative BI (Business Intelligence): Discussion of projects integrating generative AI for reporting and decision support.
	•	Project Mentions:
	•	“TBMs, the strocking with lia project piano” (the details are somewhat unclear, but these appear to be internal code names or project references).
	•	A “phase two” rollout is coming soon, possibly for a next-stage AI or machine-learning tool.
	•	User Feedback:
	•	The group wants someone unbiased (e.g., Erica or Wesley) to provide feedback on AI’s accuracy and utility.
	•	Current AI accuracy is reported at 91%, which they note is often better than what humans achieve—though there’s some question about the thoroughness of the resources supporting it.

3. Discussion on Electronic Trading & Market Conduct
	•	Market Conduct Rules: Brief mention of “market conduct for ETPs” (Exchange-Traded Products) and possible inclusion in the upcoming Brian meeting agenda.
	•	CBA Switch / Puzzle 3: There is a mention of a “puzzle for CBA switch,” though the relevance to the meeting’s main agenda is uncertain. It might be included in broader regulatory updates (e.g., “Basel 3,” European submission).

4. Regulatory / Basel 3 Updates
	•	Follow-Up for Brian: They want to combine recent updates on Basel 3 and other European regulatory changes into one summary for Brian.
	•	Addressing Brian’s Questions: There were questions posed by Brian previously (possibly about Basel or capital adequacy), and the team intends to provide a verbal update or bullet points clarifying those.

5. Second Collateral Allocator Issue
	•	Year-End Material Issues:
	•	There were multiple DRC (Default Risk Charge) and SOKR (possibly “Securities or Collateral” references) issues discovered before year-end.
	•	A new “bill” was posted, but the conversation implies that some details might still be unresolved.
	•	Open Points: The team is trying to recall specifics and ensure Brian is updated on these items if they are significant.

6. Metrics & Remediation Progress
	•	ATLC Findings:
	•	Initially quite high (21 issues), reduced to 14, but further progress has been slow or complicated by new items.
	•	Term Structure / “Tier One Age” Findings:
	•	Talk of metrics going from 54 down to around 20-something. The official numbers are stale (from November) and likely improved by year-end.
	•	GBM Findings:
	•	Not as much progress as hoped. Internal push is needed since the front office is apparently comfortable breaching “track” but not “work” (i.e., not meeting internal deadlines but not necessarily failing official regulatory deadlines).
	•	The team wants to escalate this reluctance to Brian and/or Alex to enforce accountability.

7. Communication & Escalation Strategy
	•	Follow-Up with GBM:
	•	The group has trouble getting consistent updates from GBM on remediation.
	•	Leadership in GBM told staff it is fine to breach the internal trackers (frack?), just not the official regulatory ones—a stance the MRM/validation team finds unacceptable.
	•	Involving Senior Leadership:
	•	Alex and Brian may intervene directly (e.g., phone calls) to reiterate the importance of meeting internal timelines and obligations, not just external regulatory ones.
	•	Maintaining “Statute”:
	•	The MRM team wants to keep up pressure and avoid undermining their own authority. They plan to phrase remediation deadlines as mandatory rather than negotiable.

8. Market & Trading-Book Observations
	•	Discount Curve Steepening:
	•	Nearly 200 basis point difference between lower short-term rates and the 10-year, while the Fed has cut rates 75 bps.
	•	The team wonders if there are notable trades or modeling issues tied to this rate environment.
	•	Risk Limits and VAR:
	•	In GTM space, the desk is apparently long USD 2.7 billion, but net risk is offset or “carnations inside,” so the VAR isn’t drastically affected. The group wants color on the rationale behind these positions.

9. Additional Model-Related Items
	•	CCAR Scenario & Narratives:
	•	Some new or ongoing approach to running the CCAR scenario with narrative explanation.
	•	The governance around these new modeling efforts is still being documented.
	•	“Canal” Ambitious Model:
	•	Possibly focusing on hedge funds or natural resources counterparties.
	•	There’s some confusion over classification by counterparty (natural resources) vs. classification by risk factor.

10. Final Preparations & Next Steps
	•	Meeting with Alex (Friday):
	•	The team plans to brief Alex or run certain items by him before bringing them up with Brian.
	•	There may be “red items” or urgent topics to discuss, but details are limited.
	•	Action Items:
	1.	Regulatory/AI/Model Updates: Finalize bullet points for Brian.
	2.	Finalize Basel 3 Follow-Up: Combine into a single document/summary.
	3.	Escalation on GBM Findings: Provide specific examples and names if needed so Alex/Brian can intervene.
	4.	Check on Market Risk Positions: Look into the discount curve steepening trades and how the bank is positioned.
	5.	Continue Gathering User Feedback on AI Tools: Identify an unbiased user champion (e.g., Erica, Wesley).

Overall Takeaway

The conversation revolves around preparing a thorough update for senior management (notably Brian, possibly Alex) covering:
	1.	Regulatory developments and outstanding remediation items (particularly around Basel 3 and the year-end findings).
	2.	AI initiatives and governance (accuracy rates, use cases, next-phase deployments).
	3.	Internal compliance challenges (GBM’s reluctance to meet MRM internal timelines).
	4.	Market insights (steepening rate curves, large positional bets).

The team is focused on ensuring a clear, consolidated message for Brian’s meeting, spotlighting progress, risks, and necessary escalations for effective remediation and accountability across business units.









Summary of the Transcript

The transcript outlines various updates and discussions on model risk management (MRM), remediation timelines, validation processes, and upcoming regulatory exams. Below is a summarized version of the key points:

1. Model Submissions and Remediation Timelines:
	•	Abilitiesization and Launch Timeline: The project has started but is not fully on track; the deadline is March.
	•	Prime Model BCD Review: Due by the end of January, focusing on outcomes analysis and implementation. Challenges are manageable, and findings will likely be combined with GSSEV validation (due mid-February).
	•	MR Remediation: Several findings with staggered timelines:
	•	Fed-raised issues require resolution by March.
	•	Sequencing steps involve December, February, and March milestones.
	•	Risk of findings remaining open for MR submission, though efforts are being made to avoid this.

2. Backtesting:
	•	Implementation has been received and is under review.
	•	Milestones for thresholds and frameworks are delayed until March.
	•	High-level testing is ongoing; main flaws may lie in the implementation phase.

3. Model Group and Gap Analysis:
	•	Reviews are on track, including:
	•	Theta model gaps (targeting 2025).
	•	Non-parallel scenarios (pending timeline adjustments after December 24th communication).

4. Calibrations and Monitoring:
	•	A decision on full model recalibration versus annual reassessment is pending, with recalibration likely, potentially resolving findings.
	•	New scenarios and metrics are being developed for cross-currency bases and sensitivity analysis.
	•	Frameworks for identifying key assumptions in sensitivity analysis are being finalized.

5. Exams and Exercises:
	•	ILST Exam: Materials are due by January 15th, with the exam in March. Key focus areas include governance, IT data, modeling documentation, and ongoing monitoring.
	•	BAU LGD Exercise: Scope is broad, including dependencies like FLR models, with a focus on inventory findings and validation logs.

6. General Risks and Concerns:
	•	Several findings are delayed, but efforts are being made to manage risks and ensure compliance with deadlines.
	•	Scope creep in certain exercises (e.g., BAU LGD) may require additional clarification and resource management.

Overall, the discussion reflects ongoing progress with manageable delays, a focus on implementation reviews, and preparations for regulatory exams and validations.












Below is a more detailed explanation of the DRC (sometimes referred to as “Decentralized Risk Categories” or similarly named regulatory/capital calculations) discussion and how they can be categorized, based on the transcript. The ultimate goal is to provide clarity on which DRC items fall under current policy scope (U.S. capital), which apply to specific non-U.S. legal entities, and which may fall outside capital rules altogether (e.g., liquidity requirements).

Why Categorize DRCs?

In the transcript, there was a concern that “DRCs” appear in multiple contexts—some are for U.S. capital calculations, some apply to foreign legal entities, and some may be tied to other regulations beyond capital (like liquidity or resolution planning). The team needs a systematic way to track each DRC so they can:
	1.	Explain the current state: Which DRCs are already covered by policy?
	2.	Identify gaps: Where do we lack clarity on coverage (e.g., newly discovered DRC items for non-U.S. entities)?
	3.	Plan next steps: Decide what to uplift, what to address later, and how to handle DRCs outside the “official” policy scope.

Three-Tier Categorization Approach

A straightforward approach is to create separate sections or tables that group DRCs by their applicability and underlying regulation:
	1.	Table A: U.S. Capital (Current Policy Scope)
	•	What’s included: All DRCs that fall under existing U.S. regulatory capital rules (Federal Reserve, OCC, FDIC).
	•	Subsections:
	•	Already Uplifted: DRCs that have been identified and fully addressed in policies/procedures.
	•	Pending Prioritization: DRCs recognized as in-scope for U.S. capital but not yet remediated or prioritized.
	•	In Development: Future changes (e.g., Basel 3 Endgame, FRTB) that will require new or updated DRCs.
	2.	Table B: Non-U.S. Legal Entities
	•	What’s included: DRCs that apply to legal entities beyond the U.S. scope, such as GSI (in the UK), GSIB, GSPE, or more specialized entities (e.g., GSJC for real estate).
	•	Goal: Clarify whether each DRC is (or should be) covered under your firm’s global capital policy, or if it’s governed by local rules (e.g., PRA in the UK, ECB for EU entities).
	•	Format: For each legal entity, list:
	•	DRC Name
	•	Purpose (e.g., local regulatory capital requirement, local liquidity coverage, resolution planning)
	•	Governing Regulator
	•	Current Status (covered in existing policy or not)
	3.	Table C: Non-Capital Requirements (Liquidity, Resolution Planning, etc.)
	•	What’s included: DRC items that are not strictly capital-related but may be risk or regulatory-driven, such as LCR (Liquidity Coverage Ratio), resolution planning, or other reporting requirements.
	•	Key Question: Are these truly DRCs (in the sense of capital/risk models), or are they something else (like a purely operational or accounting reserve)? If they’re capital-like items, do they fall under any existing policy or do they need a new governance path?

Sample Breakdown of Each Category

Here is a simplified illustration of how you might lay out the tables. (The exact content and naming conventions would depend on your firm’s taxonomy.)

Table A: U.S. Capital

DRC Name	Regulatory Source	Policy Status	Next Steps
DRC 1 – US Fed	Federal Reserve	Uplifted in 2023	Periodic review in Q1 2024
DRC 2 – FDIC Rule	FDIC (US)	Pending Prioritization	Finalize by Q2 2024
DRC 3 – Basel 3E	US Implementation	In Development	Monitor upcoming Basel 3 Endgame framework

Table B: Non-U.S. Legal Entities

Legal Entity	DRC Name	Regulator	Included in Policy?	Notes
GSI (UK)	DRC 4 – PRA Capital	PRA/BoE (UK)	Not in current US scope	Potential alignment with group-level capital policy
GSJC (Real Estate)	DRC 5 – FDIC Reserve?	FDIC? or Local Reg?	Unclear (entity-specific)	Needs further confirmation from Controllers or Tiago
GSIB (Int’l)	DRC 6 – EBA?	European Regulators	Not in current US scope	Evaluate if it belongs to a group-wide policy extension

Table C: Non-Capital Requirements

Requirement	DRC or Similar	Regulatory Driver	Policy / Governance
Liquidity Coverage (LCR)	LCR DRC?	Federal Reserve / Basel	Potentially outside capital policy
Resolution Planning	-	FDIC / Fed – Title I	Separate resolution planning processes
Other Reporting	-	Varies (ECB, PRA, etc.)	Not capital-related; governance unclear

Key Points from the Transcript
	1.	Clarify Missing or “Random” DRCs
	•	Some DRCs appear to be for very narrow applications (e.g., a real estate entity’s reserve calculation).
	•	Verify with Controllers (or relevant owners) whether these items belong in your consolidated capital/risk policy scope.
	2.	Understand the Regulatory Source
	•	FDIC might apply to certain U.S. entities, PRA/BoE for UK entities, ECB/EBA for EU, etc.
	•	If the DRC is truly U.S. capital-related, it should already be in scope (or at least flagged for inclusion). If it’s missing, you need to determine why.
	3.	Push for a Unified View
	•	The conversation suggests you can rely on Tiago or a Controllers resource to collect and confirm the correct universe of DRCs.
	•	Once you have that list, present it in a coherent structure (e.g., the three tables above).
	4.	Ultimate Purpose
	•	Make it easy for senior management (e.g., Brian, Alex) to decide which items need urgent uplifting, which can wait, and how to expand policy scope if needed.

Action Items to Finalize DRC Categorization
	1.	Gather Detailed Inventory
	•	Work with Controllers, Finance, and other first-line teams to get the complete list of DRC items (both U.S. and non-U.S.).
	2.	Identify the Regulator & Entity
	•	For each DRC, confirm if it’s governed by Fed, FDIC, PRA, ECB, or another body.
	3.	Determine Policy Inclusion
	•	Check whether each DRC is already covered in the current U.S. capital policy.
	•	If not, decide whether to include it in a future global policy update or treat it separately.
	4.	Draft the Tables
	•	Create the “3-Table” framework (U.S. Capital, Non-U.S. Entities, Non-Capital Requirements) and populate with the data.
	5.	Review & Approval
	•	Present to management (e.g., Brian/Alex) for alignment on next steps, prioritization, or expansions of the policy scope.

Final Thoughts

The DRC categorization is intended to give you a clear roadmap of which rules belong where, who oversees them, and how they relate to your existing policies. By separating U.S. capital items from non-U.S. legal entities and non-capital items, you gain a straightforward, “bite-sized” view of a potentially complex web of regulatory requirements.





#!/usr/bin/env python
# coding: utf-8

# In[1]:


from logging import debug
from typing import Dict
import os
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, dcc, html
from dash.dependencies import ALL, State

from myfuns import (genres, get_displayed_movies, get_highly_rated_movies,
                    get_recommended_movies)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], 
               suppress_callback_exceptions=True)
server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H3("Movie Recommender", className="display-8"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("System 1 - Genre", href="/", active="exact"),
                dbc.NavLink("System 2 - Collaborative", href="/system-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])

def render_page_content(pathname):
    if pathname == "/":
        return html.Div(
            [
                html.H1("Select a genre"),
                dcc.Dropdown(
                    id="genre-dropdown",
                    options=[{"label": k, "value": k} for k in genres],
                    value=None,
                    className="mb-4",
                ),
                html.Div(id="genre-output", className=""),
            ]
        )
    elif pathname == "/system-2":
        movies = get_displayed_movies()
        return html.Div(
            [
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.H1("Rate some movies below to"),
                                    width="auto",
                                ),
                                dbc.Col(
                                    dbc.Button(
                                        children=[
                                            "Get recommendations ",
                                            html.I(className="bi bi-emoji-heart-eyes-fill"),
                                        ],
                                        size="lg",
                                        className="btn-success",
                                        id="button-recommend",
                                    ),
                                    className="p-0",
                                ),
                            ],
                            className="sticky-top bg-white py-2",
                        ),
                        html.Div(
                            [
                                get_movie_card(movie, with_rating=True)
                                for idx, movie in movies.iterrows()
                            ],
                            className="row row-cols-1 row-cols-5",
                            id="rating-movies",
                        ),
                    ],
                    id="rate-movie-container",
                ),
                html.H1(
                    "Your recommendations", id="your-recommendation",  style={"display": "none"}
                ),
                dcc.Loading(
                    [
                        dcc.Link(
                            "Try again", href="/system-2", refresh=True, className="mb-2 d-block"
                        ),
                        html.Div(
                            className="row row-cols-1 row-cols-5",
                            id="recommended-movies",
                        ),
                    ],
                    type="circle",
                ),
            ]
        )

@app.callback(Output("genre-output", "children"), Input("genre-dropdown", "value"))
def update_output(genre):
    if genre is None:
        return html.Div()
    else: 
        return [
            dbc.Row(
                [
                    html.Div(
                        [
                            *[
                                get_movie_card(movie)
                                for idx, movie in get_highly_rated_movies(genre).iterrows()
                            ],
                        ],
                        className="row row-cols-1 row-cols-5",
                    ),
                ]
            ),
        ]
    
def get_movie_card(movie, with_rating=False):
    return html.Div(
        dbc.Card(
            [
                dbc.CardImg(
                    src=f"https://liangfgithub.github.io/MovieImages/{movie.movie_id}.jpg?raw=true",
                    top=True,
                ),
                dbc.CardBody(
                    [
                        html.H6(movie.title, className="card-title text-center"),
                    ]
                ),
            ]
            + (
                [
                    dcc.RadioItems(
                        options=[
                            {"label": "1", "value": "1"},
                            {"label": "2", "value": "2"},
                            {"label": "3", "value": "3"},
                            {"label": "4", "value": "4"},
                            {"label": "5", "value": "5"},
                        ],
                        className="text-center",
                        id={"type": "movie_rating", "movie_id": movie.movie_id},
                        inputClassName="m-1",
                        labelClassName="px-1",
                    )
                ]
                if with_rating
                else []
            ),
            className="h-100",
        ),
        className="col mb-4",
    )
    
@app.callback(
    Output("rate-movie-container", "style"),
    Output("your-recommendation", "style"),
    [Input("button-recommend", "n_clicks")],
    prevent_initial_call=True,
)    
def on_recommend_button_clicked(n):
    return {"display": "none"}, {"display": "block"}

@app.callback(
    Output("recommended-movies", "children"),
    [Input("rate-movie-container", "style")],
    [
        State({"type": "movie_rating", "movie_id": ALL}, "value"),
        State({"type": "movie_rating", "movie_id": ALL}, "id"),
    ],
    prevent_initial_call=True,
)

def on_getting_recommendations(style, ratings, ids):
    rating_input = {
        ids[i]["movie_id"]: int(rating) for i, rating in enumerate(ratings) if rating is not None
    }
  
    recommended_movies = get_recommended_movies(rating_input)
 
    return [get_movie_card(movie) for idx, movie in recommended_movies.iterrows()]


@app.callback(
    Output("button-recommend", "disabled"),
    Input({"type": "movie_rating", "movie_id": ALL}, "value"),
)
def update_button_recommened_visibility(values):
    return not list(filter(None, values))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use PORT environment variable if it's set, otherwise default to 8080
    app.run_server(port=port, debug=True)

# In[ ]:





# In[ ]:




