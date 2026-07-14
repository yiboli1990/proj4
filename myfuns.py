I need to draft an quarterly update to FRAC. Please first read some good examples in the past:
[Examples]
Artificial Intelligence
There is continued growth in the development of AI models, including recent approvals of
* A new Tier 1 Corporate Treasury generative Al model (Payment Settlements Al) used to automate matching of incoming payments
** Three high-severity findings related to performance, evaluation metrics, and testing were remediated through scope restrictions, enhanced performance metrics and monitoring, and expanded test coverage, resulting in improved performance and oversight
** The modelwill be rolled out in phases, initially operating in parallel with the current human review process and targeting a reductionin manual review of cash receipts from 13% to 2%
* A new Tier 2 GBM Public non-generative Al model (Albert Market Simulator), the first transformer-based model (a neural-network architecture widely used in modern Large Language Models (LLMs)) applied within the equity options/futures trading business
** The model predicts the distribution of key equity volatility surface parameters and produces optimized portfolio weights for rebalancing subject to multiple constraints
** During the validation, enhancements have been made to the optimizer and testing in response to Model Risk feedback, resulting in better convergence and more robust ongoing monitoring
* Two new Tier 2 Engineering generative Al models (M365 Copllot Web Grounding and Al Bing Search) that enable web search
grounding for queries within M365 Copilot and GS AI Assistant for GPT models, respectively
** Web grounding improves accuracy and reduces hallucinations by referencing web content when responding to user prompts
** Two high-severity findings on M365 Copilot Web Grounding, relating to insufficient model performance and testing, have been remediated through model enhancements prior to approval
** Following initial approval, Model Risk approved further enhancements to AI Bing Search, including infrastructure enhancements andupgraded LLM, addressing validation findings related to instability in the Bing search service and weighting of indvidual search results, which contributed to increased hallucinations
* Enhancements to the Tier 1 generative AI Guardrail Model for the GS AI Platform, including use of a larger GS proprietary dataset refining
system prompts and testing, incorporating human-tagged GS Al Assistant user prompts

Collateralized Lending
There is continued focus on development and validation work supporting the collateralized lending business, relating to extending coverage of FLR and tail risk models to reduce reliance on fallback methodologies and enhancing data inputs and methodologies to improve model accuracy.This includes approvals of:
* A new Tier 1 model used to estimate through-the-cycle GD for use in FLR calculations for GS Select performing loans
** The model supports Corporate Treasury's initiative to pledge GS Select exposures to the Federal Reserve discount window, enabling recognition of the collateralized nature of the portfolio and more accurately reflecting the risk profile of the exposures
* Enhancements to the Tier 1 FLR and tail risk models for residential mortgage to cover hybrid fix-and-flip and lot loan deals, extending coverage to asset classes previously handled through fallback methodologies and improving accuracy
* Enhancements to the Tier 1 residential mortgage tail risk model to incorporate interest rate swaps into collateral valuation, leveraging more comprehensive collateral-level data and improving tail risk accuracy
* Enhancements to the Tier 1 transport tail risk model, incorporating new data for stress calibration, updates to upstream pricing model including an index-based approach for lease probability of default, and improved differentiation between performing and non-performing leases, addressing prior validation findings

Global Banking & Markets
Validation activity during the period primarily related to:
* Risk management enhancements, including approvals of:
** Incorporation of control variates (adjustments to match market prices) into the Tier 1 pricing model for multi-asset autocallables, reducing Monte Carlo variance and enhancing stability in risk calculations
* A new Tier 1 model for estimating Vega risk in commodity products, using an improved numerical implementation for greater accuracy and deployed on the Griffin infrastructure for faster computation relative to the previously used infrastructure (CPL)
* CCR model enhancements, including recent approvals of:
** Enhancements to the Tier 1 interest rate franchise benchmark model to align stress loss aggregation with the Unified Benchmark Model, as part of ongoing harmonization efforts for shortfall benchmark models, resulting in reduced stress losses and improved backtesting performance across client portfolios
** Enhancements to the Tier 1 Prime Brokerage (PB) equity margin model to incorporate composite average daily volume (ADV) for European stocks in the Delta liquidation charge, aggregating trading volume across venues within the same currency and aligning with the US approach

Corporate Treasury
Model Risk approved a new Tier 1 vendor model used to calculate Bloomberg liquidity assessment (LQA) score at the security level, which is a key input into the firm's Liquid & Readily Marketable (LRM) qualitative approach used to classify securities as "Liquid & Readily Marketable" for purposes of calculating liquidity metrics and capital requirements
* This approval closes a finding from the initial validation of the Tier A qualitative approach approved last year
* The Bloomberg LQA Score is a vendor machine learning model that estimates liquidation costs and assigns percentile-based liquidity rankings for fixed-income securities used in the RM classification
* Two high-severity findings related to insufficient documentation were remediated prior to approval

Risk
Validation activity during the period primarily related to:
* Liquidity risk model enhancements, including approvals of:
** Enhancements to the Tier 1 MLO models to capture liquidity impacts from digital assets and SIMM, reducing the current overlays relating to MLO model limitations to zero and remediating two associated validation findings
*** This approval is part of an ongoing effort to improve the methodology, make the models more robust, and reduce reliance on overlays
** Enhancements to the Tier 1 Prime tail liquidity loss model, including incorporating synthetic term commitments and additional margin requirements as mitigants such as inflows from excess margin from certain clients, resulting in a benefit to the firm's PTL ratio
*** The PTL ratio measures mitigants (e.g., overnight debits) relative to short-term funding exposure (e.g., shorts departure) under a post-MLO tail risk scenario and is subject to FRAC and BRC limits
* Ongoing validation work related to new Fundamental Review of the Trading Book (FRTB) requirements, with a current focus on incremental US requirements, including approval of enhancements to the Tier 1 model used for constructing 10-day returns using 1-day historical return time series for risk factors to incorporate additional credit bond and mortgage risk factors
* Validation of methodologies for GSBE Internal Capital Adequacy Assessment Process (ICAAP) and Internal Liquidity Adequacy Assessment Process (ILAAP) was completed ahead of the mid-March submission to the European Central Bank (ECB)
** 82 models and qualitative approaches were used for ICAAP and 39 methodologies for ILAAP
** The review included, among others, validation of new methodologies to estimate Credit Valuation Adjustment (CVA) and Funding Valuation Adjustment (FVA) losses for commodity derivatives, provis ons for asset secured lending (ASL) portfolio, as well as economic internal perspective (EIP) capital requirements for identified risks related to equity compensation, and changes to climate as well as strategic and business environment
** 38 new findings were raised by Model Risk this cycle, out of which five have been remediated and closed, including both high-severity findings on revenue projection models related to model performance, which have been addressed through methodology enhancements

Regulatory Updates
ECB Supervisory Review and Evaluation Process (SREP) Feedback: ECB confirmed closure of the finding related to model inventory completeness, in particular, to ensure inclusion of approaches used to determine whether capital requirements are attributable to certain risk types for Pillar 1 and Pillar 2 capital
* Remediation involved training, inventory review and attestation by responsible business units, and updates to the GSBE Policy and Procedure Risk Handbook


[instructions]
Please we need to be neutral on the tone. Do not use extreme wors like "significant" "instrumental" etc. The purpose is just to state the fact. Not to brag.
Need to use plain language, define the acronyms as the first time of using.
Do not use the word "issue", because this has different meanings in the FRAC reporting.
You can help me write the sentences better, but do not make significant changes or changes to the bullet point structure, as the current draft is based on experience. But will let you know if otherwise.
It is not mandatory, but we should try to keep one sentence for one bullet point.
The below are some section specific instructions:
First section is AI:
Need to specify new model or model enhancements.
Need to specify agentic, generative, or non-generative model
Need to use parenthesis for the actual model name
High severity findings need to be highlighted in the sub-bullet, such as "High severity finding related to... has been remediated..." 
The second section is Collateralized Lending:
Need to separate the part for (1) extension to increase coverage, (2) extensions to incorporate additional bespoke deal types, which reduces reliance on fallback methodologies, and (3) enhancements to improve the accuracy of existing FLR and Tail Risk methodologies 
Note that previous examples might not be that good structure.
The third section is Global Banking & Markets:
This part lead with "Validation activity during the period primarily related to:"
Subsections include (as needed):
Risk management enhancements, including approvals of:
Valuation adjustments, including approvals of:
The annual recalibration of and changes to the methodology for the Standard Initial Margin Model
CCR model enhancements, including recent approvals of:
The forth section is as needed, including AWM, Corporate Treasury, and Platform Solutions
The fifth section is Risk or Risk and Capital
This part might also include CCR in terms of coherent shortfall model, for which we should lead as: There is continued focus on development and validation work related to enhancements to CCR management capabilities as part of the firm's ERMF uplift plans...
Other topics we should lead with "Model Risk has validated and approved.."

[Draft, please write better based on the above]
In the draft below, I will include details in the [info:...] for you to read as contexts and details.
Artificial Intelligence
There is continued growth in the development of Al models, including recent approvals of:
* A new Tier 1 Compliance generative Al model (Surveillance Al for Unusual Movement of Assets) used to close transaction monitoring surveillance alerts that would otherwise require human review
** The model leverages the same framework previously approved for insider trading surveillance, closes ~40%, and provides reasoning to help humans process the rest more efficiently
[info: MRM has validated and approved the model Surveillance Al for UMA (Model ID 28741, Tier 1) which uses an Agentic Al framework to auto-close low-risk alerts from a money laundering perspective associated with transactional activities within the firmwide classic portfolio. This portfolio includes PWM, FICC, Equities and Folio businesses. The model acts as a booster on top of the existing machine learning based UMA Classic model (ID: 27501, Tier 2), to reduce the volume of alerts generated that require manual investigation. In addition, the model reviews an entity's transactional activity from a money laundering perspective, summarizing the key facts and indicators relevant to the investigation to assist human review. MRM approves the model after independent review of conceptual soundness, implementation, testing and ongoing monitoring, and concludes that this model reduces the number of false positives by ~40% while maintaining an acceptable recall of 97.5%, above target threshold of 95%. Five severity-2 findings were raised as part of the validation, two were remediated before approval.]

* A new Tier 2 Risk generative Al model (Commentary Al) used to draft risk factor narratives for financial institution credit reviews
** The model is only used for financial institutions where internal credit ratings (ICRs) are not modeled with mandatory human-in-the-loop review and has no impact on risk factor scoring or ICR determination, which remain fully determined by Credit Risk
** A high-severity finding, related to generation of unsupported statements, has been remediated through prompt enhancements and implementation of a control to detect and flag unsupported content for analyst review, resulting in improved performance and oversight
[info: MRM has validated and approved Commentary Al (Risk, Tier 2), a generative Al model that uses a structured prompt driven framework to draft credit reviews commentaries across four risk factors: Asset Quality, Liquidity and Funding, Profitability, and Capitalization within the Financial Institution Internal Credit Rating (ICR) template. The model generates draft commentary on financial performance and risk drivers with mandatory human-in-the-loop review. There is no impact on risk factor scoring or internal credit ratings (ICR) determination, which remain fully determined by Credit Risk. The initial submission was rejected by MRM due to major concerns regarding a material level of unsupported statements in the model-generated commentaries. To address these concerns, the following changes were implemented:
Structured prompt enhancement: Updated the prompt to remove instructions that caused generating unsupported assertions. Critic control implementation: Added a critic control to detect and flag potentially unsupported content in generated commentary for reviewer attention. The Severity 1 finding was closed prior to approval.
Additional enhancements remain required under two Severity 2 findings, including further prompt refinements and ongoing monitoring. As shown in the plot below, commentary-level accuracy improved across stages-rising from 61% initially (pre-remediation) to 75% after prompt remediation, and ultimately to 94% in the delivered
version with critic control. MRM approves use only for the documented scope and intended use (Financial Institutions template risk-factor drafting in Review Manager with mandatory human review and acceptance); any scope expansion requires separate MRM approval.]

* Enhancements to the Tier 2GBM Private agentic Al model (CSG Al Agent), used to synthesize information across documents and enhance question-answering capabilities in the Capital Solution Group (CSG), to expand its capability from single-deal research to multi-deal comparative analysis
** During validation, Model Risk identified an implementation error where the agent generated incorrect document IDs, for which subsequent fix reduced query failure rates from 12% to 0% and lowered compute costs by 16%

* A new Tier 2GBM Public generative Al model (Equinox ETF) designed to convert free-form chat messages into structured Request for Quote (RFQ) and Request for Trade
(RFT) for the US Equities ETF business

* Anthropic models with Bing search in the Tier 2 Engineering generative Al model (M365 Copilot Web Grounding), improving overall web grounding capabilities compared to current GPT models
** Web grounding improves accuracy and reduces hallucinations by referencing web content when responding to user prompts

* Enhancements to GBM Public neural network-based non-generative Al models, including approvals of:
** Enhancements to the Tier 1 equity share buybacks pricing model (Buyback ML Pricer to support multi-currency transactions through integration of FX notional modeling
** Extension to the Tier 2 order-fill probability estimation model (TradeScore) allows the algo trading model to take input from the TradeScore model to optimize its decision based on the probability of order fill for for Latam Interest Rates algo trading business for BRL swap quoting
[info: MRM validated and approves the extension of TradeScore Quoting Model and X-Asset Utility Quoter (Tier 2, model ID: 27901, 20921) for Latam Interest Rates algo trading business for BRL swap quoting. This extension allows the algo trading model to take input from the TradeScore model to optimize its decision based on the probability of order fill. MRM independently tested both models and identified two medium severity findings on regime change capture, and ongoing monitoring. Both findings were remediated and closed.]

Collateralized Lending
* There is continued focus on development and validation work supporting the collateralized lending business, including approvals of:
** Extension to the Tier 1 FLR Fallback model to cover secured lending exposures to Business Development Companies (BDCs), increasing coverage previously not covered by the FLR framework
** Extension to the asset-specific FLR and Tail Risk models to incorporate additional bespoke deal types, including private equity facilities backed by put option on the equity, and loans backed by Bitcoin, supporting business growth while reducing reliance on fallback methodologies
** Enhancements to improve the accuracy of existing FLR and Tail Risk methodologies, including improved OAS calibration for Mortgage Servicing Right facilities, and enhanced recovery rate estimation for Tail Risk residential mortgage and FLR corporate credit models
[info: Collateralized Lending. MRM approved extending Facility Level Rating (FLR) coverage to secured lending exposures to Business Development Companies (BDCs) using the fallback approach. BDCs are regulated investment vehicles that provide financing to middle-market private companies, and GS' exposure is primarily through Revolving Credit Facilities secured by the underlying loan portfolios held by the BDCs. This extension results in approximately $0.5Bn in CPE migrating from High-Yield per ICR to Investment Grade per FLR. 4 model enhancements in asset-specific FLR and Tail Risk models are validated and approved by MRM in June, including (1) FLR model enhancements to support single asset backed private credit facilities, and enhanced OAS calibration for Mortgage Servicing Right facilities, contributing to approximately $O.7Bn in CPE migrating from High-Yield to Investment Grade. (2) Tail Risk model enhancements to support private equity facilities backed by an equity position and a put option written on that equity, and loans backed by Bitcoin, resulting in $0.4Bn shortfall under 1.25x coherent scenario]

















import pandas as pd
import requests
import numpy as np

# Define the URL for movie data
myurl = "https://liangfgithub.github.io/MovieData/movies.dat?raw=true"

# Fetch the data from the URL
response = requests.get(myurl)

# Split the data into lines and then split each line using "::"
movie_lines = response.text.split('\n')
movie_data = [line.split("::") for line in movie_lines if line]

# Create a DataFrame from the movie data
movies = pd.DataFrame(movie_data, columns=['movie_id', 'title', 'genres'])
movies['movie_id'] = movies['movie_id'].astype(int)

genres = list(
    sorted(set([genre for genres in movies.genres.unique() for genre in genres.split("|")]))
)

top_movies_per_genre_df = pd.read_csv('https://raw.githubusercontent.com/yiboli1990/proj4_1/main/top_movies_per_genre.csv')

def get_highly_rated_movies(genre: str):
    if genre in top_movies_per_genre_df.columns:
        # Get the movie IDs for the specified genre
        movie_ids = top_movies_per_genre_df[genre].dropna().astype(int).tolist()

        # Ensure the movies DataFrame has 'movie_id' as int for proper merging
        movies['movie_id'] = movies['movie_id'].astype(int)

        # Filter movies DataFrame for those IDs
        popular_movies = movies[movies['movie_id'].isin(movie_ids)]

        # Ensure the order is the same as in the CSV by setting a categorical
        # with the order defined by the CSV list
        movies_order = pd.Categorical(
            popular_movies['movie_id'],
            categories=movie_ids,
            ordered=True
        )
        popular_movies = popular_movies.assign(order=movies_order)
        popular_movies = popular_movies.sort_values('order').drop('order', axis=1).head(10)

        return popular_movies
    else:
        return pd.DataFrame()


def myIBCF(new_user, sim_matrix_url):
    # Load the similarity matrix
    sim_matrix = pd.read_csv(sim_matrix_url, index_col=0)

    # Initialize a dictionary to hold predicted ratings
    predictions = {}

    # Loop through each movie
    for movie in sim_matrix.columns:
        if pd.isna(new_user[movie]):  # Check if the movie is unrated by the new user
            # Select the top 30 similar movies
            top_movies = sim_matrix.loc[movie].dropna()
            top_movies = top_movies[top_movies.index.isin(new_user.index)]
            
            # Check for overlapping ratings
            overlapping_movies = top_movies.index[top_movies.index.isin(new_user.dropna().index)]
            if overlapping_movies.empty:
                continue  # Skip if no overlapping ratings

            # Compute prediction
            numer = sum(top_movies[overlapping_movies] * new_user[overlapping_movies])
            denom = sum(top_movies[overlapping_movies])
            if denom != 0:
                prediction = numer / denom
                predictions[movie] = prediction
            else:
                predictions[movie] = np.nan

    top_recommendations = sorted(predictions.items(), key=lambda x: x[1], reverse=True)[:10]

    # Check if we have fewer than 10 recommendations
    if len([rec for rec in top_recommendations if not pd.isna(rec[1])]) < 10:
        # Number of additional recommendations needed
        additional_needed = 10 - len([rec for rec in top_recommendations if not pd.isna(rec[1])])

        # Get movies not rated by the user
        unrated_movies = ratings_matrix.columns[ratings_matrix.loc[new_user.name].isna()]
        
        # For simplicity, pick the most-rated movies as additional recommendations
        most_rated_movies = ratings_matrix.count().sort_values(ascending=False)
        additional_recommendations = [(movie, np.nan) for movie in most_rated_movies.index if movie not in [rec[0] for rec in top_recommendations] and movie in unrated_movies]

        # Append these additional recommendations to the list
        top_recommendations.extend(additional_recommendations[:additional_needed])

    # Extract only the movie IDs from the top recommendations and convert them to integers
    top_movie_ids = [int(movie_id[1:]) for movie_id, _ in top_recommendations]  # Remove 'm' prefix and convert to integer

    return top_movie_ids

    # Check if we have fewer than 10 recommendations
    if len([rec for rec in top_recommendations if not pd.isna(rec[1])]) < 10:
        # Number of additional recommendations needed
        additional_needed = 10 - len([rec for rec in top_recommendations if not pd.isna(rec[1])])

        # Get movies not rated by the user
        unrated_movies = ratings_matrix.columns[ratings_matrix.loc[new_user.name].isna()]
        
        # For simplicity, pick the most-rated movies as additional recommendations
        most_rated_movies = ratings_matrix.count().sort_values(ascending=False)
        additional_recommendations = [(movie, np.nan) for movie in most_rated_movies.index if movie not in [rec[0] for rec in top_recommendations] and movie in unrated_movies]

        # Append these additional recommendations to the list
        top_recommendations.extend(additional_recommendations[:additional_needed])

def get_displayed_movies():
    return movies.head(100)

def get_recommended_movies(new_user_ratings):
    # Load the similarity matrix
    sim_matrix = pd.read_csv('https://raw.githubusercontent.com/yiboli1990/proj4_1/main/processed_similarity_matrix.csv', index_col=0)

    # Initialize a new Series with NaN values and an index that matches the similarity matrix
    new_user_ratings_series = pd.Series([np.nan] * len(sim_matrix.columns), index=sim_matrix.columns)

    # Update the series with the new user ratings
    # Prefix the movie IDs with 'm'
    for movie_id, rating in new_user_ratings.items():
        movie_key = 'm' + str(movie_id)
        if movie_key in new_user_ratings_series.index:
            new_user_ratings_series[movie_key] = rating
    
    top_movie_ids = myIBCF(new_user_ratings_series, 'https://raw.githubusercontent.com/yiboli1990/proj4_1/main/processed_similarity_matrix.csv')
    # Return the top recommendations
    # Create a DataFrame from the list of recommended movie IDs
    recommended_movies_df = pd.DataFrame(top_movie_ids, columns=['movie_id'])

    # Merge with the movies DataFrame to get full movie details
    recommended_movies_df = recommended_movies_df.merge(movies, on='movie_id')

    return recommended_movies_df

