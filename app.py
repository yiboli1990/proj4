I agree. The grouped bullet should still give enough context so the Committee understands what was enhanced and why. I’d keep it as one main bullet with two sub-bullets.

Counterparty Credit Risk (CCR) model enhancements, including recent approvals of:

* Enhancements to the Tier 1 Equity Franchise Benchmark model to harmonize stress methodologies with Synthetic Products Group portfolios as part of the broader CREST Unified Benchmark Model (UBM) migration.
    * The changes align equity liquidation, fund liquidation and credit stress assumptions across the two frameworks, supporting automation of the combined benchmark process and reducing reliance on manual overlays.
* Enhancements to Tier 1 Prime Brokerage and Franchise benchmark models across Equity and Interest Rate products, addressing validation findings and improving consistency of shortfall calculations.
    * Enhancements to the Prime Brokerage and Franchise Equity shortfall models introduced a dedicated crypto sector classification and more conservative concentration shocks to better capture the risk profile of crypto-related equities.
    * Enhancements to the Franchise Interest Rate Benchmark model incorporated variation margin and improved allocation of agent lender repo haircuts for repurchase agreements, resulting in more accurate shortfall calculations.

I think this is about the right balance:

* Main bullet: high-level theme.
* Sub-bullet 1: Equity / crypto enhancement.
* Sub-bullet 2: Interest Rate / repo enhancement.

It tells the Committee what changed without getting into implementation details like Agent Lender Disclosure (ALD) feeds or pledged value calculations, which are probably too technical for FRAC.


I agree with both comments.

For IR Delta, I think it deserves two bullets: one explaining why the work was done, and one explaining the outcome.

For Risk Management, I’d make every approval its own bullet, just like prior FRAC updates. For CCR, I’d make the UBM migration stand out, then group the remaining finding-driven enhancements.

⸻

Global Banking & Markets

* Model Risk approved a revised Interest Rate Delta backbone methodology for the NYC Volex portfolio used in Standard Initial Margin Model (SIMM) calculations.
    * During the significant Tier 1 revalidation, Model Risk identified limitations in the existing Interest Rate Delta methodology and raised a validation finding following independent benchmarking and analysis of longstanding counterparty SIMM disputes.
    * The revised methodology removes the previous backbone treatment, reducing overstated interest rate risk and associated initial margin requirements. Following implementation, the business observed a reduction in counterparty disputes and expects to close a related National Futures Association (NFA) and Securities and Exchange Commission (SEC) filing.

Validation activity during the period primarily related to:

Risk management enhancements, including approvals of:

* A new Tier 1 model used for pricing and risk management of interest rate index products, providing clients with efficient access to fixed income markets through index-based products.
    * Approval is currently limited to trades that are not eligible for the Standard Initial Margin Model (SIMM), pending completion of the SIMM methodology.
* A new Tier 1 methodology for callable overhedge management in equity autocallable products, improving the stability of risk measures and supporting more consistent pricing and trading management.
* New Tier 1 models used to price listed and over-the-counter American equity warrants, extending coverage of the previously approved local volatility framework to products with more complex dividend characteristics and resolving an existing model waiver.
* A new Tier 1 reserve methodology for Financial Transmission Rights (FTRs), replacing the existing reserve framework to improve valuation consistency and better align reserves with observed market pricing.
* A recalibration of the Tier 1 Mortgage Agency prepayment model used in private bank mortgage pricing, improving prediction of borrower prepayments and remediating an existing validation finding.

Counterparty Credit Risk (CCR) model enhancements, including recent approvals of:

* Enhancements to the Tier 1 Equity Franchise Benchmark model to harmonize stress methodologies with Synthetic Products Group portfolios as part of the broader CREST Unified Benchmark Model (UBM) migration, supporting greater consistency across shortfall benchmark models and reducing reliance on manual overlays.
* Enhancements to Tier 1 Prime Brokerage and Franchise benchmark models across Equity and Interest Rate products, addressing validation findings through improvements to crypto equity stress calibration, variation margin treatment for repurchase agreements, and allocation of agent lender repo haircuts within shortfall calculations.

⸻

I think this reads much closer to previous FRACs:

* Every approval is a single business-oriented bullet.
* The purpose is explained before the technical change.
* The UBM migration is clearly the headline CCR item.
* The remaining CCR work is presented as a collection of enhancements that resolve findings, rather than four very technical model changes. This is likely more useful for FRAC.





Yes. I think the overall structure is good and consistent with prior FRACs. I would mainly refine the language to be more neutral, reduce repetition, and make the bullets read more smoothly. I also incorporated some of the improvements we’ve discussed over the past few months.

⸻

Artificial Intelligence

There is continued growth in the development of AI models, including recent approvals of:

* A new Tier 1 Compliance agentic AI model (Surveillance AI for Unusual Movement of Assets) used to close transaction monitoring surveillance alerts that would otherwise require human review.
    * The model leverages the same framework previously approved for insider trading surveillance, automatically closes approximately 40% of alerts, and provides supporting reasoning to assist human review of the remaining alerts.
    * Three medium-severity findings were remediated prior to approval, with two additional medium-severity findings remaining open for ongoing enhancements and monitoring.

Comment: I changed generative to agentic because the model is clearly described as an agentic workflow rather than simply an LLM.

⸻

* A new Tier 2 Risk generative AI model (Commentary AI) used to draft risk factor narratives for Financial Institution credit reviews.
    * The model is used only for Financial Institutions where Internal Credit Ratings (ICRs) are not modeled, with mandatory human review; risk factor scoring and ICR determination remain fully performed by Credit Risk.
    * A high-severity finding related to unsupported statements was remediated through prompt enhancements and implementation of a critic control to detect and flag unsupported content for analyst review prior to approval.

I like this better because it clearly separates scope from validation outcome.

⸻

* Enhancements to the Tier 2 GBM Private agentic AI model (CSG AI Agent) used to synthesize information across documents and support question answering for the Capital Solutions Group (CSG), expanding its capability from single-deal research to multi-deal comparative analysis.
    * During validation, Model Risk identified an implementation defect causing incorrect document references; remediation reduced query failure rates from 12% to 0% while also reducing compute costs.

I removed the 16% compute reduction because I don’t think FRAC really cares unless it relates to model performance.

⸻

* A new Tier 2 GBM Public generative AI model (Equinox ETF) used to convert free-form chat messages into structured Requests for Quote (RFQs) and Requests for Trade (RFTs) for the U.S. Equities ETF business.

(Simple is sufficient here.)

⸻

* Enhancements to the Tier 2 Engineering generative AI model (M365 Copilot Web Grounding) incorporating Anthropic models with Bing Search to improve web-grounding capabilities.
    * Web grounding improves response accuracy and reduces hallucinations by incorporating relevant web content into model responses.

I think this wording is cleaner than “compared to GPT models.” We don’t need to compare models at FRAC.

⸻

* Enhancements to GBM Public neural network-based non-generative AI models, including approvals of:
    * Enhancements to the Tier 1 Buyback ML Pricer supporting multi-currency transactions through integration of foreign exchange (FX) notional modeling.
    * Enhancements to the Tier 2 TradeScore model supporting the LatAm Interest Rates algorithmic trading business by incorporating order-fill probability estimates into quoting decisions for Brazilian Real (BRL) swaps.
    * Two medium-severity findings related to regime change capture and ongoing monitoring were remediated prior to approval.

I think it is better to say enhancements to the TradeScore model than “extension to the probability estimation model.”

⸻

Collateralized Lending

I think I’d actually restructure this slightly. We discussed this a lot, and I think the three themes are now very clear.

* There is continued focus on development and validation work supporting the collateralized lending business, including approvals of:
    * Extension to the Tier 1 Facility-Level Rating (FLR) fallback model to cover secured lending exposures to Business Development Companies (BDCs), expanding coverage to exposures previously outside the FLR framework.
    * Extensions to asset-specific FLR and Tail Risk models to incorporate additional bespoke deal structures, including private equity facilities backed by equity positions with put options and loans backed by Bitcoin, supporting business growth while reducing reliance on fallback methodologies.
    * Enhancements to existing FLR and Tail Risk methodologies to improve risk measurement accuracy, including enhanced option-adjusted spread (OAS) calibration for Mortgage Servicing Right facilities and improved recovery rate estimation for residential mortgage and corporate credit portfolios.

⸻

Overall comments

I think this version is more consistent with previous FRAC updates because:

* Every main bullet starts with “A new…” or “Enhancements to…”.
* The sub-bullets explain:
    1. what the model does,
    2. what changed,
    3. important validation outcomes (especially high-severity findings).
* The tone is neutral and factual.
* Acronyms are defined the first time they appear.
* There is no marketing language (“well-designed”, “robust”, “significant”, “instrumental”, etc.).
* Individual bullets remain one sentence where practical.

I think this is very close to the style used in your previous FRAC submissions.






AI Risk and Controls Council Discussion Points

Meeting Date/Time: [Month DD, 2026] / 9:30 am ET
Meeting Type: Regular
Chairperson(s): Michael Schlee, Bill Keirstead
Secretary: Caroline Shulman
Attendance: Adequate representation from business and control side members was recorded.

[1] Controllers Data Reconciliation - Approval (Presenters: Rachel Rajkovich, Mike McKinlay, Alka Singh, Sumathi Gokulan)

Decision: AIRC approved the “Matching Agent” in Controllers Data Reconciliation for 8 pilot break sheets.

Pre-go-live Conditions: None

Other Follow-ups:

1. Confirm impact of rollout on Hong Kong. (Owner: Rachel Rajkovich; Control-side Contact: Alexis Vassilikas)
2. Update precision/recall numbers following completion of model validation. (Owner: Rachel Rajkovich; Control-side Contact: Bo Hu)
3. Return to AIRCC to discuss change management for skill files. (Owner: Alexis Vassilikas)

Key Discussion Points:

* AI component used for reasoning around exceptions not handled through deterministic checks (approximately 1% of cases, representing 150–200k breaks).
* Agent inherits the entitlements of the user. All data is contained within Harmony and accessed through an MCP server. Agents are specific to a given break sheet, with access constrained at the break sheet level to reflect reconciliation-specific logic.
* Agent recommendations are presented through a human-in-the-loop review process, with users responsible for accepting or rejecting recommendations before exceptions are finalized and published.
* Skills and prompts are managed in GitLab under the standard SDLC process.
* Post-go-live monitoring includes performance thresholds and operational kill switches to pause the agent if predefined quality or operational thresholds are breached.
* Approximately 400 Controllers break sheets are in scope for the Anthropic work, compared with approximately 2,000 break sheets across firmwide reconciliation processes, including GBM Operations.
* Scope of approval is limited to the 8 pilot break sheets. Expansion beyond this scope will require separate approval, potentially through the Streamlined Approval Process where the use case and risk profile remain unchanged.

[2] Administrative Items

* Posting on China AI Chatbot approval.
* Approval of meeting minutes from the May 26, 2026 meeting.



MRM approved Marquee Sales AI Chat (GBM Public, Tier 3), an agentic AI solution supporting the OneGS 3.0 Sales Enablement initiative by enabling sales teams to query client information across multiple internal systems through a natural-language interface.
* MRM independent testing demonstrated 96.4% grounding accuracy, while validation identified and remediated four findings related to hallucination controls and guardrails prior to approval.MRM approved enhancements to the Tier 1 Buyback ML Pricer supporting multi-currency transactions through integration of foreign exchange (FX) notional modeling.
* During validation, MRM identified and remediated a coding defect affecting FX direction and strengthened regression testing to improve detection of similar implementation issues.




AIRCC approved the Controllers Reconciliation Matching Agent, an agentic AI solution developed with Anthropic to automate manual transaction matching within the Harmony reconciliation platform.
* The initial rollout covers 8 pilot reconciliation breaksheets (of 280 in scope), with human review retained for all agent recommendations and phased expansion subject to performance thresholds, MRM validation, and penetration testing.



Absolutely. The email chain provides much stronger compensating controls than the first page because it documents review by senior Strats and explicit approval conditions. Here’s a polished waiver summary.

⸻

Transaction Waiver Summary

Desk

Equities – Structured Products Group (SPG)

Trade

Variable Strike Option

Waiver Scope

Bulk waiver with an aggregate notional limit of USD 250 million, with individual trades up to USD 100 million.

Underlier

ABGSCMD8 Risk Premia Basket

Maturity

1–3 years

Expected Economics

Approximately 1% per annum (index carry plus option volatility premium).

⸻

Trade Description

The transaction is a call option with a variable strike referencing the ABGSCMD8 risk premia basket.

On each rebalancing date, the strike is dynamically adjusted using a self-financing equation to preserve the option’s economic exposure as the underlying evolves. The implementation also incorporates transaction costs, observation date lag, and non-daily rebalancing frequency.

⸻

Reason for Waiver

The variable strike functionality has already been implemented and tested by Strats, but has not yet completed the formal MRM approval process. The desk intends to book the trade using the new implementation while the validation is finalized.

⸻

Proposed Booking During Waiver Period

The trade will be booked using the new implementation within the EqSp CMS Linked Note framework. The implementation supports all required product features and will be formally submitted to MRM during the following week.

⸻

Compensating Controls

The desk noted that the implementation has undergone review by senior Strats prior to booking, with approval granted subject to specific implementation checks.

In particular:

* The implementation has been reviewed with a focus on the self-financing equation, including the treatment of interest rates for excess return and total return assets.
* Transaction costs will be fixed for the initial trades, limiting uncertainty associated with transaction cost modelling during the waiver period.
* The desk will verify that all risk measures, including T+1 risk, are functioning correctly before and during production use.
* The remaining modelling limitation relates to the treatment of daily transaction cost accrual for excess return assets, which Strats assessed to have only a small pricing impact.
* The desk will continue evaluating incorporation of interest rate terms into the self-financing equation to improve consistency with standard option theta calculations as part of the formal model implementation.

⸻

Remediation Plan

* Submit the completed implementation to MRM for formal review and approval.
* Incorporate any required refinements identified during validation, including enhancements to the self-financing equation where appropriate.
* Complete MRM validation following submission of the implementation.

⸻

I think this compensating controls section is stronger because it is evidence-based. Rather than simply saying the implementation was tested, it documents that:

1. Senior Strats reviewed and conditionally approved the implementation.
2. They identified the specific residual modelling issue (transaction cost accrual), assessed it as immaterial.
3. They required verification of T+1 risk calculations before production.

Those are exactly the types of controls MRM committees typically look for in implementation waivers.


Absolutely. Here’s a polished Transaction Waiver Summary in the same format as the previous ones.

⸻

Transaction Waiver Summary

Desk

FICC – Hybrid Rates

Trade

Triple Rate Binary Option

Tradable

Eq Hybrid Binary

Counterparty

Hedge Fund

Notional

USD 5 million

Maturity

3 months

Underliers

* 2Y USD Swap Rate
* 2Y EUR Swap Rate
* 2Y GBP Swap Rate

Economics

Expected P&L: USD 250,000

⸻

Trade Description

The transaction is a 3-month triple rate binary option referencing three interest rates across different currencies.

The binary payoff depends on all three rates remaining within their respective predefined ranges:

* 2Y USD: 3.7% – 4.1%
* 2Y EUR: 2.6% – 2.95%
* 2Y GBP: 3.9% – 4.3%

The structure extends the existing dual-rate binary framework by incorporating a third rate while maintaining the same underlying pricing methodology.

⸻

Reason for Waiver

A validation was previously introduced in the Eq Hybrid Binary calculator preventing trades referencing more than two rates following approval of the dual-rate binary implementation.

The requested transaction references three rates, causing the booking validation to reject the trade despite analysis indicating that the calculator prices this specific cross-currency structure correctly.

⸻

Proposed Booking During Waiver Period

The trade will be booked using the existing Eq Hybrid Binary tradable, with the validation restricting trades to two rates relaxed for this specific transaction.

⸻

Compensating Controls

The desk noted that the pricing methodology implemented in the Eq Hybrid Binary calculator was benchmarked against the multivariate Gaussian copula model used in FICC’s generic formula-based calculator.

The benchmarking demonstrated:

* Close agreement between the Eq Hybrid Binary calculator and the independent CT Strip pricing model across a range of inter-rate correlation assumptions.
* Consistent pricing for both mid-market and offer valuations under the proposed payoff structure.
* Comparable results when reducing the structure to dual-rate binaries, providing additional validation against existing approved functionality.
* The booking representation of offer correlation through barrier shifts produces pricing broadly consistent with directly calibrated offer correlations.

These benchmarking results support that relaxing the booking validation does not introduce a material pricing inconsistency for this specific three-rate structure.

⸻

Remediation Plan

* Remove the booking validation restricting the calculator to two-rate structures where appropriate.
* Complete review and testing of the three-rate implementation.
* Submit the enhancement for formal MRM approval following completion of validation activities.

⸻

I think this one has a stronger compensating control than many of the previous waivers because it is supported by independent model benchmarking. Rather than simply stating the desk believes the model is correct, it demonstrates that:

1. the production calculator agrees closely with an independent Gaussian copula implementation,
2. results are stable across multiple correlation assumptions, and
3. the model reproduces existing approved dual-rate structures. These are exactly the kinds of arguments MRM reviewers typically find persuasive.




I would make this more like an executive update rather than walking through the table line by line. Bill will likely care about (1) regulatory context, (2) size of the work, (3) resourcing risk, and (4) where management decisions may be needed.

Here’s a polished version.

⸻

Introduction

Hi Bill. We wanted to give you a brief overview of the Basel III Finalization validation program, including the regulatory timelines, the overall validation inventory, expected resource demand, and our current project plan.

Regulatory timeline

Before getting into the validation plan, I’ll start with the regulatory landscape.

* For the FRB, the Basel III Endgame re-proposal was published in March 2026, but the final rule has not yet been issued, so the implementation timeline remains uncertain.
* For the PRA, the implementation timeline is well defined, which is why most current development and validation efforts are focused on the PRA deliverables.
* For FRTB IMA, although implementation is not expected until 2028, Strats intends to complete development this year and have the models validated ahead of the regulatory deadline.
* For the ECB, the Basic Approach applicable to Goldman Sachs has already been approved. The Internal Models Approach for Market Risk has been deferred until the end of 2029.

Validation overview

Moving to the validation plan.

Based on the information we’ve gathered so far, the program currently consists of 52 validation items across Standardized Credit Risk, FRTB-CVA and FRTB Market Risk. Based on our standard effort assumptions, this translates to approximately 4 annualized FTEs, or roughly 16 FTEs if concentrated into a single quarter.

The largest resource demand is expected to come from FRTB Market Risk, followed by FRTB-CVA, while the DRC work is primarily comprised of low- to moderate-effort validations.

The development timeline, particularly for the DRC workstream, should be viewed as preliminary because it may shift depending on the timing of the final FRB implementation rule.

Resourcing

Based on the current plan, we believe existing staffing is sufficient.

The peak resource demand is expected during Q4 2026, when multiple FRTB Market Risk validations are expected to run in parallel. Depending on how the development schedule evolves, we may require one to two additional validators during that period.

Validation synergies

One point worth highlighting is the significant validation synergies across jurisdictions.

Much of the FRTB Market Risk and FRTB-CVA work, particularly the risk factor models and core model infrastructure, is common across GS entities. Once the PRA validations are completed, we expect the subsequent FRB validations to require primarily incremental work, with approximately one-third of the original validation effort.

Inventory

The remainder of the presentation provides the detailed inventory.

For FRTB-CVA, we’ve already started receiving the initial model submissions, and the first wave of validations is expected to complete during Q3.

For FRTB Market Risk, validation is already underway for several workstreams. We expect most of the remaining validations to complete by year-end, with a limited number of lower-priority IMA items potentially extending into Q1 2027.

Closing

One challenge throughout this exercise has been that the work is spread across multiple jurisdictions, workstreams and regulatory priorities, making it difficult to maintain a consolidated view.

The objective of this inventory is to provide a single view of the overall program so that we can track progress, monitor resource demand, and identify any emerging capacity constraints as the program progresses.

⸻

I think this version sounds more like a VP/MD presentation. It emphasizes the management messages rather than narrating the spreadsheet, and naturally leads Bill toward the questions he’ll likely ask (timelines, resources, and risks).

Overall, your table is very good and captures the right structure. There are, however, a few factual updates and some opportunities to make it more useful for tracking the B3F program.

Accuracy review

Item	Assessment	Comment
FRB Basel III Re-Proposal	✅ Mostly correct	March 2025 is the current re-proposal. Final rule and implementation remain TBD.
PRA Final Rules	⚠️ Slight wording	Better to call it Basel 3.1 Final Rules (PS1/26) rather than just “Final Rules”. Published 20 Jan 2026.  
ECB CRR3	✅ Correct	CRR3 published June 2024.
ECB BA-CVA/SA-CVA go-live Jan 2025	✅ Correct	CVA reforms became effective with CRR3 in Jan 2025.
ECB FRTB-SA/IMA Jan 2027	⚠️ Needs update	The EU has since proposed delaying the market risk framework again beyond Jan 2027 while awaiting international alignment. If your tracker reflects the current regulatory position, note that implementation is under further delay review.  
PRA FRTB IMA Jan 2028	✅ Correct	Confirmed in PS1/26.  

⸻

I would make the table look like this

Regulator	Framework	Component	Rule Publication	Current Go-live	Validation Impact
FRB	Basel III Endgame Re-proposal	Standardized / SA	Mar 2025	TBD	High
		FRTB-SA	Mar 2025	TBD	High
		FRTB-IMA	Mar 2025	TBD	High
		BA-CVA / SA-CVA	Mar 2025	TBD	High
PRA	Basel 3.1 Final Rules (PS1/26)	FRTB-SA	Jan 2026	Jan 2027	Medium
		BA-CVA / SA-CVA	Jan 2026	Jan 2027	Medium
		FRTB-IMA	Jan 2026	Jan 2028	High
ECB	CRR3	BA-CVA / SA-CVA / AA-CVA	Jun 2024	Jan 2025	Complete
		FRTB-SA	Jun 2024	Delayed (currently under review)	Medium
		FRTB-IMA	Jun 2024	Delayed (currently under review)	High

⸻

I would also add two additional columns

These would make the table much more useful for your B3F planning.

Regulator	Component	Published	Go-live	MRM Validation Start	Status
FRB	FRTB-SA	Mar-25	TBD	Q3 2026	Planning
FRB	FRTB-IMA	Mar-25	TBD	Q3/Q4 2026	Planning
PRA	FRTB-SA	Jan-26	Jan-27	Q3 2026	In Progress
PRA	FRTB-IMA	Jan-26	Jan-28	Q4 2026	Planning
ECB	BA-CVA	Jun-24	Jan-25	Complete	Live

This aligns much better with the inventory tracker you built.

⸻

One terminology suggestion

Instead of Current go-live/application date, I’d use

Effective Date

or

Current Regulatory Effective Date

It is more standard regulatory language and accommodates situations where the implementation date changes.

Overall, I’d rate the current table 8.5/10. With the updated EU status, clearer framework names, and two planning columns (“MRM Validation Start” and “Status”), it becomes a much stronger executive tracking tool.



MRM approved one new Facility-Level Rating (FLR) model and an extension to the FLR fallback model to support GS Select and secured lending to Business Development Companies (BDC), expanding production model coverage.
* Continued enhancements to existing FLR and Tail Risk models, including:
    * 11 model enhancements to improve the accuracy and risk sensitivity of existing FLR and Tail Risk methodologies.
    * 10 model extensions to incorporate additional bespoke deal types, supporting continued business growth while reducing reliance on fallback methodologies.



Continued significant volume of bespoke lending transactions requiring new FLR and Tail Risk model coverage to support appropriate post-trade risk measurement. (YTD: approximately $XXbn of new bespoke transactions.)
* YTD, MRM approved one new model and 22 FLR and Tail Risk model extensions to incorporate new bespoke deal structures and reduce reliance on fallback methodologies.
* MRM also approved enhancements to existing FLR and Tail Risk models to improve risk measurement accuracy, including more appropriate treatment of investment-grade versus high-yield exposures and other bespoke lending features.



SIMM Interest Rate Delta Methodology

* MRM approved the revised Interest Rate Delta backbone methodology for the NYC Volex portfolio used in SIMM calculations, addressing a longstanding model finding that contributed to overstated Initial Margin and persistent counterparty disputes.
* Following implementation, Portfolio Reconciliation and Valuations observed a $146mm reduction in disputes, with the enhancement expected to support closure of a longstanding dispute with Nomura and an associated NFA/SEC filing.



Here are my suggested revisions.

⸻

1. PRA IRB Approach Uplift (address Caroline’s comments)

I agree with the comment. It’s better to group by Corporate and Super Large Corporate rather than alternating between ICR and PD.

PRA Internal Ratings-Based (IRB) Approach Uplift: Validation on track for

* Corporate models (target completion: Jul 31):
    * Corporate Industry Segment ICR validation is progressing, with medium-severity findings on methodology, assumptions, implementation and monitoring communicated to developers.
    * PRA Corporate Industry IRB model validation is focused on the Margin of Conservatism (MoC) framework and legacy rating calibration.
* Super Large Corporate models (target completion: Aug 28):
    * Super Large Corporate ICR validation identified two high-severity implementation findings, with remediation underway.
    * PRA Super Large Corporate Industry IRB validation commenced following receipt of the initial submission.
* Rule compliance (~800 rules; target completion: Sep 4):
    * Review of all 119 PD Master Scale rules has been completed, with Risk Strats targeting remediation by Jul 17; review of Corporate IRB rules is underway.

This is much easier to follow and gives Bill natural talking points.

⸻

2. Collateralized Lending (CRO)

I’d simplify it substantially. The Board doesn’t need all the individual counts.

Option 1 (my preference)

Collateralized Lending: Continued expansion of quantitative model coverage supporting the Collateralized Lending business, reducing reliance on fallback methodologies and improving risk measurement.

* YTD, MRM approved one new model and 22 model enhancements across Facility-Level Rating (FLR) and Tail Risk models, expanding coverage for GS Select, Business Development Company lending and more complex lending structures.
* Enhancements also incorporated additional hedging capabilities and improved risk measurement across ASL, PECC and Direct CRE portfolios.

⸻

Or, if Bill wants the numbers more prominently:

Collateralized Lending: Continued expansion of quantitative model coverage supporting the Collateralized Lending business.

* YTD, MRM approved one new model and 22 FLR and Tail Risk model enhancements, expanding coverage while reducing reliance on fallback methodologies.
* Key enhancements include support for GS Select and Business Development Company lending, more complex deal structures, and improved hedge recognition across lending portfolios.

I think the second version is cleaner.

⸻

3. CRO Top Focus Area (Mortgage)

I agree—“phased enhancements” is now outdated since Strats submitted the full package together.

I’d revise to:

* High-severity finding on the Mortgage Pass-Through Pools Pricing model identified incorrect treatment of pool price floors under stressed scenarios; remediation increased risk limit utilization, with temporary departmental limit increases implemented.
* The finding has prompted broader enhancements to the mortgage risk framework, including comprehensive updates to mortgage prepayment and rate models, recalibration to recent market conditions, and ongoing MRM validation to improve alignment between desk pricing and independent Risk measurements.

Or, if you want it a bit shorter:

* The finding has prompted broader enhancements to the mortgage risk framework, including updates to mortgage prepayment and rate models and recalibration to recent market conditions, with MRM validation underway to improve alignment between desk and Risk measurements.

I actually prefer the second version because it reflects the latest status (single comprehensive submission) and explains what the enhancement package contains, rather than referring to a phased rollout that no longer exists.



I agree. For the CRO deck, I’d add just enough context so Bill can speak to each topic without making the bullets too technical.

⸻

Mortgage Agency Pricing Model Uplift

* GBM Strats submitted a comprehensive enhancement package for the Mortgage Agency Pricing Model to address longstanding differences between desk pricing and independent Risk measurements.
    * The submission includes enhancements to the mortgage prepayment and mortgage rate models, together with recalibration to recent market conditions.
    * MRM validation is underway, with completion targeted by end-July.

⸻

GBM Trading Net Interest Income (NII) Modeling

* Validation remains on track for completion by 7 August, with potential high-severity findings communicated to GBM.
    * Key concerns relate to insufficient support for model assumptions, including macroeconomic drivers, management judgment-based parameters, and implementation issues.
    * Risk, Controllers, GBM and Treasury continue to reconcile CCAR and EaR results, with particular focus on Repo funding expenses under the revised models.

⸻

India Model Risk Management Guidance

* The Reserve Bank of India issued draft Model Risk Management guidance for India legal entities; MRM’s initial assessment indicates broad alignment with the firm’s existing framework.
    * The proposal places greater emphasis on Board oversight, broader model inventory requirements, and periodic validation of all models, including vendor models.
    * MRM will continue assessing the guidance and any implications for the firm’s India model risk governance framework.

⸻

CCR – Enhanced Equity Relative Value (RV+)

* MRM continues review of the proposed Equity Relative Value (RV+) enhancements, which would reduce stress charges for eligible well-diversified equity portfolios subject to defined risk guardrails.
    * In response to MRM feedback, Strats submitted an updated methodology incorporating Axioma factor risk analytics and residual factor risks into the portfolio eligibility assessment.
    * MRM is assessing whether the revised framework appropriately captures residual portfolio risks while preserving the intended capital benefits.

⸻

CCR – Coherent Shortfall Model

* MRM approved enhancements to the Coherent Shortfall model (Risk, Tier 1), which estimates potential counterparty credit risk shortfalls under stressed market conditions.
    * Key enhancements improve hedge recognition, liquidation methodologies, and portfolio scope and netting treatment.
    * The changes remediate three medium-severity findings, improving model stability and risk sensitivity while reducing reliance on overly conservative methodologies.

⸻

SIMM v2.8+2512 Recalibration

* ISDA will implement SIMM v2.8+2512 on 11 July following its semi-annual model recalibration, with an estimated ~1% reduction in overall Initial Margin.
    * Interest Rate risk weights have been frozen after industry concerns that the standard recalibration could materially reduce margin requirements and increase backtesting breaches.
    * ISDA is evaluating methodology enhancements to the Interest Rate calibration framework, with updated parameters targeted for the December 2026 production release.

⸻

Cross Currency Risk Migration

* MRM validated a strategic migration of interest rate and cross-currency risk calibration across 41 EMEA and Asia currencies to establish a globally consistent risk framework.
    * The changes standardize cross-currency risk representation across regions, replacing inconsistent local market conventions.
    * Validation also identified implementation issues and remaining enhancements, with findings raised to support completion of the migration.

I think these are about the right level for a CRO audience: concise enough to fit on the slide, but with enough context that Bill can explain the business significance without referring back to detailed notes.



Recipient Name

Mortgage Underwriting Department

Company Name

TD Bank, N.A.

Address

6000 Atrium Way

City, State, ZIP

Mt. Laurel, NJ 08054


[E] Mortgage Agency Pricing Model Uplift
GBM Strats submitted a comprehensive enhancement package for the Agency Fundamental Model, replacing the previously planned phased rollout.
The submission includes enhancements to the mortgage prepayment and rate models, together with recalibration to recent market conditions, addressing longstanding divergence between desk pricing and independent Risk measurements.
MRM validation is underway, targeting completion by end-July. [Optional: Temporary risk limit increases expire on 17 July; discussions are ongoing regarding interim arrangements while validation is completed.]
[F] CCAR – NIM Modeling Changes
Validation remains on track for completion by 7 August, with potential high-severity findings communicated to GBM.
Key concerns relate to model assumptions with insufficient support, including macroeconomic factor dependencies, management judgment-based parameters, and implementation issues.
Risk, Controllers, GBM and Treasury continue to reconcile CCAR and EaR results, with current focus on the large negative Repo expenses generated under the revised modeling framework.



SIMM v2.8+2512 Recalibration

* ISDA SIMM v2.8+2512 will be implemented in production on 11 July 2026, reflecting the annual recalibration using historical data through 31 December 2025.
* Overall SIMM Initial Margin is expected to decrease by approximately 1%, driven by lower Equity and Commodity requirements, partially offset by increases in Credit and FX.
* Interest Rate (IR) risk weights have been frozen at the v2.8+2506 calibration following industry concerns that the standard recalibration would materially reduce IR Initial Margin and increase backtesting breaches.
* ISDA is evaluating methodology enhancements to the IR calibration framework, including improvements to the representative rate index used for calibration, with investigations expected to conclude by 31 July 2026.
* The revised methodology is expected to be included in SIMM v2.9+2512 for regulatory review in August 2026, with updated IR parameters targeted for production in the December 2026 (v2.9+2606) release.




Enhanced Equity RV (RV+)

* MRM continues review of the proposed Equity Relative Value (RV+) enhancements, which would reduce stress charges for eligible well-diversified equity portfolios subject to risk guardrails.
* In response to MRM feedback, Strats submitted an updated methodology incorporating Axioma and residual factor risks into the portfolio eligibility assessment.
* MRM is assessing whether the revised framework appropriately captures residual portfolio risks while maintaining the intended risk sensitivity.



SIMM Interest Rate Risk Weight Calibration

* Industry implementation of recalibrated SIMM interest rate risk weights has been deferred following concerns that lower risk weights would materially reduce initial margin and increase backtesting breaches.
* ISDA is evaluating methodology enhancements, including improvements to the representative interest rate index used for calibration, before proceeding with recalibration.





Validation in progress for:
    * Super Large Corporate ICR, with two high-severity findings identified on model implementation and a medium-severity finding relating to support for the $3bn Net Sales segmentation threshold.
    * Corporate Industry Segment ICR, with six medium-severity findings communicated to developers, focused on Margin of Conservatism methodology, legacy rating calibration, and remediation of prior findings.
* Validation commenced for the Super Large Corporate Industry IRB model following receipt of the initial submission.
* Rule compliance: Second-line review of the PD Master Scale rules has been completed, while review of [XXX] PRA IRB regulatory rules continues with Capital Risk and EY, including the initial assessment of the Super Large Corporate Industry IRB rules.




MRM raised a medium-severity thematic finding relating to model inventory completeness within Prime Services Inventory Management.
* The review identified models omitted from the model inventory, including projection models supporting PCE buffer and GCLA sizing.
* Remediation is underway to address remaining inventory gaps and strengthen first-line inventory governance and oversight.



High-severity finding on the Mortgage Pass Through Pool Pricing model identified incorrect treatment of pool price floors under stressed scenarios; remediation increased risk limit utilization, with temporary departmental limit increases implemented.
* The finding has driven a broader program to enhance the mortgage risk framework, addressing longstanding divergence between desk risk views and independent Risk measurements during periods of market stress through a phased model enhancement and validation program.



MRM’s assessment is based on internal discussions within MRM, as well as discussions with first-line model developers and other relevant stakeholders, as appropriate. As part of the NAC review process, MRM reviews NAC memoranda for which an MRM assessment is required to identify any new models or model changes associated with the proposed activity. MRM signs off in the Firmwide New and Expanded Business Activities (NEBA) system on the basis that all required models and model changes have been approved by MRM in accordance with the Firmwide Policy on Model Control prior to production use. Where required model approvals have not yet been obtained, MRM’s sign-off is contingent upon an approved model waiver in accordance with the Firmwide Policy on Model Control.



MRM’s assessment is based on internal discussions within MRM, as well as discussions with first-line model developers and other relevant stakeholders, as appropriate. As part of the NAC review process, MRM reviews NAC memoranda to identify any new models or model changes associated with the proposed activity and confirms that all required models and model changes have received MRM approval in accordance with the Firmwide Policy on Model Control prior to production use. MRM then provides its approval in the Firmwide New and Expanded Business Activities (NEBA) system. Where required model approvals have not yet been obtained, MRM’s approval is contingent upon an approved model waiver in accordance with the Firmwide Policy on Model Control.


Below is how I would update it based on Bill’s comments. I’ve inserted [placeholders] where owners need to provide updates and added comments in [ ] to indicate what Bill was looking for.

⸻

Top of Mind

2024 FRB MRM Exam

* The FRB closed the Matter Requiring Attention (MRA) on Weaknesses in the Model Validation Controls Framework.
* Remediation included enhancements to the Annual Review framework, with 742 required reviews completed before 2025 year-end.
* Ongoing monitoring for the credit card loss forecasting model was also enhanced, addressing incremental CCAR feedback.

PRA Internal Ratings-Based (IRB) Approach Uplift

TBU

* [Update latest PD Master Scale status and rule review.]
* [Include total number of PRA rules under review (XXX) with Capital Risk and EY support, not just the 119 PD Master Scale rules.]

Mortgage Pass Through Pool Pricing Model

TBU

* [Latest submission / validation status.]

GM Trading Net Interest Income (NII) Model

TBU

* [Latest validation progress and key focus areas.]

[NEW] GSS Finding (if raised before Thursday)

* [Summarize new GSS finding and current remediation discussions.]

⸻

Validation Activities

CCR

* MRM approved enhancements to the Coherent Shortfall (COSF) model (Risk, Tier 1), which estimates potential counterparty credit risk shortfalls under stressed market conditions.
* Key enhancements include improved hedge recognition, more stable liquidation methodologies, and updated portfolio scope and netting treatment.
* The changes remediate three medium-severity findings and improve model stability, risk sensitivity, and consistency.

⸻

ASL

* Continued progress supporting the ASL business through expansion of quantitative model coverage, reducing reliance on fallback methodologies, and addressing longstanding MRM findings.
* MRM approved extension of the Facility Loss Rate (FLR) fallback model (Risk, Tier 1) to Business Development Company (BDC) lending, expanding quantitative model coverage.
* Validation is underway for Tail Risk model enhancements, transitioning from single-path to simulation-based methodologies.
* [Add broader context requested by Bill — e.g., YTD approvals, reduction in fallback reliance, number of asset classes covered, or other metric showing structural progress rather than isolated approvals.]

⸻

[NEW] Significant Tier 1 Revalidations (Bill requested to bring back)

* [Provide mid-year status of the Significant Tier 1 revalidation program (XX completed of XX, XX% complete, on track for two-year cycle).]
* [Summarize overall outcome (e.g., no high-severity findings; key themes from findings).]

⸻

[NEW] Cross Currency Migration (if update available)

* [Summarize validation progress supporting migration to a consistent cross-currency risk framework.]

⸻

[Optional] IPO Post-Implementation Review (if enough content)

* [Provide post-event assessment of model performance across liquidity, pricing, capital and market risk models supporting the IPO.]
* [Include any lessons learned or confirmation that no material model issues were identified.]

⸻

Additional items Bill asked us to explore (not yet drafted)

* RV+ — Obtain latest validation status and determine whether there is a meaningful update.
* SIM rollout delay — Check with Andreas whether timing and expected Initial Margin benefit are sufficiently concrete for CRO.
* GBM inventory / findings trends — Consider adding a Q2 reflection (inventory growth, AI models, findings opened vs. closed).
* LMM / One-Day SOFR — David to provide summary for potential inclusion.
* ICAP exam — Reassess after this week’s regulator meetings.
* AI documentation tool rollout — Better suited for Strats update, but prepare rollout timeline and messaging.

⸻

I think this is now very close to Bill’s intent. The biggest addition from the discussion is that ASL and Significant Tier 1 should become program-level progress updates rather than simply individual model approvals. Those were the two themes he emphasized most.



Here are the action items I heard from Bill, grouped by priority. I’ve included suggested wording and placeholders where information needs to be gathered.

⸻

Top of Mind

1. MRA Closure

Action: Keep at the top.

⸻

2. IRB

Action: Update latest status (you’ve already done this).

⸻

3. Mortgage Pricing Model

Action: Update latest submission / validation status.

⸻

4. NIM

Action: Update latest validation status.

⸻

5. GSS Finding (NEW)

Bill suggested moving this to Top of Mind if the finding is raised.

Placeholder

GSS: MRM raised a [Severity X] finding relating to [placeholder]. Remediation discussions are underway with Engineering.

Owner: Jamie / GSS team

⸻

Validation Activities

6. ASL

Bill wants much broader context.

Current wording is too transactional.

Suggested intro:

Continued progress supporting the ASL business through expansion of quantitative model coverage and reduction of reliance on fallback methodologies for new business.

Possible additional stat (placeholder)

• Since [date], MRM has approved XX ASL model enhancements / expanded model coverage across XX asset classes.

Need from David/Muyan:

* how much fallback reduced?
* approvals YTD?
* % of new trades now covered?

Bill specifically wants to tell the story:

“We’re making structural progress rather than approving isolated model changes.”

⸻

7. Significant Tier 1 Revalidation

Bill explicitly asked to bring it back.

Suggested summary

Significant Tier 1 Revalidations remain on track, with approximately XX% of the two-year cycle completed and no high-severity findings identified to date.

Maybe

* XX completed
* XX remaining
* 0 High severity

⸻

8. Cross Currency Migration (NEW)

Bill specifically asked whether we have something.

Placeholder

MRM continues validation supporting migration of cross-currency risk models onto a consistent firmwide framework across currencies.

Owner:
Canal / Andreas

⸻

9. IPO Reflection (NEW)

Not another pre-IPO update.

Bill wants a retrospective.

Suggested placeholder

Completed post-implementation review of model support for the recent IPO, covering liquidity, capital, market risk and pricing models. No material model issues observed.

Need:

* lessons learned
* model performance
* anything unexpected

⸻

10. SIM Delay (NEW)

Bill specifically mentioned.

Placeholder

Review ongoing of delayed rollout of SIM enhancements for IR products. Delay expected to defer reductions in Initial Margin requirements pending backtesting window completion.

Owner:
Andreas

⸻

11. RV+

Bill specifically asked.

Need latest validation update.

Placeholder

Validation continues on proposed RV+ enhancements, with ongoing discussions on portfolio guardrails and treatment of factor-based strategies.

⸻

Strats Updates

12. GBM Inventory

Bill asked:

show inventory at Q2

Need simple slide or bullet

Possible:

* total GBM models
* by FICC / Equities
* YTD change
* AI models

⸻

13. GBM Findings Trend

Bill also suggested

Could add

Findings opened vs closed YTD

or

Inventory + findings together

⸻

14. LMM / One-Day SOFR

David requested.

Need summary.

Placeholder

Completed review of LMM methodology identifying issues in one-day SOFR modelling; findings communicated to developers with remediation underway.

Owner:
David

⸻

AI

15. Ryan Horwood

Bill wants reminder only.

No slide change.

Add speaker note.

⸻

16. Prism

Bill wants update from Alex.

Specifically

* God mode
* follow-ups

Need answer from Alex.

⸻

17. AI Model Documentation Tool (NEW)

Bill definitely wants this.

Suggested wording

AIRCC approved broader rollout of MRM’s AI-assisted model documentation tool following successful pilot. Rollout planning underway to support wider adoption across model developers.

Need

* rollout timing
* scope
* partners informed?

⸻

18. AI Coding Observations

Bill asked if worth mentioning.

Possible talking point only:

Developers increasingly using AI-assisted coding and documentation. Early observations indicate improved documentation quality, although additional review remains necessary for AI-generated content.

Not sure this goes in slides.

⸻

Regulatory

Nothing additional.

⸻

Miscellaneous

No ICAP update yet.

Wait until meetings conclude.

⸻

Assignments

Topic	Owner
ASL broader context / fallback reduction statistics	Muyan / David
Significant Tier 1 progress statistics	You
Cross Currency migration	Canal / Andreas
IPO post-event review	Equity / Liquidity teams
SIM rollout delay	Andreas
RV+ latest status	CCR team
GBM inventory & findings trends	You
LMM / One-day SOFR	David
GSS finding	Jamie
AI documentation rollout	Engineering / AIRCC
Prism follow-up (God Mode)	Alex

Overall, I counted about 10–12 new items, but the ones Bill clearly emphasized as highest priority are:

1. ASL broader story.
2. Significant Tier 1 progress.
3. GSS finding.
4. IPO retrospective.
5. AI documentation tool rollout.
6. GBM inventory/findings reflection at Q2.




MRM approved enhancements to the Coherent Shortfall (COSF) Model (GBM Public, Tier 1), which estimates potential counterparty credit risk shortfalls under stressed market conditions.
Key enhancements include improved recognition of hedged equity exposures, more stable liquidation methodologies for interest rate volatility and bond futures, and refinement of portfolio scope and netting treatment.
The changes remediate three medium-severity findings, improve model stability and risk sensitivity, and reduce reliance on overly conservative methodologies.

ASL
Continued focus on development and validation work supporting the ASL business, expanding model coverage to reduce reliance on fallback methodologies and addressing MRM findings.
MRM approved extension of Fallback Loss Rate (FLR) model coverage to Business Development Company (BDC) lending, expanding quantitative model coverage.
Validation commenced for enhancements to Tail Risk models, transitioning from single-path to simulation-based methodologies.


MRM approved extension of the Fallback Loss Rate (FLR) model to Business Development Company (BDC) lending, expanding model coverage and reducing reliance on fallback methodologies.
* Validation is underway for enhancements to tail risk models, including migration from single-path to simulation-based methodologies to address existing MRM findings.




Validation continues across the PE Fund, ASL, and Sovereign ICR models.
    * PE Fund ICR: Sev1 finding on missing data treatment; remediation being finalized.
    * ASL and Sovereign ICR: Review of remediation and finalized Sev2 findings related to calibration methodology, data quality, and model assumptions.




Identified a medium-severity finding during the Significant Tier 1 revalidation of the Equity Convertible Bond model, with remediation underway to standardize the funding spread methodology across regions


Approved the Probability of Default (PD) Master Scale model, the first model supporting the PRA Internal Ratings-Based (IRB) uplift for the firm’s corporate credit rating framework




FRB closed the 2024 Model Risk Management Matter Requiring Attention (MRA) related to the model validation controls framework
* Completed entity-specific validation of 50 models supporting UK ICAAP 2026 and approved the Probability of Default (PD) Master Scale model for the PRA Internal Ratings-Based (IRB) uplift
* Approved the revised IR Delta backbone methodology for the NYC Volex portfolio, reducing overstated initial margin and contributing to a $146mm reduction in counterparty disputes



AIRCC approved the Funds Oversight Agentic AI use case, co-developed with Anthropic, which assists XIG Fund Controllers in investigating investment holding reconciliation breaks.


MRM approved Anthropic models with Bing Search for the M365 Copilot Web Grounding model (Engineering, Tier 2), improving overall web grounding capabilities.
    * Anthropic + Bing performs better on legal, regulatory, and political queries, while Gemini + Google performs better on macroeconomic and financial questions.



For Bill’s talking points, I’d make them much punchier:

AI – Validation Highlights

* MRM rejected IB Summaries (GBM Public, Tier 3), a Marquee model that summarizes client sales and trading conversations.
    * MRM found only 40% of summaries were accurate, with errors in trade direction, deal status, and trade terms.
    * Following MRM feedback, accuracy improved to ~80%; developers are targeting 90% before resubmission.
* MRM approved Anthropic models with Bing Search for M365 Copilot Web Grounding (Engineering, Tier 2).
    * Anthropic + Bing performs comparably to Gemini + Google overall, with stronger performance on legal and regulatory queries, while Gemini + Google performs better on macroeconomic and financial topics.

This version is shorter, emphasizes the key messages, and is easier for Bill to speak to.



Upcoming regulatory meetings include:

Headcount & Attrition (YTD)

* Overall headcount remains within established guardrails, with year-to-date attrition of 18 employees across MRM and ETSC (14 MRM; 4 ETSC).
* Internal mobility to GBM remains the primary driver of ETSC attrition, accounting for 3 of 4 departures (75%) year-to-date.
* ETSC attrition has been concentrated in Bengaluru, where three employees (two Vice Presidents and one Associate) transitioned to GBM engineering and Strats roles during Q2.
* Across MRM, two Vice Presidents also transferred to GBM Desk Strats, reflecting continued demand for experienced model risk and quantitative talent.





* FCA (Jul 16): AI supervisory meeting covering AI adoption, governance, risk appetite, human oversight, controls, incidents, and Board oversight.
    * SEC / FINRA (TBD): One Goldman Sachs 3.0 update covering AI-enabled sales, lending and risk workflows, vendor governance, regulatory reporting, and Payments Settlements AI.
    * Federal Reserve (Jul 24): Q3 Head of AI meeting covering strategic AI execution, agentic AI deployment, governance framework, standardized controls, AI metrics, and organizational updates.



MRM approved Cookie Doc AI (Platform Solutions, Tier 2), which classifies unattributed Apple Card customer documents to automate routing and prioritization within Consumer Card Operations.
* MRM analysis indicated 89% classification accuracy, exceeding the 60% business requirement, with all model outputs subject to operations staff review and override.    MRM rejected IB Summaries (GBM Public, Tier 3), a model that summarizes sales and trading client conversations and identifies trading themes and opportunities.
* MRM found the model produced accurate summaries in only ~40% of cases, with errors affecting key trade details and outcomes.
* Following MRM feedback, model performance improved to ~70%; developers are targeting >80% accuracy before resubmission for approval.

    MRM found only ~40% of summaries were accurate, with errors including incorrect trade direction, deal status, and trade terms.
* Following MRM feedback, model performance improved to ~70%; developers are targeting >80% accuracy before resubmission for approval.


The agent is triggered only after deterministic checks identify a mismatch, with all recommendations subject to controller review before final action.





Based on the minutes, I’d make them a bit more reflective of what AIRCC actually approved and what the key controls were.

Zoom AI

* AIRCC supported expansion of Zoom AI meeting summaries to internal project, product, and transformation teams to improve the efficiency and consistency of meeting documentation.
* The expansion remains subject to human review of all AI-generated summaries, with follow-up work focused on delivery workflows (portal vs. email) and user access prior to ARC review.

Fund Oversight AI

* AIRCC approved the Funds Oversight Agentic AI use case, which assists XIG Fund Controllers in investigating investment holding reconciliation breaks by analyzing supporting documents and recommending whether administrator data should be accepted or rejected.
* The agent is invoked only after existing deterministic checks identify a mismatch, with all recommendations subject to controller review and final approval prior to go-live following completion of MRM validation and penetration testing.

I think these are stronger than the previous versions because they:

* clearly describe what the AI actually does,
* highlight the existing deterministic controls (a key discussion point),
* and emphasize the human-in-the-loop and pre-go-live conditions, which were the main AIRCC focus.


A 



Yes. Bill made a point that I think is worth capturing because it reflects a governance consideration rather than a technical one.

His point was essentially:

* Today: If the agent is disabled, controllers simply revert to the existing manual process because no headcount reduction is assumed.
* In one or two years: As confidence in the agent grows, the business may rely on it more and potentially reduce incremental hiring or capacity. At that point, if the agent fails, the business may not be able to immediately revert to the same level of manual processing. That becomes a firm risk appetite question rather than a technology question.

I would capture it like this:

Council members discussed contingency planning should the agent need to be disabled. The presenters explained that, for the initial rollout, controllers would revert to the existing manual review process, as the implementation does not assume any reduction in controller oversight or staffing. The chairperson noted that this contingency becomes a more important governance consideration over the longer term, observing that in one to two years the business may become more reliant on agentic capabilities as business volumes grow and hiring is reduced. The chairperson noted that determining the level of operational resilience and manual fallback capacity in such a scenario will ultimately be a firm risk appetite decision rather than a technology decision.

This captures Bill’s point accurately without overexplaining it. It’s also the kind of governance observation that is useful to preserve in meeting minutes.control-side reviewer confirmed that no noteworthy Technology Risk findings had been identified to date and noted that penetration testing remains in progress. The presenters confirmed that both Technology Risk activities and MRM validation must be completed before go-live, and that any material findings identified through these processes would be remediated prior to implementation.




Yes. Reading the discussion carefully, they did converge on the portal option. The remaining open question was not portal vs. email, but rather who should receive access under the portal workflow (host only vs. host/co-host vs. broader participants).

The sequence was:

1. Caroline expressed a preference for the portal because it avoids email retention/sampling issues.
2. Sarah raised a practical concern that the meeting organizer is often not the person who drafts the minutes.
3. Tamila and Mirona responded that the human-in-the-loop review is a required control and that training will reinforce this.
4. Bill and Daniel both voiced support for moving forward.
5. They discussed whether the portal output could be shared with co-hosts or others.
6. Bill summarized that the use case itself was supported, and the remaining operational detail was how the portal workflow should work.
7. Lauren clarified the intent, and Caroline agreed.
8. They concluded the concept was approved for ARC, with the host/co-host workflow to be finalized.

So I’d rewrite that section as:

Council members discussed the human-in-the-loop requirement and the practical workflow where the meeting organizer may not be the individual responsible for preparing meeting minutes. A council member noted that, in practice, a senior meeting organizer may delegate preparation of meeting minutes to a junior team member and questioned whether the portal workflow would align with existing business practice. The presenters emphasized that meaningful human review remains a required control regardless of the delivery mechanism and that users will receive training on their responsibility to review AI-generated summaries before they are incorporated into firm records or distributed. Council members agreed that the portal-based workflow is the preferred approach because it better addresses legal hold, retention, and email sampling considerations. Members discussed whether summaries should be made available only to meeting hosts or also to co-hosts or other designated participants to better support existing workflows, and agreed to finalize those operational details as a follow-up.

I would also update the Decision section accordingly. Instead of:

…subject to further review of the operational workflow…

I would say:

Decision: The council supported the proposed expansion of Zoom AI for the defined project, product, program management, and transformation population. The council supported implementation using the portal-based workflow, with follow-up to finalize recipient access (e.g., host and co-host) before escalation to ARC.

That is more faithful to what was actually agreed in the meeting.


Council members discussed the human-in-the-loop requirement and the practical workflow for meeting summaries. A council member noted that, in practice, the meeting organizer is often a senior individual who delegates preparation of meeting minutes to a junior team member. Under the proposed portal workflow, the meeting organizer would receive the AI-generated summary and would be expected to review it before taking further action. The council member questioned whether this reflects actual business practice and noted that users may simply forward the summary to the individual responsible for preparing the minutes without conducting the intended review.

The presenters emphasized that the human-in-the-loop review is a key control regardless of the delivery mechanism and that users will receive training on their responsibility to review AI-generated content before it is incorporated into firm records or distributed. The presenters noted that this control cannot be fully enforced through technology and therefore relies on user training, policy, and governance. Council members acknowledged the practical workflow considerations while agreeing that the proposed control framework should continue to require meaningful human review before AI-generated summaries are relied upon or shared.




Council members discussed the tradeoffs between the Zoom portal and email-based delivery approaches. A council member asked whether the strategic firmwide solution is expected to move away from email. The presenters explained that the strategic solution is intended to integrate meeting summaries into the relevant user workflow, such as CRM for client-facing users, and potentially other workflow tools for non-client-facing users, rather than relying on email distribution. The presenters noted that the portal approach is directionally closer to the strategic solution because the meeting organizer would receive a link, review the summary in the Zoom portal, and then take an action on the output.

A council member asked why the proposed project and product management population should not start with the portal approach, given that it mitigates email sampling, retention, and legal hold concerns. The presenters explained that these users currently work heavily through email, Jira, and Confluence, and that email-based summaries may be more immediately useful because they fit existing workflows and support discoverability by tools such as Copilot. The presenters noted that, under either approach, a human-in-the-loop step is required before the summary is used or distributed.

Council members discussed that the portal approach better mitigates certain control risks because unreviewed Zoom-generated summaries would not automatically enter the email ecosystem. However, members also noted that the portal approach may introduce practical workflow challenges, particularly where the meeting organizer is not the person responsible for preparing or finalizing meeting notes. The presenters and council members agreed that the key question is not whether the use case should proceed, but which interim workflow best balances user adoption, discoverability, human review, and legal, retention, and surveillance considerations before the strategic solution is available.




Draft below in the old AIRCC minutes style, with “committee” changed to council.

1. Materials: AIRCC Materials dated June 30, 2026

2. Zoom AI Expansion – Approval

The presenters requested approval to expand Zoom AI meeting summary functionality to a limited population of project, product, program management, and transformation personnel. The presenters explained that the proposed population is limited to individuals whose full-time roles are in project or product management functions or whose HCM job description includes product or project management. The presenters noted that these users regularly prepare meeting minutes, document business requirements, and maintain records in tools such as Jira, Confluence, and email.

The presenters explained that the proposed expansion would be limited to internal meetings and would exclude sensitive topics, including regulatory remediation, EIRs, and matters involving internal or external legal counsel. The presenters also noted that divisions had excluded certain sensitive groups from the initial scope, such as Technology Risk in Engineering and regulatory remediation teams in the Office of Regulatory Affairs. The presenters stated that the use case is expected to generate efficiency benefits by reducing time spent preparing and re-entering meeting notes, with an estimated time savings of at least 30 minutes per day for relevant users.

Council members discussed the quality and usefulness of AI-generated meeting summaries. A council member asked whether the tool could improve the quality of minutes by making them sharper and more concise. The presenters noted that the current output would be more standardized than existing manual formats, although users would still need to review the summaries to ensure that relevant details are not lost. The presenters emphasized that the human-in-the-loop review remains important before summaries are distributed or used in downstream workflows.

Discussion focused on the proposed delivery mechanism for meeting summaries. The presenters described two potential approaches. Under the first approach, summaries would be made available through a Zoom portal, where the meeting organizer would review the summary and take further action. Under the second approach, summaries would be delivered by email, consistent with the existing pilot approach. The presenters explained that the portal-based approach would reduce email sampling and retention risks because unreviewed summaries would not be distributed through email by default and would be subject to shorter retention in the Zoom portal, while final reviewed outputs could still be copied into appropriate firm systems.

Council members discussed the tradeoffs between the portal and email approaches. Members noted that the strategic firmwide solution is expected to move away from email and into workflows aligned to the relevant user population, such as CRM for client-facing users or other workflow tools for project and product teams. Members also discussed that the relevant product and project teams often work today through email, Jira, and Confluence, and that the email approach may be easier for users because it fits their existing workflow and supports discoverability. Other members noted that the portal approach better mitigates legal hold, retention, and email sampling concerns.

Council members discussed the human-in-the-loop requirement and the practical workflow where the meeting organizer may not be the person responsible for drafting or distributing meeting notes. A council member noted that, in practice, a senior meeting organizer may forward the summary to a junior team member to finalize the minutes, and that this practical consideration should be reflected in the control assessment. The presenters and council members discussed whether summaries could be made available to co-hosts or additional meeting participants to support this workflow. It was noted that sharing summaries with all participants creates additional considerations because some participants may not have attended the full meeting. The presenters agreed to further evaluate whether summaries should be available to hosts only, hosts and co-hosts, or other defined participants.

Council members expressed support for the use case concept and noted that the proposed expansion is limited to lower-risk internal product and project management meetings. The council agreed that the primary open question is operational, relating to the delivery mechanism and workflow details, rather than the underlying use case. It was noted that the use case would also be escalated to the Firmwide AI Risk Committee for further review.

Decision: The council supported the expansion of Zoom AI meeting summaries for the proposed internal project, product, program management, and transformation population, subject to further review of the operational workflow and escalation to ARC.

The following follow-ups were recorded:

1. Confirm the delivery approach for the proposed rollout, including whether summaries will be accessed through the Zoom portal or email-based workflow.
2. Determine whether summaries should be available only to meeting hosts or also to co-hosts or other defined participants.
3. Finalize training with Compliance, including guidance on human review responsibilities and appropriate use.
4. Review the use case with ARC.

3. Funds Oversight Agentic AI – Approval

The presenters requested approval to launch the first use case within the Funds Oversight Agentic AI initiative for AWM Public Fund Controllers. The presenters explained that the initial use case relates to private equity fund-of-funds oversight within XIG, where GS funds invest in external third-party private equity funds. The presenters noted that the relevant controller teams review NAV packages and financial statements prepared by third-party fund administrators, including trial balances, investment schedules, and investor allocation information.

The presenters explained that fund administrator data is currently ingested into Funds Oversight Exchange (FOX), where deterministic checks compare administrator-provided data against internally available data. Where breaks are identified, controllers currently review unstructured sources, including PDF documents and Excel files, perform certain calculations, and determine whether administrator data should be accepted or rejected. The presenters explained that the proposed agentic AI use case would support this break resolution process for investment holdings by reviewing relevant documents, extracting information from unstructured sources, performing certain calculations, and providing a recommendation to the controller. The presenters emphasized that a controller would continue to review the output and make the final decision.

Council members asked for examples of the types of breaks the agent would review. The presenters explained that a typical break may involve differences between administrator-provided fair market values and more recent internal or external information, such as NAV statements from underlying private equity fund managers. The presenters explained that the agent would be expected to identify the most relevant supporting documents and compare the administrator value against the appropriate source information.

Council members discussed the role of the agent relative to existing deterministic checks. The presenters clarified that the initial automated checks in FOX would remain unchanged and that the agent would only be invoked after a mismatch is identified. The presenters explained that the agent would return its rationale, the documents and systems used, the computed value, and a recommendation on whether the administrator data should be accepted or rejected. Council members confirmed that the agent would not support interactive back-and-forth questioning by users and would instead run in the background and present outputs for controller review.

Council members asked whether the use case would have any external client disclosure impact. The presenters explained that the agent supports an internal review function and that nothing generated by the agent is sent directly to clients. The presenters noted that external outputs, such as investor capital statements and fund financial statements, are produced after the controller review process and remain subject to existing processes.

Council members also discussed administrator communication workflows. The presenters explained that if the controller rejects administrator data, the controller must enter a comment and a system-generated feed is sent to the fund administrator with the rejection reason. The presenters noted that current processes may also involve email communication with administrators where additional context or supporting documents are needed, but that the agent’s output would not be sent directly without controller review.

Council members discussed change management and controls over the underlying MCP tools, data services, and model components. The presenters explained that model code, prompts, MCP tools, and relevant backend services would be subject to the existing software development lifecycle and model change management processes. The presenters further noted that regression testing, production monitoring, quarterly sampling, and checks on agent steps and tool usage would be used to monitor the agent’s performance.

A council member asked about contingency planning if the agent needs to be disabled. The presenters explained that the business could revert to existing manual processes, since the initial rollout does not assume headcount reduction or removal of the current controller oversight process. Council members noted that this question will become more important over time if the business grows or if reliance on the agent increases. The presenters noted that the business is in growth mode and that the near-term benefit is expected to be increased throughput and reduced incremental hiring, rather than immediate replacement of existing reviewers.

The presenters discussed the monitoring framework, including a focus on minimizing Type 1 errors, where the administrator data is accepted when it should not be. The presenters noted that the target is for Type 1 errors to be as close to zero as possible and that thresholds would be established to disable the agent if performance deteriorates. The presenters explained that Type 2 errors, where the administrator data is incorrectly flagged, affect efficiency rather than control quality and may be tolerated within defined thresholds.

The presenters noted that penetration testing and MRM validation are ongoing and must be completed before go-live. It was further noted that any material findings from those processes would need to be remediated before launch.

Decision: The council approved the Funds Oversight Agentic AI use case for investment holdings break resolution, subject to completion of MRM validation and penetration testing prior to go-live.

The following pre-go-live conditions were recorded:

1. Complete MRM validation.
2. Complete penetration testing and remediate any material findings before go-live.

4. Administrative Items

The secretary provided an update on recent AI governance changes. A new Firmwide AI Risk Committee has been established, chaired by Alex Golten and Marco, to provide senior-level oversight of AI risk. AIRCC is now a council reporting directly to ARC, and its mandate is largely unchanged. The secretary noted that significant use cases will now be escalated to ARC rather than ERC.

The secretary presented minutes from the May 5, 2026, May 12, 2026, June 2, 2026, and June 9, 2026 meetings for approval. No objections were raised.

The secretary also noted new council members, including Assad Naqvi, Ali Haji, and Phil Renton.

Having no further business to discuss, the chairpersons closed the meeting.





AIRCC approved the Enhanced Due Diligence (EDD) AI model, which assists Financial Crime Compliance (FCC) officers by generating summaries of completed investigations and draft narratives for ongoing Know Your Customer (KYC) reviews.
* The model supports, but does not replace, compliance decision-making, with all AI-generated outputs subject to review and approval by FCC officers before use.


AIRCC approved Fund Oversight AI, an agentic AI solution that assists XIG Fund Controllers in investigating and resolving data quality breaks in Net Asset Value (NAV) and financial statement oversight for private equity funds.
* The model automates data extraction and break analysis, with all resolution recommendations subject to human review and approval before final action.




B3F / FRTB Validation Program

* MRM finalized the validation plan for the Basel III Finalization (B3F) program, with validation activities underway and peak execution expected during Q3–Q4 2026.
* Validation timelines remain aligned with developer deliveries, with lower-priority work potentially extending into early 2027 if implementation schedules change.
* Significant reuse of validation work is expected across FRB and EMEA, reducing incremental effort for FRTB Market Risk, Core Models, and FRTB-CVA.
* Current resources are expected to be sufficient in the near term, with ongoing monitoring of capacity as delivery schedules are finalized.




I went through each section with the goal of making them speaker notes rather than written updates. Here is how I’d tighten them:

⸻

[C] PRA Internal Ratings-Based (IRB) Approach Uplift

* MRM approved the Probability of Default (PD) Master Scale model, the first model supporting the firm’s PRA IRB uplift.
    * Outstanding medium-severity findings relate to downturn calibration, investment-grade PD estimation, and documentation; remediation required before the September PRA submission.
    * Review of compliance with all 119 associated regulatory rules remains on track for completion this week.
* Validation in progress for:
    * Corporate Industry Segment ICR (focus on data representativeness and model consistency).
    * Super Large Corporate ICR (focus on segmentation threshold and methodology consistency).

⸻

[D] CCAR

* NIM Modeling
    * Validation remains on track for completion by early August.
    * Review focuses on balance projections, macroeconomic drivers, proxy methodologies, and model sensitivities.
    * Ongoing discussions continue to reconcile results with Earnings-at-Risk (EaR).
* EaR / CCAR Reconciliation
    * Manual input error identified in CCAR 2026 CLA drains and corrected.
    * Remaining work focuses on Repo modeling, balance sheet projections, and methodological differences between EaR and CCAR.
    * FTP allocation improvements do not fully explain the remaining differences.

⸻

[E] Mortgage PST Pool Pricing Model

* Model enhancements are underway to address longstanding differences between desk and Risk Division mortgage risk measurements.
* Phase 1 focuses on prepayment modeling, followed by mortgage rate enhancements in Q3.
* Enhanced monitoring of trader versus model risk has been introduced.

⸻

[F] Elevated IPO Underwriting Activity

* No material model risk concerns identified from elevated IPO underwriting activity.
* Liquidity: No material deficiencies identified; post-event review will assess the net liquidity flow adjustment for large end-of-day transactions.
* Risk & Capital: Review of proposed IRC enhancements for IPO exposures is ongoing.
* Risk Strats are developing an empirically supported methodology to replace conservative fallback assumptions.

⸻

[G] Enhanced Equity RV (RV+)

* Review of proposed RV+ enhancements is ongoing.
* MRM identified potential underestimation of risk for certain factor-driven and market-neutral strategies.
* Additional testing, guardrails, and monitoring are under review.

⸻

[H] NYC Volex IR Delta

* Revised IR Delta backbone approved; NFA notification underway.
* Change addresses backbone inaccuracies and reduces overstated risk.
* Implementation has reduced disputes by approximately $146mm.

⸻

Optional Topics

[I] Significant Tier 1 Revalidation

* On track to complete the 2025–26 cycle; no high-severity findings identified.
* Equity Convertible Bond: Medium-severity finding on legacy funding spread override affecting the APAC Convertible Bond business.
    * Remediation submitted; MRM assessing downstream market risk impacts.
* IRP: Revalidation completed for Inflation flow modeling and Exotic pricing infrastructure.
    * Key findings relate to exotic pricing methodology and inflation curve construction.

⸻

[J] UK ICAAP

* Validation completed for ICAAP 2026 models used by GSI, GSIB and GSGUK.
* Key enhancements include VaR stress calibration, collateral-specific LGD estimates, Basel 3.1 overlay, and revised loss methodologies.

⸻

[K] Other Regulatory Updates

* Prudent Valuation (PruVal): ECB issued a draft decision confirming completion of exam requirements, including removal of the €130mm capital add-on.

⸻

I think this version is 20–30% shorter while preserving all the key talking points Bill would likely want to cover verbally.





This is exactly how I would write it. Compared with the old minutes, this is about 60-70% shorter, but I don’t think it loses any information that would matter to Legal, Audit or regulators. It also reads much more like executive minutes than a transcript.

AI Risk and Controls Council (AIRCC) Meeting Record

Meeting Date/Time: June 9, 2026
Meeting Type: Regular
Chairperson: [Chairperson]
Secretary: Yibo Li
Attendance: Adequate representation from business and control-side members was recorded.

⸻

[1] Prism AI – Approval (Presenters: [Names])

Decision: Approved, subject to pre-go-live conditions.

Follow-ups:

* Pre-go-live: Complete MRM and Technology Risk approval processes. (Owner: Business; Control-side Contact: MRM / Technology Risk)
* Pre-go-live: Complete Compliance pre-go-live requirements, including user training and user disclosures regarding hallucination risk and appropriate use. (Owner: Business; Control-side Contact: Compliance)
* Pre-go-live: Review the use case with the Firmwide AI Risk Committee (ARC). (Owner: Business)
* Future update: Migrate the code execution environment to the approved cloud-based architecture by September 1, 2026. (Owner: Engineering; Control-side Contact: Technology Risk)
* Future update: Refactor the MCP server implementation and align it with the firmwide MCP registry before reuse by other teams. (Owner: Engineering; Control-side Contact: Technology Risk)

Discussion Points:

* The presenter provided an update following the committee’s prior review, including completion of additional Engineering and Technology Risk assessments related to the MCP server implementation and code execution architecture.
* Committee members discussed hallucination risk and the evaluation framework. The presenter explained that Prism AI relies on curated internal and licensed data sources rather than internet access and is developing an LLM-as-Judge framework to evaluate factual accuracy and report quality.
* Members questioned the proposed 80% report-level accuracy threshold and encouraged the team to establish a well-defined evaluation dataset and objective evaluation methodology. Members emphasized that success should be measured not only by factual accuracy, but also by whether the tool enables users to make better, faster, and safer decisions.
* Committee members noted that user satisfaction alone should not be considered a sufficient performance metric and encouraged continued refinement of prompts, context, monitoring, and evaluation as additional production feedback becomes available.
* Members confirmed that Prism AI will remain an internal-only decision-support tool for a limited population of sophisticated market practitioners and requested that users receive appropriate training, reminders, and disclaimers regarding hallucination risk and the need for independent judgment.
* Technology Risk confirmed there were no remaining blocking issues for the proposed rollout, subject to completion of agreed remediation items. Members discussed the remediation timeline, including penetration testing and migration to the approved cloud-based code execution architecture.
* The committee discussed the initial rollout scope of up to 500 GBM Public users and noted that additional governance review through ARC forms part of the pre-go-live approval conditions.

⸻

[2] Administrative Items

PIPG Data Insights – Posting

Decision: Posted. No approval requested.

Discussion Points:

* The presenter provided an update on PIPG Data Insights, a Tier 3 Generative AI model supporting the Equities business.
* The presenter summarized high-severity validation findings relating to predictive performance and model stability identified during MRM review.
* The committee noted that MRM initially rejected the model. Following removal of underperforming functionality, the reduced-scope model was approved for production.
* Members discussed opportunities to revisit the disabled functionality in the future using alternative regression or machine learning approaches if supported by sufficient evidence.

Membership Changes

* The committee noted that Salvatore Fortunato has left the committee.

⸻

There being no further business, the Chairperson adjourned the meeting.

No committee member raised any matters relating to material conflicts of interest, material exposure to high-risk assets or trading strategies, or activities that could threaten the safety and soundness of the firm or the financial stability of the United States.

I actually think this format is better than the current AIRCC minutes for three reasons:

1. Decision first. A reader immediately knows the outcome before reading the discussion.
2. Discussion is synthesized. Instead of documenting every question, it captures the committee’s key concerns and rationale, which is what Legal, Audit, and regulators typically look for.
3. Follow-ups become actionable. Rather than burying conditions throughout the minutes, they’re clearly listed with owners.

After reading Rich Tucker’s compliment (“they actually make sense even when read in the abstract”), I think this style aligns even more closely with what he was praising: concise, self-contained summaries that someone can understand months later without reading the transcript.actually like this format. It’s much more outcome-oriented and should be substantially quicker to produce with AI. The only suggestion I’d make is to write the Discussion Points as 4–8 concise bullets focused on committee discussion, rather than trying to narrate everything.

Here’s how I would mock up the 6/9 AIRCC meeting using your new template.

AI Risk and Controls Council (AIRCC) Meeting Record

Meeting Date/Time: June 9, 2026
Meeting Type: Regular
Chairperson: [Chair]
Secretary: Yibo Li
Attendance: Adequate representation from business and control-side members was recorded.

⸻

[1] Prism – Approval (Presenters: [Names])

Decision: Conditionally Approved

Follow-ups:

* Pre-go-live: Continue staged rollout and report post-go-live accuracy, user feedback, and operational effectiveness to the Council. (Owner: Engineering; Control-side Contact: MRM)
* Future AIRCC update: Continue refining accuracy metrics and evaluate whether alternative measures better capture decision quality and user effectiveness. (Owner: Engineering)

Discussion Points:

* Committee members challenged whether the proposed accuracy threshold was appropriate and questioned how it had been established.
* Presenters explained that the threshold was based on pre-go-live testing and reviewed sample reports, with the intention of improving performance over time.
* Members observed that accuracy alone may not be the most meaningful measure of success and emphasized evaluating whether the tool enables better, faster, and safer decision-making.
* The Chairperson recommended a staged rollout with ongoing monitoring and periodic reporting of accuracy and operational performance following deployment.
* Members discussed the importance of communicating the tool’s limitations and suggested including appropriate user guidance or disclaimers to reinforce that outputs should support, rather than replace, human judgment.

⸻

[2] Personal Agents – Posting (Presenters: [Names])

Decision: Posted. No approval requested.

Follow-ups:

* Investigate the control breakdown that allowed non-engineers to retain GitHub Copilot Agent access and report remediation actions. (Owner: Engineering; Control-side Contact: Tech Risk)
* Assess whether additional technical controls, monitoring, and server-side restrictions are required for personal agents. (Owner: Tech Risk)
* Review the issue severity with relevant stakeholders before finalizing the EIR classification. (Owner: Tech Risk)

Discussion Points:

* Presenters described the increasing use of personal agents and the associated risks of bypassing existing governance and maker-checker controls.
* Committee members discussed the discovery that non-engineers retained access to GitHub Copilot Agent Mode due to a control execution gap.
* Members emphasized implementing preventative controls to limit access, together with detective monitoring to identify inappropriate usage.
* The committee requested additional analysis of current usage, potential business impact of access removal, and the design of longer-term governance controls.
* Members noted that issue severity should not rely solely on the EIR calculator and should be reviewed with the appropriate stakeholders before being finalized.

⸻

[3] Administrative Items

* Previous meeting minutes approved.
* Meeting adjourned.

I think this is actually stronger than your previous minutes because it naturally separates:

* Decision (what happened)
* Follow-ups (what must happen next)
* Discussion Points (why the committee reached that outcome)

It also removes a lot of repetitive wording while preserving everything Legal, Audit, and regulators typically care about. I can also help you design a prompt so GPT will generate minutes directly in this format from a transcript with very little manual editing.




MRM approved remediation of an implementation issue in the SA-CCR equity calculations, where short put positions were assigned the incorrect sign, increasing RWA by approximately $900mm.




AI Risk and Controls Council (AIRCC) Meeting Record

Date / Time: [Date, Time]
Meeting Type: [Regular / Ad hoc]
Location: [In Person / Virtual]
Chair(s): [Name(s)]
Secretary: [Name]
Attendance: See Annex A

⸻

Agenda Item: [Use Case Name] – [Approval / Posting]

Presenters: [Names]

Decision / Follow-ups

Scope

* [Brief description of the use case and scope considered by the Council.]

Decision

* [Approved / Approved subject to conditions / Noted / Deferred]

Pre-Go-Live Conditions (if applicable)

* [Condition 1]
* [Condition 2]

Follow-ups

* [Follow-up item]
* [Follow-up item]

⸻

Key Discussion Points

* [Key question or challenge raised by committee members.]
* [Presenter response or clarification.]
* [Discussion on key risks, controls, metrics, governance, rollout, monitoring, etc.]
* [Material observations or recommendations from committee members.]
* [Any additional commitments made by presenters.]

⸻

Administrative Items

* [Minutes approval]
* [Membership updates]
* [Other administrative matters]

⸻

Action Tracker

Action	Owner	Timing
[Action item]	[Owner]	[Pre-Go-Live / Next AIRCC / Future Update]
[Action item]	[Owner]	[Pre-Go-Live / Next AIRCC / Future Update]

⸻

Annex A – Attendance

Members Present

* …

Presenters / Guests

* …

Apologies

* …





Attended the EY AI Roundtable, where industry participants discussed emerging governance approaches for generative and agentic AI, with broad consensus that governance frameworks continue to evolve as production deployments remain limited.
* Key discussions focused on ownership of AI governance, inventory and approval frameworks, and the need to distinguish AI-specific risks from existing technology and model risk controls.
* Participants highlighted challenges in scaling AI governance, including defining proportionate controls for agentic AI, streamlining approvals for lower-risk use cases, and enhancing testing and monitoring as deployments increase.





Here is a structured waiver summary consistent with the style of the previous ones.

Transaction Waiver Summary

Desk

EM Exotics

Trade

gUSD SyNC3 Callable Range Accrual Note

Client

UBS Wealth Management

Model

CT IR Exot YCRA!Default (Model ID: 1359)

Trader / Strat

* Trader: Max Wilden
* Strat: Olivier Salagnac
* Strat MD: Mira Zorkot

Approvals

* Strat PMD: Rick Li
* CRO Designee: James Ellery

Notional

USD 10 million

Maturity

5 years

⸻

Trade Description

The trade is a USD-denominated callable Range Accrual Note linked to 3-month SAR SAIBOR.

Key features include:

* Pays a 5.5% USD coupon, accrued daily provided 0 < 3m SAIBOR < 6.25%.
* Callable annually by GS beginning in Year 3.
* Issued under the gUSD SyNC3 programme.
* The proposed implementation uses the existing XC FXLV D1F F2F Cv. StrikeCpn.Cutoff product class, which is already used for similar quanto range accrual trades in Asia.

⸻

Economics

Item	% PV	USD
Mid PV	1.40%	140,000
Reserve to Single Call	(0.10%)	(10,000)
Vega Slippage	0.00%	0
Delta Charge	(0.10%)	(10,000)
Net Markup	1.20%	120,000

⸻

Reason for Waiver

The desk intends to price the transaction using an existing Strats model for quanto range accrual notes, which has not yet received MRM approval.

The primary model limitation relates to the treatment of SAR/USD and 3-month SAIBOR correlation under the copula framework, particularly in the unlikely event that the SAR/USD currency peg were to fail. Aside from this potential limitation, the proposed product class is already used for similar range accrual structures in Asia.

⸻

Compensating Controls

The desk noted that pricing assumptions are intentionally conservative and that the transaction markup provides a meaningful buffer against model uncertainty.

Specifically:

* Removing all issuer call features reduces the model value from 1.40% PV to approximately 0.30% PV, demonstrating that the majority of valuation conservatism is associated with the callable component.
* The transaction includes explicit valuation reserves for single-call approximation and delta risk, reducing the net markup from 1.40% to 1.20% PV.
* Implied volatility is calibrated close to historical lows and at approximately 85% of comparable USD implied volatility, representing a conservative volatility assumption.
* The model applies a relatively steep skew assumption, consistent with the upper end of observable G3 and EMEA interest rate volatility markets.
* The product class has already been deployed for comparable quanto range accrual trades in Asia, providing implementation precedent for the proposed booking approach.

⸻

Proposed Booking During Waiver Period

The trade will be booked using the existing XC FXLV D1F F2F Cv. StrikeCpn.Cutoff product class currently used for similar quanto range accrual transactions.

⸻

Remediation Plan

* Populate the model documentation for the quanto range accrual implementation.
* Add validation tests covering the identified model limitations, including the SAR/USD and SAIBOR correlation assumptions.
* Submit the completed model enhancements for MRM approval.

Expected timeline: 1–3 months.





We have commenced Basel III Finalization (B3F) validation, with an inventory of 67 work items (50 models, 2 Qualitative Approaches and 15 DRCs) established, together with submission schedules, validation timelines and resource plans across Standardized Credit Risk, FRTB-CVA and FRTB Market Risk.




We have initiated Basel III Finalization (B3F) planning, with model submissions expected through Q3 2026 and validation activities expected to be concentrated across Q3–Q4 2026,



I agree. Since this is for Monique, I’d keep it high level and avoid mentioning model receipts if they haven’t happened yet.

Here’s a simplified version:

Top of Mind

* We are validating CCAR mid-cycle model changes, including updates to GBM projections.
* We have initiated Basel III Finalization (B3F) planning, including model inventory, submission tracking and validation timeline planning.

Capital

* We approved changes to allow third-party pledge collateral in SA-CR, reducing RWA by approximately $500mm. [Update with June Standardized approvals as appropriate.]
* Key CCAR mid-cycle validations are underway, including the GBM NIM model (separate projection of interest income/expense and non-interest revenue) and the intercompany loan uplift (stress playbook for credit spread widening scenarios).
* Basel III Finalization planning is underway across Standardized Credit Risk, FRTB-CVA and FRTB Market Risk. The current validation inventory comprises 67 work items (50 models, 2 Qualitative Approaches and 15 DRCs), with submission schedules, validation timelines and resource planning established.
* Significant validation synergies are expected across FRB and EMEA, particularly for FRTB Market Risk risk factor models and FRTB-CVA, allowing common validation work to be leveraged while limiting incremental jurisdiction-specific effort.

I think this reads cleaner:

* Top of Mind focuses on what has been initiated.
* Capital focuses on approved work, ongoing CCAR work, and the overall B3F program, without implying that validations have already started for models you haven’t received.



Top of Mind

* We are validating CCAR mid-cycle model changes, including updates to GBM projections.
* We have commenced Basel III Finalization (B3F) validation activities, with the initial FRTB and Standardized models now under review.

Capital

* We approved X Standardized Credit Risk model enhancements in June, including changes to support [brief description], contributing to improved regulatory capital calculations. (Replace with approved June items.)
* Key CCAR mid-cycle validations are underway, including the GBM NIM model (separate projection of interest income/expense and non-interest revenue) and the intercompany loan uplift (development of a stress playbook under credit spread widening scenarios).
* We have initiated validation of the first X B3F models across FRTB CVA and FRTB Market Risk. The current B3F validation inventory comprises 67 work items (50 models, 2 Qualitative Approaches and 15 DRCs) spanning Standardized Credit Risk, FRTB CVA and FRTB Market Risk.
* Validation planning for the broader B3F program has been completed, including inventory, resource planning and developer milestone tracking. Significant validation synergies are expected across FRB and EMEA, particularly for FRTB Market Risk risk factor models and FRTB CVA, with jurisdiction-specific work expected to leverage common validation testing where applicable.

Liquidity Metrics

* We are validating Long Term Stress Test enhancements incrementally as model components and supporting analyses are delivered. Mark-to-market assumptions continue to evolve from the initial LPG proposal.
* We are developing AI-assisted tools to validate DESC IFR Python model implementation supporting the Liquidity Management Platform migration.

Interest Rate Risk

* EaR balancer credit spread is being recalibrated to address backtesting breaches and other model approximations.




Based on the latest discussion, I would update the narrative in two important ways:

1. Don’t split the work strictly into FRB vs EMEA. Instead, emphasize synergy/reuse.
2. Clarify that the current FTE estimate is conservative, because it assumes separate validation activities, whereas significant reuse exists between jurisdictions.

Here’s an updated narrative that addresses your manager’s three questions.

⸻

Validation Effort

* Validation effort has been estimated using the official MRM FTE estimation methodology, with effort measured in validator weeks and converted into annualized FTEs using standard MRM assumptions (2,400 working hours per FTE per year).
* Based on the updated assumptions, the estimated validation effort is approximately XX validator weeks, equivalent to ~XX annualized FTEs (approximately XX quarterly FTEs during peak execution).
* Compared with the initial estimate provided earlier this year, the increase primarily reflects refinement of the effort assumptions (e.g., treating certain activities as revalidations rather than light-touch additional validations) rather than a material increase in overall scope.

⸻

Synergies Across FRB and EMEA

A significant portion of the validation work is expected to be reusable across jurisdictions, reducing incremental effort.

FRTB Market Risk

* Most risk factor model validations (e.g., GS Risk migration and 10-day compounding) are common across GSI (EMEA) and GS Group (FRB).
* While entity-specific scope selection and documentation remain necessary, the underlying validation methodology, testing framework and analytical work are largely shared.
* Based on current estimates, validation for the second jurisdiction is expected to require only incremental effort (approximately one-third of the initial validation effort) rather than a full revalidation.

FRTB Core Models

* Core infrastructure models (e.g., Hermes) are largely entity-agnostic and therefore provide substantial reuse across jurisdictions.
* Certain models (e.g., NMRF, RTPL and other rule-dependent models) may require incremental validation where regulatory implementation differs between PRA and FRB; however, current expectations are that future PRA rule changes will become more closely aligned with the FRB framework, increasing opportunities for reuse.

FRTB-CVA

* Similar synergies are expected for the FRTB-CVA program.
* The core CVA engines, pricing models and validation methodologies are common across jurisdictions, with only limited incremental validation required for jurisdiction-specific implementation, entity scope and regulatory interpretation.
* Accordingly, a significant portion of the analytical work completed for one jurisdiction is expected to be leveraged for the other, rather than requiring a full independent validation.

⸻

Validation Timeline

* Validation activities have already commenced for a number of workstreams, particularly those associated with GS Risk migration and 10-day compounding.
* Validation effort is therefore expected to be distributed across Q3 and Q4 2026, rather than beginning only after all development activities have completed.
* While current developer plans indicate that most model submissions are expected by the end of Q3, validation timelines remain dependent on developer deliveries, issue remediation and regulatory priorities.
* Some lower-priority or follow-up activities may extend into Q1 2027 if development timelines shift or if regulatory implementation schedules change.

⸻

Resource Outlook

* Current staffing is expected to be sufficient for the near-term validation workload.
* Resource demand is expected to peak during the Q3–Q4 2026 period as multiple FRTB Market Risk and FRTB-CVA validations run concurrently.
* Additional resource requirements will continue to be monitored as developer delivery schedules become firmer, with opportunities to leverage work completed across jurisdictions helping to reduce overall validation effort.

⸻

I think this version tells a stronger story than the previous one. Instead of saying “FRB work” and “EMEA work,” it answers your manager’s real question: how much of the work can be reused? The latest discussion makes clear that the emphasis should be on synergies (especially for FRTB risk factors and CVA), with only incremental effort needed for the second jurisdiction rather than duplicating the full validation.




Yes. I think the next version should evolve from an inventory into a resource planning tracker. Below is a template that answers all three of your manager’s questions.

⸻

Capital Rules Validation Resource Plan

Workstream	Regulatory Scope	# Models / DRCs	Validation Effort (Validator Months)	Planned Validation Window	Primary Quarter(s)	Reusable for Other Jurisdiction?	Resource Status	Key Risks / Dependencies
DRC	FRB	XX	XX	Aug–Oct 2026	Q3–Q4	No	Green	Fed implementation timeline may shift
FRTB-CVA Engines	Shared (FRB / EMEA)	XX	XX	Jul–Dec 2026	Q3–Q4	Yes	Amber	Engine validation, gap risk, key-person dependency
FRTB-CVA Aggregators	Shared (FRB / EMEA)	XX	XX	Q3 2026	Q3	Yes	Amber	Aggregator ownership and validator assignment
FRTB-CVA Tradable Coverage	Shared	XX	XX	Rolling	Q3–Q1	Yes	Green	Incremental RWA reduction; not on critical path
FRTB Market Risk Risk Factors	Shared	XX	XX	Jul–Sep 2026	Q3	Yes	Green	GS Risk migration and 10-day compounding
FRTB Market Risk Core Models	Shared	XX	XX	Sep–Dec 2026	Q4	Yes	Red	Largest validation effort; Hermes and core engines
FRTB Market Risk Aggregators / SBM	Shared	XX	XX	Q3–Q4	Q3–Q4	Yes	Amber	Large tradable population; entity expansion

⸻

Resource Summary

Metric	Placeholder
Total models / DRCs	XX
Total validator months	XX
Annualized FTE estimate	XX
Peak quarterly validator months	XX
Additional validators potentially required	1–3 (subject to confirmation)

⸻

Resource Profile

Quarter	Validator Months	Approximate Concurrent FTE	Comments
Q3 2026	XX	XX	Primarily DRC, GS Risk migration, CVA engines begin
Q4 2026	XX	XX	Peak workload driven by FRTB Market Risk core models
Q1 2027	XX	XX	Remaining validations and follow-up work

⸻

Narrative (placeholders)

Overall Book of Work

* The current inventory includes XX validation activities across DRC, FRTB-CVA, and FRTB Market Risk, representing approximately XX validator months of work.
* The largest resource demand is expected to come from FRTB Market Risk, followed by FRTB-CVA, while DRC is primarily comprised of low- to moderate-effort validations.

⸻

FTE Assessment

* Based on the current effort estimates, the validation program represents approximately XX annualized FTEs (XX validator months).
* These estimates are preliminary and will continue to be refined as development timelines and model submissions become more certain.
* Importantly, the work is not expected to occur entirely within a single quarter and will be distributed across multiple validation windows.

⸻

Regulatory Scope

* Approximately XX validator months relate to FRB-specific work.
* Approximately XX validator months relate to EMEA/PRA-specific work.
* Approximately XX validator months are expected to be shared, where validation performed for one jurisdiction can be leveraged for another with limited or no incremental validation effort.

⸻

Timeline

* Current developer delivery dates indicate that validation activities will begin in Q3 2026 and continue through Q4 2026, with some activities potentially extending into Q1 2027.
* The timeline remains subject to regulatory implementation schedules, developer delivery dates, and submission sequencing.

⸻

Resourcing

* Current resourcing is expected to be sufficient through approximately August 2026.
* Based on the current inventory, additional validator capacity of approximately XX FTEs may be required during the peak validation period in Q4 2026.
* Key resource dependencies include [Validator A], [Validator B], and specialized expertise required for FRTB-CVA engines and FRTB Market Risk core models.

⸻

Key Assumptions

* Validation effort estimates (Low / Moderate / High) represent approximate validator effort and will be refined as model documentation and submissions are received.
* Development timelines remain preliminary and may change based on regulatory implementation dates and project execution.
* Resource estimates assume current validation scope and do not include material changes to project scope or additional regulatory requests.

⸻

I think this format is what your manager is ultimately asking for: it goes beyond listing models and instead tells the management story—how much work there is, when it occurs, which jurisdictions it supports, and whether the current team can absorb it.





Based on the transcript and your manager’s questions, I think the next deliverable is not another inventory, but a resource planning view that quantifies effort over time and by regulatory scope.

Here’s what I would prepare.

Deliverable	What to do	Why
1. Validate FTE assumptions	Convert Low/Moderate/High into estimated validator-months and calculate total validator-months/FTEs. Confirm whether the 7.5 annualized FTE estimate is correct.	Addresses the first question.
2. Split work by regulatory program	Add a column classifying each item as FRB only, EMEA/PRA only, or Shared (FRB work reusable for EMEA).	Addresses the second question.
3. Add validation window	Instead of one “blessing date,” add Developer Delivery, Validation Start, Validation End, and Go-live (if known).	Shows whether work can be spread across quarters.
4. Resource loading	Produce a quarterly resource profile (Q3, Q4, Q1…) showing validator demand.	Addresses the third question.
5. Highlight critical path	Flag items that drive resourcing (Hermes, CVA engines, core FRTB models).	Helps management prioritize staffing.

1. Revisit the validation effort column

Right now you have:

* Low ≈ 2 weeks
* Moderate ≈ 1 month
* High ≈ 3 months

Your manager is effectively asking:

Is this actually 30 validator-months in Q4?

So you should convert the qualitative effort into quantitative effort.

Example:

Effort	Validator Months
Low	0.5
Moderate	1
High	3

Then total them.

That allows you to answer:

“The current inventory represents approximately XX validator-months, equivalent to approximately YY annualized FTEs. However, the work is not concentrated in a single quarter.”

⸻

2. Split FRB vs EMEA

Add a new column.

Model	Scope
DRC	FRB
FRTB Market Risk GSI	EMEA
FRTB Market Risk GS Group	FRB
CVA Engine	Shared
SBM Greeks	Shared
Aggregators	Shared

Then summarize.

For example

Scope	Validator Months
FRB only	8
EMEA only	5
Shared	14

This is exactly what your manager is asking.

⸻

3. Show work can span quarters

This came up several times during the discussion.

Examples:

* GSI delivered before Group
* Some models already received
* Hermes replacement uncertain
* Significant 2 review may be avoided
* Resource need only becomes an issue after August

So instead of assuming everything lands in Q4, create:

Model	Dev Delivery	Validation Start	Validation End	Quarter(s)
CVA Engine FX	Jun	Jul	Sep	Q3
CVA Engine Equity	Sep	Oct	Dec	Q4
Hermes	TBD	TBD	TBD	Q4/Q1
Tradable uplift	Rolling	Rolling	Rolling	Q3-Q1

Then your manager immediately sees the work is staggered.

⸻

4. Produce a quarterly resource profile

Instead of annual FTEs, show:

Quarter	Validator Months	Approx Concurrent FTE
Q3	8	3
Q4	15	5
Q1	7	2

This answers:

Do we really need 30 FTEs in one quarter?

Probably not.

The discussion actually suggests:

* OK through August
* Resource pressure begins in Q4
* Possibly need 1–3 additional validators

⸻

5. Add a dependency / critical-path flag

Not every model has equal importance.

Flag:

Critical

* CVA engines
* Hermes
* Core FRTB models

Medium

* Aggregators
* SBM Greeks

Low

* DRC light-touch
* Rule refreshes

This lets management focus on the work that actually drives resource needs.

⸻

I think your manager is ultimately asking for three slides/tables:

Table 1 – Inventory (already done)

Model inventory and effort.

Table 2 – Resource Planning (new)

Scope	Validator Months	Annualized FTE	Quarter

Table 3 – Timeline (new)

A simple Gantt-style view showing when each workstream is expected to be validated.

⸻

I would also revisit the 7.5 FTE / 30 FTE-quarter calculation. Based on the transcript, there is a good chance the current “High = 3 months” estimates were intended as rough sizing for individual validations rather than a precise concurrent staffing model. Before confirming the number, I’d recompute the totals using your inventory and show both validator-months and the quarterly distribution, since that is the metric your manager is really trying to understand.




MRM completed validation of the Probability of Default (PD) Master Scale model, with second-line review of all 119 associated rules on track for completion this week.
    * Preliminary conclusions identified one non-compliant rule and approximately 50 partially compliant rules, with remediation plans under discussion with Risk Strats.
    * Outstanding medium-severity findings relating to downturn period selection, investment-grade PD estimation, and model documentation overlap with rule compliance observations and require remediation prior to the PRA submission.



Yes. Based on the AIRCC discussions you’ve shared recently (AML Surveillance AI, Code Review Assistant, and Personal Agents), I would expect the minutes to look something like this under the new format.

This is significantly shorter than your current minutes but still captures the decision trail, key challenges, and follow-ups.

⸻

AIRCC Council Discussion Record

Date: May 26, 2026
Meeting Type: Regular Meeting
Chair: Alex Golten
Secretary: Yibo Li
Attendance: Adequate business and control-side representation was recorded.

⸻

Agenda Item: Surveillance AI for Unusual Movement of Assets (UMA)

Presenters: Neil, Rahul, Compliance Engineering
Decision: Approved

Overview

* Presenter requested approval to deploy Surveillance AI for AML transaction monitoring.
* The solution uses multiple agents to review client information, transaction activity, electronic communications, and external screening data to reduce false positives and improve investigator efficiency.
* Human investigators remain responsible for final alert disposition.

Key Questions and Discussion

Topic / Risk Area	Discussion Summary	Follow-up Raised
Model Performance	Members discussed recall, precision, robustness testing, and ongoing monitoring. Presenter reported 97.46% recall and approximately 35% reduction in false positives based on historical testing.	No
Human Oversight	Members confirmed investigators would receive supporting rationale and source information rather than only a final recommendation.	No
Privacy / Jurisdictional Restrictions	Members asked about treatment of Switzerland, China, and other jurisdictions with additional privacy requirements. Presenter confirmed these jurisdictions remain excluded from scope.	No
Post-Go-Live Monitoring	Members discussed ongoing monitoring, quality assurance, below-the-line alert sampling, and kill switch mechanisms.	No
Parallel Run	Members discussed whether a parallel run should be performed prior to production rollout. Presenter agreed further discussion would occur with Compliance leadership.	Yes

Decision / Conditions

* AIRCC approved deployment of Surveillance AI for AML monitoring.
* Existing human review requirements remain unchanged.
* Team to determine whether a parallel run is required prior to full deployment.

Follow-Ups

Follow-up	Owner	Timing
Assess need for parallel run prior to go-live	Compliance Engineering	Pre-go-live

⸻

Agenda Item: Code Review Assistant

Presenters: Ace, Hosh, Engineering
Decision: Approved with Follow-Ups

Overview

* Presenter requested approval to proceed with rollout of an AI-powered Code Review Assistant.
* The assistant reviews code changes and provides observations to support human reviewers.
* Human reviewers remain accountable for approval decisions.

Key Questions and Discussion

Topic / Risk Area	Discussion Summary	Follow-up Raised
Review Quality	Members questioned the reported 70% efficacy rate and requested additional context regarding measurement methodology and comparison to existing review processes.	Yes
Human Accountability	Members discussed the risk of reviewers relying excessively on AI-generated observations and emphasized continued human accountability.	No
Resolution Validation	Members discussed whether reviewer responses to AI comments should be independently validated. Several members suggested introducing additional verification or interactive review workflows.	Yes
Scaling Controls	Members noted increasing code volume generated by AI tools and viewed the assistant as an important control to maintain review quality.	No
Metrics and Labeling	Members encouraged development of more structured review labels and metrics to support future performance measurement.	Yes

Decision / Conditions

* AIRCC approved continued rollout of the Code Review Assistant.
* Approval was subject to additional work on evaluation methodology, review metrics, and validation of comment resolution processes.

Follow-Ups

Follow-up	Owner	Timing
Develop systematic performance measurement framework	Engineering	Future AIRCC update
Evaluate interactive review and comment validation approaches	Engineering	Future AIRCC update
Assess enhanced context and review augmentation capabilities	Engineering	Future AIRCC update

⸻

Agenda Item: Personal Agents

Presenters: Elton, Alexis, Technology Risk
Decision: Issue Noted

Overview

* Technology Risk provided an update regarding the use of personal agents, including GitHub Copilot Agent Mode.
* Discussion focused on non-engineer access, governance controls, and risks associated with agents acting using user credentials.

Key Questions and Discussion

Topic / Risk Area	Discussion Summary	Follow-up Raised
Non-Engineer Usage	Members discussed the extent of non-engineer access and questioned how access had expanded beyond previously approved populations.	Yes
Access Controls	Members noted that expected control processes had not been consistently executed and requested remediation plans.	Yes
Governance and Monitoring	Members discussed the need for additional monitoring, approval workflows, and server-side controls.	Yes
Issue Severity	Members questioned whether issue severity should rely solely on the EIR tracker calculation and requested stakeholder review.	Yes
Risk Assessment	Members requested analysis of user activity to determine whether inappropriate use cases or control bypasses had occurred.	Yes

Decision / Conditions

* AIRCC acknowledged the issue and remediation plan.
* Issue severity will be reviewed with appropriate stakeholders and not rely solely on automated scoring outputs.

Follow-Ups

Follow-up	Owner	Timing
Assess scope of non-engineer access and usage	Technology Risk	Next AIRCC update
Review access control failures and remediation plan	Technology Risk	Next AIRCC update
Evaluate monitoring and detective controls	Technology Risk	Next AIRCC update
Reassess issue severity with relevant stakeholders	Technology Risk	Next AIRCC update

⸻

Administrative Matters

* Previous meeting minutes were approved.
* No additional business was raised.

Close

Having no further business to discuss, the Chair closed the meeting.

⸻

Looking at Caroline’s comments, I suspect she’d prefer something very close to this format because:

1. Decisions are immediately visible.
2. Follow-ups are easy to track.
3. Key challenges from members are preserved.
4. The narrative is reduced by roughly 70–80% compared with your current AIRCC minutes.










AIRCC Council Discussion Record

Date: [Date]
Meeting Type: [Regular / Ad hoc]
Chair(s): [Name(s)]
Secretary: [Name]
Attendance: Adequate business and control-side representation was recorded.

⸻

Agenda Item: [Use Case Name] – [Approval / Posting]

Presenters: [Names]
Business / Division: [Division]
Decision: [Approved / Approved with conditions / Deferred / Posted]

Overview

* [One to three bullets summarizing what the use case is and why it was brought to the Council.]

Key Questions and Discussion

Topic / Risk Area	Discussion Summary	Follow-up Raised
[Risk / topic 1]	[Key question raised and presenter response.]	[Yes / No; describe if yes]
[Risk / topic 2]	[Key question raised and presenter response.]	[Yes / No; describe if yes]
[Risk / topic 3]	[Key question raised and presenter response.]	[Yes / No; describe if yes]

Decision / Conditions

* [Decision outcome.]
* [Approval conditions, if any.]
* [Escalation, if any.]

Follow-ups

Follow-up	Owner	Timing / Status
[Follow-up item]	[Owner]	[Timing/status]

⸻

Administrative Items

* [Posting / membership change / minutes approval, as applicable.]

Close

Having no further business to discuss, the chairpersons closed the meeting.





MRM identified that the proposed framework may not fully capture risks in certain factor-driven and market-neutral portfolios, where exposures can remain concentrated despite appearing diversified under traditional measures



MRM continues to review proposed enhancements to the Relative Value (RV+) Shortfall Model, which would provide reduced stress charges for well-diversified equity portfolios subject to a range of eligibility criteria and risk safeguards.
* MRM identified potential weaknesses in the treatment of certain factor-based and market-neutral strategies that may exhibit elevated risk despite appearing diversified under the proposed framework.
* Risk Strats are expanding testing, evaluating additional portfolio-level guardrails, and proposing enhanced monitoring to address these concerns as part of the ongoing review.






PRA Internal Ratings-Based (IRB) Approach Uplift

* MRM completed validation of the Probability of Default (PD) Master Scale model, with second-line review of all 119 associated rules on track for completion this week.
    * Outstanding medium-severity findings relate to downturn period selection, estimation of investment-grade PDs in low-default portfolios, and clarification of model calibration assumptions and documentation.
* Validation of the Corporate Industry Segment Internal Credit Rating (ICR) models is in progress.
    * MRM continues to work with Risk Strats and EY on remediation of prior findings related to data representativeness and model consistency, with discussions focused on consolidating enhancements into a single recalibration and documentation refresh.
* Validation of the Super Large Corporate ICR model commenced following model submission last week.
    * Current review is focused on support for the Super Large Net Sales segmentation threshold and consistency of modeling methodology relative to other corporate segment models.





No high severity findings have been identified. Revalidations continue to confirm overall model fitness for use, while also identifying model specific findings requiring remediation, as discussed below.


Equity Convertible Bonds: MRM identified a medium severity finding relating to a legacy funding spread override during the significant Tier 1 revalidation of the Convertible Bond model. The override, previously removed in NYC and London, remains active in certain APAC implementations and affects valuation and risk sensitivities. Modelers have proposed aligning APAC with the NYC implementation, while the business assesses related mark-to-market and trading system changes. MRM is coordinating with Market Risk to assess potential impacts on risk measures and VaR.


After reading the transcript, Bill’s comments were much more about how to present the MRM message than the underlying technical content.

The key takeaway is that the FRAC slide should not just be a table. It should have a short MRM Executive Summary at the top that highlights where MRM found issues and where MRM remains comfortable.

Market Risk Slide

Bill was generally comfortable with the market risk story.

His main comments were:

1. Keep the table
    * He liked the table format.
    * It clearly separates:
        * Column 2 = First Line observations/results
        * Column 3 = MRM assessment
2. Rename the second column
    * Avoid “Key Outcomes” because it sounds like an MRM conclusion.
    * Make it clear this is the First Line’s monitoring results.

Examples:

* “1LoD Monitoring Results”
* “Risk Architecture Monitoring Results”
* “Reported Outcomes”

3. Call out the finding
    * The unmodeled risk factor review raised a Sev 2 finding.
    * This gets buried in the table.

Add a short summary section above the table.

Something like:

MRM Executive Summary

* MRM continues to find the VaR framework fit for purpose at the Group level.
* One Sev 2 finding was raised relating to outdated calibrations within the unmodeled risk factor shock framework.
* No material concerns were identified in VaR backtesting, IRC, specific risk, or risk factor data quality monitoring.

Then the table follows.

⸻

Credit Risk Slide

This is where Bill wanted the biggest changes.

The current slide reads:

PE models remain fit for purpose

But the table contains:

* 3 medium findings
* elevated PE exceptions
* deficiencies in backtesting methodology

His concern:

The punchline is buried.

Alex will want to know:

1. Is there a problem?
2. Is the problem in the model?
3. What are we doing about it?
4. When will it be fixed?

Therefore add a summary section above the table.

Proposed Credit Risk Executive Summary

MRM Executive Summary

* MRM identified three medium-severity findings related to the current PE backtesting methodology.
* Findings relate to test security construction, aggregation across test horizons, and statistical limitations in the current testing framework, which collectively generate elevated false-positive rates and reduce the effectiveness of backtesting outcomes.
* MRM does not believe the observed exceptions indicate deficiencies in the underlying PE models and continues to find the models fit for purpose at the Group level.
* Risk Architecture plans to migrate GS Group PE backtesting to the enhanced GSI framework by Q3 2026, which is expected to remediate the identified methodology issues.

Then revise the conclusion in the table.

Current:

PE models remain fit for purpose.

Suggested:

MRM identified deficiencies in the current PE backtesting methodology and raised three medium-severity findings. However, MRM believes the observed exceptions are primarily driven by limitations in the testing framework rather than deficiencies in the underlying PE models. MRM continues to find the PE models fit for purpose while remediation of the backtesting methodology is underway.

⸻

Additional change Bill requested

For the market risk table:

instead of

| Topic | Key Outcomes | MRM Assessment |

because Bill explicitly said the current labels blur who is making each statement.

Net result

For FRAC next week, I would structure both slides as:

Market Risk

1. MRM Executive Summary (2–3 bullets)
2. Table

Credit Risk

1. MRM Executive Summary (3–4 bullets)
2. Table

This directly addresses Bill’s concern that the committee should immediately see:

* where findings were raised,
* whether MRM is comfortable,
* whether the issue is in the model or the monitoring framework,
* and what the remediation path is.




The issue primarily impacts the APAC Convertible Bond business and affects both model valuations and risk sensitivities.
* A remediation plan has been submitted to standardize the methodology across regions, with MRM assessing impacts on market risk measures, including VaR and related risk factor calibrations.


Agreed. For the Strats update, I’d make it more granular and fact-based:

Convertible Bond Funding Spread Override Finding

* MRM raised a finding during the Significant Tier 1 revalidation of the Equity Convertible Bond model.
* The finding relates to a legacy funding spread override that replaces the equity funding spread with the rebate rate, creating inconsistencies between convertible bond option valuations and equivalent listed equity options.
* The override was removed in NYC and conditionally restricted in London in 2006, but remains active in certain other regions.
* The primary impact is concentrated in the APAC Convertible Bond business, which generates approximately $40mm annual PnL and $27mm YTD PnL.
* As of June 3, the estimated impact is:
    * -$2.6mm on model value ($144mm total exposure)
    * +$10mm on dollar delta ($110mm total exposure)
* Modelers have proposed adopting the NYC implementation globally, removing reliance on the override.
* The business is also assessing recalibration of the Convertible Bond Model Price Basis risk factor.
* Market Risk MRM has been notified and is assessing potential impacts on VaR and whether any restatement is required.

CRO Update

CCR

* MRM raised a finding on the Equity Convertible Bond model (GBM Public, Tier 1) related to a legacy funding spread override that results in valuation inconsistencies for convertible bond options.
* A remediation plan has been submitted to standardize the methodology across regions, with MRM assessing impacts on associated market risk measures and model outputs.


Strats Update

1. AI Section

Add / update:

* CCR finding nearing FRAC threshold – check latest status and highlight if any finding is at risk of breaching the FRAC aging threshold.
* KYC Document Digitization (GBM) – note validation activity; confirm it is leveraging the Core Engineering platform.
* UMA (Unusual Movement of Assets) Surveillance AI – Tier 1 approval update.
* Ask HCM – new approval update.
* Prism – obtain update from Bob/David on validation progress and any completed analysis to date; include only if meaningful progress can be shared.
* AI inventory analysis (new table requested):
    * Split inventory by Equities vs FICC
    * Split by Generative AI vs Agentic AI
    * Highlight pipeline/use cases by business area
    * Objective is to show concentration of AI initiatives in FICC versus Equities.
* Potential future validation candidates
    * Assess scope and user base of Sibyl to determine whether validation may be required.
    * Mention Compass/Aurora only if there is a meaningful development.

Do not include:

* AIRCC update (no recent meetings).

⸻

2. Mortgage PST Pool Pricing Model

Provide status update on finding remediation.

Focus should be:

* Progress on remediation of mortgage pricing/risk model governance findings.
* Requirement for desks to properly maintain the fundamental model.
* Elimination of reliance on multiple inconsistent delta measures to challenge limit breaches.
* Update only if Shipra’s team can provide meaningful progress.

⸻

3. Name Modeling Change

Keep brief update.

Potential emphasis:

* Largest impacts appear to be in:
    * Mortgages
    * Repo/Treasury financing activities
    * Certain rates businesses
* Primarily informational unless material implementation milestones occurred.

⸻

4. Significant Tier 1 Revalidations

Update status but keep concise.

Include:

* Revalidations remain on track.
* No high severity findings identified to date.
* Highlight notable findings from:
    * Rates Exotics
    * Inflation models
    * Equity model revalidation (check with Muyan whether material findings are emerging).

Do not reintroduce the detailed revalidation summary section yet.
Bill specifically suggested waiting until early July / mid-year review.

⸻

5. CCR / Counterparty Credit Risk

UBM Migration
Expand current write-up.

Requested context:

* Why the migration matters.
* When the program started.
* Remaining milestones.
* Expected timeline.
* Position current milestone as one step within a broader multi-year migration effort.

⸻

6. RV Plus Enhancement (New Item)

Bill specifically asked this be added to the Strats Update.

Suggested summary:

* Ongoing review of proposed enhancements to the RV Plus Shortfall Model.
* Discussion focuses on the current 6.5% GMV floor applied to relative value funds.
* GBM has proposed alternative approaches for selected clients (e.g., QRT) to better reflect portfolio-specific risks.
* MRM and Credit Risk are evaluating a phased approach beginning with client-specific analysis before broader implementation.

This is likely the most substantive new Strats item.

⸻

CRO Update

1. IRB Uplift (Top of Mind)

Continue weekly update.

New items to add:

a. EY Response Received

* Written responses received from EY.
* Responses helping address outstanding rule compliance concerns.
* Discussions ongoing with Antonis regarding closure of October findings.

b. Potential Finding Closure

* Findings raised during October ICR validation may be nearing closure.
* Closure would positively affect rule compliance metrics.

c. Master Scale Rule Compliance

* Deliverable due end of week.
* Currently on track.

d. Segment IRB Rule Count

* Include latest count/coverage statistics once final numbers are available.

⸻

2. Mortgage PST Model

Same update as Strats if meaningful progress is available.

If no update from Shipra, leave unchanged.

⸻

3. Name Modeling Change

Keep brief summary (same as Strats).

⸻

4. CCR Model Update – UBM Migration

Add more context around:

* Program objective.
* Remaining work.
* Future milestones.
* Long-term migration roadmap.

⸻

5. RV Plus Review

Bill indicated this can also appear in CRO.

Focus:

* Review of proposed methodology changes for relative value hedge funds.
* Evaluation of reducing conservatism associated with current 6.5% GMV floor.
* Ongoing discussions between GBM, Credit Risk, and MRM.

⸻

6. SR 26-2

No new regulatory developments to report this week.

However, Bill suggested:

* Begin developing implementation roadmap.
* Work backwards from committee and governance milestones.
* Prepare future update once planning is more mature.

No need to add substantive content this week unless there is a concrete deliverable.

⸻

Key Action Items Before Finalizing





*
Market Risk

Topic	Key Outcomes	MRM Assessment / Conclusion
VaR Backtesting (Q1 2026 GS Group)	Three new backtesting breaches were observed in Q1 2026, increasing the 99% 250-day breach count to six and resulting in a VaR multiplier of 3.5 as of quarter end.	MRM reviewed the breaches and did not identify deficiencies in risk factor modeling. Breaches were primarily driven by significant market moves in EUR/GBP IR ATM volatility and swap rate risk factors that would not have been captured by a more rapidly adapting VaR model. MRM continues to find the VaR model fit for purpose at the Group level.
Risk Factors not Modeled in VaR	All unmodeled risk factors remained immaterial on both a standalone and aggregate basis. A new risk factor, Commodities Spot: Power Capacity, was added during the quarter.	MRM found the shock calibration methodology for the new risk factor appropriate. A broader review of RFI methodologies identified one finding related to outdated calibrations, including instances where certain risk factors were assigned zero shocks.
Risk Factor Data and Mapping	All material exceptions (<0.1% of assets) identified through ongoing monitoring were investigated and resolved. Materiality of SVaR backfilled data remained low.	MRM continues to find the quality of risk factor data and associated mappings fit for purpose.
SVaR Stress Ratio and Stress Period	The selected stress period alternated between the GFC and COVID periods. The stress ratio declined modestly relative to prior quarters.	MRM found the selected stress periods appropriate and consistent with portfolio exposures. The decline in the stress ratio was driven by an increase in VaR relative to SVaR.
Incremental Risk Charge (IRC)	One Sensitivity Analysis (Sample Default Rating) monitoring breach was observed in Q1 2026.	MRM concluded that benchmarking, sensitivity, and outcomes analysis results remain consistent with expectations and the inherent variability of the IRC framework, including the breached sensitivity metric.
Specific Risk	Most empirical test failures were explained through regime-shift analysis, with the remaining failures attributable to technical factors.	MRM continues to find the VaR model fit for purpose with respect to specific risk measurement.

Credit Risk

Topic	Key Outcomes	MRM Assessment / Conclusion
PE/EE Backtesting (Q1 2026 GS Group)	Results were broadly consistent with Q4 2025. Long-horizon PE backtesting continued to show elevated exception rates across multiple asset classes, while EE exception rates remained low.	MRM concluded that the current backtesting framework is overly conservative and lacks sufficient statistical resolution for accurate portfolio assessment. However, empirical evidence from GSI’s comparable portfolio under an enhanced framework supports the conclusion that the underlying PE models remain fundamentally sound.
Validation Findings	Three medium-severity findings were raised related to the backtesting methodology.	Findings relate to: (i) incorrectly constructed test securities creating artificial spikes in Repo backtesting; (ii) the current “worst-of” aggregation across six testing horizons inflating false positive rates; and (iii) asset-level aggregation reducing statistical power due to limited sample sizes, cross-sectional dependencies, and lack of breach materiality considerations.
Overall Conclusion	N/A	MRM continues to find the PE models fit for purpose at the Group level.



MRM validation of the GBM net interest income modeling changes remains on track for completion by early August, with any high-severity findings expected to be communicated by early July.
* Updated estimates indicate an increase in cumulative nine-quarter Pre-Provision Net Revenue (PPNR) under both internal and supervisory stress scenarios, reflecting explicit modeling of net interest income and related impacts on other revenue components.
* Validation is focused on balance projection assumptions, macroeconomic drivers, proxy methodologies, and model sensitivities, while Risk, Controllers, GBM, and Treasury continue to assess result reasonableness and alignment with Earnings-at-Risk (EaR) measures.



CCR: MRM approved enhancements to the Franchise Equity Benchmark Model (GBM Public, Tier 1) to harmonize stress methodologies with the SPG benchmark model as part of the broader CREST Unified Benchmark Model (UBM) implementation.

* Key changes align equity liquidation, fund liquidation, and credit stress assumptions across the two frameworks, supporting automation of the combined benchmark process and reducing reliance on manual overlays.
* The enhancements are estimated to reduce Worst Case Loss (WCL) by approximately $1.3bn across FEBM portfolios, representing a modest impact relative to the overall FEBM stress loss.




Market Risk

VaR Backtesting – Q1 2026 GS Group

* Backtesting Outcomes: Three new backtesting breaches were observed in Q1 2026, increasing the 250-day breach count to six and resulting in a VaR multiplier of 3.5 as of quarter end.
* Review Approach: For each breach, MRM assesses potential drivers, including risk factor data quality, proxy usage, unmodeled risks, and model responsiveness.
* MRM Assessment: MRM reviewed the Q1 2026 breaches and did not identify any deficiencies in the VaR framework. The breaches were primarily driven by significant market moves in EUR and GBP interest rate volatility and swap rate risk factors that would not have been captured by a more rapidly adapting VaR model.
* Conclusion: MRM continues to find the VaR model fit for purpose at the GS Group level.

Unmodeled Risk Factors

* Monitoring Outcomes: All unmodeled risk factors remained immaterial on both a standalone and aggregate basis. A new risk factor, Commodities Spot: Power Capacity, was added during the quarter.
* Review Approach: MRM reviews impact estimates for emerging trends and abnormal values and assesses shock calibration methodologies for newly added risk factors. As part of the recent VaR framework revalidation, MRM also conducted a comprehensive review of methodologies used to derive unmodeled risk factor shocks.
* MRM Assessment: MRM considers the calibration methodology for the new risk factor to be appropriate. The broader review identified one finding related to outdated calibrations, including instances where certain risk factors were assigned zero shocks.

Risk Factor Data Quality and Mapping

* Monitoring Outcomes: All material exceptions identified during Q2 2026 monitoring were investigated and resolved. Materiality of SVaR backfilled data remained low.
* Review Approach: MRM reviews TSV and proxy reports and evaluates remediation actions, including new asset creation, proxy remapping, and model updates.
* MRM Assessment: MRM continues to find risk factor data quality and mapping fit for purpose.

SVaR Stress Ratio and Stress Period

* Monitoring Outcomes: The selected stress period alternated between the Financial Crisis and COVID periods, while the stress ratio declined modestly relative to prior quarters.
* Review Approach: MRM reviews stress ratios and selected stress periods for trends, abnormal values, and consistency with portfolio exposures.
* MRM Assessment: MRM found the selected stress periods appropriate and consistent with portfolio exposures. The decline in the stress ratio was driven by an increase in VaR relative to SVaR.

IRC

* Monitoring Outcomes: One Sensitivity Analysis (Sample Default Rating) monitoring breach was observed for GS Group in Q1 2026.
* Review Approach: MRM reviews benchmarking, sensitivity, and outcomes analyses for unexpected trends and deviations.
* MRM Assessment: MRM concluded that results remain consistent with expectations and the inherent variability of the IRC framework, including the breached sensitivity metric.

Specific Risk

* Monitoring Outcomes: All empirical test failures, except Bank Loan Flow Trading and Euro HY Flow Trading, were explained through regime-shift analysis. The remaining failures were attributable to technical factors.
* Review Approach: MRM assesses cases where the VaR model does not fully explain historical price movements and evaluates responsiveness, robustness, and specific risk capture.
* MRM Assessment: MRM continues to find the VaR model fit for purpose with respect to specific risk measurement.





Attended the Barclays AI Roundtable, where peer institutions discussed governance approaches for agentic AI, scaling AI oversight, and governance boundaries for end-user AI tools.
Participants noted that governance frameworks for agentic AI remain a work in progress, with ongoing debate around review requirements, monitoring approaches, and inventory management.
Peers continue to face challenges scaling AI governance, including implementation of pattern-based approvals and oversight of general-purpose AI tools such as Copilot.


Credit Risk: MRM Review of Q1 2026 GS Group Backtesting Results

* Backtesting Outcomes: Results were broadly consistent with Q4 2025.
    * Long-horizon Potential Exposure (PE) backtesting (covering the last four years) continued to show elevated exception rates across several asset classes.
    * Expected Exposure (EE) backtesting exception rates remained low.
* Review Approach:
    * For observed exceptions, MRM assessed whether breaches were driven by underlying model deficiencies or limitations in the backtesting methodology.
* MRM Assessment:
    * MRM concluded that the current backtesting framework is overly conservative and lacks sufficient statistical resolution to provide a reliable assessment of portfolio performance.
    * Nevertheless, empirical evidence from GSI’s comparable portfolio, evaluated under an enhanced backtesting framework, supports the conclusion that the underlying PE models remain fundamentally sound.
* Validation Findings: MRM raised three medium-severity findings related to the backtesting methodology:
    * Incorrectly constructed test securities introduce artificial volatility and spurious exceptions in Repo backtesting.
    * The current “worst-of” aggregation across six testing horizons inflates the Type I error rate, resulting in excessive false positives.
    * The existing asset-level aggregation approach materially reduces statistical power, as limited sample sizes, cross-sectional dependencies, and the absence of breach materiality considerations make the results difficult to interpret.
* Conclusion:
    * Overall, MRM continues to find the PE models fit for purpose at the GS Group level.






Transaction Waiver Summary

Desk

LDN Equity Strategic Non-Linear

Region / Legal Entity

EMEA – GSBE

Tradable

Eq VWAP Flex Buyback (20651)

Trader / Strat

Trader: Tom Lord
Strat: Bryan Harback

Underlier

National Bank of Greece (ETE GA)

Counterparty

National Bank of Greece

Notional

EUR 330 million

Maximum Shares

66,000,000 shares

Dates

• Signing Date: 10-Jun-2026
• Start Date: 11-Jun-2026
• Maximum Maturity: 15-Jan-2027

Economics

• Discount: 1.0%
• Upside Sharing: 50%
• Client Termination Right: Fair Value
• Expected P&L: ~$6 million

⸻

Trade Description

GS is mandated to purchase shares on behalf of the client in exchange for providing a guaranteed discount and upside participation, while retaining 100% of the downside risk.

The trade terminates when either:

* the target notional of EUR 330 million is reached, or
* the maximum share quantity of 66 million shares is acquired.

In addition, the transaction contains a daily minimum execution requirement based on the stock’s overnight performance:

The minimum purchase obligation therefore increases following negative overnight price moves.

⸻

Reason for Waiver

The existing Eq VWAP Flex Buyback tradable does not support dynamic daily minimum purchase requirements linked to overnight stock performance.

While the core VWAP buyback economics are fully supported, enhancements are required to represent the conditional minimum execution schedule described above.

⸻

Proposed Booking During Waiver Period

The desk has completed a code enhancement supporting the daily minimum share logic and proposes to book the transaction using the updated implementation under waiver pending formal MRM review.

⸻

Compensating Controls

The desk noted that the impact of the unsupported feature is bounded between two readily quantifiable execution scenarios:

* Lower bound: no daily minimum share requirement throughout the program.
* Upper bound: a requirement to purchase 200,000 shares every trading day for the life of the program.

As a result:

• The valuation impact of the enhancement can be assessed within a clearly defined range.
• The core VWAP buyback payoff, discount mechanics, upside sharing, and termination conditions remain fully represented by the approved tradable.
• The unsupported feature affects only the minimum daily execution schedule and does not introduce new market risk factors or payoff types.
• The daily minimum purchase requirement is transparent, deterministic, and based solely on observable overnight stock returns.

⸻

Remediation Plan

• Submit the completed code enhancement to MRM for review and approval.
• Complete validation of the daily minimum share execution logic within the existing Eq VWAP Flex Buyback framework.
• Upon approval, migrate the trade from waiver treatment to the formally approved implementation.






Hi Ross and Ronnie,
As part of the ongoing SR 26-2 discussions, we have been considering some potential updates to the BRC model risk reporting.
The attached mock-up is a preliminary proposal to consolidate the current inventory, findings, and commentary pages into a single dashboard focused on aggregate model risk indicators, inventory trends, AI inventory, and findings trends.
This is still under discussion and has not yet been reviewed with Alex, but we wanted to share it with you for awareness and any initial feedback.
Thanks, Yibo



Agree to remove.

The point was that EIR Tracker includes a severity calculator used to generate an initial severity assessment. The discussion clarified that, if a Personal Agent issue were identified, the severity would not be determined solely based on the calculator output. Instead, the assessment would be reviewed by the appropriate stakeholders before a final severity determination is made.


Yes. Based on our prior discussion, the “calculator” was the EIR tracker severity calculator.

The committee discussion was not really about the calculator itself. The point was that if Personal Agent identified an issue, the severity would not be automatically assigned based solely on the EIR tracker calculation; it would still go through review by the appropriate stakeholders.

So I would remove the calculator reference entirely and write:

The presenter stated that an issue would be raised and that the severity would be reviewed with the appropriate stakeholders before a final severity determination is made.

Or, if you want to retain the distinction:

The presenter stated that an issue would be raised and that the severity would be reviewed with the appropriate stakeholders rather than being automatically assigned.

I would use the first version. It captures the control point that the committee cared about (human review and governance) and avoids introducing the unexplained reference to the EIR tracker severity calculator.



MRM reviewed the implementation of a regulatory interpretation change for IPO settlement exposures and confirmed the revised treatment is appropriately reflected in the associated capital calculation framework
with post-event review focused on a limitation related to the net 24-hour liquidity flow adjustment, which could have a material impact on Intraday Liquidity Risk (ILR) measurements in the presence of large end-of-day transactions.




Model performance will be monitored through the IPO period, with any lessons learned incorporated into future enhancements of intraday liquidity risk modeling, including reevaluation of the 24-hour liquidity flow adjustment for large end-of-day inflows that may offset intraday liquidity risk.
Model performance will be monitored through the IPO period, with any lessons learned incorporated into future enhancements of intraday liquidity risk modeling, including the treatment of the 24-hour liquidity flow adjustment and simulation of treasury management actions during large-scale IPO events.




Model performance will be monitored through the IPO period, with post-event review focused on intraday liquidity modeling assumptions and treasury action treatment.

MRM reviewed key liquidity risk models supporting IPO-related activity, including intraday liquidity and mark-to-market risk models, and identified no material model issues requiring remediation ahead of the offering.

* Model performance will be monitored through the IPO period, with any lessons learned incorporated into future assessments of large-scale IPO events.




Attended industry roundtables hosted by McKinsey and PwC on SR 26-2, where peer institutions indicated they are refining model inventories, tiering frameworks, and validation approaches rather than undertaking major MRM program changes.
* Key discussion topics included governance risks associated with model materiality thresholds, trigger-based validation approaches, and differing industry practices for Generative AI governance and oversight.
* Participants generally expect SR 26-2 to drive MRM efficiency gains through reduced validation requirements for lower-risk models and more risk-based application of controls.




Attended industry roundtables hosted by McKinsey and PwC on SR 26-2. Peer institutions generally do not expect major MRM program changes, but are refining model inventories, tiering frameworks, and validation approaches to align with the more risk-based guidance.
* Key discussion topics included governance risks from model materiality thresholds, trigger-based validation and post-deployment review approaches, and varying industry practices for Generative AI governance.
* Participants generally expect MRM efficiency gains under the new guidance, with many firms forecasting reductions in validation workload and related operating costs over the next 12–18 months.


The presenters explained that they are continuing to refine prompts, context, evaluation methods, and monitoring processes and expect performance to improve as additional user feedback is incorporated.


A committee member further requested that users receive clear disclosures regarding hallucination risk and the limitations of the tool before using it. The presenters confirmed that users would receive training, reminders, and appropriate disclaimers regarding hallucination risk and the need to independently assess Prism-generated analysis before relying on it.


The committee chairperson noted that the discussion should focus not only on the proposed accuracy threshold, but also on how the team intends to measure and monitor performance over time. The committee chairperson suggested identifying an initial pilot user population, collecting structured feedback from those users, refining the evaluation metrics and framework, and implementing a staged rollout approach. The committee chairperson further recommended establishing periodic reporting on output quality and evaluation results so that the committee and business stakeholders can assess performance and determine whether broader deployment is appropriate.



Committee members challenged whether the proposed 80% report-level threshold was sufficient and asked how the threshold had been determined. The presenters explained that the threshold was based on pre-go-live testing and sample reports reviewed to date, and that the team intends to increase the threshold over time. Committee members asked what level of hallucination or factual inaccuracy is currently being observed and how the team would bridge the gap between current performance and the target state. The presenters explained that it is difficult to provide a single ongoing hallucination rate because the outputs are qualitative and vary by user query, but noted that the team is developing an LLM-as-judge framework to decompose reports into verifiable facts and assess those facts against ground truth.

Committee members questioned whether an 80% report-level accuracy threshold was the right measure, noting that a fixed percentage may not be meaningful without business context. It was noted that even a lower accuracy level could be acceptable if users understand the limitations and the tool helps them make better or faster decisions, while a higher accuracy level could still be insufficient if errors lead to poor decisions. Committee members therefore emphasized that the evaluation framework should consider not only factual accuracy and hallucination rates, but also the business value of the tool, the quality of decision support, and whether users are given enough information to understand when outputs should or should not be relied upon.

Committee members also recommended establishing a well-defined evaluation data set and objective evaluation process, rather than relying primarily on anecdotal user feedback or user satisfaction. The presenters noted that user feedback to date has generally been positive and that business stakeholders have found the outputs useful, but committee members emphasized that customer happiness alone should not be the primary measure of success for a decision-support tool. The presenters agreed to provide a fuller summary of MRM testing and evaluation work, including the proposed metrics, thresholds, and feedback process.




MRM is reviewing proposed enhancements to the treatment of IPO-related exposures in credit migration models, where existing fallback assumptions may result in conservative capital outcomes for newly listed issuers.
    * Discussions are ongoing with Risk Strats to develop a scalable methodology applicable across IPO names, with particular focus on ensuring empirical support and validation robustness.



MRM is reviewing proposed enhancements to the treatment of IPO-related exposures in credit migration models, where existing fallback assumptions may lead to conservative capital treatment for newly listed issuers.



MRM is in discussion with Risk Strats on proposed changes to the fallback rating treatment for IPO-related exposures, prompted by the potential for material underwriting-related exposure associated with the SpaceX IPO.
* The review is assessing whether the current fallback approach is overly conservative for newly listed issuers, given historical IPO credit performance, and whether a more risk-sensitive and scalable methodology can be supported through empirical analysis and validation.



Validation of the Probability of Default (PD) master scale model remains on track for completion next week.
    * Preliminary findings relate to calibration methodology, use of historical default data, and support for low-default portfolios, with remediation discussions underway with Risk Strats.
* Validation of the Corporate Industry Segment Internal Credit Rating (ICR) models is in progress.
    * MRM continues to review remediation evidence for prior findings and is assessing the impact of a recently identified data processing issue affecting model calibration outputs.
* Rule Compliance Review: Initial assessment has been completed for all 119 rules submitted for the PD master scale model; approximately 800 rules are expected to require MRM review as part of the broader IRB program.


Following the recently identified high-severity finding, MRM and Strats are progressing a broader remediation program to address longstanding limitations in the mortgage risk framework that have contributed to differences between desk and Risk Division risk measurements during periods of market volatility.
* Planned enhancements will be delivered in phases, with initial changes focused on improving prepayment modeling and subsequent work targeting mortgage rate modeling and related risk measurement methodologies.
* Enhanced monitoring has been established to track differences between trader and model risk estimates and support timely identification and escalation of material divergences.


Following the recently identified high-severity finding, MRM, Market Risk Strats, and Desk Strats are progressing a broader remediation program to address longstanding differences between trader views of mortgage risk and Risk Division measurements, particularly during periods of elevated market volatility.
* Desk Strats are planning a phased rollout of model enhancements. The first phase will focus on recalibration of the mortgage prepayment model, addressing an existing MRM finding, with submission expected by end-June. A second phase, targeted for Q3, will introduce enhancements to mortgage rate modeling.
* As an interim control, Strats have enhanced monitoring of trader versus model DV01 and will actively track divergences to enable timely investigation and remediation where needed.



Below is a draft with more detail on Q&A and less on presentation walkthrough.

1. Materials: AIRCC Materials dated June 9, 2026

2. Prism AI – Approval

The presenters provided an updated overview of Prism AI, following the committee’s prior review on June 2, 2026, where approval was deferred pending follow-up with Engineering and Technology Risk regarding implementation, MCP servers, and related controls. The presenters explained that Prism AI is intended to support GBM Public market synthesis and analytical finance use cases by combining LLM reasoning with Goldman Sachs proprietary data, licensed market data, real-time market information, economic data, and MCP-enabled tools. The presenters noted that the tool is designed to support internal market practitioners by generating analysis, reports, charts, and other artifacts to help contextualize market events and support decision-making.

Discussion focused heavily on output reliability, hallucination risk, evaluation metrics, and business-use safeguards. A committee member asked how the presenters would ensure hallucination risk is minimized, particularly given that users may make decisions based on Prism outputs. The presenters explained that they cannot guarantee there will be no hallucinations, but that they are seeking to reduce the risk through better context, higher-quality inputs, more constrained data access, and use of curated sources. The presenters noted that Prism does not currently perform open internet search and instead relies on controlled data sources, including approved APIs and identified sources of truth for market and economic data.

Committee members pressed further on hallucination risk and asked whether the team had quantitative data on the current level of hallucination. The presenters explained that the use case is more qualitative than traditional deterministic model outputs and that Prism is intended to support, rather than replace, user judgment. The presenters noted that they are developing an LLM-as-judge framework to break down outputs into falsifiable statements that can be checked against ground truth. The presenters indicated that they are targeting an 80% threshold for report-level evaluation and a higher threshold, approximately 90%, for atomic factual accuracy, such as specific market or economic data points.

Committee members challenged whether the proposed 80% threshold was sufficient and asked how the threshold had been determined. The presenters explained that the threshold was based on pre-go-live testing and sample reports reviewed to date, and that the objective is to improve the metric over time. Committee members noted that 80% may not be the right metric or threshold, particularly if the tool is being used to support decisions. Committee members further noted that a user may find the tool helpful even where accuracy is below a specific percentage, but that the relevant question is whether the tool enables better, faster, and safer decision-making.

A committee member summarized the concern that the discussion appeared to focus heavily on user satisfaction and qualitative usefulness, while the more important consideration may be the business outcome and the risk of bad decisions resulting from an imperfect tool. Committee members discussed that customer happiness alone may not be an adequate metric and that the evaluation framework should capture business value and decision-support quality, including whether users can identify when outputs should or should not be relied upon. Committee members also noted that the firm should move toward AI metrics that demonstrate value creation, time saved, decision acceleration, and improved outcomes, rather than relying only on accuracy or user satisfaction metrics.

Committee members recommended that the presenters establish a well-defined evaluation data set and objective evaluation framework. The presenters explained that they already have testing in place for factual accuracy, tool calls, and deterministic components, and that they are working with Model Risk Management on the broader evaluation framework. Committee members asked that the team identify an initial target user set, collect structured feedback from that pilot group, refine the relevant metrics, and develop a checkpoint to assess accuracy, usefulness, and business-value measures before broader rollout.

Committee members also asked whether Prism would be used externally or made available to clients. The presenters confirmed that Prism is an internal-only tool, intended for use by a limited population of sophisticated market practitioners, and not for publication through Marquee or external client access. The presenters further explained that users will be reminded that Prism is a decision-support tool, that outputs may contain errors or hallucinations, and that users must perform their own review before relying on the analysis.

Discussion also returned to technology and control items from the prior committee meeting. A committee member noted that Technology Risk and Engineering had completed a deeper review of the MCP servers and code execution approach. Engineering stated that, for the proposed pilot, there were no blockers from the MCP server review, subject to agreed remediation. Engineering noted that the current MCP server implementation should not be reused by other teams until it is refactored, reconciled with the MCP server registry, and reviewed under the standard process. Engineering also noted that any future expansion beyond the proposed GBM Public pilot would require the MCP-related action items to be completed.

Committee members also discussed the code execution sandbox. Engineering noted that the current implementation runs on-prem and that the team should migrate to the recommended cloud-based code execution approach, including Bedrock Agent Code Interpreter or another approved architecture. The presenters agreed to move the implementation to cloud by September 1, 2026, and noted that this migration was included in the remediation roadmap.

Technology Risk noted that penetration testing had not yet been completed and that any high or critical findings identified through that process would need to be remediated before pilot launch. Technology Risk also noted that certain findings had system-generated remediation dates, but that the expectation is for the team to complete several items earlier than those formal dates.

Committee members asked about the scope of the initial rollout. The presenters explained that the request is for a limited GBM Public pilot of approximately 300 to 500 users, with potential access for management committees or their nominees given senior stakeholder interest. Committee members noted concern that the proposal still relied heavily on intentions and future remediation, and asked whether the relevant evaluation and business-value metrics could be better defined before approval. One committee member stated that they were not comfortable signing off based on the current materials without clearer metrics and a better articulation of business value and decision-support safeguards.

The committee chairperson noted that Prism AI would be escalated to ARC given the level of senior management interest in the use case. The committee agreed to recommend escalation to ARC with a recommendation to approve, subject to conditions. The presenters were asked to complete and provide the agreed pre-go-live items, including penetration testing, user training and disclaimers, Technology Risk remediation items, and the MRM testing and evaluation summary.

The following pre-go-live conditions and follow-ups were recorded:

1. Complete penetration testing and remediate any high or critical findings before pilot launch
2. Provide a full summary of MRM testing and evaluation work, including the LLM-as-judge framework, factual accuracy metrics, and other evaluation criteria
3. Define the initial pilot user population and establish a structured process to collect user feedback and evaluate accuracy, usefulness, and business value
4. Provide appropriate user training and disclaimers regarding hallucination risk and user responsibility for reviewing outputs
5. Complete agreed Technology Risk remediation items, including MCP server refactoring, MCP server registry reconciliation, and cloud migration for code execution
6. Review any future expansion beyond the proposed GBM Public pilot with Engineering, Technology Risk, and relevant control functions before broader rollout

3. Administrative Matters

PIPG Data Insights – Posting

The secretary posted an update on PIPG Data Insights, a GBM Public Tier 3 model used by the Equities business. The presenter explained that the model was designed to analyze past Goldman Sachs quotes for equity structured products and available market information to identify similar products and predict quantitative values, such as potential client charges or pre-catch amounts.

The presenter noted that Model Risk Management identified significant performance issues during validation. Specifically, the model’s predictive performance was near zero in certain cases, with R-squared results close to or below zero, indicating that some outputs were effectively equivalent to a random number generator. MRM also observed instability in the results due to native LLM variability, including cases where the model identified different similar quotes across repeated runs of the same question. In addition, MRM benchmarked the generative AI approach against simpler methods and found that regression or machine learning approaches performed better for certain components.

As a result, MRM initially rejected the model and raised two high-severity findings. The presenter explained that the developers disabled the features that were not performing adequately, and MRM approved the final reduced-scope solution for production. A committee member asked how the developers improved the model’s accuracy from the initial poor performance. The presenter explained that the underperforming features were disabled and that the developers may explore regression or machine learning alternatives for those components in the future.

Membership Changes

The secretary noted that Sal had retired from the firm and, as a result, had left the committee.

Having no further business to discuss, the chairpersons closed the meeting.

To the extent transaction(s) were discussed, no committee member raised issues related to the transactions regarding any (i) material conflict of interest, (ii) material exposure to high-risk assets or high-risk trading strategies that could significantly increase the likelihood that the firm could incur a substantial financial loss, or (iii) activity that would otherwise pose a threat to the safety and soundness of the firm or the financial stability of the United States.




BRC Deck Changes

1. Remove detailed inventory / validation activity slides from BRC

There was broad agreement that the current BRC deck is too operational and detailed for Board-level reporting.

Proposed removals

Likely remove or significantly reduce:

* Inventory detail slides
* Approval status breakdowns
* Detailed validation activity pages
* Detailed findings aging charts
* Detailed RAS commentary pages

Specifically, they were referring to current “slides 6–8”.

The rationale was:

* SR 26-2 no longer explicitly emphasizes Board-level model risk reporting
* Board reporting should align with other risk domains
* BRC should focus on:
    * material model risk
    * aggregate trends
    * emerging risks
    * high-level indicators

There was repeated feedback that:

“Do we really need this level of detail for the Board?”

⸻

2. Do NOT fully eliminate aggregate inventory/finding information

Bill pushed back on removing too much.

Key message:

Model risk exists in the aggregate

He felt the Board still needs:

* some sense of scale
* inventory evolution
* findings flow
* model development trends
* what types of models are being added (especially AI)

So instead of deleting entirely, the direction is:

Replace multiple detailed slides with 1–2 high-level aggregate slides

Potential content:

* total model inventory trend
* new vs retired models
* findings opened vs closed
* inventory by major category/tier
* AI model growth
* high-level finding trends

But avoid:

* operational-level detail
* approval status minutiae
* excessive breakdowns

⸻

3. Focus on “flow” metrics instead of static snapshots

Bill specifically noted current charts miss the “story”.

Example concern:

“How did you get from 782 to 693?”

So recommended additions:

* models added / retired during period
* findings raised / findings closed
* net change
* trend over time

This was viewed as more meaningful than static inventory counts.



⸻

4. UK ICAAP Validation

Move from validation section into CRO update if material.

Potential bullet:

* Completed validation of UK ICAAP models supporting GSI, GSIB and GSGUK capital planning processes, including enhancements to stress calibration, LGD estimation and Basel 3.1 overlays.

⸻

5. NFA Model Risk Roundtable

Avoid regulatory-sounding headline.

Instead use:

Industry Engagement

* MRM participated in NFA model risk roundtable discussions covering model governance, initial margin model oversight, substituted compliance and supervisory expectations.

⸻

6. Significant Validation / Tier 1 Activity (New Theme)

David specifically asked for thematic summaries since quarter end.

Possible item:

Recent Significant Tier 1 Validation Activity

* Completed several significant Tier 1 validations and model enhancements across capital, market risk and treasury areas; preparing thematic summary of key risk management improvements and business impact.

⸻

7. GBM Topics (Need Input from Muyan / others)

Potential topics:

Profound Closure

David explicitly called this out as a success story.

* Completed closure of Profound related model work, resulting in release of associated capital requirements and resolution of longstanding model risk constraints.

SpaceX / IPO Activity

David wants investigation, not necessarily reporting yet.

Action:

* Check with GBM, Treasury, Securities and Commodities teams.
* Determine whether there are:
    * Liquidity model implications
    * IPO financing/stabilization modelling impacts
    * Risk measurement challenges

Potential future CRO item:

* Elevated IPO underwriting activity (including large transactions such as SpaceX) reviewed for potential liquidity and risk measurement implications; no material model risk concerns identified to date.

⸻

Strats Update

1. SIM IR Delta Backbone Change

Should appear in Strats as well.

Potential bullet:

* Production rollout completed for SIM IR Delta backbone methodology enhancement.
* Improved alignment between model sensitivities and observed risk exposures.
* Expected reduction in IM disputes and improved consistency of margin calculations.

⸻

2. TCM Migration / Front Bridge

Continue existing update.

Potential bullet:

* Front office migration to TCM framework continues. Remaining Tier 2 and Tier 3 findings are linked to migration activities and associated retirement of legacy models.

⸻

3. AI Landscape Discussion (Main Strats Topic)

David clearly wants a strategic discussion rather than individual model updates.

Requested framing:

Group together:

* Prism
* Compass
* Aurora
* Bumblebee
* BondNation / TBM-related chatbot tools
* Bobby AI

Question for management:

Why do we have multiple chatbot / market intelligence platforms with overlapping functionality?

Suggested update:

GBM AI Assistant Ecosystem

* Reviewed growing set of AI-enabled market intelligence and conversational assistant platforms across GBM (Prism, Compass, Aurora, Bumblebee, Bobby AI and related initiatives).
* Management discussion focused on platform differentiation, governance, development efficiency and long-term operating model.
* Requested greater clarity regarding target users, data sources, overlap in functionality and strategic positioning across platforms.

This is probably the item David most wants discussed with Alex.

⸻

4. Mortgage PST Issue

Mention in Strats only if there is material new information from Shipra.

⸻

5. IPO / SpaceX Theme

David actually broadened this beyond SpaceX.

Potential bullet:

* Reviewing implications of increased IPO and capital markets activity for model inventory, liquidity modelling and risk measurement frameworks.

⸻

Follow-ups Before Finalizing

Shipra

* Mortgage PST model issue status.

Muyan / GBM

* Profound closure details.
* Any SpaceX / IPO related model risk topics.
* Commodities developments (oil volatility, collateralized structures, long-dated options).

SIM Team

Gather numbers for:

* Old vs new delta sensitivities.
* IM reduction (~$300mm).
* Largest dispute counterparties.
* Estimated dispute reduction statistics.

Those are the items David seemed most interested in elevating for Alex. The SIM IR Delta backbone change and the AI platform landscape discussion are likely the headline items.




Based on the discussion, I would structure the updates as follows.

CRO Update

1. IRB Uplift Program (keep as recurring item)

Message: Continue providing progress update as Alex remains interested.

Potential bullet:

* IRB uplift program remains on track, including PD master scale enhancements and associated validation activities. Updated status and key milestones to be provided based on latest program progress.

2. Mortgage PST Model Issue (Shipra)

Action: Check with Shipra and keep as a standing update.

Potential bullet:

* Ongoing monitoring of mortgage PST model issue. Provide latest status, remediation progress, and expected timeline once confirmed with stakeholders.

⸻

3. SIM IR Delta Backbone Methodology Change (Major CRO Item)

This appeared to generate the most interest.

What they want:

* Update that methodology has gone live and been approved.
* NFA notification forthcoming.
* Include quantitative impact.

Suggested CRO bullets:

SIM IR Delta Backbone Enhancement

* Approved and implemented revised IR Delta backbone methodology for SIM calculations; NFA notification process underway.
* Change reduces overstated sensitivities and lowers posted/received initial margin requirements by approximately $300mm in aggregate.
* Analysis indicates expected reduction in client margin disputes, particularly among counterparties with historically large SIM disagreements.

Additional table requested


⸻

4. UK ICAAP Validation

Move from validation section into CRO update if material.

Potential bullet:

* Completed validation of UK ICAAP models supporting GSI, GSIB and GSGUK capital planning processes, including enhancements to stress calibration, LGD estimation and Basel 3.1 overlays.

⸻

5. NFA Model Risk Roundtable

Avoid regulatory-sounding headline.

Instead use:

Industry Engagement

* MRM participated in NFA model risk roundtable discussions covering model governance, initial margin model oversight, substituted compliance and supervisory expectations.

⸻

6. Significant Validation / Tier 1 Activity (New Theme)

David specifically asked for thematic summaries since quarter end.

Possible item:

Recent Significant Tier 1 Validation Activity

* Completed several significant Tier 1 validations and model enhancements across capital, market risk and treasury areas; preparing thematic summary of key risk management improvements and business impact.

⸻

7. GBM Topics (Need Input from Muyan / others)

Potential topics:

Profound Closure

David explicitly called this out as a success story.

* Completed closure of Profound related model work, resulting in release of associated capital requirements and resolution of longstanding model risk constraints.

SpaceX / IPO Activity

David wants investigation, not necessarily reporting yet.

Action:

* Check with GBM, Treasury, Securities and Commodities teams.
* Determine whether there are:
    * Liquidity model implications
    * IPO financing/stabilization modelling impacts
    * Risk measurement challenges

Potential future CRO item:

* Elevated IPO underwriting activity (including large transactions such as SpaceX) reviewed for potential liquidity and risk measurement implications; no material model risk concerns identified to date.

⸻

Strats Update

1. SIM IR Delta Backbone Change

Should appear in Strats as well.

Potential bullet:

* Production rollout completed for SIM IR Delta backbone methodology enhancement.
* Improved alignment between model sensitivities and observed risk exposures.
* Expected reduction in IM disputes and improved consistency of margin calculations.

⸻

2. TCM Migration / Front Bridge

Continue existing update.

Potential bullet:

* Front office migration to TCM framework continues. Remaining Tier 2 and Tier 3 findings are linked to migration activities and associated retirement of legacy models.

⸻

3. AI Landscape Discussion (Main Strats Topic)

David clearly wants a strategic discussion rather than individual model updates.

Requested framing:

Group together:

* Prism
* Compass
* Aurora
* Bumblebee
* BondNation / TBM-related chatbot tools
* Bobby AI

Question for management:

Why do we have multiple chatbot / market intelligence platforms with overlapping functionality?

Suggested update:

GBM AI Assistant Ecosystem

* Reviewed growing set of AI-enabled market intelligence and conversational assistant platforms across GBM (Prism, Compass, Aurora, Bumblebee, Bobby AI and related initiatives).
* Management discussion focused on platform differentiation, governance, development efficiency and long-term operating model.
* Requested greater clarity regarding target users, data sources, overlap in functionality and strategic positioning across platforms.

This is probably the item David most wants discussed with Alex.

⸻

4. Mortgage PST Issue

Mention in Strats only if there is material new information from Shipra.

⸻

5. IPO / SpaceX Theme

David actually broadened this beyond SpaceX.

Potential bullet:

* Reviewing implications of increased IPO and capital markets activity for model inventory, liquidity modelling and risk measurement frameworks.

⸻

Follow-ups Before Finalizing

Shipra

* Mortgage PST model issue status.

Muyan / GBM

* Profound closure details.
* Any SpaceX / IPO related model risk topics.
* Commodities developments (oil volatility, collateralized structures, long-dated options).

SIM Team

Gather numbers for:

* Old vs new delta sensitivities.
* IM reduction (~$300mm).
* Largest dispute counterparties.
* Estimated dispute reduction statistics.

Those are the items David seemed most interested in elevating for Alex. The SIM IR Delta backbone change and the AI platform landscape discussion are likely the headline items.




MRM completed validation of models used by GSI, GSIB, and GSGUK for ICAAP 2026.
* Key enhancements addressing MRM findings included updates to the Value-at-Risk stress calibration framework and the introduction of new provisioning models with collateral-specific Loss Given Default (LGD) estimates.
* Additional validated enhancements included a Basel 3.1 regulatory overlay, improvements to loss methodologies for commodity derivatives and equity swaps, and revisions to the residual risk add-on framework.




MRM attended the NFA Model Risk Roundtable in New York, which focused on governance expectations for approved Initial Margin and Capital models, including oversight of Risks Not in VaR (RNIV), model performance monitoring, and new product approvals.
* Key discussion topics included formalization of RNIV capitalization processes, governance expectations for model performance reviews, and efforts to streamline regulatory approval requirements for new products and model extensions.




• Model inventory grew by [X]% year over year, reflecting continued model development activity across the firm, particularly in [AI / Engineering / Risk Management].

• AI model inventory increased by [X]% year over year. Generative AI adoption continues to expand across business and control functions and remains an area of ongoing monitoring and governance focus.

• Validation findings inventory declined by [X]% year over year due to sustained remediation activity. Findings closure rates exceeded new findings raised during the quarter.

• Aggregate model risk remains stable. MRM continues to monitor emerging risks associated with [AI adoption / regulatory developments / model complexity], while maintaining all Model Risk Appetite metrics within approved thresholds.


Based on this discussion, Bill appears to be converging on a single aggregate inventory slide for BRC that focuses on trends and emerging risks rather than operational activity. The key changes are:

1. Remove Validation Activities / Model Approvals

Bill explicitly said:

“I don’t think showing model approvals is that interesting.”

Therefore:

❌ Remove:

* Validation activities
* Initial validations
* Annual reviews
* Revalidations
* Approval counts

These can remain in MRCC/FRAC reporting.

⸻

2. Keep Total Model Inventory as the Lead Metric

Top-left section should be:

Model Inventory

Show:

Quarter	Inventory	QoQ Change	YoY Change
2Q25	x		
3Q25	x		
4Q25	x		
1Q26	x	+x%	+x%

Add:

* New models
* Retired models

Potential format:

Quarter	Total	New	Retired

Bill specifically suggested:

show quarterly for a few years

rather than monthly.

⸻

3. Add Dedicated AI Inventory Section

This was one of the strongest pieces of feedback.

Bill said:

AI inventory is where it’s more interesting to show change

you’ll see big growth

show a longer trend

New section:

AI Model Inventory

Show:

Quarter	Total AI	GenAI	Non GenAI

and/or

Stacked bar chart:

* Tier 1
* Tier 2
* Tier 3

Bill specifically wanted:

✅ Growth trend

✅ Tier breakdown

✅ Longer history

Potential title:

AI Inventory Growth

⸻

4. Findings Stay

Bill agreed findings remain relevant.

Keep:

Validation Findings

By severity:

Quarter	Sev 1	Sev 2	Sev 3

or

Open findings trend over time.

Again:

* Quarterly
* QoQ
* YoY

rather than monthly.

⸻

5. Add Commentary / Highlights Box

Bill liked the idea of narrative commentary.

Instead of approval statistics, add a small callout box.

Example:

Key Inventory Developments

• AI inventory increased 18% QoQ driven by growth in GenAI applications across Engineering and GBM.

• Total inventory remained stable with new model development largely offset by retirements.

• Validation findings remained within historical ranges with no material change in severity profile.

This seems exactly what Bill was asking for.

⸻

6. Focus on Trends, Not RAS

Important nuance:

You suggested:

everything within threshold

Bill pushed back:

This isn’t about RAS metrics.

The commentary box should discuss:

* inventory changes
* AI growth
* findings trends
* emerging themes

not whether metrics are green.

RAS already has a separate page.

⸻

Proposed BRC Inventory Slide

Aggregate Model Risk Profile

Top Left

* Total Inventory Trend (quarterly)
* New / Retired Models
* QoQ and YoY changes

Top Right

* AI Inventory Trend
* GenAI vs Non GenAI
* Tier breakdown

Bottom Left

* Validation Findings Trend
* Severity breakdown
* QoQ and YoY changes

Bottom Right

* Key Inventory Developments / Emerging Trends
    * AI growth
    * notable inventory shifts
    * findings themes
    * emerging risk observations

This aligns closely with the broader direction discussed for SR 26-2 and the revised BRC reporting approach: high-level aggregate model risk indicators, trends, and emerging risks rather than operational validation activity.



introduces the use of a fine-tuned generative LLM to extract sentiment from Japanese-language analyst research.




The enhancement extends FinBERT coverage to Japanese equities by incorporating local analyst research and a fine-tuned Qwen 2.5 32B large language model (LLM), replacing the traditional transformer-based approach used in the existing framework.



Resource summary

Area	Resource Need	Key Points
DRC	Manageable with current resources	Mostly low to moderate effort. Need to confirm coverage because several people who worked on prior DRCs have left. Avoid concentrating work on one person.
FRTB-CVA	Meaningful resource pressure	Full validations needed for several CVA engines, each likely requiring 2–3 months from a validator. Key person risk around Piyush, especially for engines, tradable uplift, and aggregator knowledge. Aggregator work still needs an identified owner.
FRTB Market Risk	Highest resource demand	Existing resources likely sufficient through August, but Q4 may need 1–3 additional people. Pressure comes from core models, Hermes 10-day, SBM / Greek stability testing, and competing Significant 2 reviews.

Short management summary

DRC appears manageable with existing resources, subject to confirming validator availability and avoiding single-person concentration. FRTB-CVA has more acute key-person risk, particularly around Piyush and the aggregator work. FRTB Market Risk is expected to require the highest level of resources, with current capacity likely sufficient near term but potential need for 1–3 additional validators in Q4.






MRM validation is in progress for Prism AI (GBM Public, Tier 2), an agentic AI assistant that supports traders with market research, trade ideas, and scenario analysis.
* MRM has identified findings related to information leakage through agent memory, segregation between agent-generated and production code environments, and agent behavior resulting in inaccurate responses; remediation is underway.
* AIRCC deferred approval of Prism AI pending follow-up with Engineering Platform and Technology Risk on sandbox implementation, Model Context Protocol (MCP) server governance, and completion of the Technology Risk review before returning to the committee for further consideration.




MRM approved enhancements to FinBERT (EAWM, Tier 2), extending the model’s coverage to Japanese equities within the existing sentiment analysis framework.
* FinBERT is used by Quantitative Investment Strategies (QIS) to generate daily sentiment signals from analyst research, which serve as inputs to equity portfolio construction and risk attribution models.
* The enhancement introduces a Japanese-language methodology using analyst reports from local providers and a fine-tuned Qwen 2.5 32B large language model (LLM) to generate sentiment scores for Japanese stocks.



Yes. The comment is valid because the current draft could be interpreted as saying that liquidity/concentration effects are always handled outside the pricing model through separate VAs, which is not strictly true. In some cases, conservatism is implemented directly within the pricing framework through parameter adjustments or payoff modifications.

I would revise the paragraph as follows:

The pricing models themselves do not generally incorporate liquidity or concentration considerations as part of their model performance assessment framework. Instead, these risks are typically addressed through valuation adjustments (VAs) applied on top of model generated valuations. These adjustments are determined and reviewed by Controllers and are subject to periodic reassessment and governance processes. For example, additional reserves may be applied to reflect liquidity considerations, concentrated exposures, or other market specific risks not captured directly by the pricing model.

In certain cases, where a conservative valuation adjustment can be represented through model parameters or payoff features, the adjustment may be incorporated directly into the pricing framework. Examples include barrier shift valuation adjustments and call date write off adjustments for Bermudan products. Such adjustments remain subject to the same governance, review, and periodic reassessment processes as other valuation adjustments.

Model performance is assessed through standard validation and ongoing performance monitoring processes, including sensitivity analysis, benchmarking, and outcomes analysis. In addition, all Tier 1 models are subject to Regression Testing (“RegTest”), a suite of automated tests designed to assess ongoing model performance. The tests are implemented as computer code (“test scripts”) and are run daily through an automated RegTest management system. Any failures are reported to model developers, with persistent failures escalated through governance channels, including to MRM.

This version preserves the original message while acknowledging the exception for model-integrated VAs and tying them back to the same governance framework.



3. AskHCM – Approval

The presenters provided an overview of AskHCM, a chat-driven interface intended to serve as a digital front door for HCM-related inquiries. The presenters explained that employees currently interact with HCM through self-service tools, help lines, and direct outreach to HCM personnel, and that AskHCM is intended to provide a unified conversational interface for a range of HCM self-service activities. The presenters noted that the initial rollout would be limited to approximately 1,100 HCM full-time employees and would support a defined set of use cases, including personal information updates, employment verification letters, vacation and absence inquiries, and related HCM workflows.

Committee members asked whether the pilot would include all HCM employees globally, including China. The presenters clarified that AskHCM is delivered through GS AI Assistant and therefore would not be available in mainland China, where GS AI Assistant is not currently available.

The presenters described the system architecture, including an orchestration layer that receives user requests and determines whether a query should be fulfilled through an HCM MCP service, responded to directly, or escalated to a live HCM support agent. Committee members asked whether the orchestration agent had been trained and how routing decisions are made. The presenters explained that the orchestration behavior is governed through prompts, contextual guidance, and routing instructions rather than model training. The presenters further noted that significant effort had been devoted to defining how the orchestrator handles different query types, including sensitive requests, unsupported use cases, escalation scenarios, and employee frustration, to ensure consistent routing and user experience.

Discussion also focused on data access and entitlements. The presenters explained that AskHCM operates using the end user’s authentication token and does not rely on a privileged system account with broad access to HCM data. As a result, users can only access and act upon information that they are already entitled to view. For the initial pilot, this limits users to querying and updating their own information rather than accessing information relating to other employees.

Committee members asked about the MCP integrations supporting the use case. The presenters explained that the solution connects to Oracle HCM and other HCM systems through MCP services that support activities such as personal information updates, vacation and leave management, and generation of employment verification letters. The presenters further explained that a live-agent handoff capability has been incorporated to allow conversations to be escalated to HCM personnel when required.

Discussion then focused on testing and validation. The presenters described a multi-layer testing approach consisting of automated agent evaluation, product testing, functional testing, business UAT, and MRM validation. Committee members asked how the automated evaluation framework operates. The presenters explained that they developed a judge-based evaluation framework that assesses responses across criteria including fidelity, faithfulness, integrity, compliance, safety, and quality. The presenters noted that approximately 175 test cases were used to validate the evaluation framework and that the framework will also support ongoing monitoring and drift detection after deployment.

Committee members asked about bugs identified during testing and the readiness of the solution for deployment. The presenters explained that testing identified a combination of AI-related issues and traditional functional defects, including prompt interpretation issues and implementation defects in supporting workflows and widgets. The presenters noted that all critical and high-severity issues had been remediated and retested, while the remaining open items were medium- and low-severity issues that were not considered blockers for rollout.

The presenters also described the post-go-live monitoring framework. The presenters explained that the automated evaluation framework will be used on an ongoing basis to monitor model performance and that access to full prompt histories will be restricted to a limited group of authorized HCM personnel for investigation, compliance, employee relations, and service improvement purposes. The presenters noted that the pilot is intended to inform a broader rollout across the firm later in the year.

The committee approved AskHCM for the initial pilot deployment to HCM employees.


Committee members asked detailed questions regarding the Prism context framework, including how institutional market knowledge is stored, how the LLM accesses context, whether memory and retrieval structures are developer-defined, and how context is retrieved at runtime. The presenters explained that Prism stores market knowledge, user context, prior thread history, analytical guidance, and market intelligence in a structured hierarchy of markdown-based context files and supporting data stores. Committee members specifically questioned whether the system was creating self-organizing memory structures or graph-based representations. The presenters clarified that the storage hierarchy, retrieval pathways, and available tools are predefined by developers and exposed through MCP services.

Committee members further explored the runtime execution process, including how the model determines which context to access and which tools to invoke. The presenters explained that the model is provided with guidance on the overall structure of the context framework and uses a “progressive disclosure” approach, retrieving additional context only as needed rather than loading all available information at once. The model can determine which predefined tools and context sources to access based on the user query, but it operates within a developer-defined framework and does not autonomously create new memory structures or retrieval pathways. The presenters therefore characterized the current implementation as semi-deterministic, with predefined storage and retrieval structures combined with LLM-driven navigation and tool selection at runtime.


Committee members asked detailed questions regarding the Prism context framework, including how institutional market knowledge is stored, whether the system creates and manages its own memory structures, how context is retrieved, and whether retrieval behavior is deterministic. The presenters explained that Prism stores market knowledge, user context, prior thread history, and analytical guidance in a structured hierarchy of markdown-based context files. The LLM accesses this information through MCP tools that expose both the context files and associated retrieval functions. Committee members specifically questioned whether the system was building self-organizing memory or graph structures and whether it was independently determining how information should be stored and retrieved. The presenters clarified that the storage structure and retrieval pathways are predefined by developers and that the LLM navigates those structures using guidance contained within the framework. While retrieval is not entirely deterministic because the LLM determines which context to access based on the user request, the underlying memory organization remains developer-defined and controlled. The presenters therefore characterized the current implementation as semi-deterministic rather than a fully autonomous memory architecture.


Recent approvals include:

• Surveillance AI for Unusual Movement of Assets (UMA) (Compliance, Tier 1), which applies the previously approved insider trading surveillance framework to AML transaction monitoring and is expected to suppress approximately 35% of false-positive alerts while maintaining a recall rate of approximately 97.5%; the tool also provides investigators with AI-generated research summaries that are expected to reduce average review time from 26 to 19 minutes per alert

• Code Review Assistant (Engineering, AI Platform), approved for an initial rollout, which reviews GitLab code changes and provides comments and summaries to support human reviewers as increasing AI-generated code volumes place greater pressure on existing code review processes

• AskHCM (HCM, Tier 3), approved for an initial pilot to approximately 1,100 HCM employees, which enables employees to obtain support for selected HCM self-service activities through an AI-powered interface capable of answering queries and executing approved HCM workflows using the employee’s existing entitlements

• Prism AI (GBM Public, Tier 2), an agentic AI platform intended to support market synthesis, research, and analytical finance use cases by combining LLM reasoning with market data, firm data, and MCP-based tools
– AIRCC discussion focused on MCP governance, code execution sandbox controls, architecture, and information security requirements
– Approval was deferred pending completion of Tech Risk review and resolution of architecture, MCP registry, and sandboxing follow-up items




1. Materials: AIRCC Materials dated June 2, 2026

2. Prism AI – Approval Deferred

The presenters provided an overview of Prism AI, a GBM Public use case intended to support market synthesis and analytical finance workflows by combining LLM reasoning with firm data, market data, MCP tools, and a limited Python execution environment. The presenters noted that the initial target population would be approximately 300 to 500 GBM users, with any broader rollout expected to return to the committee.

Discussion focused on the architecture, MCP implementation, Tech Risk review status, and execution environment. Committee members asked whether the MCP servers had been registered through the appropriate MCP registry and whether they would be deployed in the production registry before rollout. The presenters explained that the current implementation was running in a developer sandbox and that the plan was to migrate to production after AIRCC approval. Committee members clarified that production rollout should use the production MCP registry and that MCP servers should go through the required Tech Risk review before launch. A follow-up was recorded to align with Engineering and Tech Risk on MCP registry and review requirements.

Committee members also asked about outstanding Tech Risk findings. Tech Risk noted that its review had recently been completed or was in the process of being finalized, and that certain baseline controls, including TLS and on-behalf-of token handling, still required review or remediation. Committee members noted that any higher-risk or baseline-control issues would need to be addressed before go-live.

Discussion then focused on the Python / code execution sandbox. Committee members asked where the infrastructure was running and how code execution was isolated. The presenters explained that the sandbox was currently running on an on-prem machine with limited network connectivity and restricted read / write access. Committee members noted that the firm’s AI security standards include specific requirements for sandboxed code execution and suggested that the team consider approved cloud-based or containerized execution environments rather than an on-prem DC setup. A follow-up was recorded to review the sandboxing approach with Engineering and Tech Risk.

Committee members asked several questions regarding the Prism context framework, including how market knowledge is stored, how the LLM accesses context, and whether memory / retrieval is deterministic. The presenters explained that Prism uses context files and markdown-based guidance to capture institutional knowledge, user context, prior thread history, and market information, which the LLM can access through MCP tools. The presenters clarified that the current structure is predefined and semi-deterministic, rather than a fully self-organizing memory or graph structure.

Committee members also asked whether the MCP server itself contains an LLM. The presenters clarified that the LLM sits outside the MCP server through the GS AI platform, and that the MCP server exposes tools and context to the LLM. Committee members noted that this architecture should be more clearly reflected and reviewed as part of the follow-up.

Given the remaining open questions and the pending Tech Risk review, the committee deferred approval of Prism AI. The item is expected to return to the committee after the team addresses the architecture, MCP registry, Tech Risk, and sandboxing follow-ups. Committee members also noted that the use case is expected to be referred to ARC given the level of interest in the topic.

The following follow-ups were recorded:

1. Confirm MCP server registration and production MCP registry requirements before rollout
2. Complete Tech Risk review and address baseline control issues, including TLS and on-behalf-of token handling
3. Review the code execution sandbox approach with Engineering and Tech Risk, including use of approved cloud or containerized sandboxing
4. Clarify the Prism architecture, including MCP server boundaries, LLM interaction, context retrieval, and memory structure
5. Return to AIRCC for further review once the above items are addressed

3. AskHCM – Approval

The presenters provided an overview of AskHCM, a chat-based interface intended to serve as a digital front door for HCM-related queries. The presenters explained that the initial rollout would be limited to approximately 1,100 HCM full-time employees, and that the tool would initially support a defined set of straightforward use cases such as personal information updates, employment verification letters, vacation / absence inquiries, and related HCM self-service workflows.

Committee members asked whether the pilot would include all HCM employees globally, including China. The presenters clarified that AskHCM is delivered through GS AI Assistant and therefore would not be available in mainland China, where GS AI Assistant is not available.

Discussion focused on data access, entitlements, and the protection of sensitive HCM information. The presenters explained that the tool uses the end user’s authentication token and does not rely on a privileged system account with broad access to HCM data. The presenters further clarified that users in the initial pilot would only be able to query or act on their own information, and would not be able to access information about other employees or direct reports.

Committee members asked about the scope of HCM system integrations. The presenters explained that AskHCM connects through back-end MCP services to Oracle HCM and other HCM systems, including homegrown systems for vacation tracking, timesheets, and employment verification. The presenters noted that the MCP services support specific approved workflows and that live-agent handoff is available where a query requires escalation or human support.

The presenters discussed the testing and validation approach, including automated agent evaluation, product testing, functional testing, business UAT, and MRM validation. A committee member asked how the automated judge-based evaluation worked. The presenters explained that they first validated the judge framework using approximately 175 test cases and then used the framework to assess responses across criteria such as fidelity, faithfulness, integrity, compliance, safety, and quality. The presenters noted that this framework would also support ongoing monitoring and drift detection.

Committee members asked about bugs identified during testing. The presenters explained that testing identified a range of issues, including prompt / interpretation issues and functional implementation bugs. The presenters noted that all critical and high-priority issues had been closed and retested, and that remaining open items were medium or low priority and not viewed as blocking for go-live.

The presenters also discussed post-go-live monitoring. The presenters explained that the automated testing framework would be used periodically after launch and that prompt review would be restricted to a small group of senior HCM employees where review is required for investigations, compliance, employee relations, or service optimization. The presenters noted that lessons from the HCM-only pilot would inform a potential broader firmwide rollout later in the year.

The committee approved the AskHCM use case for the initial HCM employee pilot.

4. Use of Personal Data in GS AI Assistant – Posting

The secretary posted that the committee chairpersons had approved the use of personal data in GS AI Assistant on behalf of the committee. The secretary noted that this follows the limited AWM rollout approved last year, the establishment of rules on use of personal data in the AI Standard, and implementation of a new guardrail intended to detect misuse of personal data.

A committee member asked whether the control is implemented at the API back end or at the web UI level. The secretary explained that the posting relates to use of GS AI Assistant in the UI and that the current terms of use restriction on personal data is being lifted. Legal and Compliance further explained that updates to the AI Standard address responsible use of personal data across AI tools and helped support removal of the restriction in GS AI Assistant, together with the detective control.

5. Administrative Matters

Use of Personal Data in GS AI Assistant Extension Approval was posted to the committee, as described above.

Having no further business to discuss, the chairpersons closed the meeting.




The pricing models themselves do not explicitly incorporate liquidity or concentration considerations as part of their model performance assessment framework. Model performance is assessed through the standard validation and ongoing monitoring processes, including benchmarking, sensitivity analysis, stress testing, and periodic model reviews.

Liquidity and concentration risks are addressed separately through valuation adjustments (VAs) applied on top of model-generated valuations. These adjustments are determined and reviewed by Controllers and are subject to periodic reassessment and governance processes. For example, additional reserves may be applied to reflect liquidity considerations, concentrated exposures, or other market-specific risks not captured directly by the pricing model.

Evidence supporting model performance can be provided through the model validation documentation, annual review reports, and ongoing performance assessments, which include backtesting (where applicable), sensitivity analysis, stress testing, and other model monitoring activities. While there is no dedicated model performance metric specifically measuring the impact of liquidity and concentration, these risks are captured through the firm’s valuation adjustment framework and associated monitoring processes.


AI Risk and Controls Committee (AIRCC)

* AIRCC reviewed risks associated with personal agents in GitHub Copilot, including unintended access by non-engineers and potential bypass of maker-checker controls.
    * Follow-up actions include access remediation, governance enhancements, strengthened monitoring, and a postmortem assessment of the incident.
* AIRCC approved Prism AI (GBM Public, Tier 2), an agentic AI assistant that supports traders with market research, trade ideas, and scenario analysis.
    * Model validation remains in progress, with remediation underway for findings related to agentic AI controls, security, and reliability.
* AIRCC approved Surveillance AI for Unusual Movement of Assets (UMA) (Compliance, Tier 1), which automates review of transaction monitoring alerts that would otherwise require human investigation.
    * The model leverages the same framework previously approved for insider trading surveillance, with enhancements tailored to anti-money laundering use cases.
* AIRCC reviewed the Code Review Assistant (Engineering, AI Platform), an agentic tool designed to support software code reviews by generating comments and review summaries.
    * Future enhancements include performance measurement, structured reviewer feedback, and additional controls to improve review quality and effectiveness.

    MRM is supporting the transition from the AI Risk and Controls Committee (AIRCC) to the newly established AI Risk Council (ARC), including updates to governance documents, operating protocols, and committee responsibilities.
* Several AI governance initiatives, including non-engineer access to developer AI tools, personal AI agents, and enhanced controls for agentic AI, are being transitioned to ARC for further review and oversight.






The presenters explained that, although manager approval controls were in place, a follow-up engineering control intended to remove or restrict access for non-engineers had not been implemented as expected, resulting in continued access for a non-trivial number of users over an extended period of time.



This follow-up primarily came from Dmitri’s comments around making reviewer feedback more systematic and measurable, rather than relying on open-ended acknowledgements. Dmitri specifically suggested constraining reviewer responses through standardized labels or categories so the firm could better track review outcomes, evaluate effectiveness over time, and improve observability of the code review process. The discussion was further reinforced by Una’s point that structured responses would make it easier to distinguish whether observations were substantively addressed versus simply acknowledged.


Yes — that follow-up primarily came from Mike and Dmitri, with some reinforcement from Una. The underlying concern was that the current workflow only requires users to “acknowledge” comments, which makes it difficult to systematically evaluate whether review comments were meaningfully addressed.

The clearest transcript support is here:

“The more we constrain the language of these feedbacks and the types of labels that we use … the more systematic we become and the more explicit we are in the types of labels that we want the people and the programs themselves … to use.”

and:

“I would encourage the team to think about … what are the types of labels that we would like to associate with every single merge request? What do we think is going to be most informative and how do we want to track that over time.”

Also from Una:

“if you have a comment, then using AI it should be pretty easy to determine … is it like a positive ACK or is it a negative … it would help us to capture more systematic feedback.”

So I would rewrite the follow-up to make the intent clearer and tie it more directly to the discussion:

Explore more structured reviewer feedback mechanisms, including standardized labels or categorized responses to assistant observations, to improve observability, evaluation, and tracking of how review comments are addressed over time



Identified a high-severity finding in the mortgage pass-through pool pricing model, with remediation increasing risk limit utilization and prompting broader enhancements to the mortgage risk framework


CCAR – Net Interest Income (NII) Modeling: MRM is closely coordinating with developers and CCAR Controllers on planned enhancements to explicitly project interest income and expense, with model submissions targeted for May 27 and validation completion targeted for August 7.
    * The enhancements, originally planned for CCAR 2026, are expected to materially increase projected pre-provision net revenue (PPNR) under both internal and supervisory stress scenarios, driven by refined interest-earning balance modeling and updated assumptions for gross credit mark-to-market revenue projections.




During the weekly touchpoint with CCAR Controllers, regulators continued to focus on the private equity beta change used in internal scenarios, including the appropriateness of using unrealized mark-to-market data from external vendors to support the selected beta assumptions.


The overlay remediates the portion of the associated validation finding related to the GCLA repo rollover assumption, while a new medium-severity finding will track strategic systemization of the fix within the model framework.


* MRM approved an overlay for the DESCIFR Maximum Liquidity Outflow (MLO) model (Tier 1) to address a deficiency identified during validation of the new Global Core Liquidity Account (GCLA) repo monetization framework.
    * The deficiency related to inconsistent treatment of GCLA repo rollover assumptions between liquidity models, resulting in overstated inflows and understated MLO outflows.
    * The overlay remediates the associated validation finding, while a separate finding will track strategic systemization of the fix.
* MRM has started reviewing enhancements to the Long-Term Stress Test (LTST) model (Tier 1), which assesses liquidity outflows under prolonged stress scenarios.
    * Enhancements received to date include additional backtesting using recent stress events, recalibration of market and behavioral outflows, and updates to mitigating action assumptions related to liability raising activities.
    * The proposed enhancements are intended to address an existing validation finding.





Key PRA IRB milestones remain on track, including delivery of the Corporate segment IRB models and remediation evidence for Internal Credit Rating (ICR) findings due this week, ahead of the planned PRA submission in September 2026.
* Validation of the Probability of Default (PD) master scale model remains on track, with any material findings requiring remediation prior to submission expected to be communicated over the coming week.
* Validation of the remaining IRB models, including the Large Corporate ICR and PRA IRB models, remains targeted for completion by end-August.
* MRM has completed an initial assessment of 57 of the 119 second-line rule compliance submissions related to the PD master scale model.



AIRCC approved the Code Review Assistant, an agentic tool designed to support GitLab code reviews and help reduce increasing human review burden amid growing AI-generated code volumes and larger merge requests, with discussion focused on reviewer capacity, effectiveness metrics, structured feedback mechanisms, and opportunities to enhance review consistency and control coverage across the SDLC
* AIRCC approved Surveillance AI for Unusual Movement of Assets (UMA), an AML surveillance use case leveraging agentic workflows to reduce false positives and assist investigators with alert summaries, with testing indicating ~35% reduction in false positives while maintaining recall above risk tolerance thresholds, and with follow-ups on jurisdictional restrictions, prompt tuning terminology, and potential parallel-run implementation prior to production rollout
* AIRCC reviewed risks relating to the use of personal agents in GitHub Copilot, including unintended access by approximately 2,600 non-engineers and potential bypass of maker-checker controls, with discussion focused on access remediation, governance gaps, server-side controls, and monitoring enhancements, and with follow-ups to return to the committee with a postmortem, issue assessment, and remediation plan


MRM approved and released the model remediation on May 22 for the high-severity finding related to incorrect treatment of pool price floors under shocked scenarios.
* The remediation resulted in increased utilization of IR +50bps and CSW top sheet risk limits, with temporary limit increases approved by Market Risk through July 17.


ETSC is observing increased use of AI coding assistants, primarily GitHub Copilot, in development of electronic trading control code across Fixed Income and Equities businesses.
    * Increased use of AI-assisted development has led to more instances where AI-generated code introduced bugs, omissions, or extraneous tests that were not identified during development review.
    * As part of recent review work, ETSC identified high-severity control deficiencies in a European corporate bonds auto-quoting migration, including missing quote size checks and inaccurate risk exposure control logic.
    * ETSC is deploying internal AI-based code validation tools to support the increased validation workload associated with AI-assisted development.
* ETSC approved U.S. Rates bilateral price streaming, a new electronic trading activity for U.S. Treasury bond liquidity provisioning.
    * All high-severity control findings related to data staleness validation, position consistency checks, and exposure controls were remediated prior to approval



ETSC is observing increased use of AI coding assistants, primarily GitHub Copilot, in development of electronic trading control code across Fixed Income and Equities businesses.
    * AI-assisted development has accelerated code delivery and increased documentation, testing, and code review automation, but ETSC has also observed instances where AI-generated code introduced control deficiencies that were not identified during development review.
    * As part of recent review work, ETSC identified and remediated high-severity control issues in a European corporate bonds auto-quoting migration, including missing quote size checks and inaccurate risk exposure control logic.
    * ETSC is deploying internal AI-based code validation tools to support the increased validation workload associated with AI-assisted development.
* ETSC approved bilateral price streaming for U.S. Treasury bond liquidity provisioning, with several high-severity control findings remediated prior to approval.
    * Remediated issues included data staleness checks for pricing references and limits, position consistency checks between pricing and risk systems, and exposure controls for unavailable risk positions or limits.



The presenters agreed to return to the committee with additional detail on the issue, including the postmortem, proposed remediation actions, and governance approach for personal agent usage. The following follow-ups were recorded:

1. Implement controls to prevent additional non-engineer access pending remediation
2. Assess and remediate existing non-engineer access to personal agent tooling
3. Review whether any activity performed through personal agents requires additional quality assurance, investigation, or escalation
4. Confirm proposed server-side and lifecycle-management controls for personal agents
5. Return to the committee with the postmortem, issue severity assessment, and remediation plan



Below is a draft in the refined AIRCC minutes style.




	Committee members also asked how the robustness and consistency testing was performed. The presenters explained that the agents are run three separate times against the same data set, prompts, and system configuration in order to measure consistency of outcomes. Committee members specifically asked how often the three runs produced divergent results. The presenters explained that, for positive cases that would be escalated by compliance investigators, the robustness score was approximately 95%, meaning that the three runs produced consistent outcomes approximately 95% of the time. The presenters noted that the robustness testing methodology is currently under review by Model Risk Management.

⸻

1. Materials: AIRC Materials dated May 26, 2026

2. Surveillance AI for Unusual Movement of Assets (UMA) – Approval

The presenters provided an overview of the request to approve Surveillance AI for Unusual Movement of Assets (UMA), the firm’s anti-money laundering transaction monitoring surveillance. The presenters noted that the use case follows the same general framework and control approach previously approved for Surveillance AI for insider trading surveillance, with differences driven by the AML-specific agents, data sources, and alert review process.

Discussion focused on how the AI would support the existing UMA workflow. The presenters explained that the surveillance currently generates approximately 1,300 alerts per week and that investigators spend approximately 26 minutes reviewing each alert. The proposed use case is expected to reduce false positives and provide narrative summaries to help investigators review alerts more efficiently.

Committee members asked whether the same model and evaluation approach used for insider trading surveillance would be used for UMA. The presenters explained that the current implementation uses Gemini 2.5 Pro, with different prompts and test sets tailored to the AML use case. The presenters clarified that the evaluation methodology, including precision, recall, predicate-based summary evaluation, and robustness testing, is consistent with the prior insider trading surveillance use case. A committee member noted that future model deprecation should be monitored, and the presenters confirmed that the model pipeline would be rerun before any model transition.

The presenters explained that UMA uses several agents, including client and counterparty research, transaction analysis, e-communications, decision, and validation agents. Committee members asked about the use of e-communications data and jurisdictional restrictions. The presenters explained that the e-communications agent is used to identify information relevant to the purpose of transactions where such communications are available, and that the use case is undergoing privacy review, including a DPIA. In response to questions regarding Switzerland, China, and other jurisdictions, the presenters explained that Swiss surveillance is separate and not in scope for this launch, and that China and certain other jurisdictions would not be included. A follow-up was noted to confirm any additional country exclusions pending the DPIA.

Committee members asked how the human review process would work. The presenters explained that compliance investigators would remain in the loop and would receive the agent-generated summary, reasoning, and links to the underlying data used by the agents. The presenters confirmed that this approach is consistent with the insider trading Surveillance AI use case, with the human investigator responsible for reviewing and dispositioning the alert.

Committee members asked about the expected reduction in alert volume and review time. The presenters explained that testing over approximately two years of historical alerts indicated that the model could suppress approximately 35% of false positives while maintaining recall of approximately 97.46%, above the applicable 95% benchmark. For alerts that continue to be sent to compliance investigators, the presenters stated that average review time is expected to decrease from approximately 26 minutes to approximately 19 minutes based on testing.

Committee members asked for clarification on language in the materials referring to the model being “trained.” The presenters clarified that the use case does not involve training a frontier model and that the work relates to prompt tuning and evaluation. A follow-up was noted to update the materials accordingly.

Committee members also asked whether the use case would include a parallel run before production launch. The presenters explained that a parallel run had been used for the insider trading surveillance launch because it was the first Surveillance AI use case in Compliance, and that the team was discussing whether to use the same approach for UMA. Committee members indicated that a parallel run would be appropriate, and a follow-up was recorded.

The committee approved the Surveillance AI for UMA use case. The following follow-ups were recorded:

1. Update the materials to refer to prompt tuning / evaluation rather than model training
2. Confirm country exclusions and DPIA-related restrictions before launch
3. Confirm whether a parallel run will be conducted before production launch

3. Code Review Assistant – Approval

The presenters provided an overview of the Code Review Assistant, an agentic tool designed to review code changes in GitLab and provide comments and summaries to support human reviewers. The presenters noted that the tool is intended to help address increasing code review demand as use of AI coding tools increases the volume and size of merge requests. The presenters also noted that the human reviewer remains responsible for final approval.

Discussion focused on the control rationale for the tool. Committee members noted that, as AI coding tools increase code generation, human review may become a bottleneck and there is a risk that reviewers may not be able to review all generated code with the same level of rigor. The presenters explained that the Code Review Assistant is intended to provide an additional control by giving reviewers a consistent package of observations and context before approval.

Committee members asked whether the tool would apply only to code generated by Devin or more broadly. The presenters explained that an Internal Audit commitment specifically relates to agentic commits from Devin, but that the tool is expected to have broader value across code generated by humans and other AI coding assistants, including GitHub Copilot and Claude Code.

Committee members asked whether the increase in lines of code and merge requests was driven by AI tools. The presenters explained that AI tools appear to be increasing developer velocity and the size of units of change, although more precise metrics are still being developed. Committee members suggested tracking lines of code per reviewer and other measures to understand whether review burden is increasing in a way that could create control risk.

Committee members asked what the tool does and whether it could approve, reject, or modify code. The presenters clarified that the tool is advisory only and cannot approve, reject, or modify code. It reviews merge requests, adds inline comments and summaries, and provides observations to the author and reviewer. The human reviewer must still review and approve the merge request through the existing software development lifecycle process.

Committee members asked how comments raised by the assistant would be resolved and whether there is quality assurance over those resolutions. The presenters explained that comments must be acknowledged or resolved in the merge request workflow, but acknowledged that users could potentially provide low-quality responses. Committee members discussed whether additional controls could be added, including requiring more structured responses, using an additional agent to assess whether comments were adequately addressed, or performing sample-based testing after the fact.

Committee members asked whether the assistant provides alternative code that could be copied by users. The presenters explained that the tool is expected to provide qualitative review comments rather than acting as a code generator, reducing concern that users would copy code from the reviewing agent without adequate scrutiny.

Committee members asked whether the assistant has access only to the merge request or to the broader repository context. The presenters explained that the assistant receives the merge request, the relevant diff, and broader repository context through a code graph, enabling it to assess how the proposed change fits within the code base. Committee members noted that this broader context is important to avoid false comfort from a narrow review of only the incremental change.

Committee members challenged the reported 70% efficacy metric and asked how it should be interpreted. The presenters explained that the metric was based on pilot review of assistant observations and reflected whether comments were viewed as true positive observations. Committee members noted that the metric needed clearer definition, benchmarking, and a more systematic approach to evaluation. The presenters agreed that additional work is needed to define and scale evaluation, including through check-and-challenge using separate models and ongoing AI observability.

Committee members emphasized that this use case is important given the expected scale of AI-generated code and the central role of code review controls. Committee members encouraged the team to develop more structured labels and feedback mechanisms so that reviewer responses can be analyzed consistently over time. Committee members also noted that the tool should be rolled out carefully but promptly, as it is itself an important control to support increasing AI-assisted development.

The committee approved the Code Review Assistant use case. The following follow-ups were recorded:

1. Develop a more systematic approach for evaluating assistant performance and defining efficacy metrics
2. Explore structured feedback / labels for reviewer responses to assistant observations
3. Consider additional controls, including interactive review assistance and broader context augmentation

4. Use of Personal Agents in GitHub Copilot – Posting

Technology Risk provided a posting on the use of personal agents, focused primarily on GitHub Copilot agent mode and the potential for such agents to bypass intended maker-checker controls. The discussion noted that the issue relates to use of approved tooling in ways that may not align with the scope of prior committee approvals or the intended control design.

Committee members asked whether the issue was limited to engineers or also involved non-engineers. The presenters explained that access had not been removed from certain non-engineers as intended, and that approximately 2,600 non-engineers had used the tooling. The presenters noted that analysis indicated a distinction between users with superficial usage and users more heavily invested in the toolkit, and that the team was considering aggressive removal of access for users with limited usage while separately assessing the population with more meaningful usage.

Committee members asked how non-engineers were able to use the tool if the approval was limited to engineers. The presenters explained that a control expected to revoke access for non-engineers had not been executed for a non-trivial period of time. The presenters stated that a postmortem is being prepared and that the team would return to the committee with the results and proposed remediation.

Committee members emphasized that immediate controls should be implemented to prevent the population from growing while remediation is developed. The presenters agreed that the onboarding / approval process should be addressed promptly and that additional controls may be needed, including second-level approval or separation-of-duty controls.

Discussion covered proposed remediation actions, including removing inappropriate access, ensuring personal agents are developed and used through approved lifecycle management, updating applicable standards and guidance, enforcing server-side controls to block certain high-risk actions such as payment approvals or production code merges, and enhancing monitoring to detect inappropriate usage.

Committee members asked how the issue would be documented and rated. The presenters stated that an issue would be raised, likely as a high severity issue, and that the severity would be reviewed with appropriate stakeholders rather than relying solely on the calculator output. Committee members noted that the matter is significant and expected to receive senior management attention.

Committee members also asked whether there would be a review of what affected users had done with the tool. The presenters agreed to assess available data and determine whether any activity occurred that would require further quality assurance or escalation. Committee members clarified that the review should not be limited to malicious activity, but should also consider activity inconsistent with expected use or requiring additional control review.

The presenters agreed to return to the committee with the postmortem, issue rating, immediate access remediation plan, and any additional proposed controls.








B
Area

Rule / Program

Model / DRC ID

Model / DRC Name

Status

Change Type

Scope of Work

Complexity

Developer Target Date

Expected MRM Validation Timing

MRM Lead

Resource Need / Constraint

Key Risk / Comment

DRC

Basel III / Fed capital rules

TBD

Credit risk DRC 1

Existing

Update / additional validation

Confirm rule compliance and assess changes

Low / Medium

Aug / Sep

TBD

TBD

TBD

Timeline may change depending on Fed implementation date

DRC

Basel III / Fed capital rules

TBD

Operational risk RWA DRC

New

New validation

Validate new deterministic calculation

Medium

Aug / Sep

TBD

TBD

TBD

New DRC, but not expected to be highly complex

FRTB-CVA

Fed / PRA

TBD

CVA desk-pricer model

New

New validation

Extend desk engine for capital use, including gap risk and other capital-specific requirements

High

End of Q2

Q3 estimate

TBD

Potential bandwidth issue

Major validation effort; likely needs multiple validators

FRTB-CVA

Fed / PRA

TBD

Equity CVA engine / Marco aggregation

New / modified

New validation / methodology review

Assess use of equity simulation with Marco aggregation logic

High

TBD

TBD

TBD

TBD

Extra review needed due to linkage between two engines

FRTB-CVA

PRA-heavy

TBD

SA-CVA aggregator

Existing

Additional validation

Validate rule changes / deterministic aggregation

Medium

TBD

TBD

TBD

May need PRA-side support

Rule-based but still requires review

FRTB Market Risk

Fed / PRA

TBD

Risk factor migration

Existing

Infrastructure migration

Confirm output reconciliation and code migration controls

Low

TBD

~1 week per risk factor

TBD

TBD

Methodology already validated; focus is implementation

FRTB Market Risk

Fed / PRA

TBD

10-day compounding risk factor

Existing / new

Methodology validation

Validate 10-day compounding methodology where not previously covered

Medium

TBD

~4–6 weeks

TBD

TBD

Timing may be affected by development back-and-forth

FRTB Market Risk

Fed / PRA

TBD

Core models, e.g. Hermes 10-day

New / modified

New validation

Validate new / modified core capital models

High

Late / TBD

TBD

TBD

Potential resource issue

Late developer delivery may create validation pressure

FRTB Market Risk

Fed / PRA

TBD























ulk Transaction Waiver Summary

Desk

SPG – Equity Derivatives

Trade

Daily Crash Put – Fixed Share with Notional Cap and Bilateral OET

Waiver Scope

Bulk waiver covering up to USD 3bn aggregate notional

Reference Waiver

Enhancement to previously approved waiver #11290 (strike-cap version of the payoff)

Example Counterparties

D. E. Shaw, Morgan Stanley, Qube

Underliers

Korean single stocks, including:

* 000660.KS
* 005930.KS

Indicative Trade Details

• Trade Type: 6m Daily Crash Put – Fixed Share
• Indicative Notional: ~USD 100m per trade
• Maturity: 3m / 6m / 1y
• Premium: ~4–7% annualized, paid upfront
• Settlement: TRS settlement upon exercise
• OET: Bilateral / Unbreakable

⸻

Trade Description

The structure is a fixed-share daily crash put designed to hedge the desk’s Jump-to-Default (JTD) exposure.

Key features include:

* Daily strike reset at 55% of previous closing price
* Fixed-share exposure subject to a 130% notional cap
* The payoff transitions from fixed-share to fixed-notional if the underlying rallies sufficiently
* GS holds a one-time exercise right, after which the trade terminates
* Bilateral Optional Early Termination (OET) rights apply, with reimbursement payments amortizing over time following notice

Indicative payoff:

\text{Min(Fixed Shares × } S_{t-1}, \text{ Max Notional)} \times \text{Max(Strike % − } S_t/S_{t-1}, 0)

For bilateral OET:

* booking flags reflect bilateral termination rights and notice periods
* the option is priced assuming effective expiry at PD + notice period
* reimbursement payments amortize through PD + 30d

⸻

Reason for Waiver

The current implementation supports:

* fixed-share crash puts with strike caps

but does not yet support:

* fixed-share structures with notional caps, or
* bilateral OET reimbursement mechanics with linear amortization

As a result, enhancements are required to:

* correctly model the transition from fixed-share to fixed-notional exposure following rallies
* support reimbursement scheduling and booking flags associated with bilateral OET rights

⸻

Proposed Booking During Waiver Period

• Trades will initially be booked using the existing strike-cap version of the payoff
• The notional-cap enhancement will be implemented within approximately 2 weeks
• For bilateral OET events:

* reimbursement payments will be settled manually
* a replacement trade will be booked reflecting the applicable notice period

⸻

Compensating Controls

The desk noted that the existing EqSP CMS Linked Note framework correctly captures the crash and gap risk profile until the notional cap threshold is breached.

During the waiver period:

• The current approved implementation captures the core crash-put payoff mechanics and downside exposure profile
• Residual risk relates primarily to the transition from fixed-share to fixed-notional exposure once the cap is reached
• Bilateral OET reimbursement flows will be operationally managed through manual settlement and rebooking procedures
• The structure remains subject to explicit notional caps, limiting exposure growth following underlying rallies
• Trades are short-dated (3m–1y), reducing long-horizon model uncertainty
• The waiver applies only to an enhancement of an already approved strike-cap framework rather than a new payoff type

⸻

Remediation Plan

• Release an updated version of the EqSP CMS Linked Note supporting:

* notional cap mechanics
* bilateral OET functionality
* reimbursement amortization logic

by the trade booking date

• Submit the full enhanced model to MRM by the end of the week in which the trade is booked




CRO Updates

IRB / ICR Program

* Validation of the Corporate Industry Segment Internal Credit Risk (“ICR”) models is underway following receipt of the latest submissions last week
* MRM highlighted progress on the Independent Review Process (“IRP”) program, including ongoing second-line reviews across submitted model packages and continued execution against agreed timelines
* The team discussed emphasizing more concrete execution progress in reporting, including completed second-line reviews and closure of initial documentation gaps for recently submitted models
* As part of the broader IRB program, MRM continues to progress Article 185-related workstreams and associated governance reviews

SR 26-2 / Regulatory Guidance

* MRCC reviewed the recently issued SR 26-2 interagency guidance and implications for model risk governance and reporting
* Discussion focused on the continued applicability of model risk management expectations to quantitative methods and electronic trading algorithms despite the shift toward a more principles-based framework
* The team plans to reference industry and regulatory FAQ language clarifying that electronic trading and quantitative methods remain within scope of supervisory expectations
* Consider combining SR 26-2 and broader industry/regulatory conference themes into a single regulatory update section

Mortgage PST Model Issue (Top of Mind)

This was clearly identified as a major discussion topic and should likely be elevated into a “Top of Mind” item rather than a routine validation update.

Suggested framing:

* MRM approved the Preventative Change Control (“PCC”) related to the mortgage PST model issue, with production deployment pending
* The issue prompted broader work to address longstanding limitations in the mortgage risk framework where desk views of risk and risk division measurements have diverged during periods of market volatility
* The agreed remediation plan includes material enhancements to the underlying risk methodology, governance, and limit framework to improve consistency in risk measurement and escalation
* The program is expected to require a multi-month implementation effort, with ongoing updates to be provided as milestones are completed
* Management emphasized the importance of eliminating recurring disputes regarding risk representation during stressed market conditions

Validation / Model Activity Updates

IOSD Model Changes

* Material IOSD model enhancements are expected to complete next week, addressing an existing MRM finding and resulting in material model impact

Long-Term Stress Testing

* Recent approvals related to long-term stress testing methodologies were completed

Counterparty Credit Risk (“CCR”)

* MRM approved enhancements to Agent Lender Disclosure (“ALD”) repo treatment within the Interest Rate franchise benchmark framework
* The changes build on prior enhancements and address an outstanding validation finding

CCAR / Regulatory Engagement

* The team discussed potential inclusion of preliminary CCAR-related supervisory feedback received from the Federal Reserve
* Discussion noted that some findings may move toward soft closure in the coming months, though updates should remain focused on model-specific implications

ETSC / AI-Assisted Coding Controls

This was viewed as a potentially important emerging risk theme.

Suggested CRO framing:

* MRM discussed recent observations related to AI-assisted software development within electronic trading environments
* A recent migration exercise using AI coding assistance identified several control weaknesses, including missing trading controls and implementation logic errors
* The discussion highlighted increasing model and operational risk considerations associated with AI-generated code and the need for enhanced governance and testing standards as AI-assisted development expands
* Management noted the broader challenge of determining how AI-assisted coding oversight should be incorporated within existing model risk and AI governance frameworks

BAU / Findings

* Several high-severity findings were remediated and closed during the period
* Simplify wording and focus on closure/remediation outcomes rather than detailed operational descriptions

⸻

Strats Updates

Mortgage Model Risk Issue

* Include the mortgage PST issue here as well given relevance to trading risk measurement and desk-limit interactions
* Emphasize:
    * ongoing remediation effort
    * enhancements to fundamental mortgage risk modeling
    * alignment between desk and independent risk measurement
    * expected multi-phase implementation timeline

CCR Findings / Metrics

* One CCR-related finding is expected to close shortly
* However, separate findings tied to the same broader control area may continue to pressure thresholds due to timing and implementation dependencies

AI / AIRCC Updates

* AIRCC updates include approval activity related to AIR Hub and Agentic Slang AI
* GBM updates include extensions to machine learning trade score / quoting models
* Discussion also covered broader firmwide AI governance restructuring and integration of AI oversight responsibilities into a centralized governance framework

AI-Assisted Development Controls

This should probably appear in Strats as well because the example originated from trading technology activity.

Suggested wording:

* Recent reviews of AI-assisted development activity identified examples where AI-generated code introduced control deficiencies and implementation errors within trading-related workflows
* Findings included missing control logic and incorrect implementation behavior, reinforcing the importance of enhanced testing and governance for AI-assisted software development

Regulatory / Exam Activity

* Ongoing market risk management examination activity continues, including extensive requests for model and validation documentation
* Team discussed continued supervisory focus on quantitative methodologies and trading model governance

General Direction / Tone Feedback from Bill

A major theme from the discussion was that updates should:

* move away from purely “work in progress” language
* emphasize completed milestones and tangible progress
* include clearer statements on execution status and outcomes
* elevate major strategic/remediation themes (especially mortgages and SR 26-2 implications) rather than listing only operational updates




Counterparty Credit Risk (CCR): MRM approved enhancements to the Interest Rate Franchise Benchmark model (GBM Public, Tier 1) to improve allocation of Agent Lender Disclosure (ALD) repo haircuts between Agent Lender and Principal Lender entities for Treasury Execution Services (TES) and short-term interest rate trading activities.
* The enhancement builds on prior changes that mapped ALD repo exposures to the underlying collateral level, improving accuracy of shortfall calculations and addressing a validation finding.


Here are the key takeaways and recommended changes from the discussion, separated into BRC deck changes and policy changes.

BRC Deck Changes

1. Remove detailed inventory / validation activity slides from BRC

There was broad agreement that the current BRC deck is too operational and detailed for Board-level reporting.

Proposed removals

Likely remove or significantly reduce:

* Inventory detail slides
* Approval status breakdowns
* Detailed validation activity pages
* Detailed findings aging charts
* Detailed RAS commentary pages

Specifically, they were referring to current “slides 6–8”.

The rationale was:

* SR 26-2 no longer explicitly emphasizes Board-level model risk reporting
* Board reporting should align with other risk domains
* BRC should focus on:
    * material model risk
    * aggregate trends
    * emerging risks
    * high-level indicators

There was repeated feedback that:

“Do we really need this level of detail for the Board?”

⸻

2. Do NOT fully eliminate aggregate inventory/finding information

Bill pushed back on removing too much.

Key message:

Model risk exists in the aggregate

He felt the Board still needs:

* some sense of scale
* inventory evolution
* findings flow
* model development trends
* what types of models are being added (especially AI)

So instead of deleting entirely, the direction is:

Replace multiple detailed slides with 1–2 high-level aggregate slides

Potential content:

* total model inventory trend
* new vs retired models
* findings opened vs closed
* inventory by major category/tier
* AI model growth
* high-level finding trends

But avoid:

* operational-level detail
* approval status minutiae
* excessive breakdowns

⸻

3. Focus on “flow” metrics instead of static snapshots

Bill specifically noted current charts miss the “story”.

Example concern:

“How did you get from 782 to 693?”

So recommended additions:

* models added / retired during period
* findings raised / findings closed
* net change
* trend over time

This was viewed as more meaningful than static inventory counts.

⸻

4. Keep Executive Summary

No proposed changes to Executive Summary structure.

They explicitly said:

“We keep the executive summary the same as before”

⸻

5. RAS metrics remain in BRC

Important clarification:

* RAS metrics are NOT being removed
* only detailed commentary and supporting operational slides may be streamlined

⸻

6. Simplify BRC RAS presentation

Directionally:

* collapse tiers together more aggressively for Board reporting
* less granular than FRAC/MRCC

Discussion leaned toward:

* grouping Tier 1/2/2+/3 together
* potentially only emphasizing Tier 1 at Board level
* avoiding excessive rows/zeros

The guiding principle:

Board should focus on material risk

⸻

Policy Changes

1. Do NOT materially rewrite the policy

This was the biggest conclusion.

Initially they proposed adding explicit language that:

* BRC reporting only includes:
    * material model risks
    * emerging risks
    * significant trends
    * aggregate indicators

But after discussion, Bill noted:

* current wording is already somewhat ambiguous
* adding new language may unintentionally imply a substantive policy reduction

So the final direction was:

Minimal policy change approach

Likely:

* retain existing first paragraph
* add only a narrow clarifying statement
* avoid major rewrite

This aligns with your manager’s earlier “minimal approach” comments.

⸻

2. Clarify that detailed requirements apply to FRCC/MRCC/FRAC, not necessarily BRC

This became the core policy clarification.

Current issue:

* policy wording ambiguously suggests all detailed inventory/finding requirements also apply to BRC

Proposed fix:

* clarify that detailed operational reporting requirements apply to:
    * FRC
    * MRCC
    * FRAC

while BRC receives higher-level reporting.

This is probably the most important actual policy change.

⸻

3. Align policy language with firmwide risk reporting standards

They explicitly referenced Ross’s firmwide risk reporting policy.

Goal:

* ensure model risk reporting follows the same Board reporting principles as other risk domains

Meaning:
Board reporting should emphasize:

* aggregate risk profile
* material issues
* trends
* emerging risks

not operational process metrics.

⸻

Additional Non-BRC Policy / Standards Discussions

These were side discussions but likely actionable later.

4. Potential future streamlining for Tier 2 / Tier 3 standards

Ideas discussed:

* lighter documentation requirements
* lighter findings standards
* possibly reducing Sev3 findings on Tier 2/3 models

No decisions yet.

⸻

5. Electronic Trading Controls wording

They discussed removing wording implying MRM validates electronic trading controls themselves.

New direction:

* MRM verifies control validation occurred
* but does not itself perform/control-validation ownership

This reflects stronger independent ET governance now existing elsewhere.

⸻

6. PCC / Annual Review philosophy

Important strategic theme:

* encourage more PCC/pre-approval review
* reduce heavy retrospective annual review burden

Key message:

ongoing incremental review is more efficient than year-end accumulation

No immediate policy change proposed, but likely future direction:

* incentivize lower-tier developers to use PCC more frequently
* potentially lighten annual review burden when ongoing PCC exists

⸻

Overall Direction / Executive Interpretation

The meeting direction was essentially:

Move BRC reporting toward:

* strategic
* aggregate
* trend-focused
* material-risk-focused

Move away from:

* operational detail
* inventory mechanics
* validation process statistics
* granular findings reporting

But:

avoid making the policy rewrite look too aggressive or like a weakening of oversight.

That “minimal-change but practical streamlining” theme came up repeatedly.





Please see below talking points for the board deck, can you please help write it better. Simplify the last bullet a bit

* Utilization for model risk metrics remained within thresholds during the period
* There are no significant concerns to highlight with respect to model risk

* Key drivers of ongoing validation work relate to continued growth in the use of Al across the firm, strategic enhancements to support counterparty credit risk management capabilities as part of ongoing harmonization efforts for shortfall benchmark models, reducing stress losses and improving backtesting performance, collateralized lending business that extend model coverage to reduce reliance on fallback methodologies and enhance data inputs and methodologies to improve model accuracy, and formation of Domestic Liquidity SubGroup (DoLSub) to support the firm's application for PRA approval to manage GSI and GSB liquidity on a consolidated basis



Modelers agreed with the findings and will retain limited generative AI functionality for lightweight summary and recommendation features, while exploring quantitative regression or traditional machine learning approaches for GC prediction.


    Key drivers of ongoing validation activity include continued growth in AI use cases across the firm, strategic counterparty credit risk model enhancements to support shortfall benchmark harmonization and improve backtesting performance, collateralized lending model enhancements to expand model coverage and improve methodologies and data inputs, and Domestic Liquidity Sub-Group (DoLSub) model changes supporting the firm’s PRA application to manage GSI and GSIB liquidity on a consolidated basis



    The model will continue to use limited generative AI functionality for lightweight summary and recommendation features.


MRM approved an extension to the neural network-based TradeScore Quoting Model and X-Asset Utility Quoter (GBM Public, Tier 2) to support Brazilian swap quoting for the LatAm Interest Rates algo trading business.
    * The enhancement enables the algo trading model to incorporate TradeScore order fill probability estimates into quoting decisions to optimize execution outcomes.
* MRM rejected the PIP AI Agent model (GBM Public, Tier 3), a generative AI model intended to predict structured trade charges (Gross Credit, GC) based on historical trade configurations and charges, due to insufficient predictive performance.
    * MRM analysis identified significant prediction noise and lack of predictive power, partly driven by LLM output variability.
    * Modelers agreed with the findings and acknowledged that a quantitative regression or traditional machine learning approach would likely be more appropriate for the use case.




The first version of AIRHub is now live, digitizing the AIRCC intake, review, and approval workflow.
* Pilot AI use cases are being onboarded over the coming weeks, with planning for Phase 2 enhancements currently underway.



MRM raised a high-severity finding on the Mortgage PST Pool Pricing model (GBM Public, Tier 1) related to the treatment of the price floor, which may understate risk due to inconsistent handling of duration and option-adjusted spread (OAS) shocks between pools and reference to-be-announced (TBA) securities.

MRM raised a high-severity finding on the Mortgage PST Pool Pricing model (GBM Public, Tier 1) related to an implementation issue in the application of pool price floors relative to reference to-be-announced (TBA) securities.
* The remediation is expected to increase utilization of the IR +50bps Topsheet risk limit, and a proposal for a temporary limit increase is under discussion; Strats have also enhanced desk reporting to include trader risk estimates for monitoring purposes.
* MRM is working with Strats to assess model-related drivers contributing to the discrepancy between model and trader DV01 estimates.



PRA Internal Ratings-Based (IRB) Approach Uplift: Development and validation timelines for the PRA IRB submission are being finalized between MRM and Risk Strats, with validation of the Corporate industry segment Internal Credit Rating (ICR) models targeted for completion by mid-July and remaining IRB models by end-August, ahead of PRA submission in September 2026.

* Validation of the PD master scale model is in progress, with initial documentation gaps identified during review and subsequently addressed by Risk Strats.
* Timelines for second-line regulatory compliance review are also being finalized.


PRA Internal Ratings-Based (IRB) Approach Uplift: Validation of the Probability of Default (PD) model is underway, with initial documentation gaps identified during review and subsequently addressed by Risk Strats.

* Submission of the Corporate industry segment Internal Credit Rating (ICR) models feeding into the PD model is expected this week, with MRM validation targeted for completion by end-June.
* Remaining submissions, including the Large Corporate ICR model and PRA Corporate / Large Corporate Industry IRB models, are targeted from end-May to end-June, with validation expected from mid-July to mid-August ahead of PRA submission in September 2026.





PRA Internal Ratings-Based (IRB) Approach Uplift: Corporate Internal Credit Rating (ICR) model submission from Risk Strats is expected this week, with MRM validation targeted for completion by [June/July 2026] ahead of the planned PRA submission in September 2026.

* Validation of the overarching Probability of Default (PD) model is in progress, with initial documentation gaps identified during review and subsequently addressed by Risk Strats.
* Significant work remains ahead of PRA submission, including validation of the revised Corporate and Large Corporate ICR models, remediation of validation findings, and completion of supporting regulatory documentation and governance processes.



CCR aged validation findings are nearing resolution, with one remaining finding related to backtesting breaches.
* Additional issues were identified during remediation review, including insufficient stress ratios and limited drilldown capabilities for Commodities backtesting breach analysis; MRM is working with Strats to finalize a remediation plan, which remains the final dependency for closure.





The main changes/comments to the deck from this discussion are:

* Reuse the Agentic AI “Top Focus Area” / emerging risk content that was removed last time, as the group agreed it is still an appropriate top focus area for MRM
* Update wording in the AI approval bullet to clarify this is the “first use of a transformer-based neural network” rather than just “neural network”
* Keep CCR and Collateralized Lending updates at a higher level for the BRC deck rather than including detailed model-level descriptions
* Add/update the liquidity summary bullet to mention completion of Phase 1 model changes
* Refresh all inventory/activity/finding/RAS numbers with final automated production figures, while noting minor changes may still occur after reconciliation checks
* Circulate additional detail supporting the large increase in model inventory activity, especially:
    * High number of Tier 1 declarations (~31)
    * Large volume of new model declarations and deactivations
    * Breakdown showing many Tier 1 additions relate to ICR/risk models
* Prepare historical trend analysis (last 8–12 quarters) for:
    * New model declarations
    * Tier 1 model additions
    * Deactivations
        This was requested to determine whether current inventory growth is a trend or a one-time spike
* No immediate changes to the BRC deck structure tied to SR 26-2/new guidance yet; discussion deferred to the broader workstream
* Include SR 26-2/revised guidance discussion in the dedicated regulatory update slide only (already sent to the Direct team)

Most concrete edit requested:

* Revise the executive summary AI bullet language:
    * Replace “first use of a neural network” with “first use of a transformer-based neural network”


Committee members also asked whether the tool could be rolled out to users in Hong Kong given existing restrictions relating to certain AI models. The presenters explained that, while Slang AI defaults to Anthropic models for most users, Hong Kong users would automatically be routed to Gemini models instead, with Anthropic models excluded based on existing entitlements and geographic restrictions.


Committee members also asked about the anticipated size of the user base and how adoption would compare to other coding assistant tools used across the firm. The presenters noted that the current Slang AI chatbot has approximately 2,500 weekly users and estimated that the enhanced agentic version could ultimately be used by approximately 4,000 SecDB developers. The presenters further noted that, while expected to be widely adopted within the Slang developer community, the user base would likely remain smaller than broader firmwide coding assistant tools such as Claude Code and GitHub Copilot.



The presenters walked through the scope of the proposed agentic capabilities, noting that Slang AI can assist with development workflows by writing code, generating tests, running linting tools, reviewing logs, and preparing code reviews. A committee member asked what types of “execution” the tool could perform and whether approval by a developer could cause the tool to make a production change. The presenters explained that execution refers to development activities such as running tests or linting code, and clarified that Slang AI operates only in Safe Mode. The presenters further explained that the tool cannot directly update SecDB databases, check code into CVS, or push code to prod source. Any code generated by Slang AI would remain subject to the same software development lifecycle controls as human-developed code, including human approval, code review, and any applicable MRM review for model code changes.

Committee members asked about beta testing results and areas where the tool did not perform as expected. The presenters explained that testing identified code hallucinations, where the model could propose Slang functions or names that do not exist. In response to a committee member’s question on whether this issue had been mitigated, the presenters explained that Slang AI was updated to check Slang syntax and lint code before presenting proposed changes to users. The presenters noted that this has reduced the issue, although results remain non-deterministic given the nature of LLMs. Committee members noted that these issues appeared more likely to create user frustration than direct control risk, given that experienced Slang users can identify incorrect outputs and code changes remain subject to human review and existing development controls.

Committee members also asked whether the tool performs differently for more complex or idiosyncratic code, including graph code. The presenters explained that Slang AI performs well for explaining existing graph code, although code generation for graph-related use cases remains an area for further refinement with the developer community. The presenters noted that Slang-specific best practices and tribal knowledge are being incorporated into skills and prompts to improve output quality. Discussion also covered code reuse, with the presenters noting that the model initially tended to write new code even where existing libraries could be extended. The presenters explained that mitigants were added to require the tool to search for existing Slang code before proposing new code, and that feedback from beta users had already resulted in improvements to skills and tooling.





Below is a revised draft in the more summary-oriented AIRCC minutes style.

⸻

1. Materials: AIRC Materials dated May 12, 2026

2. Agentic Slang AI – Approval

The presenters provided an overview of the request to expand the previously approved Slang AI use case to include agentic functionality. The presenters noted that Slang AI was initially approved in August 2025 as a Q&A-based assistant for SecDB and Slang developers, and that the proposed enhancement would allow the tool to take actions in support of developer workflows while remaining within existing user sessions and entitlements.

Discussion covered the rationale for the enhancement, including the need to support developer productivity within a controlled environment. A committee member asked whether the risk of developers using less controlled alternatives outside the intended environment was theoretical or tangible. The presenters explained that developers could use other approved tools or hand-rolled workflows in ways that are not necessarily prohibited but may sit outside the control framework originally envisioned for SecDB and Slang use cases. Committee members noted that this should be further considered as controls and engagement protocols continue to evolve.

The presenters walked through the scope of the proposed agentic capabilities, noting that the tool can assist with activities such as writing code, generating tests, running linting tools, and preparing code reviews. In response to questions regarding execution risk, the presenters clarified that Slang AI operates only in Safe Mode and cannot directly update SecDB databases or push code to production. The presenters further explained that code changes remain subject to the same software development lifecycle controls as human-developed code, including human approval, code review, and any applicable MRM review for model code changes.

Committee members asked about beta testing results and areas where the tool did not perform as expected. The presenters noted that testing identified issues such as code hallucinations and a tendency for the model to generate new code where existing libraries could be reused. The presenters explained that mitigants were added to prompt the model to check Slang syntax, lint code before presenting it to users, and search for existing code before proposing new code. Committee members noted that these issues appeared more likely to create user frustration than direct control risk, given human review and existing development controls, but emphasized the importance of continued monitoring.

Discussion also covered the tool’s handling of graph code, proprietary Slang practices, and community feedback from beta users. The presenters noted that the tool performs well for code explanation and that quality is expected to improve as additional Slang-specific skills, prompts, and best practices are incorporated. The presenters also noted that feedback from the beta testing community had already resulted in improvements to skills and tooling.

Committee members discussed entitlement and access risks. The presenters explained that Slang AI inherits the user’s existing read entitlements within the user’s SecDB session, while Safe Mode prevents write activity. A committee member noted that inherited entitlements may have different implications for senior developers with broader access, and asked whether the agent could use those entitlements outside SecDB. The presenters explained that such actions would require human approval and that additional controls could be introduced quickly if specific risks are identified. Committee members asked the presenters to further review sandboxing and entitlement-related controls.

The presenters summarized key risk mitigants, including human approval for write or execute actions, audit logging of agent activity, use of the GS AI Platform gateway, source validation to prevent unauthorized invocation, and the ability to restrict or disable functionality. Committee members also asked about kill switches and monitoring. The presenters explained that kill switches exist both at the GS AI Platform level and within the Slang AI implementation, and that the tool can also be moved back to a non-agentic planning mode.

Committee members challenged the proposed monitoring threshold for triggering escalation or disabling functionality, noting that a 50% threshold appeared low for an agentic tool compared with a chatbot. The presenters explained that the threshold was initially carried over from the prior version of Slang AI, but acknowledged that a higher threshold may be appropriate given current beta results and the additional actions enabled by the agentic workflow. A follow-up was recorded to revisit the threshold.

The committee approved the expansion of Slang AI to include agentic functionality. The following follow-ups were recorded:

1. Revisit the monitoring threshold used to determine escalation, plan mode, or kill switch invocation
2. Review sandboxing and entitlement-related controls, including whether additional constraints are needed for agentic activity

3. Administrative Matters

The secretary presented changes to the Firmwide Policy on Artificial Intelligence, the Firmwide Standard on Artificial Intelligence, and the Committee Charter. The secretary noted that the changes were made following the recent discussion on the revised remit of the AI Steering Group, now the AI Strategy Group, and primarily remove references to the prior AISG from roles and responsibilities sections.

Since no objections were raised, the following documents were approved:

* Firmwide Policy on Artificial Intelligence
* Firmwide Standard on Artificial Intelligence
* Committee Charter

Having no further business to discuss, the chairpersons closed the meeting.


Such reporting should be consistent with the Firmwide Policy on Risk Reporting and provide an aggregate view of the Firm’s Model Risk profile, including material Model Risks, significant trends, and emerging risks, as appropriate.





The CRO provides periodic reporting to the BRC on the Firm’s Model Risk profile at scheduled meetings, which occur at a minimum of four times per year. BRC reporting should focus on material Model Risks, significant trends and emerging risks, key regulatory developments, and aggregate Model Risk indicators relevant to the Board’s oversight responsibilities.

The Head of the MRM group is responsible for reporting to the FRC, MRCC, and FRAC at least quarterly on significant Model Risks from individual Models and in aggregate. Reporting to senior management committees may include more detailed operational, inventory, validation, and remediation-related information, as appropriate to the responsibilities of each committee. The frequency of reporting to any other senior management committee is stipulated by such committee.

The MRM group should provide an overall assessment of aggregate Model Risk and changes in the Model Risk profile based on relevant risk indicators, thematic analysis, and related trends, which may include the following:

* Model Risk Appetite metrics:
    * Performance of Model Risk metrics against tolerances established by the BRC
* Model inventory and risk profile:
    * Summary information regarding the Model Inventory, including material changes, risk assessments, concentrations, and trends
* Model validation activities and findings:
    * Summary of significant validation findings, including compensating controls, overdue remediation items, and assessment of impact at both the individual Model and aggregate levels
    * Summary of material validation activities, including initial validations, annual reviews, and revalidations
* Other Model Risk indicators:
    * Significant Policy or Standards exceptions, associated risks, compensating controls, and remediation plans
    * Status of significant Model Risk-related regulatory or Internal Audit findings
    * Significant updates to Model Risk governance, policies, or standards
    * Other relevant items, which may include results of self-assessments, training initiatives, or resource updates



Based on the discussion, the main implication of SR 26-2 for the Model Control Policy / standards is not a fundamental governance overhaul, but rather a simplification and clarification of Board-level reporting expectations under a more risk-based approach.

The key edits/themes appear to be:

1. Simplify BRC Reporting Requirements

This was the clearest action item from the discussion.

Current issue:

* Existing policy language appears overly prescriptive for Board Risk Committee (BRC) reporting
* It explicitly requires detailed inventory tables, findings, waivers, blessed models, tier breakdowns, etc.
* This creates “pages and pages of zeros” and excessive operational reporting burden

Direction of change:

* Move detailed operational reporting expectations down to MRCC / FRAC level
* Keep BRC reporting higher-level, focused on material risk themes, trends, and significant issues

Likely policy edit:
Instead of saying BRC receives detailed inventories/findings metrics, revise language to something like:

“BRC reporting includes material model risk themes, significant emerging risks, key regulatory developments, and aggregated model risk metrics, while more detailed operational reporting is provided to MRCC and FRAC.”

Or:

“Detailed model inventory, findings, and waiver reporting is provided to senior management risk committees, with Board-level reporting focused on material trends and significant issues.”

This aligns with:

* SR 26-2’s risk-based philosophy
* Existing Board reporting policy
* Feedback that Board materials should be more concise and decision-oriented

⸻

2. Reduce Granularity of RAS Metrics

Another major theme.

Current issue:

* Too many separate zero-threshold metrics
* Tier-by-tier breakdowns create clutter with little value

Proposed direction:

* Collapse multiple metrics into fewer aggregated measures
* Keep historical trend columns
* Retain ability to explain detail if breached

Example:
Instead of:

* Tier 1 aged waivers
* Tier 2 aged waivers
* Tier 3 aged waivers
* Tier 4 aged waivers

Potentially move to:

* Aggregate aged waivers metric
* Aggregate aged findings metric

This is more:

* Board-friendly
* Consistent with “materiality-focused” reporting
* Easier to interpret

Importantly:

* This is NOT changing the RAS framework itself
* Mainly simplifying presentation/reporting

⸻

3. Clarify Committee Responsibilities

They repeatedly discussed clarifying:

* What goes to BRC
* What goes to MRCC/FRAC

So policies likely need:

* Cleaner separation of Board vs management committee reporting
* Explicit statement that operational/model-level detail belongs at management committee level

This may require:

* Updates to Model Control Policy
* Potential updates to Reporting Standards / Governance Standards
* Cross-check against Ross’s enterprise reporting policy

⸻

4. Conduct Cross-Policy Consistency Review

They explicitly mentioned checking:

* CCAR standards
* Tier 1 standards
* DRC policies
* QA standards
* Other references to Board reporting requirements

Goal:

* Ensure no conflicting language requiring detailed Board-level appendices/tables

Likely outcome:

* Most changes concentrated in central Model Risk Reporting / Governance sections
* Only spot edits elsewhere

⸻

5. Align With SR 26-2 “Risk-Based” Supervisory Philosophy

Although not stated explicitly in policy language terms, this is the underlying rationale.

The discussion reflects SR 26-2 themes:

* Less prescriptive reporting
* More proportionality
* Focus on materiality
* Avoid unnecessary operational detail
* Emphasize governance effectiveness over mechanical reporting

So policy wording should likely:

* Remove overly rigid reporting lists
* Avoid exhaustive mandatory appendix requirements
* Use more principles-based language

Example shift:
From:

“BRC shall receive model inventory, findings, waiver, and threshold reporting…”

To:

“BRC shall receive reporting sufficient to assess the firm’s overall model risk profile, material developments, and significant emerging risks.”

⸻

6. No Immediate Implementation Changes

Important governance/process point from the discussion:

* These are proposal-stage changes only
* Not intended for immediate June/July reporting cycle
* Need:
    * Internal drafting
    * Bill review
    * Potential MRCC approval
    * Alignment with broader reporting policy

So implementation language should avoid implying:

* immediate operational change
* retroactive reporting modifications

⸻

7. Potential Additional Cleanup Items

A few secondary themes surfaced:

a) “Head of MRM or Designee”

They expressed concern about prior governance wording changes.

Action:

* Review where this wording was inserted
* Potentially roll back if it diluted accountability/escalation clarity

b) Avoid Transcript-Style Committee Minutes

Not SR 26-2 directly, but governance simplification theme:

* Minutes should summarize key discussions and decisions
* Not capture every discussion detail

Could affect committee governance standards.




PRA Internal Ratings-Based (IRB) Approach Uplift: Submission of the Corporate Internal Credit Rating (ICR) models is expected this week pending Risk Strats delivery, with the validation timeline currently being finalized.
* Validation of the overarching Probability of Default (PD) model is underway, with initial documentation deficiencies identified and communicated to Risk Strats.




ECB ICAAP Exam: ECB and Bundesbank examiners are expected onsite from late June through September for an end-to-end review of the firm’s capital planning framework, with focus areas including Operational Risk and ICAAP capital calculations.
* Initial information requests due June 8 include ICAAP risk quantification methodologies, Pillar 2 validation documentation, operational risk validation procedures, and outsourced ICAAP activities.




CCR: MRM approved enhancements to the Prime Brokerage and CREST Equity margin shortfall models, and Franchise Equity Benchmark model (GBM Public, Tier 1) to address a validation finding related to the treatment of crypto-related stocks.
* The changes introduce a dedicated crypto sector classification and more conservative concentration shocks in Worst Case Loss (WCL) calculations to better capture the risk profile of crypto-related equities






ECB AI Workshop: MRM, together with Engineering, Legal, and other functions, participated in a 3.5-hour ECB workshop focused on the firm’s AI framework and use cases; overall discussions were constructive.
* Regulatory focus was primarily on cost-benefit analysis, as well as risk management, human-in-the-loop controls, and third-party oversight; the workshop also included discussion of AI governance and a walkthrough of a fraud detection use case. No findings are expected, with industry-wide observations expected later this summer.



The European Parliament reached provisional agreement on amendments to the EU AI Act, delaying implementation of the high-risk AI regime to December 2027 and certain AI transparency requirements (e.g., digital watermarking) to December 2026.
* Key implementation details remain pending legislative text, including treatment of existing AI systems and scope of the delayed transparency requirements.




The European Parliament reached provisional agreement on amendments to the EU AI Act, delaying implementation of the high-risk AI regime from August 2026 to December 2027, and certain AI transparency requirements (e.g., digital watermarking) from August 2026 to December 2026.
* The delay provides additional time for implementation and sequencing of compliance efforts, while key details remain pending legislative text, including treatment of existing AI systems and scope of the delayed transparency requirements.




I do not think removing the detailed inventory, findings, and extensive RAS commentary slides would conflict with the firmwide reporting requirements, provided the BRC materials still include an aggregate view of model risk, key concentrations/themes, material issues, and relevant RAS metrics/utilization.

The policy language is principles-based and focused on “aggregate view,” “summarize risk exposures and trends,” “tailored,” and “where relevant,” rather than prescribing specific inventory or findings reporting.

Accordingly, I think we can reasonably streamline BRC reporting by:
- Removing detailed inventory statistics and validation throughput metrics
- Replacing findings inventories with material thematic/control issues only
- Retaining concise RAS dashboards while limiting commentary to breaches, near breaches, or material trends
- Focusing BRC reporting on aggregate model risk, emerging risks, significant regulatory developments, and material remediation/control concerns

This would also align well with SR 26-2’s more risk-based and less prescriptive approach to model risk governance and Board reporting.


Yes — SR 26-2 gives you a strong basis to streamline and materially narrow BRC reporting relative to the historical SR 11-7 style approach. The revised guidance repeatedly emphasizes a risk-based, tailored, and non-prescriptive framework, and notably avoids many of the implicit governance expectations that firms operationalized under 11-7.  

Most importantly for BRC reporting:

* The guidance emphasizes that practices should be commensurate with model materiality, business impact, and organizational complexity  
* It explicitly states the guidance “does not set forth enforceable standards or prescriptive requirements”  
* Governance expectations focus on effective oversight and clear accountability, but do not prescribe detailed Board-level reporting artifacts like inventories, aged findings trackers, or broad model metrics packs  
* Aggregate model risk and material thematic risks are emphasized more than operational process metrics  

Accordingly, you can reasonably reposition BRC reporting toward:

* material model risk themes
* aggregate/model concentration risk
* RAS utilization and breaches
* emerging regulatory or AI governance topics
* material validation outcomes impacting business/risk decisions

while removing lower-value operational reporting.

Suggested direction below.

⸻

Proposed BRC Reporting Philosophy under SR 26-2

Current (11-7 era)

Broad operational oversight pack including:

* Inventory statistics
* Validation volumes
* Aged findings
* Waiver counts
* Detailed RAS commentary
* Process/control metrics
* Large model inventories and heatmaps

Proposed (26-2 aligned)

Risk-based Board reporting focused on:

* Material aggregate model risk
* Significant thematic/modeling issues
* RAS breaches/utilization trends
* Material regulatory developments
* Emerging AI/model governance risks
* Significant validation conclusions affecting capital, liquidity, stress testing, or trading risk

This is much more aligned with:

“model risk management practices appropriately vary among banking organizations based on their specific risk profiles and model usage”  

and:

“practices that are appropriate and effective for one banking organization may be inappropriate and ineffective for a banking organization with a different risk profile”  

⸻

Specific BRC Reporting Changes

1. Remove Detailed Inventory Reporting

Current

* Total model counts
* Inventory by tier/division
* Model lifecycle pipeline
* Validation throughput metrics

Proposed

Only report:

* Material changes in aggregate model landscape
* Significant concentrations or emerging exposures
* Material increase in AI/GenAI usage

Supporting rationale

SR 26-2 treats inventory primarily as an internal governance tool:

“It is common industry practice for banking organizations to maintain a comprehensive set of information…”  

Importantly, it does not elevate inventory metrics to a Board reporting expectation.

⸻

2. Remove Detailed Findings Slides

Current

* Findings aging tables
* Sev1/2 counts
* Open/closed trends
* Validation issue inventories

Proposed

Escalate only:

* Material thematic control weaknesses
* Significant unresolved model limitations
* Issues with material financial/regulatory impact
* Themes indicating elevated aggregate model risk

Potential replacement language:

“Management provides periodic reporting on material model risk themes, significant control issues, and emerging areas of model risk”

instead of:

“Management reports detailed model findings inventories and remediation status”

Supporting rationale

26-2 emphasizes:

* effective challenge
* model materiality
* aggregate risk
* business impact

rather than process metrics.  

⸻

3. Significantly Reduce RAS Commentary

Current

Heavy metric-by-metric commentary even when within appetite.

Proposed

Focus only on:

* breaches
* near breaches
* sustained utilization trends
* material thematic deterioration

Potential approach:

* Keep one concise RAS dashboard
* Remove lengthy narrative unless escalation needed

This aligns with the guidance’s move away from prescriptive governance mechanics.

⸻

4. Shift Validation Reporting to “Material Risk Themes”

Instead of:

* dozens of individual approvals/extensions

move toward:

* thematic summaries
* material portfolio/model implications
* emerging risks

Examples:

* AI governance and agentic AI developments
* Stress testing model limitations
* Market dislocation observations
* Concentration of overlays/expert judgment
* Benchmarking or analytics weaknesses
* Vendor model dependencies

This better aligns with:

“aggregate risk reflects interactions and dependencies among models”  

⸻

5. Narrow Board Role to Oversight of Material Model Risk

You could soften policy language along these lines:

Existing style

“BRC receives periodic reporting on model inventory, validation findings, model performance, waivers, and aggregate model risk”

Proposed style

“BRC receives periodic reporting on the firm’s aggregate model risk profile, material model risk themes, RAS utilization, and significant emerging regulatory or model governance developments”

or even:

“Reporting to BRC is risk-based and focused on material model risks, significant thematic developments, and matters warranting senior management or Board attention”

This language is highly defensible under 26-2.

⸻

6. Potential New BRC Structure

A much leaner BRC section could become:

Suggested BRC Sections

Top of Mind / Emerging Risks

* market events
* AI governance
* regulatory developments
* material model limitations

Aggregate Model Risk Profile

* concise RAS dashboard
* material concentrations/themes only

Significant Validation Themes

* major approvals
* material limitations
* emerging methodologies

Regulatory / Supervisory Developments

* SR 26-2 implementation
* AI regulation
* examination themes

Potentially reducing BRC materials by 50–70%.

⸻

Strongest Supporting Citations from SR 26-2

These are probably your best anchors when socializing changes internally:

Risk-based and tailored approach

“model risk management practices appropriately vary among banking organizations based on their specific risk profiles and model usage”  

Non-prescriptive framework

“This guidance does not set forth enforceable standards or prescriptive requirements”  

Materiality focus

“models deemed of higher materiality… warrant more comprehensive and rigorous oversight”  

Aggregate risk emphasis

“Aggregate risk reflects interactions and dependencies among models…”  

Governance flexibility

“The nature and sophistication of a banking organization’s model governance is typically informed by the extent and sophistication of model usage as well as the size and complexity of the organization”  

These collectively support a move away from operational/process-heavy Board reporting toward material thematic oversight.








FRB, OCC, and FDIC issued revised Model Risk Management guidance (SR 26-2), superseding SR 11-7 and reaffirming core MRM principles while adopting a more risk-based, less prescriptive framework with a narrower scope.







* The firm has begun engaging with peers, consultants, and the FRB on the revised guidance, while assessing implications and conducting a gap analysis against the new framework.




MRM approved enhancements to 11 models, qualitative approaches (QAs), and deterministic regulatory calculations (DRCs), completing Phase 1 model changes for Domestic Liquidity Sub-Group (DoLSub) formation requirements to support the firm’s application for PRA approval to manage GSI and GSIB liquidity on a consolidated basis





There is continued growth in the volume and complexity of AI use cases across the firm, including agentic AI capabilities and developer productivity tools

Examples in the pipeline include:

* US Rates AI (Prism): AI assistant for FICC Sales and Trading that synthesizes real-time market data, internal research, and client intelligence to automate macroeconomic briefings and support complex Q&A workflows
* Anthropic Platform: Standardized GS-dedicated AWS environment being developed to securely deploy and manage AI agents for use cases including KYC transformation, Controllers reconciliation, and funds oversight
* Slang AI 2.0 / Code Review Assistant: Expansion of AI-enabled engineering tools, including an assistant for the firm’s 5k+ SecDb developers and an LLM-based code review tool that provides advisory feedback within GitLab while maintaining human approval requirements


US Rates AI (Prism): Uses Model Context Protocol (MCP) and Claude Opus to combine real-time market data, internal GS research, and client intelligence to automate macroeconomic reports (e.g., CPI briefings) and support complex Q&A for FICC Sales and Trading teams through Marquee AI and email
* Anthropic Platform: Standardized GS-dedicated AWS environment and deployment blueprint being developed to securely build, manage, and operate AI agents co-developed with Anthropic, with initial use cases focused on OneGS 3.0 KYC transformation, Controllers reconciliation, and funds oversight
* Slang AI 2.0: Generative AI assistant for the firm’s 5k+ SecDb developers that answers natural language questions about the firm’s proprietary Slang language; Engineering is seeking AIRCC approval to launch Agentic Slang AI firmwide for SecDb developers, subject to training certification
* Code Review Assistant: LLM-based code review assistant that uses deterministic prompts and governed artifacts to evaluate code changes and post categorized findings directly into GitLab merge requests; the tool operates in an advisory-only capacity, with all approvals and code changes remaining subject to human reviewer oversight


US Rates AI (Prism): Generative AI platform leveraging real-time market data, internal research, and client intelligence to automate macroeconomic reports (e.g., CPI briefings) and support interactive Q&A for FICC Sales and Trading teams.
* Anthropic Secure Agent Environment: Standardized GS-dedicated cloud environment under development to securely deploy and manage AI agents, supporting use cases including OneGS 3.0 KYC transformation, Controllers reconciliation, and funds oversight.
* Slang AI 2.0: Generative AI assistant for the firm’s 5,000+ SecDB developers that answers natural-language questions about the firm’s proprietary Slang programming language; Engineering is seeking approval to roll out an enhanced agentic version subject to mandatory training certification.
* Code Review Assistant: LLM-based code review assistant that evaluates code changes using governed inputs and posts categorized comments directly into GitLab merge requests; the tool operates in an advisory-only capacity, with all approvals remaining subject to human review.



The NYC Volex desk has proposed enhancements to the analytics used for calculating IR delta, particularly at the long end, following MRM analysis conducted during revalidation
* Independent benchmark analytics developed by MRM indicate that known limitations in the desk’s existing analytics have a material impact on IR delta measurement
* To address this finding, the desk has developed revised analytics designed to improve the accuracy and robustness of IR delta calculations, which are currently under MRM review

Mortgage Agency Feeder Model Enhancement (GBM Public, Tier 1)
MRM approved changes to the mortgage agency feeder model to address divergence between modeled and observed prepayments, which had resulted in elevated interest rate sensitivity (IRDV01) for the CMO desk. The issue was identified amid recent market volatility, with a limit breach under an IR +50bps stress scenario, and a temporary limit increase granted in March. Root cause analysis indicated that the model underestimated prepayments relative to observed levels, leading to longer effective durations and overstated IRDV01 and stress losses. Enhancements included a tactical recalibration of prepayment assumptions using empirical data and the introduction of cohort-level multipliers to better capture issuer, vintage, and coupon effects. Post-implementation, IRDV01 reduced from -$4.5MM/bp to -$3.1MM/bp. MRM raised a medium-severity finding to track strategic remediation of underlying model limitations.

⸻

Mortgage PST Pool Pricing Model Issue (GBM Public, Tier 1)
MRM identified a material issue in the Mortgage PST Pool Pricing and Pool Forward OAS models related to the incorrect application of pool price as the reference TBA price, resulting in inappropriate price flooring and understatement of risk under stress scenarios. The issue was identified by Market Risk Strats and GBM Strats during ongoing model enhancements and remains outstanding. MRM has raised a high-severity (Sev1) finding and rejected the model pending remediation. As of April 16, the issue is estimated to result in an impact of approximately -$57MM under IR +50bps topsheet, -$80MM under CSW stress, and -$7MM in VaR. Remediation efforts are ongoing.

⸻

NYC Volex IR Delta Analytics Review (Tier 1 Revalidation)
As part of a significant Tier 1 revalidation, MRM reviewed the backbone methodology used by the NYC Volex desk to calculate IR Delta and identified limitations in the current approach. Independent benchmarking using enhanced MRM-developed analytics indicated an increase in IR Delta of approximately $2MM/bp. Further analysis of SIMM sensitivities for key counterparties showed that adopting alternative analytics would increase SIMM disputes, while removing the backbone assumption (i.e., calculating delta with interest rate volatility held constant) would significantly reduce longstanding disputes. Findings were consistent across multiple observation periods. MRM raised a finding requiring improvements to IR delta analytics and justification of the modeling approach. The desk has developed revised analytics, which are under MRM review, and plans to present to the SIMM Governance Forum on potential removal of the backbone to improve alignment with counterparties.



The committee approved the pilot rollout of Gemini CLI and Google-hosted MCP servers for up to 99 engineers. The presenters agreed to post back to the committee before broader CTL general availability with pilot learnings, guardrail assessment results, and any relevant findings. No additional approval was required for broader CTL rollout if the pilot results are clean, although the committee requested a posting before general availability.





Below is a draft in the same AIRCC minutes style.

⸻

1. Materials: AIRCC Materials dated May 5, 2026

2. Google Gemini Command Line Interface (CLI) – Approval

The presenters provided an overview of the request to enable Google Gemini Command Line Interface (CLI) and Google-hosted Model Context Protocol (MCP) servers for an initial group of up to 99 Goldman Sachs engineers. The presenters explained that the initial pilot population would consist of software developers and site reliability engineers across Core and GBM Engineering working on the Consolidated Trade Ledger (CTL) platform.

A committee member asked how the risk profile of Gemini CLI compares to previously approved coding assistant tools, including Claude Code. The presenters explained that Gemini CLI is functionally similar to other AI-enabled coding tools, but noted that the deployment approach differs because the tool would operate within the Google Cloud Platform (GCP) ecosystem. The presenters explained that the relevant back-end would use an unprivileged service account with no escalated privileges, with access limited to permitted reads, builds, tests and other developer activities. The presenters further noted that the tool would have no path to GSI net and would not receive write privileges to production services.

The presenters explained that the primary security benefit of the proposed approach is that data remains within the Google ecosystem and can use GCP-native controls for data and credential leakage. The presenters noted that the integration between Gemini CLI and the Google-hosted MCP servers is an interface enhancement and does not change existing security posture or authorization controls. The presenters further explained that MCP servers would be Google-owned and Google-hosted, and would act as a pass-through layer on top of existing APIs rather than creating new privileges or special tokens.

Committee members asked about egress controls, authentication and on-behalf-of flows. The presenters stated that existing egress controls would not be changed and that the deployment would use established security boundaries. The presenters explained that the developer would land into a separate unprivileged agent identity rather than the developer’s own privileged identity. The presenters further described the CTL witnesser chain, which tracks identities across internal service calls and enables additional controls where an AI-enabled identity is involved in a sensitive execution path.

The presenters described the phased rollout plan. The pilot would initially focus on use cases such as code development, writing tests and creating feature plans. The presenters noted that learnings from the proof of concept indicated strong use cases in new feature development, code modernization and incident triage, particularly given CTL’s monorepo structure and the ability to review logs, code, configuration and history together. The presenters noted that users reported productivity benefits from terminal-based integration, reduced context switching, larger context windows and faster debugging.

The presenters summarized key risk mitigants. For data leakage, the presenters noted that the deployment would rely on GCP-native controls, including organization policies, Virtual Private Cloud service controls, restricted APIs, encryption in transit and restrictions to Goldman Sachs projects and prompts. For unauthorized access, the presenters noted that access would be limited from CTL desktops through private connectivity to Google APIs, with GCP Identity and Access Management controls unchanged. For unapproved code or libraries, the presenters noted that existing software development lifecycle controls, vulnerability scanning and human review processes would continue to apply.

The presenters also discussed proposed guardrails, including integration with Model Armor for Vertex AI to support prompt auditing and controls related to profanity, hate speech, personally identifiable information and secret leakage. The presenters noted that Model Armor and related reporting would be evaluated during the pilot and expected to be in place before broader CTL general availability. Committee members clarified that broader general availability would refer to the CTL engineering population rather than firmwide deployment.

The committee approved the pilot rollout of Gemini CLI and Google-hosted MCP servers for up to 99 engineers. The committee noted that the presenters should post back to the committee with pilot learnings, including guardrail results and any relevant findings, before broader CTL general availability. The committee further noted that a subsequent approval would not be required if the pilot results are clean, but that the committee should be updated before broader rollout.

3. Legislative and Regulatory Updates – Posting

The presenters provided an update on legislative and regulatory developments related to AI across the United States, Europe and Asia.

For the United States, the presenter discussed recent federal activity, including executive orders and a national policy framework focused on AI research, national competitiveness, federal AI initiatives and potential federal legislation. The presenter noted that, in the absence of comprehensive federal AI legislation, states have continued to introduce a significant volume of AI-related bills covering topics such as child safety, energy costs, free speech, intellectual property, community impacts and AI deployment. The presenter noted that a comprehensive federal law is unlikely to be enacted before the upcoming election, but that targeted legislation, including export-related bills, may continue to advance.

Committee members discussed the interaction between potential federal legislation and state-level AI laws. The presenters and committee counsel noted that federal legislation could preempt some state laws depending on how it is drafted, but that until a comprehensive federal framework exists, states are likely to continue developing their own AI rules. The presenter further noted that AI is increasingly becoming a political topic heading into the midterm election cycle.

For Europe and the United Kingdom, the presenter noted that the European Union remains more prescriptive through the EU AI Act, while the United Kingdom continues to follow a more principles-based approach through regulators such as the Bank of England and Financial Conduct Authority. The presenter noted that the EU Digital Omnibus proposal could delay the high-risk AI provisions of the EU AI Act from August 2026 to late 2027, although this would not necessarily reduce the underlying requirements. The presenter also highlighted ongoing regulatory focus on AI adoption in financial services, financial stability risks, model explainability and potential reliance on third-party providers, including possible pressure toward localization of activity in Europe.

For Asia, the presenter described a fragmented regulatory landscape. The presenter noted that China remains among the more prescriptive jurisdictions, despite not yet having nationwide AI legislation, and has begun legislative research on AI. The presenter noted that South Korea has enacted comprehensive AI legislation focused on high-impact AI systems, while Hong Kong and Singapore continue to take more innovation-focused approaches supported by industry engagement and regulatory sandboxes. The presenter further noted that Japan continues to emphasize regulator-industry dialogue and expectation-setting.

The presenter highlighted Singapore as a key example of government engagement, noting that AI has become a national priority and a core part of Singapore’s economic strategy. The presenter explained that the firm has positioned itself as a strategic partner to the Singapore government, including through participation in the Monetary Authority of Singapore’s Pathfinder program. The presenter noted that this engagement has created opportunities for the firm to provide input on AI development and financial sector adoption.

Committee members also discussed upcoming regulatory engagement. It was noted that the firm has an upcoming workshop with European regulators and that the FCA has requested an update on Mythos and is expected to communicate its AI review focus in the coming weeks. Committee members also noted that Hong Kong regulators had raised questions following press coverage regarding restrictions on Anthropic and Claude availability in Hong Kong. The committee discussed that Microsoft Copilot access had been restored for Hong Kong users without Anthropic models, while Anthropic models remain blocked in GS AI Assistant and other tools where required.

4. Administrative Matters

The secretary welcomed new committee members Elizabeth Burns from Engineering and Luke Taylor and Mache Wolonski from GBM.

5. Prior Meeting Minutes Approval: Minutes from the committee’s meetings held on April 7, 2026 and April 21, 2026 were approved.

Having no further business to discuss, the chairpersons closed the meeting.

To the extent transaction(s) were discussed, no committee member raised issues related to the transactions regarding any (i) material conflict of interest, (ii) material exposure to high-risk assets or high-risk trading strategies that could significantly increase the likelihood that the firm could incur a substantial financial loss, or (iii) activity that would otherwise pose a threat to the safety and soundness of the firm or the financial stability of the United States.



MRM approved KYC Document Digitization (GBM Public, Tier 3), used to extract and structure Know Your Customer (KYC) attributes from client documents within the onboarding workflow.
* The model leverages optical character recognition (OCR) and large language model (LLM)-based extraction to convert unstructured documents into structured outputs, with human-in-the-loop maker-checker review prior to submission.
* MRM analysis indicates strong performance, with 97% coverage (OCR confidence >80%) and 91% accuracy, exceeding the 80% business targets for both metrics.




AIRCC approved a pilot to enable Google Gemini Command Line Interface (CLI) and Cloud MCP Server for ~100 engineers (software developers and site reliability engineers) across Core and GBM Engineering working on the Consolidated Trade Ledger platform.
* The tool provides agent-style coding capabilities similar to other industry tools, with an enhanced security posture through GCP-native controls, including protections against data and credential leakage across the workflow.



Here is a clean, structured transaction waiver summary based on the image, aligned with your usual MRM / committee style and simplifying the math where appropriate.

⸻

Transaction Waiver Summary

Desk

Equities – Dispersion Trading

Trade

Single-name to single-name volatility dispersion note (multi-currency)

Tradable

Eq Dispersion

Vega Notional

Indicative range: USD 500k – 2 million

Maturity

June 2027

Underlier

Basket of 12 European single stocks (singles-to-singles dispersion)

Greeks (Indicative)

Gamma: ~1.5v

⸻

Trade Description

The transaction is a USD volatility dispersion note, referencing a basket of European single stocks, where the payoff depends on the relative realized volatility performance across constituents.

The payoff structure includes:

* A fixed coupon (~4.7%)
* Leverage applied to dispersion performance
* A global floor and cap applied to the payout

Key indicative parameters:

* Leverage: 1/10
* Payout Floor: -10
* Payout Cap: +10
* Individual caps: capped at ~2.5× strike per name

The note includes a global floor, ensuring the client’s maximum loss is limited to the note notional.

⸻

Reason for Waiver

The Eq Dispersion tradable does not support booking a Global Cap for multi-currency dispersion structures due to an existing pricing validation constraint.

While a Global Floor is supported, the cap cannot currently be represented consistently, despite both features being economically symmetric.

This limitation is driven by the model’s inability to fully capture FX–volatility (VoVaR) correlation risk, which impacts cap modeling.

⸻

Proposed Booking During Waiver Period

The desk proposes to remove the pricing validation constraint on the Global Cap, allowing caps and floors to be treated consistently within the existing Eq Dispersion tradable.

⸻

Compensating Controls

The desk noted that the limitation impacting the Global Cap is already present in the modeling of Global Floors, and therefore the waiver does not introduce a new class of model risk.

In addition:

• Existing dispersion monitoring tools (tracking dispersion levels, floors, and VoVaR/correlation risk) will be extended to include cap monitoring
• The payoff is bounded by explicit floor and cap levels, limiting extreme outcomes
• The structure applies low leverage (1/10), reducing sensitivity to modeling gaps
• The note includes a global loss floor, capping downside exposure at the notional level
• The incremental risk relates to FX–volatility correlation, which is already recognized and monitored within current frameworks

⸻

Remediation Plan

• Extend monitoring tools to explicitly incorporate cap-related risk metrics
• Perform benchmark analysis including FX diffusion, assessing FX volatility and FX–VoVaR correlation impacts
• Use results to determine whether to:

* enhance the production model (for both floor and cap), or
* maintain current modeling with enhanced monitoring

Timeline: ~2–4 weeks of Strats work

⸻

If you want, I can also:

✅ tighten this for CRO / MRCC tone (shorter, sharper)
✅ add a 1-line explanation of dispersion for non-equity reviewers
✅ strengthen the FX–VoVaR risk explanation (this is the key model risk point)
✅ or prepare a quick Q&A for likely pushback (this one will get questions on FX correlation)

Just tell me 👍







Meeting Minutes: Q1 2026 Quarterly MRM Meeting with FRB – [Date]

MRM hosted the Q1 2026 Quarterly Model Risk Management meeting with FRB and FDIC. The meeting briefly covered standard quarterly updates, including validation activity, findings, RAS exceptions, inventory, AI/ML models, model changes, ongoing monitoring, CCAR validation, and emerging risks. The discussion primarily focused on the revised Model Risk Management guidance, SR 26-2.

⸻

1. Revised Model Risk Management Guidance SR 26-2

* David Palmer joined the meeting to discuss the revised guidance and respond to questions from GS.
* David noted that the revised guidance was intended to emphasize four key themes:
    * Greater risk focus
    * More flexibility for institutions
    * Stronger focus on material models
    * Reduced prescriptiveness and more principles-based expectations
* David emphasized that the main elements of model risk management remain broadly consistent with prior guidance, and that the revised guidance is not intended to represent a fundamental rethinking of MRM expectations.
* GS asked about the reduced emphasis on board and senior management involvement. David explained that the change is intended to align MRM oversight more closely with other risk management areas, with the board focused on higher-level oversight rather than detailed review.
* GS asked about language around organizational standing of MRM. David clarified that the agencies are not prescribing how institutions should organize MRM functions, but effective challenge remains important, particularly for material models.
* GS asked whether the additional language on model materiality, model risk, and user involvement represents new expectations. David explained that these are intended as clarifications rather than new requirements.
* GS asked about the statement that guidance is not legally enforceable. David clarified that this is not a change in legal position and is consistent with prior agency statements on supervisory guidance.
* GS asked about the removal of “process verification” language. David noted that this may reflect the broader effort to remove detail that could create confusion, and said the agencies may follow up further.
* GS asked about the treatment of AI, generative AI, and agentic AI. David noted that traditional machine learning approaches generally remain in scope of MRM guidance, while generative AI and agentic AI were scoped out because they may require different governance considerations.
* Bill noted that if generative AI is embedded into an important pricing, risk, capital, or liquidity model, GS would still expect the MRM framework to apply to the use case. David acknowledged the feedback and emphasized that the guidance is not intended to create a “cliff effect” where non-model items receive no controls.
* David noted that even where something is not scoped into the MRM guidance, institutions should still have governance and controls commensurate with risk.
* GS asked whether other SR letters with model-related expectations, such as CCAR-related guidance, may be updated. David noted this is part of a broader review of supervisory guidance, but could not confirm specific changes.
* GS asked about changes to the model definition, including the exclusion of arithmetic calculations and deterministic rules. David explained that the changes are intended to clarify that simple calculators or deterministic tools do not automatically need to be treated as models, while still requiring appropriate controls based on risk.

⸻

2. AI / Generative AI Governance and Use Cases

* FRB asked for a high-level overview of GS’s generative AI governance framework.
* Caroline explained that there have been no recent fundamental changes to the MRM program for generative AI and agentic AI, but the framework has evolved over the past few years.
* MRM has had AI-specific model requirements since 2018 and made further enhancements in late 2023 / early 2024, including establishing a fourth risk tier for certain AI tools not previously classified as models.
* Caroline explained that AI platforms, such as large language models and general-purpose tools like Microsoft 365 Copilot and GitHub Copilot, are captured in the AI inventory and broader AI governance process.
* Caroline noted that the AI Risk and Controls Committee provides broader governance over AI risks, with representation from MRM, Operational Risk, Technology Risk, Legal, Compliance, and Engineering.
* FRB asked about the effectiveness of human-in-the-loop controls as AI use cases become more complex. Caroline and Bill explained that human review is effective for lower-risk chatbot-style use cases, but may be less effective as AI models become more automated or agentic.
* Bill noted that higher-risk AI use cases receive more detailed review, including consideration of automated controls, testing, ongoing monitoring, and whether human oversight is practically effective.
* FRB asked whether agentic AI models are separately flagged in inventory. Bill confirmed that agentic AI is flagged, though the current population remains small.
* FRB asked about vendor models and large language models. Bill explained that LLMs and similar tools are captured as AI platforms, but MRM generally validates the specific business use case rather than independently validating the general-purpose platform itself.

⸻

3. Status of Validation Findings and Internal Audit Findings

* Caroline noted there were no material changes in model validation activity or the status of findings.
* FRB asked about the five additional validations. Caroline explained that additional validations are generated from the annual review process when targeted follow-up work is needed, rather than a full revalidation. GS agreed to provide follow-up details.
* Caroline noted that there were no new internal audit findings and no material changes since the prior meeting.
* The three outstanding IA findings are all lower severity and are the only open IA findings owned by MRM related to model risk.

⸻

4. RAS Exceptions and Aged Findings

* FRB asked about four unvalidated Tier 1 models in use. Caroline explained that these relate to one Controllers valuation adjustment model and three GBM models, including valuation-related and liquidity-related models.
* Caroline noted that most are within the initial waiver period, while one waiver had been extended due to additional time required to complete validation.
* FRB asked about unvalidated Tier 2 models in use. Caroline explained that the three Tier 2 items are not aged and are likely different from the prior quarter’s population.
* FRB asked about the rejected Tier 1 model. Caroline explained that it related to regression test failures that exceeded the 14-day remediation window. The issue was escalated through rejection status and has since been resolved; the issue was with the test rather than the model itself.
* FRB asked about Tier 1 models with findings aged more than six months. Caroline noted the population decreased from six to three, all related to GBM counterparty credit risk models.
* Caroline noted these remaining items are receiving senior attention from GBM Strats leadership and the CRO, with a commitment to remediate during the quarter.

⸻

5. Model Inventory and AI/ML Inventory

* FRB asked about new models in inventory without assigned risk tiers.
* Caroline explained that new declared models are captured in inventory before MRM completes initial classification and risk-tier assignment.
* FRB asked whether the AI/ML risk assessment process differs from traditional models. Caroline confirmed the process is the same: models are declared, initially classified and tiered, and then risk tier is reconfirmed during validation.
* Caroline noted that the volume of AI/ML declarations has increased, which explains why more AI/ML items may appear as pending classification.

⸻

6. Thematic Update – Model Changes and Enhancements

* MRM highlighted several notable AI model approvals during the quarter, including one Tier 1 model and three Tier 2 models.
* The Tier 1 generative AI model, owned by Corporate Treasury, automates matching of incoming payments to reduce manual review of cash receipts. Related high-severity findings on performance, evaluation metrics, and ongoing monitoring were remediated before approval.
* MRM also approved Tier 2 generative AI models enabling web-search grounding within Copilot and GS AI Assistant.
* In collateralized lending, MRM approved a Tier 1 facility-level rating model for GS Select loans, supporting recognition of collateralized exposures and Treasury’s initiative to pledge positions to the Federal Reserve discount window.
* MRM also approved enhancements to Tier 1 tail risk and facility-level rating models, including better treatment of multiple collateral types, incorporation of hedges into loss calculations, updated aviation data, and remediation of prior validation findings.
* In GBM, MRM approved a new Tier 1 income-space vega risk model, CCR benchmark model enhancements to support shortfall harmonization, and Prime Brokerage margin model enhancements for European equity average daily volume.
* In Corporate Treasury and Risk, MRM approved liquidity-related model changes, including a vendor model for security-level liquidity scores and enhancements to reduce reliance on overlays in liquidity models.
* FRB asked for additional information on Corporate Treasury liquidity scoring and MLO-related changes. GS agreed to follow up.

⸻

7. CCAR Validation

* MRM provided a brief overview of CCAR validation activity.
* MRM noted there were no material changes to the CCAR validation process.
* All models and qualitative approaches were validated and approved for CCAR 2026.
* Eight high-severity findings were raised during the process and all were remediated.
* Findings primarily related to implementation issues in GPA and AWM models, as well as some conceptual and documentation issues in new models and qualitative approaches.
* All findings from CCAR 2025 were closed.

⸻

8. Ongoing Monitoring and Emerging Risk

* MRM noted that no high-severity findings were raised during the quarter related to ongoing monitoring.
* Notable medium-severity findings included:
    * A fallback methodology issue in the GBM commodities franchise benchmark model, related to data issues and inconsistent treatment across portfolios
    * Divergence between observed and modeled prepayments in the residential mortgage agency model, resulting in longer modeled durations and elevated IRDV01
    * Deterioration in precision metrics for a Tier 2 Compliance surveillance model
* FRB asked whether recent market risk backtesting breaches indicate broader model stress due to market volatility.
* MRM explained that backtesting breaches were reviewed and were not attributed to model issues.
* MRM noted that no significant model performance issues were identified amid market volatility, though the agency mortgage prepayment issue was identified through ongoing monitoring and is being addressed through recalibration and a more strategic model uplift.





Strategic

* Align and enhance the model control framework in response to revised SR 26-2 guidance
* Advance AI governance and MRM AI initiatives, including agentic AI, and support growth and validation of new AI use cases
* Validate key regulatory models, including US Basel III Finalization (B3F), PRA IRB (ICR/PD), and Phase III ICR uplift
* Support CCR framework enhancements, including migration of PB to the Unified Benchmark Model

⸻

Near Term

* Assess implications and conduct gap analysis for SR 26-2 as a near-term priority
* Enhance AI governance, including uplift of AI Policy and rollout of AIRHub to support AIRC approvals
* Remediate CCR findings breaching FRAC thresholds, with resolution targeted by Q2 2026

⸻

April Accomplishments

* Closed Internal Audit MRA on Annual Review and engaged regulators on key initiatives (FRB SR 26-2, PRA SS1/23)
* Submitted materials for ECB AI workshop, including responses to ~100 questions
* Completed key validations, including Phase I DoLSub liquidity changes (subject to PRA approval)
* Rolled out ValDoc Assistant to support validation document drafting





The FRB noted that generative AI and agentic AI were scoped out of SR 26-2, as they may require different governance considerations from traditional machine learning models; MRM discussed the importance of maintaining appropriate controls where these capabilities are embedded in risk, capital, or liquidity models




MRM held an initial discussion with the FRB on the revised Model Risk Management guidance (SR 26-2) during the quarterly meeting, with the FRB emphasizing that the guidance is intended to be more risk-focused, flexible, principles-based, and focused on material models, while maintaining the core elements of model risk management.
* The FRB clarified that changes around Board / senior management oversight, MRM organizational standing, materiality, model definition, and guidance enforceability are intended primarily as clarifications and reduction of prescriptiveness, rather than a fundamental change in supervisory expectations.
* MRM discussed the treatment of generative AI and agentic AI under the new guidance, noting the importance of maintaining appropriate governance and controls where these capabilities are embedded in risk, capital, or liquidity models.


Modelers have submitted the overarching Probability of Default (PD) model on April 23, together with regulatory compliance assessments; MRM validation is in progress.
    * Remaining model submissions are targeted from mid-May to end-June, with validation expected from end-June to mid-August, ahead of PRA submission in September 2026.

The first PRA engagement since the guidance went live in 2024 was held on April 29 with GSI/GSIB CRO, Head of MRM, and Internal Audit to discuss the SS 1/23 survey submitted by GS in October 2025.
    * Discussions focused on the overall MRM framework and legal entity considerations, including risk appetite statement (RAS) metrics, ongoing performance monitoring, revalidation triggers, and model inventory system capabilities.



The exam is progressing as expected with no significant model-related concerns identified to date, with the final set of scheduled meetings taking place this week.
* PPNR: Regulatory focus on model segmentation and revenue projection methodology (aggregate vs. granular approaches), including MRM challenge of model choices; follow-up requested on conversion factor methodology and overlays.
* XVA: Discussions centered on exposure measurement, CVA vs. FVA split, and differences between front-office and CCAR models, including the limit framework; regulators also reviewed key modeling assumptions (e.g., one-factor vs. two-factor models, asymmetric funding curves) and implications for exit value.
* Provisions: Remaining discussions are validation-focused, covering updates to the validation framework, ongoing monitoring, key assumptions (LGD, PD, risk identification), data integrity, and drivers of model vs. scenario differences across portfolios.




Key changes include expanded coverage (e.g., integration of Prime Brokerage and Futures accounts), improved modeling of non-linear exposures, alignment with GBM margin model methodologies, and establishment of enhanced ongoing monitoring frameworks


Regulators also reviewed key modeling assumptions, including the use of one-factor vs. two-factor interest rate models for CVA, and the treatment of asymmetric funding curves, with attention on implications for exit value.



    The CCAR exam is ongoing, with the final set of scheduled meetings taking place this week.
* PPNR: Regulatory focus has shifted to model segmentation and revenue projection methodology, including the choice between aggregate vs. granular approaches (e.g., Global Core Services (GCS), Mark-to-Market (MtM), and Net Interest Margin (NIM)), as well as MRM review and challenge of these model choices. A follow-up meeting has been requested on conversion factor methodology and overlays.
* XVA: Discussions have focused on exposure measurement and the split between CVA and FVA liabilities, as well as differences between front-office pricing models and CCAR models, including the associated limit framework. Regulators also reviewed key modeling assumptions, including the use of LGM1FSV vs. 2FSV for CVA and the treatment of asymmetric funding curves, with attention on implications for exit value.
* Provisions: Remaining discussions are validation-focused, covering updates to the validation framework, robustness of ongoing monitoring, challenge of key assumptions (e.g., loss given default (LGD), probability of default (PD), risk identification, and COVID-related data), data integrity controls, and drivers of differences between model outputs and scenario projections across portfolios.


Rolled out ValDoc Assistant, a generative AI application developed by MRM to support drafting of validation documents
* Submitted materials, including existing documentation and responses to ~100 questions, for the upcoming ECB AI workshop
* Held initial discussions with the FRB on revised Model Risk Management guidance SR 26-2 during the quarterly meeting
* Engaged with stakeholders and met with the PRA to discuss the SS 1/23 model risk management survey submitted in Oct’25





Assess implications and conduct gap analysis against revised Model Risk Management guidance SR 26-2
* Continue growth and validation of new AI models
* Prioritize review of CCR findings breaching FRAC thresholds, with resolution targeted by Q2 2026
* Continue validation of model enhancements supporting CCR management and the ASL business





Continue enhancing the AI governance framework, including agentic AI, to strengthen controls and oversight
* Advance MRM AI initiatives leveraging generative and agentic AI to improve validation efficiency and coverage
* Validate models and DRCs supporting the US Basel III Finalization (B3F) pre-proposal
* Validate Corporate ICR and overarching PD models as part of the PRA IRB uplift
* Validate ICR models for structured finance, sovereigns, financial institutions, and funds as part of the Phase III CR uplift






Continued enhancement of the AI governance framework, including agentic AI, to strengthen controls and oversight
* Continued advancement of MRM AI initiatives leveraging generative and agentic AI to improve validation efficiency and coverage
* Validation of models and DRCs supporting the US Basel III Finalization (B3F) pre-proposal
* Validation of Corporate ICR and overarching PD models as part of the PRA IRB uplift
* Validation of ICR models for structured finance, sovereigns, financial institutions, and funds as part of the Phase III CR uplift



Here’s a clean, action-oriented summary of what you need to do based on the discussion — grouped by Strats / Stress materials and CRO update so you can execute quickly.

⸻

🔧 What you need to do

1) Stress / Strats materials (near-term updates)

A. Reorder + content updates

* Move CCAR / ongoing exam section to the top (Section F → top priority)
* Update:
    * Metrics / violations / blessed models → refresh with latest status by Friday
    * Validation work section → include latest activities

⸻

B. Mortgage model issue (important)

* Add a clear bullet on the mortgage model issue
    * Current status (not fixed)
    * Materiality (still material)
    * Impact:
        * VaR / GMS / stress metrics
    * Include:
        * Any backtesting results / potential additional breaches
* Follow up:
    * Confirm Strats are analyzing impact
    * Confirm CCAR date (Dec 31) not materially impacted

⸻

C. AI models / pipeline visibility

* Add updates on:
    * New AI models in pipeline (e.g., commodities, others submitted to AISG)
* Goal:
    * Ensure Strats are aware of new developments
    * Highlight lack of testing / early-stage concerns where relevant

⸻

D. RCSA (GBM)

* Optional:
    * Create simplified version excluding CCR models (URP still red)
* But:
    * Keep effort minimal (low stakeholder attention)

⸻

2) CRO Update (main focus)

A. Topics to include (priority order)

1. SR 262 (Top of Mind – lead topic)
2. AI governance (second key topic)
3. AI initiatives (progress / developments)
4. IRB / NIM / GFAS modeling changes (early view)
5. CCAR + CCAR exam updates
6. FRB quarterly updates (post-meeting)

⸻

B. Improve model change descriptions (important feedback)

For CCR / cost model:

* Don’t just say “addressing findings”
* Add:
    * What actually changed (high level)
        * e.g., specification / monitoring / implementation fixes
    * Why it matters
* Include:
    * Number of open findings (CCR + broader context)

⸻

C. FRTB / ASL updates (key structural change)

* Stop:
    * Incremental small updates each time
* Instead:
    * Provide aggregated / thematic updates
    * e.g.:
        * “Quarterly summary of key enhancements”
        * Highlight material changes (e.g., hedging, tail risk improvements)

⸻

D. Remove low-value items

* Reassess:
    * Small / niche updates (e.g., Japan mortgage model)
* Only include if:
    * Material or part of a broader theme

⸻

E. Add ETSC + AI-related control example

* Include:
    * Example of AI usage in e-trading system migration
    * Highlight:
        * Issue found (threshold vs exposure bug)
        * Controls worked (issue caught)
* Position as:
    * Evidence of effective validation / controls

⸻

F. AI in MRM (important for CRO audience)

* Add content on:
    * How MRM is using AI internally
        * e.g., PCC analysis tool
* Improve:
    * Clear distinction between:
        * AI-generated insights vs human inputs

⸻

3) New initiative (important – CRO angle)

PCC / model change analytics (AI tool)

You need to refine before presenting:

* Improve:
    * Category definitions (more coherent / less mixed)
* Add:
    * Clear labeling: AI vs human-generated fields
* Move toward:
    * Thematic insights, not raw stats
        * e.g.:
            * “Increase in commodities model changes due to volatility”
            * “Spike in EOD fixes linked to market events”
* Goal:
    * Produce trend-based, senior-friendly summary (every 2 weeks)

⸻

4) Specific follow-ups

* Clarify:
    * What is GCLA max factor model
* Get detail on:
    * Japan mortgage model (materiality + relevance)
* Confirm:
    * Mortgage model → VaR breach impact
    * Strats analysis status
* Align with Bill before sending:
    * Especially on unclear model items

⸻

🧠 Key meta-feedback (how to improve overall)

* Move toward:
    * Fewer, higher-impact updates
    * Thematic storytelling (not incremental logs)
* Always answer:
    * What changed?
    * Why it matters?
    * What’s the risk / impact?

⸻

If you want, I can convert this into a CRO-ready checklist slide or directly rewrite your CRO update draft in your preferred one-line bullet style.



    MRM reviewed 2026 Q1 backtesting results and concludes models are performing as expected.
* For the JANY/Derivatives sub-portfolio, the previously elevated VaR backtesting breaches were driven by a methodological inconsistency between VaR and realized P&L: VaR excludes P&L from STS index rebalancing under a constant composition assumption, while realized P&L includes rebalancing effects as index composition changes over time.
* As rebalancing P&L is considered new business activity, MRM’s view is that it should be excluded from backtesting comparisons; implementation of this adjustment is in progress, with preliminary results indicating no additional breaches and improved backtesting performance, consistent with the observed reduction in breaches in Q4 2025.
* Elevated sensitivity was observed in IRC (Incremental Risk Charge) correlation benchmarking for GAUS, driven by reliance on an outdated AIRB-based benchmark with higher correlation assumptions than the production model; this has been remediated through adoption of an empirically calibrated benchmark based on quarterly equity returns, resulting in reduced sensitivity and improved alignment in Q1 2026.


MRM reviewed 2026 Q1 backtesting results and concludes models are performing as expected.
* For the JANY/Derivatives sub-portfolio, the rebalancing P&L issue that had contributed to elevated VaR backtesting breaches has been resolved in 2025; in Q4 2025 (pre-renewed market volatility), breach counts declined materially, indicating improved model performance following remediation.
* Elevated sensitivity was observed in IRC (Incremental Risk Charge) correlation benchmarking for GAUS, driven by reliance on an outdated AIRB-based benchmark with higher correlation assumptions than those used in the production model. This has been remediated through adoption of an empirically calibrated benchmark based on quarterly equity return data, resulting in reduced sensitivity and improved alignment with model behavior in Q1 2026.


Market Risk

* MRM reviewed 2026 Q1 backtesting results and concludes models are performing as expected.
* For the JANY/Derivatives sub-portfolio, a rebalancing P&L issue that had driven elevated VaR backtesting breaches has been resolved in 2025, with breach levels materially reduced prior to the recent market volatility.
* Sensitivity in IRC correlation benchmarking for GAUS was observed due to an outdated benchmark with conservative correlation assumptions; this has been remediated by adopting an empirically calibrated benchmark, resulting in reduced sensitivity in the current quarter.






Good instinct — “despite” makes the message sharper and more confident. Here’s the refined version:

⸻

Emerging Risk

* Despite elevated volatility across rates, commodities, and energy markets in Q1 2026, no material model performance issues were observed, with isolated exceptions addressed through targeted model changes
* MRM approved enhancements to the Tier 1 GBM Public Mortgage Agency Feeder model following divergence between modeled and observed prepayments, which contributed to elevated interest rate sensitivity (IRDV01) and a temporary limit breach for the CMO desk during the period of heightened rate volatility
    * Tactical recalibration implemented using empirical prepayment data, including cohort-level adjustments to better capture issuer, vintage, and coupon effects
    * Medium-severity finding raised to track remediation of underlying model limitations, with strategic enhancements in progress

⸻

If you want to make it even tighter/more “board-ready,” I can compress this into 2 bullets total.




Here’s a clean, manager-level summary of required deck changes based on the transcript. I’ve grouped them by section and prioritized what actually matters for the FRB discussion.

⸻

🔴 Key Required Changes (High Priority)

1) Reframe overall meeting approach

* Add an explicit statement upfront (agenda or opening slide):
    * “No material changes across standard items (1–7); focus on AI and Emerging Risk per FRB request”
* Be prepared to skip quickly through Sections 1–7
* Ensure AI + Emerging Risk sections are crisp and discussion-ready

⸻

2) IA Findings Slide – Fix status clarity

Issue:

* Findings marked “open” despite remediation completed

Fix:

* Update status wording to:
    * “Completed by management, pending IA validation”
* Do NOT add a new column, just update wording
* Ensure consistency especially where:
    * Due dates are already past

⸻

3) Emerging Risk Slide – Major rewrite needed

This is the most important content gap

A. Add top-line takeaway (VERY IMPORTANT)

* Add a highlighted box (committee-style) at top:
    * “Q1 market volatility (rates, commodities) did not result in material model performance issues, with isolated exceptions addressed via model changes”

⸻

B. Fix content framing (current issue: too market-focused)

Problem:

* Reads like a market update, not model risk

Fix:

* Reframe to:
    1. Start with market context (1 sentence only)
        * Include interest rates (missing today – critical gap)
    2. Then focus on:
        * Model performance
        * Model issues (if any)
        * Model changes / PCCs triggered

⸻

C. Add missing key risk driver

* Include:
    * Interest rate volatility (Europe + global) ← explicitly called out as biggest omission

⸻

D. Anchor on model-specific example (mortgage)**

Add:

* Mortgage prepayment model issue:
    * Deteriorating performance under rate volatility
    * Led to:
        * Elevated IR exposure
        * Tactical fix implemented
        * Strategic fix underway
* This is your best concrete “emerging risk → model impact” example

⸻

E. Remove / de-emphasize weak items

* Reduce focus on:
    * Geopolitics (unless tied to model impact)
    * Generic market commentary
* Avoid:
    * Cyber / crypto / broad themes (explicitly rejected in discussion)

⸻

F. Align with messaging goal

End state should clearly say:

* Models performed well overall
* Validation framework held up under stress
* Only targeted issues, already addressed

⸻

4) AI / GenAI Section – Add regulatory awareness

Add content:

* Reference prior FRB AI RFI (historical)
* Add forward-looking statement:
    * Anticipated new regulatory engagement (e.g., RFI / guidance)
* Position:
    * Current framework builds on existing model risk management (SR 11-7 alignment)

Style:

* Keep slide high-level
* Expect verbal deep dive during meeting

⸻

5) Explicitly mention SR 11-7 / potential SR 26-2 linkage

* Add light reference (don’t overdo detail)
* Signals preparedness for regulatory direction

⸻

🟡 Medium Priority Improvements

6) Ongoing Monitoring vs Emerging Risk – clarify separation

Issue:

* Overlap between sections

Fix:

* Ongoing Monitoring:
    * Focus = findings identified via monitoring process
* Emerging Risk:
    * Focus = external environment → model impact

Optional:

* Add verbal bridge:
    * “Related monitoring findings are discussed in subsequent section”

⸻

7) RAS Exception / Metrics (minor callout)

* Add verbal note (optional in slide):
    * Utilization reduced (e.g., 6 → 3)
    * Trending toward remediation

⸻

8) CCAR slide – keep but de-emphasize

* Keep for consistency
* Be ready to:
    * Only discuss if asked
* Optional:
    * Mention SEP findings briefly (may attract interest)

⸻

9) ICAP/ILAP inclusion – OK to keep

* Included for consistency with prior year
* No strong need to emphasize

⸻

🟢 Low Priority / Cosmetic

10) Consistency with FRAC deck

* OK to reuse:
    * RAS
    * Thematic updates
* No major changes required

⸻

11) Add “no material issues” narrative where applicable

Across sections:

* Reinforce:
    * “No significant model performance issues observed”
* This is a key FRB expectation

⸻

📌 Suggested Final Narrative Flow (What the deck should convey)

1. No material changes in core areas
2. Models performed well despite significant Q1 volatility
3. Isolated issue (mortgage) identified and addressed
4. Strong monitoring + validation framework
5. Proactive engagement on AI and upcoming regulation

⸻

✅ Bottom Line (If you only fix 3 things)

1. Rewrite Emerging Risk slide (top message + rates + mortgage example)
2. Fix IA findings status wording
3. Add AI regulatory context (RFI / forward-looking)

⸻

If you want, I can rewrite the Emerging Risk slide in CRO/FRB style (3–4 bullets, one-liners)—that’s the piece that will matter most in the meeting.




During validation, MRM identified an implementation issue where the agent generated incorrect document IDs; the subsequent fix reduced query failure rates from 12% to 0% and improved efficiency, including a 16% reduction in compute costs.

The review to date has not identified any AI use cases currently classified as high-risk under the Act



https://links.mail.crunchyroll.com/ls/click?upn=u001.fmz2KNz0bzCl9io0-2BZrlHGBXIMJvKEOlgTJ7710AVkDuw33XLBHX8j4DEFh26DfMo5ovXJ3061Ba4Bijpekt5JaxxmDMtWkQOOO-2BlIVJMEXZ-2FKdJyBdX-2FrraEcUmLUJo1AislBBrFRLu1lCg1eqaWKf0Ehb2f9W9hRmDvNYYoo7P4ws3JTIO0to-2BdfeSiV9hHrtBKZCq7-2BE5ndpo26D-2BDdt-2BjSkcV0knS9fI6Tv71N-2BE6gUQ1FaAWoN78xdw3Kt6Nsov5ouVskaSQ33nyEpqmw-3D-3D6lS4_3k0Qyb5Nmvu3PwJIsnaKeF-2FVqm5J72bfO-2BQnByZDUod0KG6AEdHTqRI-2BHgMujDyLPTKPrrmR-2B04cfDvti4X9WmEkh55wOJCYWUR7Ww5HtFkBa0gX8AMSAgwsHFm5eeRpViPpW6b0dq7IfHYWCkaEMLi59ZGikqy-2FohEwlBAjyW2TEGVZnYiIE-2FskMjXkLtAkG3ISgg0dvg2CVgdgL5DtQfjgUciinM7dUklAcvh7kx6MQz9gvA-2F6GtmKZmVnlALxMzMXU-2BK0r-2BVjIc-2F-2FwXWKa-2BxYufFWUFYKj7T2BYMu-2FhM26cYdiECGfY-2FkzcwIePSrxwI8qQA5cNPQ-2FXoQyJuOYrR8jYa8a9rGDzGYMRSWl8fxybUdqAo4Oc964rK5fJIpdovtqEI2JxcWJm56aI0s8RZICFsHb-2BjU-2BzZ9hr7Ekb-2FmYT5syQI0hSGI7V1TRWvPDyrYNtjU-2FfKf3a19kgD7YaA3zEz8avdDEHJ3UPiHXlb8Yg9np-2BleIXHfPTNj3SJymReb5gGxKuO-2Bf2nbZM8z-2BHqwNuOi2ZC9gqkV5Nm5vZI8nk1ojCZ1tFIqTq1ePoiwYACL3SR7yh9j9q56WVGsGrL0a29eLcAb6HGHYThoGrHWRp9Licdz4qTeYC6RdjxATMxad5AHbLpLujeeJ6vylbStYE3mELoWmHKQXWjXHnI-3D



Committee members emphasized there should be no need to avoid high-risk use cases, but such use cases require a higher bar for controls, governance and reporting


M365 Copilot

* Engineering provided an update on firmwide rollout and adoption of M365 Copilot, noting continued growth following recent feature enhancements
* The discussion covered roadmap priorities to improve usability and reduce adoption friction, including enhancements across Excel, Word and PowerPoint
* Committee members discussed productivity impact and governance considerations for declarative agents, with follow-ups to assess productivity metrics and clarify governance approach

⸻

AI Steering Group

* Engineering provided an update on plans to transition the current AI Steering Group to an AI Strategy Group to reflect increased maturity of divisional AI governance
* The proposed forum would focus on firmwide strategic alignment, including product roadmap, platform patterns and cross-divisional coordination
* Committee members supported the proposal and discussed maintaining visibility into divisional initiatives through centralized tools and repositories

⸻

EU AI Act

* Legal provided an update on the EU AI Act, including timeline, scope and ongoing firmwide assessment of potential high-risk use cases
* The discussion noted that existing governance broadly aligns with expected requirements, with targeted enhancements underway
* Committee members noted that high-risk use cases remain permissible with appropriate controls, with further policy and gap analysis in progress




M365 Copilot

* Engineering provided an update on firmwide rollout of M365 Copilot, noting adoption has continued to increase following expansion beyond the initial pilot and recent feature enhancements
* The discussion covered the product roadmap, user adoption trends, and planned capabilities intended to reduce adoption friction, including improvements in Excel, Word and PowerPoint functionality, as well as additional agent-related features
* Committee members asked about evidence of productivity gains from new features and governance considerations for declarative agents, with follow-ups to assess available productivity metrics and clarify governance and inventory expectations

AI Steering Group

* Engineering provided an update on plans to transition the current AI Steering Group to an AI Strategy Group, reflecting the increasing maturity of divisional AI governance and the need to reduce duplicative review processes
* The proposed future-state forum would focus on firmwide strategic alignment, including AI product roadmap decisions, common platform patterns, technical architecture, and cross-divisional coordination on significant AI initiatives
* Committee members were supportive of the proposed direction and discussed the importance of maintaining visibility into divisional AI initiatives through common repositories and centralized tools

EU AI Act

* Legal provided an update on the EU AI Act, including the expected timeline, risk-based framework, and the firm’s ongoing assessment of potential high-risk AI use cases and related compliance requirements
* The discussion highlighted the distinction between provider and deployer obligations, noting that while some targeted uplift may be required, much of the firm’s existing governance framework already aligns with the expected requirements
* Committee members noted that high-risk use cases should not be avoided where supported by business need, but would require a higher bar for controls, governance and reporting, with further policy and control gap assessment underway







Below is a draft aligned to the guidance, example, and skeleton you shared.

⸻

1. Materials: AIRCC Materials dated April 21, 2026

2. M365 Copilot Updates – Posting

The presenters provided an update on the deployment, adoption trends and 2026 roadmap for Microsoft 365 Copilot, including native Copilot capabilities, supporting enablement work and items expected to return to the committee for review. The presenters noted that deployment expanded beyond the initial 1,000-user pilot and reached the 25,000 license cap ahead of target, with firmwide release beginning on April 7, 2026. As of the meeting date, approximately 53,000 users had been enabled, with remaining users primarily requiring attestation prior to access.

The presenters reviewed adoption metrics and user activity trends, noting increased usage across applications and improved product stickiness, with particularly strong recent growth in Excel usage following Microsoft feature enhancements. The presenters also summarized user feedback and adoption friction themes, including prior limitations in web data access, the need for broader work data integration, continued enhancement needs in PowerPoint and Excel, prompting challenges and the importance of additional training and broader license availability. The presenters noted that the roadmap is intended in part to address these adoption friction themes.

In response to a committee member question regarding the functionality previously described as “agent mode” in Excel, PowerPoint and Word, the presenters clarified that Microsoft had rebranded the feature to “edit with Copilot.” The presenters explained that the feature enables step-by-step actions and editing through natural language instructions, including updating recurring Word documents using templates and analyzing or manipulating Excel data without requiring users to create macros or pivot tables manually. The presenters further noted that PowerPoint functionality remains less mature, particularly with respect to updating presentations with new data while preserving formatting, and stated that related enhancements would return to the committee in due course.

A committee member asked whether the firm or Microsoft had data regarding productivity improvements associated with Copilot and newly released features. The presenters explained that Microsoft does not currently provide firm-specific productivity data of that kind and that internal analysis has instead focused on usage growth and “power user” activity patterns. Committee members noted that a more structured view of productivity gains by feature type would be valuable to support prioritization, training and deployment decisions, and requested follow-up on whether additional internal or Microsoft-provided productivity metrics could be developed or obtained.

The presenters then described declarative agents and related capabilities, noting that such agents function as scoped or customized Copilot experiences with predefined instructions and permitted data sources. In response to committee questions, the presenters explained that declarative agents can use structured instructions and defined steps, but do not independently determine which steps to take. The presenters also demonstrated that these agents can be configured with source restrictions and shared with specific individuals through links, but are not intended for broad organization-wide deployment without going through a different process. Committee members requested clarification on governance, including whether declarative agents should be captured within broader agent governance, registration and inventory processes. The presenters confirmed that these agents are administered through an internal portal and that an inventory exists, and agreed that governance treatment should be discussed further with relevant stakeholders.

The presenters also provided a preview of upcoming capabilities, including Anthropic model integration and Teams meeting functionality, and noted that those items would be brought back to the committee. Committee members highlighted the importance of beginning parallel discussions with Legal and Compliance on meeting-related capabilities. In response to questions regarding model choice, the presenters explained that administrative controls are expected to allow functionality to be enabled or suppressed by jurisdiction where needed.

The following follow-ups were recorded:

1. Assess whether additional productivity metrics can be obtained or developed, including from Microsoft
2. Discuss governance, registration and inventory treatment for declarative agents

3. AI Steering Group Update – Posting

The presenters provided an update on a proposed change to the remit and structure of the current AI Steering Group. The presenters explained that, as the firm’s AI governance and adoption have matured, much of the review and execution work now occurs within divisions, and the existing forum has increasingly functioned as a ratifying body rather than as the primary decision-making forum for business proposals. The presenters further noted that the current process can create duplicative governance and administrative burden for submitters.

Against that backdrop, the presenters proposed retiring the current AI Steering Group and replacing it with an AI Strategy Group. The presenters explained that the proposed forum would be intended to provide strategic alignment across the firm, including endorsement of product roadmap changes, review of common AI patterns that may warrant central solutions, discussion of strategic technical architecture decisions, and reporting by divisions on their most significant AI initiatives. The presenters noted that the proposed group would also serve as a forum for broader cross-firm discussions on topics such as evaluation strategy, token economics, training and adoption, and the evolving regulatory and control landscape.

The presenters stated that the proposed forum would be chaired by senior Engineering leadership, with membership to be solicited from divisional business and engineering leaders. The presenters further noted that the group would meet bi-weekly and that escalations would continue to be directed to AIRCC, PSG and other existing governance forums as appropriate.

A committee member noted that, although the existing forum was not designed primarily as a repository for divisional initiatives, submitted materials had been useful in helping teams understand what other divisions were already working on and in identifying opportunities for reuse or collaboration before matters reached AIRCC. In response, the presenters clarified that the proposal was not intended to eliminate divisional submission processes, but rather to shift decision-making to the divisional level while preserving common repositories and moving toward more centralized tooling to improve visibility across the firm. The presenters noted that investment in central repositories and tools is underway.

Committee members were supportive of the proposed direction and noted that the revised structure appeared more efficient while preserving the ability to coordinate strategically across the firm.

4. EU AI Act Updates – Posting

The presenter provided an update on the European Union AI Act and the firm’s work to prepare for the next stage of implementation, with particular focus on the rules applicable to high-risk AI systems. The presenter noted that the high-risk AI requirements are currently expected to take effect in August 2026, although there remains a possibility that implementation could be delayed, with formal confirmation still pending.

The presenter summarized the Act’s risk-based framework, including prohibited AI, high-risk AI, transparency requirements and general purpose AI requirements, and explained the distinction between “provider” and “deployer” roles under the Act. The presenter noted that the obligations applicable to providers are materially more extensive than those applicable to deployers and that this distinction therefore has practical significance for the firm.

The presenter then discussed the types of use cases most likely to be relevant to the firm’s high-risk assessment, including use cases in Human Capital Management relating to recruitment and employment decisions, use cases in Compliance relating to workforce monitoring, and use cases in businesses that lend to natural persons. The presenter also described the statutory exemptions, noting that they are expected to be interpreted relatively narrowly and that a human review step alone is unlikely to be sufficient to avoid high-risk classification where the AI system is performing a material evaluative task.

The presenter further explained that the provider requirements are extensive and include lifecycle risk management, quality management, data governance, accuracy, robustness, cybersecurity and post-market monitoring obligations. The presenter noted, however, that the firm already performs many related activities and that a significant portion of the implementation effort is expected to involve mapping existing controls, policies and procedures to the regulatory requirements in a way that can be clearly evidenced. The presenter also noted that there will nevertheless be some gaps where new requirements do not map cleanly to the current framework.

The presenter summarized the progress made to date, including review of adopted AI systems, outreach to divisions and assessment of potentially relevant use cases. The presenter stated that one potentially high-risk use case had been identified and reviewed in detail and that the review concluded it would not be captured as high-risk in light of how it is structured, and that an exemption would likely also have been available if needed.

Committee members emphasized that the firm should not be deterred from pursuing high-risk use cases where justified by business needs, but should instead recognize that such use cases carry a higher bar for controls, governance and reporting. Committee members also noted that a large working group led by Engineering has been reviewing deployed systems against the Act in advance of the rules becoming effective, so that the firm has visibility into its inventory and can identify potential issues early. The presenter stated that a gap analysis comparing existing policies and procedures against the Act has been completed and is under review, and that the next phase will involve engagement with stakeholders and policy owners on proposed policy, standards and control uplifts.

5. Administrative Matters

The secretary posted materials regarding the expansion of Claude Code. The secretary noted that the committee had previously approved Claude Code for up to 1,000 engineers and had requested a follow-up on learnings from that rollout, which was included in the materials. The secretary also noted that the committee chairpersons had approved further expansion to general availability on behalf of the committee, and that this decision was being posted to the committee.

The secretary also referred the committee to the AIRCC quarterly reporting materials, which included low-risk use cases approved through the streamlined approval process, inventory metrics, Category 4 use cases classified during the quarter, and committee follow-up items.

The secretary then provided an informational update on revised interagency model risk guidance issued by the Federal Reserve, OCC and FDIC, which supersedes SR 11-7. The secretary noted that the guidance largely reaffirms core model risk management principles while placing greater emphasis on a risk-based and less prescriptive approach. The secretary further noted that the initial read is that the firm’s framework is broadly consistent with the revised guidance, given the existing materiality-based approach.

The secretary highlighted two elements of particular relevance to the committee. First, the revised guidance does not apply directly to generative AI and agentic AI, given their rapid evolution, although there remains an expectation that such systems be governed appropriately. Second, the guidance permits a lighter-touch approach for immaterial models, in a manner that appears broadly consistent with the firm’s existing Tier 4 approach. The secretary noted that this is reassuring in light of the firm’s approach to AI platforms and Tier 4 standards, and added that further evaluation is ongoing, including discussions with peers and external advisors regarding broader industry reaction.

6. Prior Meeting Minutes Approval: Minutes from the committee’s meeting held on March 24, 2026 were approved.

Having no further business to discuss, the chairpersons closed the meeting.

To the extent transaction(s) were discussed, no committee member raised issues related to the transactions regarding any (i) material conflict of interest, (ii) material exposure to high-risk assets or high-risk trading strategies that could significantly increase the likelihood that the firm could incur a substantial financial loss, or (iii) activity that would otherwise pose a threat to the safety and soundness of the firm or the financial stability of the United States.

⸻

I can also turn this into a slightly more concise version that reads even closer to the March 24 example.





Model Validation Activities

* MRM approved enhancements to the CS AI Agent (GBM Private, Tier 2), expanding its capability from single-deal research to multi-deal comparative analysis.
* The model leverages retrieval-based techniques to synthesize information across documents, enhancing question-answering capabilities.
* MRM analysis indicates strong performance, with approximately 94% accuracy across a large document set.

⸻

Regulatory Updates

* The FRB–MRM quarterly meeting is scheduled next week, with regulators requesting an update on generative and agentic AI governance and validation approach, including any recent or anticipated changes.



There have been several episodes of elevated market volatility across asset classes in recent months; however, no significant model performance issues have been identified to date based on MRM’s ongoing monitoring and targeted reviews

* Precious Metals Volatility
    * Gold and silver experienced sharp declines following the Jerome Powell nomination on January 30, alongside a broader correction after the prior year’s rally, with volatility extending into Asia trading hours before partially stabilizing
    * MRM performed targeted review of commodities trading models and did not identify any material performance issues
* Japan Rates – Bear Steepening
    * The Japan snap election announcement, combined with proposed fiscal measures (including a temporary food consumption tax cut), led to fiscal concerns and a pronounced bear-steepening in Japanese government bond yields, particularly at the long end
    * MRM reviewed models supporting Japan-related trading activity; flows have been predominantly client-driven (cash bond activity) and no significant model deficiencies have been observed
* Geopolitical Risk – Energy Markets
    * The US-Israel-Iran conflict contributed to a surge in oil and natural gas prices and elevated volatility in energy markets
    * MRM continues enhanced monitoring of relevant trading models, with no material performance issues identified to date





Timeline for MRM validation is compressed, with validation of the overarching PD model and revised ICRs targeted for completion by June 2026, and Large Corporate validation by July 2026, to support PRA submission in September 2026



    Backtesting indicated deteriorating prepayment projection performance in the Tier 1 GBM residential mortgage feeder model, which may result in over-projection of prepayments; model developers are undertaking recalibration to address the issue
* Backtesting results identified deficiencies in the fallback methodology within the Tier 1 GBM commodities franchise benchmark model for certain clients, where current logic mishandles data issues and is inconsistent with treatment across portfolios; model developers are investigating root causes and implementing targeted enhancements
* Ongoing monitoring reports indicated a decline in the precision metric for the Tier 2 Compliance surveillance model used to identify intraday stock price manipulation; model developers are investigating root causes and implementing enhancements where appropriate









including prepayment component modeling (e.g., age ramp-up effects), which are not fully addressed by the current top-level adjustment.Timeline for MRM validation is compressed, with validation targeted for completion by [MM/DD] to support submission to the PRA by [MM/DD]




Model submission timelines have been revised from the original March 31 deadline, with Corporate ICR and overarching Probability of Default (PD) models now expected in mid-May, and Large Corporate ICR models in mid-June.
	•	The revised timeline requires MRM to begin review of conceptual models ahead of full model submission, with an initial version of the overarching PD model already shared.
	•	Timelines for validation and remediation are compressed, creating potential execution risk as findings are addressed ahead of regulatory milestones.
Here is a fully refined CRO-style version — cleaned for clarity, grammar, flow, and consistent tone, while keeping it concise and executive-ready:

⸻

Top of Mind
	•	MRM is reviewing a mortgage pool pricing model (GBM Public, Tier 1) issue related to the treatment of the price floor, which may understate risk under stress due to inconsistent handling of duration and option-adjusted spread (OAS) shocks between pools and to-be-announced (TBA) securities.
	•	The issue arises from inconsistent treatment of payup in stress scenarios, resulting in misalignment between pool and TBA pricing and understated risk, with potential impacts across stress scenarios and VaR.
	•	Market Risk and Strats identified the issue during recent model enhancements; preliminary analysis indicates potential increases in risk measures and limit pressures post-fix.
	•	MRM will review the proposed fix once finalized, with updated impact assessments currently being refreshed based on latest market conditions.

⸻

Validation Activities
	•	MRM approved changes to the Mortgage Agency Feeder model (GBM Public, Tier 1) to address divergence between modeled and observed prepayments, which had led to elevated interest rate sensitivity (IRDV01) for the collateralized mortgage obligations (CMO) desk.
	•	The issue was observed amid recent market volatility, with a limit breach under the IR +50bps stress scenario, for which a temporary limit increase was provided in March.
	•	Enhancements include tactical recalibration of prepayment assumptions using empirical data, incorporating cohort-level multipliers to better capture issuer, vintage, and coupon effects.
	•	MRM raised a medium-severity finding to track strategic remediation addressing underlying model limitations.
	•	CCR: MRM approved enhancements to the Franchise Interest Rates Benchmark model (GBM Public, Tier 1) to incorporate variation margin for repurchase agreements (repos) into the shortfall calculation.
	•	The enhancement addressed repo variation margin not being sourced or stressed, resolving the associated validation finding.
	•	Domestic Liquidity Sub Group (DoLSub): Validation of Phase 1 model changes is on track for completion by end of week, covering 11 models, qualitative approaches (QAs), and deterministic regulatory calculations (DRCs).
	•	During validation, additional enhancements to trapped liquidity calculations were submitted and approved, and the validation scope was expanded to include the 1-day Modeled Liquidity Outflow (MLO) calculation following MRM feedback.
	•	Medium-severity findings focus on methodology enhancements, including appropriate use of DoLSub-specific input data as it becomes available.

⸻

CCAR Exam
	•	The CCAR exam kickoff was held this week, with regulators indicating focus on scenario design assumptions, including private equity beta, and available-for-sale (AFS) loss modeling, with dedicated follow-up meetings scheduled.
	•	For GBM Trading Net Interest Income (NII) modeling, developers are targeting a May month-end submission of model enhancements to separately project interest income/expense and non-interest revenue, with MRM validation planned for August.

⸻

What improved
	•	Fixed typos and grammar (e.g., “modent cyntess” → “inconsistent treatment of payup”)
	•	Tightened wording to CRO-level clarity
	•	Standardized structure and tone across sections
	•	Reduced redundancy while preserving key risk messages

⸻

If you want, I can also compress this into a one-page CRO deck version (~30% shorter) or add “Top of Mind” headlines per bullet (Bill sometimes prefers that style).






Here is a fully refined CRO-style version — cleaned for clarity, grammar, flow, and consiste



nt tone, while keeping it concise and executive-ready:

⸻

Top of Mind
	•	MRM is reviewing a mortgage pool pricing model (GBM Public, Tier 1) issue related to the treatment of the price floor, which may understate risk under stress due to inconsistent handling of duration and option-adjusted spread (OAS) shocks between pools and to-be-announced (TBA) securities.
	•	The issue arises from inconsistent treatment of payup in stress scenarios, resulting in misalignment between pool and TBA pricing and understated risk, with potential impacts across stress scenarios and VaR.
	•	Market Risk and Strats identified the issue during recent model enhancements; preliminary analysis indicates potential increases in risk measures and limit pressures post-fix.
	•	MRM will review the proposed fix once finalized, with updated impact assessments currently being refreshed based on latest market conditions.

⸻

Validation Activities
	•	MRM approved changes to the Mortgage Agency Feeder model (GBM Public, Tier 1) to address divergence between modeled and observed prepayments, which had led to elevated interest rate sensitivity (IRDV01) for the collateralized mortgage obligations (CMO) desk.
	•	The issue was observed amid recent market volatility, with a limit breach under the IR +50bps stress scenario, for which a temporary limit increase was provided in March.
	•	Enhancements include tactical recalibration of prepayment assumptions using empirical data, incorporating cohort-level multipliers to better capture issuer, vintage, and coupon effects.
	•	MRM raised a medium-severity finding to track strategic remediation addressing underlying model limitations.
	•	CCR: MRM approved enhancements to the Franchise Interest Rates Benchmark model (GBM Public, Tier 1) to incorporate variation margin for repurchase agreements (repos) into the shortfall calculation.
	•	The enhancement addressed repo variation margin not being sourced or stressed, resolving the associated validation finding.
	•	Domestic Liquidity Sub Group (DoLSub): Validation of Phase 1 model changes is on track for completion by end of week, covering 11 models, qualitative approaches (QAs), and deterministic regulatory calculations (DRCs).
	•	During validation, additional enhancements to trapped liquidity calculations were submitted and approved, and the validation scope was expanded to include the 1-day Modeled Liquidity Outflow (MLO) calculation following MRM feedback.
	•	Medium-severity findings focus on methodology enhancements, including appropriate use of DoLSub-specific input data as it becomes available.

⸻

CCAR Exam
	•	The CCAR exam kickoff was held this week, with regulators indicating focus on scenario design assumptions, including private equity beta, and available-for-sale (AFS) loss modeling, with dedicated follow-up meetings scheduled.
	•	For GBM Trading Net Interest Income (NII) modeling, developers are targeting a May month-end submission of model enhancements to separately project interest income/expense and non-interest revenue, with MRM validation planned for August.

⸻

What improved
	•	Fixed typos and grammar (e.g., “modent cyntess” → “inconsistent treatment of payup”)
	•	Tightened wording to CRO-level clarity
	•	Standardized structure and tone across sections
	•	Reduced redundancy while preserving key risk messages

⸻

If you want, I can also compress this into a one-page CRO deck version (~30% shorter) or add “Top of Mind” headlines per bullet (Bill sometimes prefers that style).

The CCAR exam kickoff was held this week, with regulators indicating focus on scenario design assumptions, including private equity beta, and available-for-sale (AFS) loss modeling, with follow-up meetings scheduled for next week.
	•	For GBM Trading Net Interest Income (NII) modeling, developers are targeting a May month-end submission of model enhancements to separately project interest income/expense and non-interest revenue, with MRM validation planned for August.

Enhancements to the Tier 1 FLR models to expand bespoke modeling coverage and improve the accuracy of existing models, reducing reliance on fallback methodologies and improving rating accuracy


Mortgage Pool Pricing Issue
	•	MRM is reviewing a pricing model issue for mortgage pools related to the treatment of the price floor (pool price floored at TBA), which can lead to understatement of risk under stress scenarios due to inconsistent treatment of duration and option-adjusted spread (OAS) shocks between pools and TBA.
	•	The issue arises from the model not incorporating payup consistently in stress scenarios, resulting in misalignment between pool and TBA pricing and understated risk, with potential impacts across CSW, IR TopSheet, and VaR metrics.
	•	Market Risk and Strats have identified the issue during recent model enhancements, and a fix is in progress; preliminary analysis indicates potential for increased risk measures and limit pressures post-fix.
	•	MRM will review the proposed fix once finalized, with updated impact assessments currently being refreshed based on latest market conditions.

⸻

Slightly tighter version (CRO deck style)
	•	MRM is reviewing a mortgage pool pricing issue related to floor treatment, which may understate risk under stress due to inconsistent handling of payup and shocks.
	•	The issue was identified during recent model enhancements and may increase risk measures and drive limit pressures (CSW, IR, VaR) once corrected.
	•	A fix is in progress, with MRM review to follow upon completion and updated impact analysis underway.




Enhancements to the Tier 1 FLR models to remove prior conservative fallback treatments, increase use of bespoke modeling, and improve measurement accuracy, reducing reliance on fallback methodologies and the classification of exposures as high-yield, in response to a recent breach of the non-investment grade (non-IG) threshold



A The issue was observed in the context of recent market volatility, which contributed to increased risk usage for the business
	•	A limit breach occurred under the Interest Rate +50bps stress scenario, with a temporary limit increase provided in March to support business activity
	•	Elevated risk was driven both by market conditions and model underperformance, where the model underestimated prepayments relative to observed levels
	•	Lower modeled prepayments implied longer effective durations, resulting in higher IRDV01 and increased stress losses


new Tier 2 Global Banking & Markets (GBM) Public model used to simulate key equity volatility surface parameters and generate optimized portfolio weights for rebalancing, representing the first use of a transformer-based model within the equity options and futures trading business


E] Enhancements to the Tier 1 FLR models to better handle data errors and reduce reliance on fallback methodologies, which had resulted in an increased classification of exposures as high-yield
*** Enhancements were driven by an observed breach of the non-investment grade (non-IG) threshold




Market Risk Limits (Stress Scenarios only; excl. VaR)
	•	Limits applied across hierarchy (Board / Management / Department) and portfolio cuts (firmwide, desk)

GS Group
	•	Limits: 12 (Board) / 53 (Mgmt) / ~2.0k (Dept)
	•	Alerts: 0 (Board) / 5 (Mgmt) / ~1.0k (Dept)

GS Bank
	•	Limits: 10 (Board) / 40 (Mgmt) / 166 (Dept)
	•	Alerts: 0 (Board/Mgmt) / 316 (Dept)

Other LEs (Goldman Sachs International / Goldman Sachs International Bank / Goldman Sachs Bank Europe etc.)
	•	Limits: 15 (Board) / 108 (Mgmt) / 126 (Dept)
	•	Alerts: 0 (Board/Mgmt) / 182 (Dept)

Board-level scenario examples
	•	GMS severe adverse
	•	IR ±50bps (IR TopSheet)
	•	EQ -20% (EQ TopSheet)
	•	Credit spread widening (scaled; post-COVID methodology update)
	•	FX USD ±5%

Framework / recent changes
	•	2024 uplift introduced new scenarios + limits (MRIA-driven; closed 2025)

Recent development
	•	No new models driven by recent volatility
	•	US Volex Gross Vega: calibration update (data extended to Oct-2025 vs Q1-2023)
	•	Impact: ~+4% ( ~$775M → ~$805M )
	•	Under validation






Hi Miao,

Following our discussion with Bill on the FRAC deck, we wanted to better understand the ASL limit breach that was attributed to data inconsistency between first-line projections and Risk models.

Could you help clarify a few points:
	•	What was the exact root cause (e.g., collateral missing or differences in data inputs between models)?
	•	How long did the issue persist and which limits / portfolios were impacted?
	•	What remediation has been implemented (one-off fix vs broader solution)?
	•	Have any controls or monitoring been introduced to ensure consistency going forward?

We are looking to reflect this accurately in the FRAC materials, so any additional context would be helpful.



What actually happened (underlying issue)
	•	Limit breach observed
	•	A risk limit (likely FLR / tail risk / IG-related) showed a breach
	•	Root cause was NOT true risk increase
	•	Driven by data inconsistency between models, not underlying exposure
	•	Specific failure mechanism
	•	Trade initially assessed using 1st line projections (with collateral included)
	•	Shortly after, calculation switched to Risk model
	•	Collateral was missing / not captured properly
	•	Model either:
	•	Produced inflated risk, or
	•	Triggered a conservative fallback/backstop
	•	Result
	•	Artificial limit breach for a period (~weeks)
	•	Inconsistent outputs across systems



incorporating expanded GS proprietary datasets for system prompt refinement and testing, including human-tagged GS AI Assistant user prompts


Enhancements include a tactical recalibration of prepayment assumptions using empirical data, incorporating cohort-level multipliers to better capture issuer, vintage, and coupon effects.


MRM approved enhancements to the mortgage agency feeder model to address divergence between modeled and observed prepayments, which had resulted in elevated interest rate sensitivity (IRDV01) for the collateralized mortgage obligations (CMO) desk.
	•	The update improves alignment with observed prepayment behavior, resulting in a material shift in IRDV01.
	•	A validation finding has been raised for a more robust, strategic remediation, with work underway to address underlying model limitations.






The enhancement addressed repo variation margin not being sourced or stressed, resolving the associated validation finding


Fundamental Review of the Trading Book (FRTB), including ongoing validation work supporting incremental requirements, with recent approval of enhancements to the Tier 1 model used to construct 10-day returns from 1-day historical return time series to incorporate additional credit bond and mortgage risk factors



Fundamental Review of the Trading Book (FRTB), including ongoing validation work supporting incremental requirements, with recent approval of enhancements to the Tier 1 model used to construct 10-day returns from 1-day historical return time series to incorporate additional credit bond and mortgage risk factors


Approval of two Tier 2 Engineering models (M365 Copilot Web Grounding and AI Bing Search) that enable web search grounding for queries within M365 Copilot and GS AI Assistant for GPT models, respectively
*** Following approval, enhancements to AI Bing Search addressed validation findings related to (1) inconsistent activation of web search for certain queries and (2) over-reliance on individual search results, both contributing to increased hallucinations
*** Remediation included Engineering and Model Risk communicating feedback to Microsoft, which implemented updates to Azure infrastructure and model logic alongside GPT 5.2
*** Model Risk analysis indicates the updated version maintains consistent web search activation, better prioritizes authoritative sources, and adopts more conservative response behavior, resulting in improved answer quality and reduced hallucinations




Two Tier 2 Engineering models (M365 Copilot Web Grounding and AI Bing Search) that enable web search grounding for queries within M365 Copilot and GS AI Assistant for GPT models, respectively
*** Enhancements to AI Bing Search addressing validation findings related to (1) inconsistent activation of web search for certain queries and (2) over-reliance on individual search results, both contributing to increased hallucinations
*** Following validation, Engineering and Model Risk communicated feedback to Microsoft, which implemented updates to Azure infrastructure and model logic alongside GPT 5.2
*** Model Risk analysis indicates the updated version maintains consistent web search activation, better prioritizes authoritative sources, and adopts more conservative response behavior (e.g., declining responses when source quality is low), resulting in improved answer quality and reduced hallucinations


enabling recognition of the portfolio’s collateralized nature and more accurately reflecting the risk profile of the exposures.


There is continued focus on development and validation work supporting the collateralized lending business, with recent approvals extending coverage of FLR and tail risk models to reduce reliance on fallback methodologies, and enhancing data inputs and methodologies to improve model accuracy



incorporating enhanced data inputs for collateral valuation and stress calibration, and methodology enhancements to upstream pricing and collateral price dynamics, resulting in improved accuracy and addressing validation findings


extending coverage to asset classes currently handled through fallback methodologies, incorporating enhanced collateral-level data, updates to valuation and stress calibration approaches, and improved modeling techniques such as interest rate swap integration and refined probability-of-default methodologies, resulting in improved risk measurement accuracy and addressing validation findings


extending coverage to asset classes currently handled through fallback methodologies, incorporating enhanced data inputs and methodology updates, including improved collateral valuation and modeling approaches, and improving accuracy while addressing validation findings

Enhancements to Tier 1 Risk Engineering-owned models used to calculate facility-level ratings (FLR) and tail risk measures, extending coverage to asset classes currently handled through fallback methodologies, incorporating enhanced data and methodology improvements, and improving accuracy while addressing validation findings


Migration of the Equity Trading Cost Model (TCM) is underway to replace the legacy model, with an MRM finding tracking delays and a potential FRAC breach on May 28
	•	Migration is currently blocked by key technical gaps including lack of support for non-full day orders, futures requiring a separate model, and missing EMEA ETF coverage
	•	Non-full day order support remains under discussion with GSET to enhance API capabilities across all order times (Asia EDHF impacted)
	•	Futures TCM API is in development (target Q2/Q3), with users required to choose between legacy and new models and justify selection to MRM; most models currently have no committed ETA
	•	EMEA ETF support and broader migration remain delayed due to market conditions and capacity constraints, with limited ETAs (EMEA end-April, others pending) and several downstream models still without timelines



There is continued focus on Counterparty Credit Risk (CCR) model enhancements, including approvals of enhancements to the Tier 1 interest rate franchise benchmark model to align stress loss aggregation with the CREST framework as part of ongoing harmonization efforts, enhancements to the Tier 1 Prime Brokerage (PB) equity margin model to incorporate composite average daily volume (ADV) for European stocks in the Delta liquidation charge, and enhancements to the Tier 1 commodities franchise benchmark model to allow netting of offsetting exposures in the US natural gas Delta liquidation charge, resolving a validation finding

enhancements to the Tier 1 modeled liquidity outflow (MLO) models to capture liquidity impacts from digital assets and SIMM initial margin (IM) collateral as part of ongoing efforts to improve model coverage and reduce reliance on overlays, and enhancements to the Tier 1 Prime Tail Liquidity Loss (PTL) model, resulting in an improvement in the firm’s PTL ratio


Here’s a refined version of your Executive Summary – Validation activity over the quarter, keeping “There is…”, improving flow, and maintaining your style:

⸻

Validation activity over the quarter:

** There is continued growth in Artificial Intelligence (AI) models and use of new techniques, including approvals of:
*** Enhancements to the Tier 1 generative AI model designed as a monitoring framework for the GS AI Platform, incorporating expanded GS proprietary datasets for prompt refinement and testing using human-tagged GS AI Assistant user prompts, and an upgraded large language model (LLM)
*** A new Tier 1 Corporate Treasury generative AI model to automate matching of incoming payments, with phased rollout alongside the current review process and improved performance following remediation of validation findings
*** A new Tier 2 Global Banking & Markets (GBM) Public model used to predict distributions of equity market variables and generate optimized portfolio weights, representing the first use of a transformer-based architecture within the equity options and futures trading business

** There is continued focus on validation work supporting the Collateralized Lending business, including approvals of:
*** A new Tier 1 model estimating through-the-cycle loss given default (LGD) for use in facility-level rating (FLR) calculations for GS Select performing loans, enabling recognition of the collateralized nature of the portfolio and supporting Treasury’s initiative to pledge GS Select exposures to the Federal Reserve discount window
*** Enhancements to Tier 1 Risk Engineering-owned models used to calculate facility-level ratings (FLR) and tail risk measures, extending coverage to asset classes currently handled through fallback methodologies, improving accuracy and addressing validation findings

** There is continued focus on validation work related to liquidity risk model enhancements, including approvals of:
*** Enhancements to the Tier 1 modeled liquidity outflow (MLO) models to capture liquidity impacts from digital assets and SIMM initial margin (IM) collateral, as part of ongoing efforts to systematically capture liquidity overlays and improve model robustness
*** Enhancements to the Tier 1 Prime Tail Liquidity Loss (PTL) model, resulting in an improvement in the firm’s PTL ratio

⸻

If you want, I can next:
	•	Tighten this further into a CRO / Board-level ultra-short version
	•	Or align wording exactly with your Q4 Executive Summary for consistency across quarters

Approval of a new Corporate Treasury generative AI model (Payment Settlements AI) to automate matching of incoming payments, with phased rollout alongside the current review process and improved performance following remediation of validation findings



Engineering will follow up on governance and controls for Model Context Protocol (MCP) servers and other recent GS AI Assistant enhancements, as well as provide a future update on the effectiveness of implemented AI guardrails


The model generates draft commentary on financial performance and risk drivers, with no impact on internal credit ratings (ICR), which remain fully determined by Credit Risk reviewers.


The application generates structured first drafts of validation documents based on user inputs, including template selection, model documentation, and MRM commentary, supporting more efficient document preparation.


Here is a refined CRO-style AI update, making it clearer, more concise, and business-focused, while keeping the structure.

⸻

Top of Mind
	•	ValDoc Assistant, a generative AI application developed by MRM, has been rolled out across MRM to support drafting of validation documents.
	•	The tool generates fully formatted first drafts in a single step, reducing drafting time for simpler models from several days to a few hours.
	•	MRM validators remain fully accountable for the underlying analysis and final document quality.

⸻

AI Risk and Controls Committee (AIRCC)
	•	Engineering provided an update on the GS AI Platform and GS AI Assistant, including the enablement of agent-to-agent (A2A) interactions, supported by a centralized agent registry.

⸻

Validation Activities
	•	MRM approved Commentary AI (Risk, Tier 2), a generative AI model used to draft risk factor narratives for financial institution credit reviews.
	•	The model operates as an analyst-assist tool with mandatory human-in-the-loop review prior to use in final outputs.
	•	A high-severity validation finding in the initial version, related to generation of unsupported statements, has been remediated prior to approval through prompt enhancements and implementation of a critic control to detect and flag unsupported content for analyst review.

⸻

Internal Audit Updates
	•	Internal Audit concluded an “Effective” rating for the audit of the Firmwide AI Standard and its enforcement mechanisms, confirming that governance and processes are operating as designed.

⸻

If you want, I can also tighten this further into ultra-compressed CRO deck format (≈20–30% shorter) or align tone exactly with your non-AI CRO updates.



Here’s a refined version of your Risk section, keeping it structured, neutral, and consistent with earlier sections:

⸻

Risk
	•	Liquidity risk model enhancements, including approvals of:
** Enhancements to the Prime Tail Liquidity Loss (PTL) model (Risk, Tier 1), resulting in a material improvement in the firm’s PTL ratio
*** The PTL ratio measures mitigants, such as overnight debits, relative to short-term funding exposure under a post-modeled liquidity outflow (MLO) tail risk scenario, and is subject to FRAC and BRC limits
*** Enhancements include incorporation of previously omitted synthetic term commitments and additional margin-related mitigants, such as inflows from excess margin for certain clients

** Enhancements to the Modeled Liquidity Outflow (MLO) models (Risk, Tier 1) to capture liquidity impacts from digital assets and SIMM initial margin (IM) collateral
*** Enhancements reduce reliance on methodological overlays in MLO to zero, remediating two validation findings
*** Part of ongoing efforts to systematically capture liquidity impacts and improve model robustness
	•	Fundamental Review of the Trading Book (FRTB): Continued focus on validation work related to new FRTB requirements, including approval of an enhancement to the Tier 1 FRTB IMA 10-Day Returns model to incorporate additional credit bond and mortgage risk factors
** The model constructs 10-day returns using 1-day historical return time series for risk factors
	•	GSBE Internal Capital Adequacy Assessment Process (ICAAP) / Internal Liquidity Adequacy Assessment Process (ILAAP): Validation completed ahead of mid-March ECB submissions, covering 57 models and 2 qualitative approaches (QAs) for ICAAP and 22 models and 11 QAs for ILAAP
** Notable work included new methodologies for interest rate and credit spread risk in the banking book, enhancements to VaR stress calibration, and an overlay reflecting expected FRTB-SA implementation, along with related updates also applied in CCAR

⸻

If you want, we can next:
	•	Convert this into a short Executive Summary version
	•	Or align phrasing tightly with your Q4 Risk section for consistency across reporting cycles
	•	Or do a full-document consistency pass before finalizing the deck



*** Enhancements to the interest rate franchise benchmark model to align stress loss aggregation with the CREST framework, as part of ongoing harmonization of shortfall benchmark models, resulting in reduced stress losses and improved backtesting performance across client portfolios
*** Enhancements to the Prime Brokerage (PB) equity margin model to incorporate composite average daily volume (ADV) for European stocks in the Delta liquidation charge, aggregating trading volume across venues within the same currency and aligning with the US approach
*** Enhancements to the US natural gas Delta liquidation charge within the commodities franchise benchmark model to allow netting of offsetting exposures, resolving a validation finding


Here’s a cleaned and aligned version of your Global Banking & Markets section, keeping the structure and tone consistent with prior sections:

⸻

Global Banking & Markets
	•	Validation activity during the period primarily related to:

** Risk management enhancements, including approvals of:
*** Incorporation of control variates into the Tier 1 pricing model for multi-asset autocallables, aligning model outputs more closely with market prices, reducing Monte Carlo variance, and improving stability of risk measures
*** A new Tier 1 model for estimating vega risk in commodity products, using an improved numerical approach for greater accuracy and deployed on Griffin infrastructure for faster calculation compared to the previous CPNL platform

** Valuation adjustments, including approval of:
*** Enhancements to the Tier 1 model used for survival curve construction for Credit Valuation Adjustment (CVA), enabling implied CDS spreads for counterparties without liquid CDS markets

** CCR model enhancements, including approvals of:

⸻

I left the last section open so you can continue adding bullets under CCR model enhancements.

If you want next step, I can:
	•	Help draft the CCR bullets in the same style
	•	Or tighten this further for Executive Summary consistency
	•	Or ensure terminology matches Q4 (e.g., “risk measures”, “faster calculation”, etc.)


Here’s a refined version of your Collateralized Lending section, keeping the structure, improving flow, and ensuring consistency with your style:

⸻

Collateralized Lending
	•	Continued focus on development and validation work supporting the collateralized lending business, including approvals of:

** A new Tier 1 model estimating through-the-cycle loss given default (LGD) for use in facility-level rating (FLR) calculations for GS Select performing loans
*** Supports Treasury’s initiative to pledge GS Select exposures to the Federal Reserve discount window, enabling recognition of the collateralized nature of the portfolio and avoiding an increase in reported high-yield exposures

** Enhancements to the Tier 1 FLR and tail risk models for Residential Mortgage to cover hybrid fix-and-flip and lot loan transactions, extending coverage to asset classes previously handled through fallback methodologies and improving accuracy

** Enhancements to the Tier 1 Residential Mortgage tail risk model to incorporate interest rate swaps into collateral valuation, leveraging more comprehensive collateral-level data and improving tail risk measurement

** Enhancements to the Tier 1 transport tail risk model, incorporating new data for stress calibration, updates to upstream pricing including an index-based approach for lease probability of default, and improved differentiation between performing and non-performing leases, addressing prior validation findings

** Adoption of Merton jump diffusion and conditional probability-of-default mapping in Tier 1 FLR models for margin loans and private equity facilities, improving capture of collateral price dynamics

⸻

If you want, I can next:
	•	Tighten this into a short Executive Summary version
	•	Or align wording with your Q4 collateral section so the narrative is consistent across quarters (this is usually important for FRB readers)


Here’s a refined version of your Q1 Artificial Intelligence section, keeping your structure, neutral tone, and plain language, while tightening phrasing and improving consistency:

⸻

Artificial Intelligence
	•	Continued growth in the development of AI models, including approvals of:

** Enhancements to the Tier 1 Engineering Guardrail model for large language models (LLMs), used as a monitoring framework for AI usage across the GS AI Platform
*** Enhancements include expansion of GS proprietary datasets for prompt refinement and testing, incorporating human-tagged GS AI Assistant user prompts, and an upgrade to Gemini 2.5 Flash with refined system prompts

** A new Tier 1 Corporate Treasury generative AI model (Payment Settlements AI) used to automate matching of incoming payments
*** Three high-severity findings related to performance, evaluation metrics, and testing were remediated through scope restrictions, enhanced performance monitoring, and expanded test coverage, resulting in improved performance and oversight
*** The model will be rolled out in phases, initially operating in parallel with the current review process and targeting a reduction in manual review of cash receipts from 13% to 2%

** A new Tier 2 GBM Public model (Market Simulator (Albert)) used to predict distributions of equity market variables and generate optimized portfolio weights subject to constraints
*** The model represents the first use of a transformer-based architecture within the equity options and futures trading business

** Enhancements to the Tier 2 Engineering model (AI Bing Search), used to provide web search grounding for queries within GS AI Assistant for GPT models
*** Validation findings related to inconsistent activation of web search and over-reliance on individual sources, leading to increased hallucinations
*** Engineering and Model Risk communicated feedback to Microsoft, which implemented updates to Azure infrastructure and model logic alongside GPT 5.2
*** Model Risk analysis indicates improved consistency in web search usage, better prioritization of authoritative sources, and more conservative response behavior, resulting in improved answer quality and reduced hallucinations

** Lower-tier generative AI models supporting tasks such as data extraction, search enhancement, and information retrieval, developed primarily to improve productivity

⸻

If you want next step, I can:
	•	Turn this into a short Executive Summary version
	•	Or tighten further for Board-level (very compressed bullets)
	•	Or align wording with your Q4/Q3 AI sections for consistency across quarters



ValDoc Assistant, a generative AI application developed by MRM, has been released to support drafting initial versions of validation documents, improving efficiency in document preparation.
	•	The assistant is intended for use as a drafting aid, with MRM validators retaining full responsibility for the quality, accuracy, and completeness of the final documentatio




Consistent with Q3 2025 results, Securities Financing Transactions (SFTs) continue to exhibit a higher number of small-magnitude exceptions relative to other product groups

Engineering provided an update on the GS AI Platform and GS AI Assistant, highlighting the enablement of agent-to-agent (A2A) interactions for applications on the platform, supported by a centralized agent registry




MRM assessment: MRM evaluated all backtesting exceptions to assess whether they are attributable to model deficiencies
	•	No exceptions were identified as being driven by material model deficiencies
	•	Overall model performance remains stable relative to Q2 2025, with additional exceptions in commodities primarily driven by the precious metals rally in 2H25
	•	Distributional backtesting indicates satisfactory model performance
	•	MRM continues to find Potential Exposure (PE) models fit for purpose at the Group level


Market Risk
	•	MRM reviewed Q4 2025 backtesting results across GS Group and all legal entities subject to standalone capital requirements, including relevant desk-level sub-portfolios
	•	[Placeholder: Brief comment on Q1 2026 VaR breaches and associated multiplier impact (e.g., increase to 3.5)]
	•	[Placeholder: Brief reference to SVaR and IRC model performance and any notable observations]
	•	Review approach: Where breaches occur, MRM assesses potential drivers including risk factor data quality, proxy usage, unmodeled risk factors, and model conservatism at both portfolio and sub-portfolio levels
	•	[Placeholder: Commentary on treatment of RFI / non-VaR risk factors and rationale for continued exclusion from VaR framework]
	•	Backtesting outcomes: One new backtesting breach was observed for GS Group in Q4 2025
	•	The total 99% positional P&L breach count over a 250-day window was 3 as of December 2025 month-end
	•	MRM did not identify any breaches attributable to poorly modeled risk factors; observed breaches were primarily driven by market movements
	•	[Placeholder: Reference to any new risk factors (e.g., 2 additions in RFI report) and impact, if any]
	•	MRM assessment: MRM continues to find the Value-at-Risk (VaR) model fit for purpose at the Group level
	•	[Placeholder: Optional concluding statement covering SVaR / IRC and overall capital model framework if needed]



Monitoring of model performance was established to address this limitation, including comparison of realized and implied volatility, with escalation to the front office or application of capital add-ons where implied volatility is lower than realized


The model was developed and validated on an accelerated timeline to support Treasury’s initiative to pledge GS Select exposures to the Fed discount window, enabling recognition of the collateralized nature of the portfolio and avoiding a significant increase in reported high-yield exposures.



Market Risk
	•	MRM reviewed Q4 2025 backtesting results across GS Group and all legal entities subject to standalone capital requirements, including relevant desk-level sub-portfolios
	•	Review approach: Where breaches occur, MRM assesses potential drivers including risk factor data quality, proxy usage, unmodeled risk factors, and model conservatism at both portfolio and sub-portfolio levels
	•	Backtesting outcomes: One new backtesting breach was observed for GS Group in Q4 2025
	•	The total 99% positional P&L breach count over a 250-day window was 3 as of December 2025 month-end
	•	No poorly modeled risk factors were identified among the breach drivers
	•	MRM assessment: MRM continues to find the Value-at-Risk (VaR) model fit for purpose at the Group level

⸻

Credit Risk
	•	MRM reviewed Q3 2025 backtesting results for GS Group; Q4 results have not yet been provided to MRM
	•	Review approach: For observed breaches, MRM assesses whether exceptions are attributable to model deficiencies
	•	Backtesting outcomes: MRM is investigating the persistently high frequency of small-magnitude backtesting breaches (less than 5% of average PE) observed in Securities Financing Transactions (SFTs)
	•	Finding remediation: One medium-severity finding raised in Q2 has been remediated and closed
	•	During review of backtesting results for inflation-linked products within the interest rate Potential Exposure (PE) model, MRM observed increased long-horizon exceptions during periods of inflation regime transition, indicating limitations in the model’s ability to capture risk in such environments
	•	The finding was closed on February 25, 2026, following implementation of enhanced monitoring processes
	•	MRM assessment: Backtesting results remain stable relative to Q2 2025, with additional exceptions in commodities primarily driven by the precious metals rally in 2H25
	•	Distributional backtesting indicates satisfactory model performance for these products
	•	Overall, MRM continues to find Potential Exposure (PE) models fit for purpose at the Group level


Adoption of agentic AI is accelerating and introduces heightened risk, as models can take autonomous actions and interact with systems, requiring stronger controls around access, decision-making, and human oversight
	•	Current governance remains high-level and is being enhanced, with MRM and Risk working to define more prescriptive minimum standards (e.g., evaluation frameworks, monitoring, and traceability) to support safe and scalable deployment


Submission of Probability of Default (PD) models to MRM is delayed beyond the initial March 31 deadline to the 3rd–4th week of April, as Credit Risk and Strats finalize key design changes.
	•	The redesign is driven by low rating accuracy in Large Corporate exposures, evidenced by elevated override rates, with final design decisions expected by end of this week.

MRM re-approved the IRP CVA Bond Survival model (Tier 1) following additional validation, supporting CDS spread implication for counterparties without liquid CDS markets using bond, loan, formula-based, and fallback approaches
	•	Validation focused on robustness of the spread construction waterfall, covering proxy CDS, bond/loan automarkers, and formula-based spreads, ensuring appropriate survival curve construction for CVA/FVA calculations
	•	Three key findings were raised, including (i) enhancements to spread construction methodology, (ii) further investigation of spreads implied from callable bonds and loans, and (iii) inconsistencies in recovery assumptions between bond and loan automarkers
	•	Model methodology relies on calibration of survival curves from market instruments (bonds/loans), with adjustments (e.g., recovery assumptions) applied to align implied CDS spreads, though limitations in recovery treatment and non-linearity were identified
	•	Enhanced validation and remediation actions are required, particularly around recovery calibration and spread consistency, to improve robustness of CDS spread inference for illiquid counterparties



MRM approved enhancements to the Franchise Interest Rates Benchmark Model (FFIRBM, Tier 1) to align stress loss aggregation with CREST, switching the sequence to aggregate across currencies first, followed by risk factors (IR Spot, Inflation, etc.)
	•	Methodology retains IR stress scenarios targeting 99.7th percentile 5-day losses, with IR Spot continuing to use CREST “combo scenarios”; additional MRM testing confirmed adequate coverage of tail moves relative to full scenario set
	•	Recalibration of shocks across key IR risk factors (Spot, Inflation, Basis, Cross-currency) to address identified weaknesses, with updates focused on factors with material impact on live portfolios
	•	Model impact is a ~$14bn reduction in IR stress losses (e.g., ~$91bn → ~$77bn in full QA), primarily driven by removing overly conservative assumptions that ignored cross-currency diversification; aggregation change itself is not the main driver
	•	Backtesting performance improved materially, with breach levels reduced (~$270mm → ~$19mm, further to ~$10mm), enabling removal of overlays and closure of a validation finding; however, residual calibration concerns remain, leading to a new Severity 3 




MRM approved enhancements to the GSS PB Equity Delta Liquidation Charge model (v30) to introduce composite ADV for European stocks, aggregating trading volume across all venues within the same currency (aligned with existing US composite volume approach)
	•	Change impacts liquidation cost estimation methodology, where ADV is a key input to scale liquidation costs by position size; netting methodology remains unchanged
	•	Model impact is a ~$1.7bn reduction in total liquidation charge (from ~$13.5bn), reflecting higher composite liquidity assumptions for European equities
	•	MRM performed benchmarking of the 60-day ADV averaging window against alternative approaches used across business lines, with current calibration deemed appropriate
	•	Enhancement aligns with broader UBM migration, with composite ADV methodology and calibration approach expected to be incorporated into the Unified Benchmark Model under separate approval



CCR: MRM approved an enhancement to the Franchise Interest Rates Benchmark model (GBM, Tier 1) to better align stress loss aggregation with the CREST credit framework
	•	Aggregation methodology updated to first aggregate across currencies, followed by risk factors (e.g., IR Spot, Inflation)
	•	Part of broader shortfall benchmark harmonization, resulting in reduced stress losses and improved backtesting performance across client portfolios

FRTB: Continued validation progress against new FRTB requirements, including approval of an enhancement to the FRTB IMA 10-Day Returns model (Risk, Tier 1)
	•	Enhancement incorporates additional credit bond and mortgage risk factors into the 10-day return construction
	•	Model continues to derive 10-day returns from 1-day historical risk factor time series

ASL: MRM approved the FLR GS Select model (Risk, Tier 1) for GS Select performing loans
	•	Model estimates through-the-cycle LGD for use in facility-level rating (FLR) calculations




CCR:
	•	MRM approved enhancements to the Franchise Interest Rates Benchmark model (GBM, Tier 1) to better align stress loss aggregation with the CREST credit model.
	•	The change reorders aggregation to currencies first, then risk factors, improving consistency across benchmark models.
	•	The enhancement supports ongoing model harmonization, resulting in lower stress losses and improved backtesting performance across client portfolios.

⸻

FRTB:
	•	Continued validation focus on new FRTB requirements, including approval of enhancements to the FRTB IMA 10-Day Returns model (Risk, Tier 1).
	•	Enhancements incorporate additional credit bond and mortgage risk factors, improving risk factor coverage in return construction.

⸻

Asset Secured Lending (ASL):
	•	MRM approved the new FLR GS Select model (Risk, Tier 1) to estimate through-the-cycle LGD for GS Select performing loans.
	•	The model supports facility-level rating (FLR) calculations, enhancing risk measurement for the ASL portfolio.



Overlay program communication
	•	Prepare explanation:
	•	Program structure
	•	Controls in place
	•	Risks (esp. risk limit arbitrage perception)
	•	Coordinate with Andreas



Prime Brokerage Vega Liquidation Issue

Finding
	•	Vega liquidation charge in SPIRE (v5/v30) is materially understated, driven by use of a flat multiplier (0.05) that does not reflect true liquidation costs
	•	Methodology limitations:
	•	Does not capture skew vega liquidation risk
	•	Uses a flat multiplier, failing to capture vega concentration effects
	•	Materiality has increased recently, as evidenced in ongoing monitoring
	•	Issue formally captured under Finding 73163

Remediation
	•	Interim fix: Multiplier increased from 0.05 → 5 in benchmark, resulting in ~$675mm increase in vega liquidation charges across clients
	•	Margin updates for impacted clients to follow
	•	Strategic fix: Migration to UBM (target Q2) to address structural limitations
	•	Further enhancement: Ongoing recalibration of CREST vega liquidation parameters (linked to FRAC Finding 66343) to ensure appropriate risk capture




CVA implementation remains highly decentralized, creating challenges in ownership, coordination, and timely responses
	•	A modeling limitation was identified for path-dependent derivatives, where the current approach may understate volatility due to loss of path information
	•	While the current impact is not material, this represents a methodological gap that could become more relevant if exposure to complex products increases


4) CCAR / CVA modeling concerns (technical but important)

Structural issues identified:
	•	Decentralized CVA ownership
	•	No clear accountability → risk of slow responses
	•	Incorrect modeling of path-dependent derivatives
	•	Regression approach loses path information
	•	Understates volatility (though currently low materiality)

👉 Key takeaway:
	•	Not a crisis today, but modeling correctness gap exists
	•	Likely to be probed by regulators if surfaced




Engineering identified and escalated the use of an unapproved AI coding tool (OpenCode), which was made available for download via the Software Acquisition Manager (SAM)
	•	Tech Risk issued a high-risk finding and Operational Risk opened an event, with SAM and Software Development Life Cycle (SDLC) teams conducting root cause analysis, impact assessment, and defining remediation actions
	•	A forward plan will be presented to AIRC, focusing on strengthening controls over the review and approval of open-source AI tools prior to internal distribution


ECB IMM Exam Findings: Closing meeting held; GS to submit response within two weeks; 18 findings raised including 1 F4 (outsourcing), multiple F3s (backtesting, IM modeling, GSBE approvals, EEPE coverage, EAD/RWA, documentation), and additional F2 validation/modeling gaps
	•	ECB AI Workshop: Scheduled for May 7; GS to submit materials by April 9 and April 23 covering AI governance, EU AI Act, GenAI use, lifecycle, and fraud use cases
	•	SREP: ECB formally closed model inventory completeness finding following remediation (training, inventory attestation, policy enhancements)
	•	PRA SS1/23: PRA requested follow-up meetings (late April) to discuss GS submission; survey assessed MRM alignment including inventory, governance, and framework

Finding related to insufficient evidence supporting the appropriateness of applying a single PD model across jurisdictions for mid-corporates


MRM approved DistilledSentiment (AWM, Tier 2), used by Quantitative Investing Strategies (QIS) to generate standardized signals for global equities based on sentiment extracted from textual data
	•	The model leverages pre-trained transformer architectures to quantify sentiment, with outputs designed to support return prediction and systematic investment decision-making



GBM Soundbites
	•	AI adoption accelerating, but cost efficiency questioned: Xavier cited survey indicating 60%+ of programming work now has AI involvement; raised concerns on high compute costs (e.g., Claude coding usage running into thousands) and whether AI delivers net cost savings
	•	Pragmatic AI usage strategy emerging: MRM approach positions Gemini Flash as the “workhorse” for long-context tasks, with Anthropic models reserved for premium coding use cases
	•	Data and tooling modernization underway: Manish Gupta’s team driving onboarding of key datasets (CAR, liquidity, funding) onto MCP-enabled tooling to support agentic workflows
	•	Shift toward Python-centric development: New model development prioritizing Python, with Slang retained primarily for pricing and legacy functions



MRM approved Marquee Persona (GBM Public, Tier 3), leveraging generative AI to generate client-level interaction summaries across Marquee and Sales channels, enhancing client insight and enabling more targeted engagement
	•	Phased rollout underway, with initial deployment to ~50 users and full Sales rollout (~1,300 users) targeted by end-2026
MRM approved ASL Transfer Restrictions (GBM Private, Tier 2), leveraging agentic AI to extract and classify Federal Reserve pledge restriction data and remediate historical data gaps across active facilities
	•	Outputs remain non-binding and are subject to mandatory SME review prior to use, ensuring appropriate human oversight and control



Recommended version (balanced):
	•	MRM approved Banker Copilot Studio (GBM Private, Tier 2), a unified workspace leveraging automation, conversational interfaces, and intelligent search to enhance creation, editing, and retrieval of client service materials, driving efficiency and improved client engagement across banker workflows

Slightly more concise:
	•	MRM approved Banker Copilot Studio (GBM Private, Tier 2), enabling bankers to streamline creation and search of client materials through automation, conversational interfaces, and intelligent search, improving workflow efficiency and client engagement



Transaction Waiver Summary

Desk

Equities – Structured Products Group (SPG)

Trade

Eq VWAP Flex Buyback – Deferred Settlement Structure

Underlier

Hannover Rück SE (HNR1 GY)

Counterparty

HDI Haftpflichtverband der Deutschen Industrie VAG

Notional

EUR 500 million (min: EUR 499.99m, max: EUR 500m)

Maximum Shares

4,000,000 shares

Dates

• Signing Date: 16-Mar-2026
• Start Date: 19-Mar-2026
• Maximum Maturity: 19-Oct-2026

Economics

• Discount: 1.55%
• Upside Sharing: 66.67% (client participation)
• Expected P&L: ~$2.5 million

⸻

Trade Description

GS is mandated to purchase shares on behalf of the client via a VWAP-based execution strategy, in exchange for providing the client with a guaranteed discount and upside sharing, while GS retains full downside risk.

Key features:
	•	The trade terminates when either:
• total client cost (excluding upside share) reaches EUR 500m, or
• 4 million shares are acquired
	•	The client prepays EUR 500m upfront, and shares are delivered at maturity free of payment (no DvP settlement)
	•	GS executes purchases over time and accumulates shares for delivery at maturity

⸻

Reason for Waiver

The existing Eq VWAP Flex Buyback tradable does not support deferred settlement mechanics, where:
	•	cash is received upfront, and
	•	shares are delivered at maturity without payment

As a result, the tradable cannot fully capture the timing mismatch between cashflows and physical settlement obligations.

⸻

Proposed Booking During Waiver Period

The trade will be booked using the Eq VWAP Flex Buyback tradable, supplemented with additional legs to replicate settlement behavior:

• EUR 500m receivable upfront
• EUR 500m payable at maximum maturity
• As shares are purchased:
	•	book a zero-strike call with maturity equal to trade maturity
	•	reduce the EUR 500m payable by the corresponding notional

This approach ensures that final settlement obligations (cash vs shares) are correctly reflected at maturity.

⸻

Compensating Controls

The desk noted that the primary valuation difference arises from:
	•	GS effectively receiving dividends on shares acquired prior to ex-date, and
	•	the absence of daily cash settlement, resulting in a timing mismatch

The estimated PV impact of these effects is approximately EUR 53 million.

To mitigate this during the waiver period:

• Full P&L reserve is applied, ensuring that any valuation differences due to settlement mismodeling are not recognized in reported P&L
• A dedicated monitoring report will be implemented to track PV impact based on actual execution and share accumulation
• The trade economics (discount and upside sharing) are fully captured by the approved tradable, with only settlement timing requiring workaround
• The structure is deterministic in notional and bounded by maximum shares, limiting uncertainty in exposure evolution

⸻

Remediation Plan

• Implement full support for decoupled cash and share settlement schedules within the tradable
• Enhance system capability to reflect predefined and differing settlement timelines
• Expected delivery timeline: ~1 month (Strats implementation and testing)




Goal 1: Deepen Expertise in Basel III Final (B3F)

Build a strong understanding of B3F capital rules and actively contribute to related workstreams

Enhance ability to translate regulatory requirements into clear, actionable reporting and become a reliable resource on capital topics

Goal 2: Advance AI-Driven Workflow Efficiency

Leverage AI tools to streamline workflows (e.g., reporting, drafting, data processing) and reduce manual effort

Identify and implement practical AI use cases to improve efficiency and consistency across deliverables

Goal 3: Deliver High-Quality and Impactful Reporting

Maintain high standards in preparing CRO, Strats, BRC, and FRAC materials with a focus on clarity and timeliness

Continuously refine messaging to align with senior stakeholder priorities and improve overall effectiveness



Market movements were accompanied by model parameter re-marks in the NYC Volex portfolio, including barrier shifts in callable range accruals and volatility offsets used in Bermudan pricing.
	•	The re-marks offset some of the impact of the market movements, remain within agreed parameter bounds, and were approved by MRM and Controllers.
	•	MRM continues to coordinate with Market Risk Strats, Specialists, and broader Risk teams on the treatment of these parameters in VaR and backtesting, in light of recent market volatility.



Market movements were accompanied by model parameter re-marks in the NYC Volex portfolio, including barrier shifts in callable range accruals and volatility offsets used in Bermudan pricing.
	•	The re-marks offset some of the impact of the market movements, remain within agreed parameter bounds, and were approved by MRM and Controllers.
	•	MRM continues to coordinate with Market Risk Strats, Specialists, and broader Risk teams on the treatment of these parameters in VaR and backtesting, in light of recent market volatility.


The desk requested a re-mark to the volatility offset parameter, which was approved by MRM as remaining within the agreed parameter bounds.

Absent the Volex parameter re-marks, the March 12 P&L would likely have resulted in an additional 99% VaR backtesting breach, which could further increase the regulatory VaR capital multiplier (already raised following the 5th breach); MRM is reviewing the appropriateness of the remark treatmen


Notable validation work related to GSBE ICAAP included updates to methodologies for interest rate and credit spread risk in the banking book, enhancements to VaR stress calibration, and an overlay reflecting expected FRTB-SA implementation, alongside other changes aligned with CCAR model updates.


Notable validation work related to GSBE ICAAP included methodologies for interest rate risk and credit spread risk in the banking book, as well as updates to VaR stress calibration and an overlay reflecting expected FRTB-SA implementation, in addition to other enhancements aligned with CCAR-related model changes.


FRB exams: A key supervisory focus area is XVA Risk Management, one of the most complex modeling areas in the firm, with supervisors requesting four dedicated meetings, compared to one to two meetings for other exam objectives.


Below is a cleaned and updated version addressing Caroline’s comments. I fixed the following based on her notes:
	•	Clarified which limit applies to the volatility offset parameter
	•	Removed / softened the exam modeling callout framing
	•	Simplified the ICAAP validation bullet (too wordy / too many acronyms)
	•	Defined ETSC acronym at first use
	•	Fixed the missing parenthesis
	•	Slightly tightened wording overall for CRO style

⸻

Summary of Recent Activities in Model Risk

Top of Mind

Geopolitical Events:
No material model performance issues observed amid the recent US–Israel–Iran conflict.

Interest Rate Volatility Desks P&L:
Recent losses in LDN IRP and NYC IRP desks were driven by a richening of short-dated interest rate volatility (“top-left” vols) against desk short positions.
	•	Losses were partially offset by parameter re-marks in the NYC Volex portfolio, including barrier shifts in callable range accruals and volatility offsets used in Bermudan pricing.
	•	The volatility offset parameter is subject to an MRM model parameter limit; current usage is elevated but remains within approved limits, and MRM is assessing the increased usage.

⸻

CCAR

All 135 models and 53 qualitative approaches (QAs) remain on track for approval. MRM is currently focused on reviewing several recently proposed overlays, including:
	•	A high-severity finding was raised (subsequently remediated and closed) due to conceptual and implementation deficiencies in the overlay reflecting GS Bank intercompany borrowing under stress.
	•	Treasury revised the calculation to capture loan reset frequencies, apply scenario-specific inputs, and ensure consistent assumptions.
	•	The overlay applies to GS Bank CCAR results only, not GS Group.
	•	Overlay to AWM Private PPNR and GMS to reflect the impact of revising the beta of private equity to public equity paths to 0.6.

Exams:
MRM will participate in 13 of 15 supervisory meetings, including one validation-focused meeting on provisions wholesale. A key focus area relates to XVA risk management, where supervisors have requested several deep-dive discussions.

⸻

Validation Activities

Asset Secured Lending (ASL)

Notable recent model enhancements approved for the ASL business include:
	•	Enhancement to the Residential Mortgage Tail Risk model (Risk, Tier 1) to incorporate interest rate swaps into collateral valuation, leveraging more granular collateral-level data and improving tail risk accuracy.
	•	Enhancements to the Transport Tail Risk model (Risk, Tier 1) incorporating new data for stress shock calibration, updates to the upstream pricing model including an index-based methodology for lease probability of default, and improved differentiation between performing and non-performing leases, addressing prior validation findings.

⸻

GSBE ICAAP / ILAAP

Validation of 57 models and 2 QAs for ICAAP and 22 models and 11 QAs for ILAAP was completed ahead of the mid-March regulatory submissions to the ECB.

Notable validation work included:
	•	New methodologies for commodity derivatives CVA/FVA losses, ASL portfolio provisioning, and IRRBB/CSRBB for GSBE ICAAP.
	•	Updates to VaR stress calibration and an overlay reflecting the expected FRTB-SA go-live in market risk RWA projections.

⸻

Regulatory Updates

ECB Supervisory Review and Evaluation Process (SREP):
ECB confirmed formal closure of the finding on model inventory completeness.

Remediation included training, inventory review and attestation by responsible business units, and enhancements to the GSBE Policy and Procedure Risk Handbook.

⸻

Electronic Trading Software Controls (ETSC)

There has been an increase in activity related to Electronic Trading Software Controls (ETSC) validation requests for new business initiatives across Asia and EMEA Equities, including:
	•	Automated execution of client orders at guaranteed benchmark prices with risk unwinding through the One Delta Closing Facility (ODCF) (e.g., EMEA GMOC Actionable IOIs, where Guaranteed Market-on-Close (GMOC) indications are streamed to clients and risk is unwound using the ODCF algorithm).
	•	Strategic buildout of Asia Synthetic Products Group (SPG) trading capability using the GSBE entity, shifting activity from GSI to reduce funding costs (e.g., Asia SPG – GSBE Taiwan Synthetic Access, where GSBE acts as the exchange-facing entity for synthetic execution of Taiwan equities).





Heightened number of validation requests for new business initiatives across Asia and EMEA Equities, including:
	•	Automated execution of client orders at guaranteed benchmark prices with risk unwinding through the One Delta Closing Facility (ODCF). Example: validation of EMEA GMOC Actionable IOIs, where Guaranteed Market-on-Close (GMOC) indications are streamed to clients and risk is unwound using the ODCF algorithm.
	•	Strategic buildout of Asia Synthetic Products Group (SPG) trading capability using the GSBE entity, shifting activity from GSI to reduce funding costs. Example: validation of Asia SPG – GSBE Taiwan Synthetic Access, where GSBE acts as the exchange-facing entity for synthetic execution of Taiwan equities.


Asset Secured Lending (ASL): Notable model enhancements approved for the ASL business include:
	•	Residential Mortgage Tail Risk model (Risk, Tier 1): Enhanced to incorporate interest rate swaps in collateral valuation, leveraging more granular collateral-level data and improving tail risk measurement.
	•	Transport Tail Risk model (Risk, Tier 1): Enhanced through new datasets for stress shock calibration, updates to the upstream pricing model including an index-based methodology for lease probability of default, and improved differentiation between performing and non-performing leases, addressing prior validation findings.

GSBE ICAAP / ILAAP
	•	Validation of 57 models and 2 QAs for ICAAP and 21 models and 12 QAs for ILAAP was completed ahead of the mid-March regulatory submissions to the ECB.
	•	Notable validation work included new methodologies for CVA/FVA losses on commodity derivatives, ASL provisioning models, and IRRBB/CSRBB for GSBE ICAAP, as well as updates to VaR stress calibration and an overlay reflecting expected FRTB-SA implementation.

⸻

Regulatory Updates

ECB Supervisory Review and Evaluation Process (SREP)
	•	The ECB confirmed formal closure of the finding on model inventory completeness.
	•	Remediation included targeted training, inventory review and attestation by responsible business units, and enhancements to the GSBE Policy and Procedure Risk Handbook.

⸻

Electronic Trading Software Controls (ETSC)
	•	Heightened validation activity for new electronic trading initiatives across Asia and EMEA Equities, including automated client execution and expansion of synthetic trading capabilities.
	•	Examples include validation of EMEA GMOC Actionable IOIs, where guaranteed Market-on-Close indications are streamed to clients with risk unwound via the ODCF algorithm, and Asia SPG – GSBE Taiwan Synthetic Access, enabling the Asia Synthetic Products Group to execute synthetic trades through the GSBE entity to reduce funding costs.

IR volatility desks experienced losses in LDN IRP and NYC IRP, primarily driven by a richening of short-dated interest rate volatility (“top-left” vols) against desk short positions.
	•	Losses were partially offset by parameter re-marks in the NYC Volex portfolio, including barrier shifts in callable range accruals and volatility offsets used in Bermudan pricing.
	•	The volatility offset parameter is subject to an MRM control limit; current usage is elevated but remains within approved limits.

Alternative titles (also CRO-


Notable validation work included new methodologies for CVA/FVA losses on commodity derivatives, ASL portfolio provisioning, and IRRBB/CSRBB for GSBE ICAAP, as well as updates to VaR stress calibration and an overlay reflecting expected FRTB-SA go-live in MR RWA projections.

Asset Secured Lending (ASL): Notable recent model enhancements approved for the ASL business include:
	•	Enhancement to the Residential Mortgage Tail Risk model (Risk, Tier 1) to incorporate interest rate swaps into collateral valuation, leveraging more comprehensive collateral-level data and improving tail risk accuracy.
	•	Enhancements to the Transport Tail Risk model (Risk, Tier 1) incorporating new data for stress shock calibration, updates to the upstream pricing model including an index-based methodology for lease probability of default, and improved differentiation between performing and non-performing leases, addressing prior validation findings.


Enhancements implemented by Microsoft in response to these findings include Azure infrastructure improvements and an updated LLM integration, addressing system reliability issues and improving accuracy, hallucination control, consistency, timeliness, and response coherence.

MRM approved enhancements to AI Bing Search (Engineering, Tier 2), which enables web-search grounding for queries within the GS AI Assistant, addressing prior MRM validation findings.
	•	The findings related to instability in the Bing search service and weighting of individual search results, which could lead to search grounding being disabled or increase hallucination risk.
	•	Microsoft implemented enhancements following Engineering escalation, including Azure infrastructure improvements and an updated LLM integration, improving system reliability and addressing the validation findings.


used by recruiters to translate semantic search queries into profile filters and generate personalized outreach messages to potential candidates.


Transaction Waiver Summary

Desk

DESA – HIKG SPG

Region / Legal Entity

Asia – GSI

Trade

Fixed Notional Daily Crash Put on Client Portfolio Basket

Model

EqSp KO Daily Crash Put

Trader / Strat

Trader: Varun Lunia
Strat: Mayank Jalan
Strat MD: Patrick Chan

Approvals

Strat PMD Approver: Xavier
CRO Designee Approver: Dmitri

⸻

Trade Description

The desk proposes to book a client-facing fixed notional crash put referencing a synthetic basket representation of the client’s equity portfolio.

Key features include:
	•	Notional: approximately $2bn
	•	Structure: 70% Daily Crash Put on LMV exposure
	•	Maturity: 4 months, with the trade expected to roll forward at reset dates
	•	Model / Tradable: EqSp KO Daily Crash Put

The underlying basket will represent the client’s portfolio using the following construction:

Basket = 100 + a × LMV − b × SMV

where coefficients a and b are calibrated daily to maintain:
	•	basket level of 100
	•	long / short exposure ratio of 1

The basket references the client’s actual stock portfolio, allowing MRMA to expand the basket representation and run single-stock stress metrics, including TD-style stress tests.

⸻

Reason for Waiver

The EqSp KO Daily Crash Put model is already MRM approved, and the tradable captures the payoff mechanics of the structure.

The waiver relates to two implementation aspects that require further review:
	•	Basket representation: the synthetic basket construction used to represent the client’s portfolio requires validation by MRMA/MRM to confirm stress and risk metrics behave as expected.
	•	Volatility marking methodology: the desk proposes to infer implied volatility from the cleared trade price (~3%), corresponding to approximately 120% annualized volatility, which will be reviewed by MRMA/MRM.

⸻

Proposed Booking During Waiver Period

The trade will be booked using the approved EqSp KO Daily Crash Put tradable, with the client portfolio represented via the calibrated basket formulation described above.

⸻

Compensating Controls

The desk noted that the underlying tradable and payoff structure are already MRM approved. During the waiver period:
	•	The synthetic basket representation references the client’s actual portfolio, enabling MRMA to expand the basket into individual stock components for stress testing and risk analysis.
	•	Single-stock stress metrics and sensitivity analysis will be monitored using existing MRMA risk tools.
	•	The volatility assumption will be derived directly from the cleared market price of the trade, ensuring consistency between valuation and executed pricing.
	•	The trade has a short maturity (4 months) and will be reset periodically, limiting long-term exposure while model representation is reviewed.

⸻

Remediation Plan

The desk will work with MRMA and MRM to complete review and approval of:
	•	the basket asset representation methodology, and
	•	the volatility marking approach

within 3 months.




Transaction Waiver Summary

Desk

Equities – Structured Notes / IRP

Trade

Structured Notes with Running Fee on NAV (MTM)

Notional

Up to USD 500 million across notes with approved payoff structures

⸻

Trade Description

The structured notes pay a structured coupon to the retail investor, while Goldman Sachs pays a distribution fee to the third-party distributor or insurer.

Historically, this fee has been calculated as x bps of notional, paid periodically (e.g., quarterly). Under the proposed structure, the running fee will instead be calculated as x bps of the note’s MTM (NAV) at the fixing date, rather than the notional amount.

The underlying payoff structures remain standard and already approved, with the only modification being the reference used to calculate the distributor fee. As the notes are typically capital guaranteed and trade close to par, the difference between notional and MTM is expected to be limited.

⸻

Reason for Waiver

Running distribution fees are already approved and supported when referenced to notional. The proposed structure changes the reference from notional to NAV (MTM).

While this functionality is already approved and supported within the Equities (EQ) framework, MRM has not yet completed approval for the IRP implementation due to competing validation priorities and concurrent waiver resolutions.

⸻

Proposed Booking During Waiver Period

Trades will be booked in their final structure, with the running fee referenced to the note’s MTM, consistent with the intended production setup.

⸻

Compensating Controls

The desk noted that the waiver does not introduce a new payoff structure or market risk profile, as the only change is the reference used for the distributor fee calculation.

In addition:
	•	The running fee mechanism is already approved and implemented in the EQ framework, providing precedent for the calculation methodology.
	•	Structured notes involved are capital guaranteed and typically trade close to par, limiting potential deviations between notional and MTM.
	•	The MTM used for the fee calculation will be approximated using the SPV valuation, consistent with the approach currently used for MTM recovery calculations.

⸻

Remediation Plan

Implementation of Running Fee on NAV within IRP is already completed, using the SPV-based MTM approximation framework currently applied for MTM recovery calculations. Formal MRM approval will follow as part of the next validation cycle.


MRM identified increased materiality of limitations in the Equity Vega Liquidation Charge methodology used in Prime Brokerage margin shortfall modeling (GBM, Tier 1), where the flat multiplier understates vega liquidation costs and does not capture skew vega or concentration effects.
	•	The increased materiality is driven by higher client options activity in Prime Brokerage accounts; as an interim remediation, the multiplier in the shortfall model was increased from 0.05 to 5, resulting in a material increase in vega liquidation charges across clients.
	•	A strategic remediation is underway through migration to the Unified Benchmark Model (UBM) framework (target Q2), alongside recalibration of CREST vega liquidation parameters as part of remediation of an existing aged validation finding.



Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)



Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?



																													



Standardized RWA: Development of new Controllers’ deterministic regulatory calculations (DRCs) for Operational Risk RWA, and updates to existing DRCs primarily related to revised risk weights and treatment of securities financing transactions (SFTs).
	•	FRTB / FRTB-CVA: Changes to CVA RWA calculation, including implementation of the standardized CVA framework, introduction of 10-day shock calibration for market risk factors, and incorporation of default risk charge and residual risk add-ons.


ETSC approved India Synthetic Futures, a new electronic trading activity to automate client order execution and hedging for swaps referencing India single-stock futures listed on the Singapore exchange.
	•	High-severity control deficiencies were identified during review, including missing firm capital and client exposure controls, exclusion of start-of-day positions from unhedged risk checks, and lack of price and size re-validation for orders released after throttling breaches.
	•	These deficiencies were addressed prior to approval, with required controls implemented to ensure appropriate risk checks and order validation.


MRM identified an inappropriate assumption in the loss projection methodology used to translate the Stressed CCE metric into cumulative stressed loss along the CCAR path for Board limit calibration.
	•	Specifically, the methodology results in projected stressed losses being driven primarily by base exposures rather than stressed exposures, creating an inconsistency as the Board limit scales Stressed CCE while being derived from base CCE dynamics.
	•	As a result, the limit calibration is unstable (e.g., the current $325bn limit would have been ~$410bn using October data), and remediation is underway to revise the projection methodology to ensure limits are driven by stressed exposure


MRM identified limitations in the Prime Brokerage Equity Vega Liquidation Charge methodology used for margin and benchmarking, where the flat multiplier understates vega liquidation costs and does not capture skew vega or concentration effects
	•	A validation finding was raised; as an interim remediation, the benchmark multiplier was increased from 0.05 to 5, increasing estimated vega liquidation risk by ~$675mm across clients, with margin adjustments for impacted clients to follow
	•	A broader remediation is underway through migration to the Unified Benchmark (UBM) framework (target Q2), alongside recalibration of CREST vega liquidation parameters as part of an existing aged validation finding

Top of Mind
	•	Geopolitical events: No material model performance issues observed amid the recent US–Israel–Iran conflict. MRM continues monitoring the recent surge in oil and natural gas prices and has not identified modelling concerns to date.
	•	Market volatility: MRM is assessing models following the ~12% decline in the Korean stock index (KOSPI) since 9-11 that triggered exchange circuit breakers.
	•	Basel III Final Rule: Discussions ongoing regarding the FRB’s forthcoming Basel III re-proposal and the currently contemplated effective date of January 1, 2027.
	•	Standardized RWA: Development of new Controllers’ deterministic regulatory calculations (DRCs) and updates to existing DRCs are expected to complete by August, with MRM validation targeted for November.
	•	FRTB / FRTB-CVA: Risk Engineering expects to complete model development and required model changes by Q2, with MRM validation anticipated by Q3.

⸻

Validation Activities

Prime Tail Liquidity Loss (PTL)
	•	MRM approved enhancements to the PTL model (Risk, Tier 1) expected to materially improve the firm’s PTL ratio, a key metric monitored against FRAC and BRC limits.
	•	Enhancements incorporate previously omitted synthetic term commitments and additional margin-related mitigants (e.g., inflows from excess margin), supporting more robust intraday liquidity stress testing.

⸻

Prime Brokerage Vega Liquidation
	•	MRM identified limitations in the PB Equity Vega Liquidation Charge (SPIRE v5/v30) methodology, where the multiplier used to estimate vega liquidation costs was insufficient and did not capture skew vega or concentration effects.
	•	As an interim remediation, the multiplier in the benchmark was increased from 0.05 to 5, increasing estimated vega liquidation risk by ~$675mm across clients, with margin adjustments for impacted clients to follow.
	•	A broader remediation is underway through migration to the UBM framework (target Q2), which is expected to further increase risk capture while recalibrating CREST parameters as part of an existing FRAC finding.

⸻

Coherent Stress Loss
	•	MRM review of the Stressed CCE loss projection methodology identified inappropriate assumptions that resulted in the projected stressed loss being driven by base exposures rather than stressed exposures.
	•	As a result, the current Board limit calibration may be unstable; for example, the implied limit would have been $410bn rather than $325bn if recalibrated using October data.


Basel III Final Rule: Ongoing discussions regarding the FRB’s forthcoming Basel III re-proposal and the currently contemplated effective date of January 1, 2027.
	•	Standardized RWA: Development of new Controllers’ deterministic regulatory calculations (DRCs) and updates to existing DRCs are expected to complete by August, with MRM validation targeted for November.
	•	FRTB / FRTB-CVA: Risk Engineering expects to implement required model changes by Q2, with MRM validation anticipated to complete in Q3.




Bill noted that GBM appears to be increasing AI development (e.g., ~10 items in pipeline), which may signal a broader shift in adoption.
	•	If AI becomes more embedded across product lines, MRM may need to reconsider whether the current AI validation approach remains appropriate.
	•	Specifically, he is questioning whether AI validation should be more integrated into product-line validation rather than treated separately.



Continued growth & validation of new AI models, with notable upcoming approvals including Market Simulator (Albert) (GBM Public, Tier 2), a transformer-based deep learning neural network used in algorithmic trading to generate equity security weightings for portfolio optimization, and TradeScore (GBM Public, Tier 2), designed to estimate order-fill probability based on historical patterns for quote optimization

ASL Transfer Restrictions (GBM Private, Tier 2), an agentic AI solution used to analyze ASL facilities and support identification of Fed pledge eligibility, and Commentary AI (Risk Division, Tier 2), used to extract key information from financial documents and generate supporting rationale for credit risk decisions



NYC Volex IR Delta
	•	MRM identified material IR Delta inaccuracies and SIMM dispute drivers from the backbone assumption, with revised desk analytics under review and a proposal to remove the backbone to improve counterparty alignment

Internal Credit Rating (ICR)
	•	Following rollout of the new Tier 1 ICR models, MRM observed ~15% HY-to-IG overrides and is progressing an open finding to strengthen override monitoring while assessing impacts to capital and loan reserves

Prime Tail Liquidity Loss (PTL)
	•	MRM is validating PTL model enhancements incorporating previously omitted commitments and additional margin mitigants, with changes expected to materially improve the firm’s PTL ratio against FRAC and BRC limits



NYC Volex IR Delta
	•	MRM analysis identified material inaccuracies in desk IR Delta analytics and found that the current backbone assumption contributes to longstanding SIMM disputes
	•	The desk is developing revised analytics under MRM review and plans to propose removing the backbone to better align sensitivities with counterparties

⸻

Internal Credit Rating (ICR)
	•	Newly approved Tier 1 ICR models were rolled out in phases, with production experience showing ~15% of HY ratings overridden to IG
	•	MRM has an open finding requiring stronger override monitoring and is assessing potential impacts to capital and loan reserves

⸻

Prime Tail Liquidity Loss (PTL)
	•	MRM is validating PTL model enhancements expected to materially improve the firm’s PTL ratio, a key metric monitored against FRAC and BRC limits
	•	Changes primarily reflect inclusion of previously omitted synthetic commitments and additional margin-related mitigants






MRM rejected the TradeScore model (GBM Public, Tier 2), designed to estimate order-fill probability for quote optimization, due to unjustified Neural Network complexity and insufficient performance uplift
	•	MRM-designed benchmarking showed a simple 22-parameter challenger outperformed the ~11,000-parameter Neural Network across 9 of 10 metrics
	•	Modelers incorporated MRM feedback and redesigned the Neural Network; the updated version is under review with preliminary analysis indicating improved performance




Model Validation Updates
	•	MRM rejected the TradeScore model (GBM Public, Tier 2) after benchmarking demonstrated that a simple MRM challenger model with 22 parameters outperformed the production Neural Network (~11,000 parameters) across 9 of 10 metrics, indicating unjustified model complexity, weak performance efficiency, and insufficient evidence that the Neural Network architecture provides incremental value
	•	The model estimates order-fill probability based on historical trading patterns to support quote optimization for algorithmic trading desks
	•	Modelers incorporated MRM feedback and redesigned the Neural Network; the updated version is under review, with preliminary analysis indicating improved performance across key metrics
	•	MRM approved an extension of Botnation AI (GBM Public, Tier 2) to support broker quote parsing for Euro government bonds and Euro gas and power futures
	•	The model converts free-text trading messages into structured trade syntax
	•	Performance exceeds the modeler’s predefined 85% accuracy threshold following remediation of MRM feedback
	•	MRM approved Loan Notice Data Extraction (GBM Private, Tier 2), a generative AI model that extracts key information from loan notices received from agent banks and financial institutions
	•	The model replaces a vendor regex-based tool, delivering material improvements in coverage (60% → 100%) and accuracy (85% → 97%)

⸻

Why this works better (based on your typical GS messaging style)
	•	Clear rejection driver: complexity not justified by performance
	•	Uses benchmarking evidence — very strong regulator-facing rationale
	•	Avoids overly technical NN detail while still sounding credible
	•	Keeps bullets crisp and parallel across approve vs reject cases

⸻

If helpful, I can also give you:
✅ an even shorter CRO soundbite version (3 bullets total)
✅ a more regulatory-defensive version (stronger challenge language)
✅ a version emphasizing AI governance themes (complexity control, explainability, benchmarking discipline)



MRM rejected the TradeScore model (GBM Public, Tier 2) as benchmarking showed a simple 22-parameter challenger outperformed the ~11,000-parameter Neural Network across 9 of 10 metrics, indicating unjustified complexity and limited incremental value

If you want an even sharper executive version, you could use:
	•	MRM rejected the TradeScore model (GBM Public, Tier 2) after benchmarking showed a materially simpler challenger outperformed the Neural Network across most metrics, highlighting unjustified complexity and weak incremental benefit

Let me know if yo






AI Risk and Controls Committee (AIRCC)




AIRCC recently approved:
• Amazon Connect Contact Lens, used to analyze recorded client interactions for sentiment detection, emerging theme identification, and agent performance monitoring
• LinkedIn AI features, including AI-assisted candidate search, project organization, and personalized outreach

Model Validation Activities

MRM approved an extension of Botnation AI (GBM, Tier 2), used to enhance parsing of quote inquiries for Euro government bonds and Euro Gas and Power futures
• The model achieved 100% accuracy for Euro government bonds and 98% for Euro Gas and Power futures following remediation of MRM findings related to output type mismatches and removal of irrelevant prompt instructions
• Validation efficiency improved, with the initial validation completed in ~6 weeks and subsequent desk and infrastructure changes completed in ~1 week




AI development activity picked up following a slower January
AIRCC approved use of AI capabilities to analyze recorded client interactions and surface sentiment, emerging themes, and agent performance insights, with controls focused on appropriate monitoring and data handling safeguards

AIRCC also approved internal productivity features supporting AI-assisted candidate search, project organization, and personalized outreach, subject to standard governance and control requirements

Model Validation Activities

MRM progressed validation of public document extraction capabilities supporting GBM workflows, focusing on output consistency and robustness of document parsing

MRM approved an extension of Botnation AI (Tier 2) expanding coverage to Euro government bonds and Euro Gas and Power futures quote parsing following remediation of prompt design and output format issues

Post-remediation testing demonstrated strong accuracy and improved reliability, with validation timelines shortened for subsequent desk onboarding due to reuse of infrastructure and prior testing coverage

AIRCC approved use of Amazon Connect Contact Lens to analyze recorded client interactions for sentiment, emerging themes, and agent performance monitoring, enhancing supervisory oversight through integrated access to recordings, transcripts, and automated evaluation outputs

• AIRCC approved LinkedIn AI recruiting capabilities, including AI-assisted candidate search, project organization, and personalized outreach, to improve recruiter efficiency while operating within established data usage and governance controls

Compensating Controls

The desk noted that, during the waiver period, the following controls mitigate risks arising from incomplete tradable support:

• Conservative valuation treatment: The Floor feature will be implemented through floored cashflows with 1-day optionality assumed immaterial, ensuring pricing reflects intrinsic downside protection without overstating optionality value.

• Validated OET functionality: Daily Optional Early Termination rights with zero notice and no break fee are fully supported and validated, providing the ability to exit positions promptly should market conditions or model limitations warrant.

• KO risk conservatism and monitoring: The Knock-Out feature will be monitored using existing swap post-FVD monitoring tools, with scenario analysis applied to capture potential cashflow and exposure discontinuities from KO events.

• Market risk and stress controls: Exposure will remain subject to standard market risk governance, including CCAR stress scenarios and limits, which effectively constrain notional and gap risk during the interim modeling period.

• Trading scope limitations: Activity will be limited to short-dated (1m–3m) maturities aligned with futures expiry, reducing path dependency and model uncertainty associated with longer-dated exposures.

• Exchange price limit mitigation: KRX daily price limits materially reduce the probability of a 45% single-day decline, lowering the practical likelihood of KO triggering prior to full model support.

• Tail-risk validation: For the initial underlier (SK Hynix), current implied volatility levels indicate that a 45% one-day move represents an extreme tail event (greater than ~10 standard deviations), supporting the view that residual modeling gaps have limited practical impact.

• Manual oversight during rollout: Initial waiver trades will be subject to enhanced desk monitoring to ensure that exposures, KO proximity, and termination behavior remain consistent with expectations until full tradable support is implemented.

⸻

If you want, I can also give you:

✅ a shorter CRO version (3–4 bullets)
✅ a more technical validator version (mentioning payoff discontinuity / path dependency)
✅ a one-sentence soundbite for MRCC minutes
✅ a stronger “why 1-day optionality immaterial” justification (very helpful wit



Bulk Transaction Waiver Summary

Desk

SPG – Equity Derivatives

Trade

Equity swaps on Single Stock Futures incorporating daily Floor/Cap and Knock-Out (KO) features

Counterparty

Leveraged ETF fund offering 2× exposure

Underlier

Single Stock Futures (initially SK Hynix)

Scope / Notional

Bulk waiver covering up to 8 trades with an aggregate notional limit of USD 500 million

⸻

Trade Description

The trades are equity swaps referencing Single Stock Futures with daily return features including:

• Floor feature: Daily return defined with a downside floor (not below 45% of prior-day price)
• Knock-Out (KO): Triggered if the underlying falls below 45% of the previous day’s price
• Daily OET rights: Both GS and the counterparty may terminate daily with zero notice period and no break fee

The structure is designed to deliver leveraged exposure with embedded downside protection and termination flexibility.

⸻

Reason for Waiver

While Floor and KO mechanics are supported for swaps on cash equities and indices, they are not yet supported for Single Stock Futures tradables, resulting in incomplete representation of daily return floors and KO triggers. The desk expects full tradable and model support for these features within 8 weeks.

⸻

Proposed Modeling Approach During Waiver

• Daily OET functionality is already validated and will be applied without modeling limitation
• The Floor feature will be treated analogously to swaps on single stocks, with 1-day optionality assumed immaterial and pricing based on intrinsic value via floored cashflows
• The KO feature will be modeled similarly to post-FVD swap behavior, leveraging monitoring tools to capture risk and cashflow effects
• Market risk controls (including CCAR scenarios) will govern notional exposure during the interim period

⸻

Compensating Controls

The desk noted that the interim approach applies conservative floored cashflow valuation with validated daily OET rights, supplemented by monitoring tools and scenario-based market risk controls, while exchange price limits and current volatility levels imply the KO threshold represents an extreme tail event.

⸻

Interim Trading Constraints

• Trading will focus on 1m and 3m expiries where FVD aligns with futures expiry
• Exchange price limits (KRX) materially reduce the likelihood of a 45% single-day decline
• Initial trades under the waiver will be manually monitored given the limited scope

⸻

Remediation Plan

• Implement full tradable support for Floor and KO features on Single Stock Futures within 8 weeks
• Complete validation confirming floor enforcement above the 45% threshold
• Engage CRO designee and Strats PMD for formal approval of the bulk waiver





CRO focus areas are intended to highlight material risk events, emerging risks, or significant changes requiring senior management or Board attention, rather than routine updates

• Recent MRM topics (AI activity, ICR progress, annual review rollout, findings monitoring) were viewed as BAU, technical, or covered through other governance forums, and therefore not appropriate for CRO escalation

• Model risk remains well controlled with no discrete events, breaches, or material developments warranting CRO focus area inclusion at this time

• Accordingly, MRM will not provide CRO focus area content this cycle, with updates continuing through dedicated forums (e.g., CCAR, AI governance, recurring BRC thematic reporting)



•	The root issue sits in the SVLV analytics (e.g., distribution assumptions such as frozen drift).
	•	The backbone is constructed using those analytics, so the limitation is inherited and amplified through the backbone transformation.
	•	IR Delta is therefore impacted via both the analytic limitation and the resulting backbone behavior.


MRM assessment indicates limitations in the underlying SVLV analytics propagate through the backbone methodology and are not adequately mitigated in IR Delta, with enhanced MRM analytics demonstrating a material understatement of IR Delta.


MRM assessment shows that limitations embedded in the backbone methodology remain insufficiently assessed, with enhanced MRM analytics indicating a material understatement of IR Delta.


The approved Internal Credit Rating (ICR) models went live following model approval in October 2025. To date, 178 of 281 ratings have been approved under the new framework.
	•	One medium-severity finding remains open relating to override rates, particularly for IG names, as the models appear conservative. The finding calls for enhanced ongoing monitoring to assess override frequency, rationale, and associated impacts.
	•	Based on observed overrides, the model misclassifies a portion of IG names as HY, lower than the level identified during validation. MRM is assessing the impact of rating overrides from both capital and loan reserve perspectives.


MRM conducted an analysis of Internal Credit Rating (ICR) model go-live status and rating overrides, focusing on Corporates and Direct CRE portfolios.
	•	Of the re-ratings completed under the new models, 178 of 281 have been approved, reflecting a modest delay relative to the planned go-live timeline. Ten overrides were observed among approved ratings, primarily within HY-modeled names (largely upgrades), with a subset resulting in IG/HY category flips.
	•	Based on observed overrides, the model misclassifies approximately 14% of IG names as HY, materially lower than levels identified during validation (~30%), likely reflecting the limited sample size.
	•	MRM estimates an approximate ~$XXbn RWA impact associated with the rating overrides.


MRM conducted an analysis of ICR model go-live status and rating overrides, focusing on Corporates and Direct CRE portfolios.
	•	Of the total re-ratings completed through the new models, the majority have been approved, with a portion pending approval, reflecting a slight delay relative to the planned go-live schedule.
	•	Overall override activity remains limited relative to approved ratings. Overrides were primarily concentrated within HY-modeled names, with a subset resulting in IG/HY category flips.
	•	Treating Credit Risk overrides as the “true rating,” the analysis indicates a portion of IG names may be misclassified as HY by the model; however, the observed rate is materially lower than levels identified during validation.
	•	The sample size remains relatively small, and Credit Risk indicated that the selected names were randomly chosen, which may affect representativeness.


Liquidity Risk – Prime Tail Liquidity Loss (PTL)


Liquidity Risk: MRM approved enhancements to the Prime Tail Liquidity Loss (PTL) model (Risk, Tier 1), resulting in a material increase in the firm’s PTL ratio.
	•	The PTL ratio measures mitigants (e.g., overnight debits) relative to short-term funding exposure (e.g., shorts departure) and is subject to FRAC and BRC limits.
	•	Enhancements include the inclusion of previously omitted synthetic term commitments, extended debit unwind assumptions, limited position unwind recognition for two clients, and the addition of excess margin from certain clients.
	•	MRM review remains ongoing to assess the appropriateness of including excess margin from certain clients as mitigants, considering client profile characteristics and their contribution to overall mitigants.



MRM validated and approved a set of model changes that increase the Prime Tail Liquidity Loss (PTL) ratio by approximately 9% (from 137% to 146%), strengthening the firm’s liquidity position relative to short-term funding exposure.
	•	The increase reflects inclusion of previously omitted synthetic term commitments, extended debit unwind assumptions, limited position unwind recognition for two clients, and additional excess margin from certain clients.
	•	PTL remains comfortably above internal risk appetite limits (FRAC 120%, BRC 115%).
	•	MRM review is ongoing to assess the appropriateness of including excess margin from certain V26 clients as mitigants, given client profile considerations and their contribution to total mitigants.



Electronic Trading: SEC Rule 15c3-5 annual certification process is underway, requiring annual attestation of effective risk management controls for direct market access.
	•	There are currently zero overdue ETS findings, a key contra-indicator for certification.
	•	The sustained reduction in findings reflects continued strengthening of ETSC governance and control processes.


There is continued growth in the use of Artificial Intelligence (AI) models and new techniques, including recent approval of:
﻿﻿Tier 1 generative AI model owned by Corporate Treasury to automate matching of incoming payments to the appropriate internal GS bank accounts. The model will initially operate in parallel with the existing process, with the objective of reducing cash receipts requiring manual review from 13% to approximately 2%
﻿﻿Three high-severity findings relating to model performance, evaluation metrics, and testing were remediated prior to approval
﻿﻿Enhancements to the generative AI model supporting the GS AI Platform monitoring framework, including context-based personal data detection, enhanced focus on malicious intent in prompt injection monitoring, and expansion of GS proprietary datasets used for system prompt refinement and testing, including actual GS AI Assistant prompts tagged by humans
﻿﻿Lower-tier generative AI models supporting productivity use cases such as data extraction, search enhancement, and information retrieval

﻿Model Risk approved eight Internal Credit Rating (ICR) models covering Private Equity Capital Call (PECC), Direct Commercial Real Estate (CRE), and six corporate sectors, completing Phase 1 of the firm’s ICR Enterprise Risk Management Framework (ERMF) uplift plan and addressing Federal Reserve Board (FRB) feedback related to repeatability, transparency, and sustainability of the ICR framework

﻿There is ongoing focus on validation work related to Counterparty Credit Risk (CCR) management enhancements aligned with the firm’s ERMF uplift plan, including approval of enhancements to the model used to monitor incremental netting and enforceability (N&E) risk to extend coverage to Franchise and Synthetic Products Group (SPG) businesses, and enhancements to the stressed credit exposure model for margined funds to address prior validation findings




MRM also reviewed SIMM exposures with key counterparties and observed that adopting the enhanced analytics would likely increase dispute volumes, while removing the backbone assumption (i.e., calculating delta with IR volatility held constant) could materially reduce longstanding disputes

As part of the Tier 1 revalidation, MRM reviewed the IR Delta backbone methodology used by the NYC Volex desk.

Benchmarking with enhanced MRM analytics indicates IR Delta would increase by ~$2mm per bp; analysis across multiple periods shows a consistent impact

SIMM review with major vol counterparties shows adopting MRM analytics would increase disputes, while removing the current backbone assumption would materially reduce longstanding disputes

MRM raised a finding requiring methodology enhancements and formal justification; revised analytics are under review and the desk plans to engage the SIMM Governance Forum on potential changes

NYC Volex – IR Delta Analysis

As part of the significant Tier 1 revalidation, MRM reviewed the backbone methodology used by the NYC Volex desk to calculate IR Delta. Key observations:

MRM leveraged enhanced internal analytics to benchmark the desk’s approach. Using MRM analytics increases IR Delta by approximately $2mm per bp as of 13 Feb 2026.

A review of SIMM exposures for major vol counterparties (e.g., JP Morgan, Nomura) showed:

Adopting MRM analytics would increase the volume of SIMM disputes.

Removing the current backbone assumption (i.e., calculating delta with IR vol held constant) would materially reduce longstanding SIMM disputes.

Analysis across June, December, and January data shows a consistent pattern.

MRM raised a finding requiring the desk to enhance the IR delta analytics and formally justify the backbone methodology.

The desk has developed revised analytics, currently under MRM review.

The desk plans to present to the SIMM Governance Forum on potentially removing the backbone to better align with counterparties.


What Happened
Rapid sector rotations and increased market dispersion led to an underestimation of portfolio risk in EMEA EDHF, resulting in a €4mm loss from unhedged exposures
	•	Reason and Impact
The factor model adjusts slowly to abrupt market regime shifts, causing risk to lag current conditions and realized volatility to materially exceed expectations
	•	MRM Assessment
MRM assessment shows this reflects a known structural limitation of factor risk models under fast-changing markets, rather than an implementation or control issue
	•	Proposed Actions
EMEA is evaluating more responsive risk approaches, including alternative calibrations and inputs, with proposals to be submitted to MRM following testing



EDHF Factor Model Update – CRO Summary
	•	What Happened
Rapid sector rotations and increased market dispersion led the factor risk model to understate portfolio risk in EMEA EDHF, resulting in a €4mm loss from unhedged exposures
	•	Why It Happened
The model relies on longer-term historical relationships that adjust slowly during abrupt market regime shifts, causing risk estimates to lag actual market conditions
	•	Current Status & Actions
No similar impact observed in US or Asia; EMEA is evaluating more responsive risk calibration approaches, with proposed enhancements to be formally reviewed by MRM


CCAR – First Day Letter (Model Risk Focus)
	•	First Day Letter received Friday; materially model-focused, with five of nine objectives explicitly requesting model development and/or validation documentation, in addition to inventory, overlays, performance monitoring, and governance materials
	•	Obj. 1 (General Capital Planning – Monitoring): Request for summary of MRM conclusions communicated to Board and senior management (consistent with prior year); will reference MRM Board Deck and Capital Planning documentation
	•	Obj. 2 (PPNR Trading MtM): Inventory, development, and validation documents for Trading Non-Interest Income models, OAs, overlays, and adjustments; includes governance and performance monitoring
	•	Obj. 3 (Operational Loss – Monitoring): Risk and model inventory and development documentation for Op Risk models and QAs; validation documents not explicitly requested but will be prepared proactively
	•	Obj. 4 (Funding Stress in NII – Monitoring): Risk inventory, scenario assumptions, and development documentation for stressed NII models, including interest income/expense, deposit projections, and related QAs; validation not explicitly requested
	•	Obj. 5 (Wholesale Risk Capture & Translation to Loss – Monitoring): Portfolio exposures, model changes, overlays, and committee governance materials, with comparison to prior CCAR cycle
	•	Obj. 6 (Use of Models and Estimation Approaches): Inventory, development, and validation documents for wholesale loss models and QAs; specifically requests ongoing performance monitoring, 2024/2025 Annual Reviews, and MRM review of overlays
	•	Obj. 7 (xVA Risk Management): Governance over xVA P&L booking, reporting, controls, and limit breaches, including trade-level detail
	•	Obj. 8 (xVA Risk Measurement): Development and validation documentation for xVA risk metrics and curve construction models (CVA/FVA for BAU and CCAR), including treatment of risks not captured in CVA



Global Impact of Factor Risk Model Issue on EDHF
	•	Overview
Rapid sector rotations and elevated dispersion exposed limitations in Axioma/Barra factor models, resulting in risk underestimation and a €4mm loss in EMEA EDHF due to unhedged exposures
	•	EMEA Impact
	•	Trade optimization is heavily factor-model driven
	•	Portfolio risk (factor covariance–based) understated amid declining sector correlations
	•	Factor volatility inputs (250-day EMA) slow to adjust
	•	Realized volatility materially exceeded expectations
	•	Regional Comparison
	•	US: Optimization not factor-model dependent; no similar impact observed
	•	Asia: Factor model used, but no comparable portfolio impact observed
	•	MRM Assessment
	•	Reflects inherent model limitations under rapid regime shifts, not implementation deficiencies
	•	Long lookback calibration and model-derived constraints reduce responsiveness in fast-changing markets
	•	Next Steps
	•	Develop more reactive custom factor model
	•	Assess use of implied volatility for factor calibration
	•	Submit enhancements to MRM following testing as formal model change


Project Vista is a long-dated reinsurance transaction in Asia with an expected notional of approximately $240 million, potentially increasing to $400 million. The structure involves AIA ceding critical illness policy risk in Hong Kong and Macau to SCOR, which retrocedes the risk to Arrow Re to obtain capital support. Arrow Re provides capital through monthly commission drawdowns during the first year, with repayments made via retrocession premiums based on a rolling 12-month average of premiums from policies written in that period. The outstanding retrocession account balance accrues interest at the risk-free rate plus an agreed spread and is expected to amortize to zero within approximately seven years, ahead of the contract’s 11-year maturity.


Model Risk Management (MRM) performed additional validation of the Tier 1 FD CPPI Default model (Model-IT: 1717) to support a new reinsurance transaction in Asia (Project Vista) and approved its use for trade pricing. The approval enables pricing of a reinsurance structure with an expected notional of $240 million, potentially increasing to $400 million, and closes the associated transaction waiver (Waiver ID: 10979). The review focused on the model’s suitability for capturing the cash-flow dynamics of a retrocession arrangement, including monthly commission drawdowns, rolling 12-month premium-based reimbursements, interest accrual on the retrocession account balance, and the long-dated contract profile. MRM concluded that the model is fit for purpose for this transaction, with no material limitations identified that would preclude its use for the approved business.



Several audits are underway or commencing, highlighting continued focus on model governance, development, and technology controls.
	•	Model Annual Review Controls: Audit focused on recent enhancements to the Annual Review framework, including escalation, tracking, and follow-up controls.
	•	Model Development and Testing: Fieldwork in progress with walkthroughs completed; deep-dives underway on approval criteria, development logic, and ongoing monitoring.
	•	Information Security & Data Privacy (Risk Engineering / MRM): Q1 audit kicking off covering access and entitlements, configuration controls, vendor oversight, and privacy controls.


FRB requested an update, among other standard topics, on the evolution of AI/ML model use in Sales & Trading across trading, valuation, financial risk, and capital management.


Adoption of Merton Jump Diffusion and conditional probability-of-default mapping in facility-level rating models for margin loans and equities, improving capture of collateral price jumps
	•	Enhancement to the residential mortgage facility-level rating model to cover hybrid fix-and-flip and lot loan structures, extending coverage to asset classes previously handled under fallback methodologies and improving accuracy



Asset Secured Lending (ASL): MRM approved targeted model enhancements, including:
	•	FLR models (Risk, Tier 1): Adoption of Merton Jump Diffusion and conditional probability-of-default mapping for margin loans and equities, improving capture of collateral price jumps
	•	Residential mortgage FLR (Risk, Tier 1): Extension to hybrid fix-and-flip and lot loan structures, expanding coverage beyond fallback methodologies and improving risk accuracy



No significant model performance issues observed amid recent market volatility in precious metals.
	•	Gold and silver experienced their sharpest declines in decades following the Fed Chair nomination and amid a broader market correction, with volatility persisting into Asia trading hours before partially easing.
	•	MRM is reviewing precious metals trading models, with no significant deficiencies identified to date; isolated issues, including temporary risk availability constraints, routine risk-related inquiries, and expected calibration noise at short tenors, were observed.


MRM is reviewing precious metals trading models, with no model deficiencies identified to date; a small number of risk availability and risk query issues were observed and resolved.
	•	Client positions were actively unwound during the move, and models continued to perform as expected; MRM monitoring remains ongoing.


No significant model performance issues observed amid recent market volatility in precious metals, despite sharp declines in gold and silver.
	•	Gold and silver experienced their worst trading day in decades (-9% and -27%), driven in part by the Fed Chair nomination and an overdue correction following recent outsized gains, with volatility extending into Asia trading hours before partially easing.
	•	Precious metals models have remained stable, with only expected calibration noise observed at short tenors (particularly silver call wings), while ATM and 25-delta levels remain stable; H2 2025 client long VolKO positions have largely knocked out after exhausting variance budgets, and monitoring continues.


•	Gold and silver experienced their sharpest declines in decades (-9% and -27%) following the Fed Chair nomination and amid an overdue correction after recent outsized gains, with volatility persisting into Asia trading hours before partially easing.
	•	Precious metals models have remained stable through the move, with no material model issues identified; isolated risk availability and risk query issues were observed but were not model-breaking.
	•	Some expected calibration noise was observed at short tenors, particularly in silver call wings, while ATM and 25-delta levels remain stable; previously popular client long VolKO positions in H2 2025 have largely knocked out after exhausting variance budgets, and monitoring continues.


Trade Description

The trade is a daily crash put fixed-share structure with the following key features:

• Initial Price: EUR 35m
• Initial Strike Notional: EUR 80m
• Maximum Strike Notional: EUR 112m
• Maximum Number of Shares: 4.57m (Initial Strike Notional ÷ Initial Strike)
• Strike Percentage: 50%
• Strike (daily): Previous day’s closing price multiplied by the Strike Percentage
• Strike Notional: Minimum of (i) Maximum Number of Shares × Strike and (ii) Maximum Strike Notional
• Number of Shares: Strike Notional ÷ Strike
• Exercise Type: American (GS may exercise on any trading day, once only)
• Premium: 60 bps annualised, paid monthly until exercise
• Maturity: 6 months (terminates early if exercised)
• Settlement: Physical (upon exercise, GS delivers shares at the Strike)

The payoff is defined as a strip of daily units with formula:
min(Sₜ, 1.4 × S₀) × max(1 − 0.5 + Sₜ₊₁ / Sₜ, 0),
with the structure converting from fixed-share to fixed-notional if the underlying rallies sufficiently.







Transaction Waiver Summary

Desk

Equities – Volatility / Gap Risk Hedging

Trade

Daily Crash Put – fixed share structure (with conditional conversion to fixed notional)

Notional

USD 100 million per name, across 6 names

Maturity

1–2 months

Underlier

Single-name equities (including Commerzbank, Alpha Bank, T. Rowe Price)

Client

D. E. Shaw

Economics

The trade is intended to hedge the desk’s financial gap exposure in names where the firm has the largest NSFI exposure, with an indicative cost of 50–80 bps per name.

⸻

Trade Description

The transaction consists of a strip of daily crash put fix-share units, with a payoff defined as:
min(Sₜ, 1.4 × S₀) × max(1 − 0.5 + Sₜ₊₁ / Sₜ, 0).

The structure is designed to hedge short-term gap risk, with the additional feature that the payoff converts from fixed-share to fixed-notional if the underlying equity rallies sufficiently. Final payoff features are still under negotiation and will be confirmed prior to completion.

⸻

Reason for Waiver

The firm currently supports pricing and booking of fixed-notional daily crash puts, but does not yet support fixed-share daily crash puts. In addition, the trade includes a conditional feature whereby the payoff becomes fixed notional following a sufficient rally, which is not yet fully represented in existing tradables.

⸻

Proposed Booking During Waiver Period

The trade will initially be booked using the fixed-notional equivalent (EqSp KO Daily Crash Put).
An interim implementation has been developed in the EqSp CMS Linked Note, which will be migrated into production on Monday, allowing the economic exposure to be captured while full functionality is completed.

⸻

Compensating Controls

The desk noted that the EqSp CMS Linked Note correctly captures the crash risk component of the structure, with remaining features (including fixed-share behavior, immediate settlement, and physical delivery) to be incorporated through near-term enhancements.

⸻

Remediation Plan

• Release an updated version of the EqSp CMS Linked Note by Monday to correctly price gap risk
• Enhance the EqSp OMS Linked Note next week to support additional features, including physical settlement and immediate settlement
• Submit the complete model to MRM for validation by the end of next week




Transaction Waiver Summary

Desk

Equities – Hedge Fund Financing / Structured Equity

Trade

Large OET Total Return Swap (TRS) referencing a hedge fund, with gated redemption mechanics passed through upon termination

Counterparty / Client

Al Maha SPV, owned and guaranteed by Abu Dhabi Investment Council (ADIC)

Notional

USD 750 million
(Note: pipeline of similar trades, with potential scale up to USD 10 billion notional)

Terms

• Standard 1-year equity swap with Open Early Termination (OET)
• OET notice: 5 business days for client, 60 business days for GS
• Upon termination or OET, the swap enters a 2-year unwind period consistent with the underlying fund’s liquidity terms
• Redemption schedule: 12.5% notional reduction per calendar quarter (8 quarters total)
• 45 business day redemption notice
• Quarterly notional resets and equity leg payments
• Quarterly floating payments

Underlier

Walleye Opportunities Fund LP

Structure Overview

• GS sells synthetic exposure (TRS) on the hedge fund to ADIC
• GS establishes Signum Fund 4 SPV, which becomes the Limited Partner in the Walleye fund
• GS holds preferred shares in the SPV, obtaining full economic delta exposure
• SPV structure ensures transferability of hedge fund interests in case of regulatory or structural changes without manager consent

Economics

Expected P&L: >50 bps p.a. (minimum USD 5 million per annum)

Strategic Rationale

The desk believes this is the first set of trades in a scalable structure with potential to reach up to USD 10 billion in notional and generate more than USD 50 million per annum for the firm, while materially strengthening the firm’s relationship with ADIC and the broader hedge fund and large asset allocator franchise.

⸻

Reason for Waiver

The firm currently does not have a swap tradable that correctly represents the scheduled redemption and unwind mechanics of the underlying hedge fund following a swap termination or OET event.
Upon termination, rather than an immediate unwind, the trade enters the fund’s redemption cycle, leaving residual delta and funding exposure outstanding for up to eight additional quarters, which is not accurately captured in existing tradables.
The desk has confirmed with SPG Strats that no existing swap tradable appropriately models this redemption profile or the resulting Credit and ALM risk to GSIU.

⸻

Proposed Booking During Waiver Period

The trade will be booked as a structured equity trade comprising eight linked swaps, corresponding to each potential quarterly cancellation date.
• Each individual swap is set to be called on its first valid date, ensuring alignment in pricing and valuation
• As long as no cashflow is generated, the trade will function correctly in downstream systems
• This approach allows correct pricing of the economic exposure while the formal tradable enhancement is developed

⸻

Compensating Controls

The desk noted that the trade prices correctly under the proposed structure, with the primary limitation arising only when cashflows are generated, at which point exposures and unwind mechanics will be manually reviewed and monitored to ensure residual delta, funding, and credit risks during the redemption period are appropriately captured and escalated.


Sure — here’s a tighter, cleaner version with the same content but much more executive-ready and scannable:
	•	FRB CAR NPR: Submitted response on proposed model changes to PPNR, fair value option (FVO) loan losses, and Global Market Shock (GMS)
	•	ECB SREP feedback: Completed remediation of model inventory completeness finding

AIRCC approvals (YTD):
	•	XX new use cases and XX extensions approved by committee, including XX
	•	XX low-risk use cases and XX extensions approved via streamlined review, including XX

AI model approvals (YTD 2026):
	•	Approved 8 AI models (1 Tier 1, 2 Tier 2, 5 Tier 4), including:
	•	Payment Settlements AI (CT, Tier 1): GenAI model for reconciling incoming payments to correct accounts
	•	Botnation AI (GBM, Tier 2): GenAI-enhanced quote parser replacing legacy ML Botnation in FICC

Validation activity (YTD):
	•	Completed 42 model, QA, and DRC validations, including:
	•	Counterparty Credit Risk: Approved enhancements to CCR management, including:
	•	Migration of DCS shortfall benchmarking to CREST V30 (GBM, Tier 1), addressing a validation finding
	•	Enhancement to US natural gas delta liquidation charge in the Franchise FIC Commodities Benchmark model (GBM, Tier 1), enabling netting of offsetting exposures
	•	Pricing models: Approved new volatility surface calibration for Monte Carlo pricing of complex multi-cross options, replacing an unstable prior model and improving stability, performance, and noise reduction
	•	Asset Secured Lending: Approved FLR model enhancements (Risk, Tier 1), including:
	•	Extension to hybrid fix-and-flip and lot loan deals
	•	Adoption of Merton Jump Diffusion and conditional PD mapping to better capture collateral price jumps



Following confirmation from the Bureau of Labor Statistics that the October US CPI will not be published due to the government shutdown, fallback CPI values were required for US TIPS and CPI swap instruments referencing the October fixing. Two established fallback methodologies were applied, with US TIPS using the TIPS fallback, cleared inflation swaps using the ISDA fallback, and bilateral trades permitted to use either approach. Model Risk Management validated and approved the modelling of the USD CPI fallback methodologies to ensure consistent valuation and risk capture across affected products. Two Severity 2 findings were identified relating to an implementation issue, which has since been remediated, and to gaps in testing and documentation, with remediation actions underway. The overall P&L impact was minimal, as inflation curves had already been remarked in line with the approved fallback values.



In November 2025, an operational risk event occurred during a pilot of a new US Equity Delta Hedging Facility (EDHF) strategy, resulting in a ~$1.7mm loss. The loss stemmed from a manual configuration and account-mapping error, where the pilot position was traded in an account not properly set up for the strategy. As a result, the strategy misinterpreted start-of-day risk at an aggregate level without reading per-account positions, leading to an erroneous accumulation of approximately $50mm ADV exposure, which was identified and unwound within ~20 minutes by the desk. The issue created a short feedback loop that repeated several times before intervention. No broader system failures were identified, and existing hard backstop controls would have blocked activity at higher exposure levels had the issue not been detected. Remediation actions include enhanced end-to-end testing, improved model code tagging, and strengthened documentation to reduce reliance on manual configuration for future strategy pilots.


•	Deb (FRB) asked for additional detail on the three-month policy exception granted by the Head of MRM to support continued use of models and qualitative approaches inherited through a recent asset management acquisition, including the expected scope and oversight during the exception period
	•	The firm explained that the exception is intended to provide a time-bound inventory and assessment period, during which the business will:
	•	Identify models and spreadsheet-based calculations used by the acquired entity
	•	Determine whether items should be mapped to existing GS models, uplifted into the GS MRM framework as new models, or retired
	•	The firm noted that the current expectation is a limited population, with many items likely to be spreadsheets or calculations that can be mapped to existing GS models rather than requiring full validation as standalone models
	•	The firm clarified that the three-month checkpoint is intended to establish a clear remediation plan and population size; following this review, MRM will determine whether:
	•	Items can be handled through business-as-usual exception processes (if de minimis), or
	•	A time-bound extension of the policy exception is warranted to support a structured uplift plan
	•	The firm noted this approach is consistent with prior acquisitions (e.g., NNIP and other smaller integrations), where temporary policy exceptions were used to allow orderly inventory, risk assessment, and uplift to GS standards without disrupting ongoing business activity



Deb (FRB) asked whether the Guardrails monitoring model enhancements (PII detection and prompt-injection detection; false-positive reduction) were triggered by ongoing monitoring results, and more broadly how the firm is approaching ongoing monitoring for AI/ML models given that performance monitoring can be less straightforward than for traditional models
	•	The firm explained that the Guardrails model operates as part of a broader AI monitoring framework, including a dedicated AI monitoring group that reviews incidents and Guardrails metrics on a monthly cadence and includes relevant stakeholders (including Legal and Compliance)
	•	The firm noted that enhancements were informed by review of flagged cases and user/ reviewer feedback, with a focus on reducing benign false positives while continuing to capture higher-risk behavior (e.g., refining what constitutes meaningful PII and improving prompt-injection signal quality)
	•	Deb (FRB) asked whether the firm is setting explicit thresholds/metrics for AI/ML model monitoring similar to traditional models, or whether monitoring is primarily driven by qualitative feedback and incident review
	•	The firm responded that many AI/ML models do use quantitative performance thresholds, typically established by the first line and validated by MRM as part of approval (e.g., green/amber/red bands with escalation actions up to and including model shutdown if performance deteriorates), while also noting that the firm is still early in standardizing these practices and is working toward a more systematic/centralized approach over time
	•	Deb (FRB) also asked whether AI/ML models are being incorporated into the Risk Appetite Statement (RAS) framework through AI-specific metrics, or whether they fall under the existing RAS metrics
	•	The firm confirmed that AI/ML models are already captured under existing RAS metrics (RAS applies to all models), noting that Tier 3/2/1 AI models would be in-scope for the relevant RAS measures, while Tier 4 models are generally low-risk; the firm added that governance and standards will continue to evolve as higher-tier AI usage grows


Meeting Minutes

Q4 2025 Quarterly Model Risk Management (MRM) Meeting with Federal Reserve Board (FRB)
Meeting Date: [not stated in transcript; held in early January 2026]
Period Covered: Q4 2025

MRM held its quarterly meeting with the FRB to provide updates on model validation activity and findings; Internal Audit (IA) issues; issue remediation; RAS exceptions and aged items; model inventory updates including AI/ML segmentation; key model changes (enhancements and redevelopment); ongoing monitoring results and thematic observations; and progress on the “Weaknesses in Model Validation Controls Framework” MRA remediation.

In addition, FRB noted a separate request from Patrick for the firm’s model inventory inclusive of generative and agentic AI indicators, due February 10; the firm is preparing this separately and it was not included in the meeting agenda.

⸻

Key Discussions

1. Model validations and status of findings
	•	Caroline presented Q4 validation activity and the quarter-over-quarter evolution of open findings, noting a slight, moderate increase in open findings and continued focus on remediation, including 310 findings closed during the period
	•	FRB asked for details on the three models where annual review outcomes resulted in triggered revalidations; Caroline explained (i) annual review may be satisfied via scheduled revalidation for certain models, and (ii) annual review can trigger revalidation where warranted
	•	Caroline later provided additional color that the three triggered revalidations relate to three Tier 1 Risk-owned models, driven by (a) materiality/time since last revalidation for a capital model, and (b) scope/usage changes for two models (including a new feeder model identification and a climate risk model with expected scope expansion); additional details to be provided as needed

2. Internal Audit findings and MRM issues raised by IA
	•	Caroline summarized IA activity and noted that in 2025 the firm had nine audits focused on model controls (all effective opinions), and MRM also participated in 50+ additional audits where model controls were a component
	•	Caroline reviewed four open IA findings, all General (lowest severity), including:
	•	One previously discussed finding related to GitLab change control
	•	Three documentation-focused items requiring incremental enhancements to validation documentation (Tier 2 models / Tier 2 deterministic regulatory calculation (DRC))
	•	FRB asked for details on the Tier 2 DRC “feeder model” documentation item and whether it reflected an input appropriateness concern or a template issue; Caroline clarified:
	•	The issue was a documentation enhancement, not a concern that feeder inputs were inappropriate
	•	IA expectations were for more explicit acknowledgment/assessment of feeder models in the validation package, consistent with existing validation documentation requirements
	•	IA did not identify inadequacy in the firm’s actual model assessment; findings were focused on documentation completeness
	•	Caroline reported four IA findings closed in Q4, all General severity, primarily documentation-related (including Tier 1 models and a Tier B qualitative approach), with some items raised and closed quickly during the quarter

3. RAS exceptions and aged items
	•	Caroline provided the RAS update using the same format as the weekly report provided to the firmwide risk appetite committee, and confirmed no Board- or FRAC-level breaches for models under waiver during the period and generally low utilization
	•	FRB asked to confirm the standard waiver duration for unvalidated models in use; Caroline confirmed the standard waiver period is three months
	•	Caroline reviewed aged waiver thresholds (e.g., >6 months at FRAC and >1 year at Board) and noted the aged waiver metrics remained 0
	•	Caroline highlighted continued FRAC threshold breach for Tier 1 models with aged findings following the threshold tightening effective October 1 (from 9 months to 6 months past due date)
	•	Caroline noted the breach was driven by five Tier 1 Counterparty Credit Risk models (GBM/GPM); since year-end, two have been remediated/closed, and revised target dates have been set for the remaining items
	•	FRB questioned whether the tightened threshold is achievable given persistent breaches; the firm responded:
	•	The intent is to return to compliance and remain compliant; senior GBM management engagement was noted, including CRO attention
	•	The firm expects to return below the threshold by end of Q2 and emphasized the threshold is intended to drive timely remediation rather than create tolerance for aged items
	•	The firm also noted broader control pressure via RCSA, where persistent overdue remediation patterns may impact control effectiveness assessments

4. Model inventory updates, including AI/ML segmentation
	•	Caroline noted overall model inventory remained stable year-over-year (approx. +150 models), with some reclassification and re-tiering activity
	•	FRB asked about a specific case where a Tier 2 model was re-tiered to Tier 4, and clarified Tier 4 as very low-risk AI/ML; the firm explained the change reflected additional information obtained during the risk-tiering process prior to go-live, including a robust human-in-the-loop control environment
	•	FRB asked about “unclassified models”; the firm clarified these are declared models pending completion of initial risk tiering (including follow-ups to developers and internal review/approval steps)
	•	Caroline presented the AI inventory segmentation (generative vs. non-generative; agentic use cases currently small) and clarified the “AI platform” category:
	•	“Tier 1–4” refers to use-case models built on an AI platform
	•	“AI platform” refers to underlying tools/platforms (e.g., foundational LLMs and general-purpose productivity tools) that are inventoried but validated in the context of specific use cases, not “in the abstract”
	•	Caroline confirmed the forthcoming inventory submission requested by Patrick will include Tier 1–4 AI models and AI platforms, along with generative and agentic AI indicators (due February 10), with the FRB to follow up with questions after review

5. Model changes, including enhancements and redevelopment
	•	Shipra provided thematic updates on key Q4 approvals and enhancements, including:
	•	Internal Credit Rating (ICR) models: approval of eight Tier 1 ICR models (Private Equity capital call / Direct CRE / six corporate sectors), supporting ERMF uplift objectives and addressing supervisory feedback on repeatability and transparency; 13 high-severity findings raised and closed within initial validation, including remediation related to data fit/representativeness and bucketing methodology
	•	AI models: continued growth, including enhancements to the Guardrails monitor model (prompt injection detection and PII; focus on reducing false positives), two new Tier 2 approvals (web search grounding in GS AI assistant to improve latency; GenAI extraction of Japanese term sheet information in GPM), and lower-tier productivity use cases
	•	ASL / GBM / CCR / Treasury / Liquidity / Market Risk: a range of enhancements including underwriting/pre-trade extensions, CPI fallback methodology, FX calibration methodology improvements, a Tier 1 valuation adjustment model, CCR model coverage extension, DCS shortfall benchmarking migration, Prime Services banking book sensitivity model uplift, liquidity risk model enhancements (including internalization liquidity risk), and market risk infrastructure migration
	•	Policy exception for acquired models/QAs: Head of MRM granted a three-month policy extension to allow AWM to inventory and assess models/QAs from an acquisition (Industry Ventures) and define uplift/retirement/mapping plans; the firm expects a de minimis population and will reassess at the end of the three-month period, extending or transitioning to BAU exception processes as appropriate

6. Ongoing monitoring, including thematic issues and impact
	•	Shipra summarized Q4 ongoing monitoring outcomes and noted no high-severity findings raised from ongoing monitoring during the quarter
	•	Four medium-severity items were highlighted, including:
	•	AWM portfolio decomposition risk underestimation identified during annual review/OM report review (under remediation)
	•	Two franchise shortfall back-testing issues related to missing/inaccurate risk factors (remediated via model enhancements)
	•	A Tier 2 surveillance model performance deterioration addressed via retraining with latest data and additional enhancements
	•	Market risk back-testing review identified no material breaches; credit risk results remained under review, with one prior medium-severity item still open but within thresholds

7. Weaknesses in Model Validation Controls Framework MRA remediation progress
	•	Caroline confirmed completion of remediation for both the original MRA and incremental CCAR 2025 feedback by the December 19 deadline, and noted IA has initiated validation of the remediation package
	•	Caroline clarified IA previously completed an interim review of earlier remediation components (referenced as “AP 1.1 and 1.2”), including the enhanced framework and MRCC approval in September, with no additional actions identified; IA has now initiated review of subsequent remediation evidence and may request additional documentation

⸻

Follow-ups / Action Items
	•	Firm to provide additional details on the three Tier 1 models whose annual review outcomes triggered revalidation (beyond the high-level drivers shared on the call), if the FRB requests more detail
	•	Firm to deliver the year-end model inventory submission inclusive of generative and agentic AI indicators (and AI platform inventory), per Patrick’s request, due February 10
	•	FRB offered that the firm may submit AI-related policy/guidance questions in writing for routing to David Palmer; the firm may follow up separately as needed


The FRB requested our model inventory, including last and next validation dates and artificial intelligence indicators (AI/ML, Generative AI, Agentic AI), in addition to the standard inventory information previously providedRecent market volatility, including bear-steepening in rates following the Japan snap election announcement, has not resulted in any material model performance issues, and monitoring remains ongoing.
	•	The announcement of snap elections and a proposed temporary food consumption tax cut raised fiscal concerns and drove a pronounced bear-steepening in JGBs, particularly at the long end of the curve.
	•	Model Risk Management is reviewing trading models used for Japan-related activity; trading to date has been predominantly flow-driven (bond-related), with no modeling issues identified thus far.


Japan snap election: MRM is reviewing trading models used for Japan-related activity following the bear-steepening in JGBs, with trading predominantly flow-driven (bond-related) and no modeling issues identified to date.



is reviewing trading models used for Japan-related activity. To date, impacted trading has been predominantly flow-driven (bond-related), with no model deficiencies identified. The review remains ongoing.

AI Risk Management and Governance – External Benchmarking (Oliver Wyman)
	•	Met with Oliver Wyman partners on peer-bank practices in AI risk management and governance, following AI topical sessions.
	•	AI Kill Switches: Broad consensus that AI kill switches are necessary and distinct from traditional risk controls; approaches range from enterprise-level CRO controls to use-case-specific backstops (e.g., disabling chatbots when confidence thresholds are breached).
	•	MRM Scaling: CROs and Heads of MRM are focused on how MRM scales with exponential AI growth; peer approaches align with GS, leveraging automation, upskilling existing staff, and targeted strategic hiring.
	•	Monitoring Frameworks: Second line sets standards, with first line executing due to scale; banks vary between centralized monitoring teams and federated business-owned models.
	•	Governance Efficiency: Firms are moving from reviewing every AI use case to lighter-touch reviews for common patterns, consistent with GS AIRC streamlining.
	•	Third-Party AI: Practices vary, with some banks treating vendor AI as models and others, similar to GS, relying on vendor risk management.
	•	Agentic AI: Viewed as a key 2026 theme; human-in-the-loop controls are insufficient, requiring real-time monitoring, measurable KPIs, and explainability.


Artificial Intelligence

Botnation AI (GBM, Tier 2)
	•	MRM approved Botnation AI, a GenAI-enhanced quote parser for GBM.
	•	The model enhances the existing ML-based Botnation solution used in FICC, addressing areas where traditional ML underperforms.
	•	Achieved strong accuracy across asset classes: 98% for FX, 99% for Bonds, and 98% for Credit ETFs.
	•	As part of validation, MRM designed stress tests by introducing random typographical errors into quotes; accuracy declined materially under stress, highlighting a known model limitation, though performance remained superior to the ML-only Botnation.
	•	GBM plans to extend coverage across FICC, with the next review commencing in Commodities.

Guardrails for LLM (Engineering, Tier 1) – Version 3.2
	•	MRM approved version 3.2 of the LLM Guardrails framework.
	•	Enhancements include a new guardrail for PII misuse, expanding beyond detection to assess usage context and intent.
	•	Additional improvements include refinements to existing guardrails, prompt fine-tuning, and an upgrade to Gemini 2.5 Flash.

LLM Upgrades for GBM AI Models
	•	GBM AI models (e.g., Marquee AI, Sentistats) are undergoing LLM upgrades.
	•	Review processes for LLM upgrades have been streamlined by leveraging existing validation analyses where appropriate.
	•	For Tier 3 models, upgrades require notification only, with no re-approval required.






Summary
	•	Continued enhancement of the GS AI Platform monitoring framework to detect and mitigate potentially unsafe interactions between users and large language models
	•	Ongoing focus on AI governance, including recent enhancements to the AI Policy and the Standard for Agentic AI

Risk Management Actions / Next Steps
	•	Validation activities focused on monitoring framework enhancements, including context-based PII detection and improved identification of malicious intent in prompt-injection monitoring
	•	Policy enhancements reinforce expectations for increased ongoing testing as autonomy increases and human oversight decreases, and strengthen controls over agent access to data, tools, and systems, defined operating boundaries, and monitoring of agent actions and decision outcomes





The index replicates a Total Return Forward exposure by applying a 10× multiplier to the performance difference between the gross return index and the rolling futures total return index



Trade Description
	•	Trade type: Standard autocallable note on a replicated TRF decrement index
	•	Underlying: Euro Stoxx Select Dividend 30 Futures Roll EUR Total Return Index, with a replicated TRF decrement mechanism
	•	Index construction: The index replicates a leveraged Total Return Forward exposure by applying a systematic percentage decrement to benchmark performance
	•	Decrement methodology: The decrement is based on the performance difference between the gross return index and the rolling futures total return index, representing the TRF funding component
	•	Rebalancing: Index is rebalanced periodically in line with predefined rules
	•	Coupon: Fixed annual coupon
	•	Autocall feature: Quarterly observation dates starting at the end of year 1; early redemption at par plus accrued coupon if the autocall barrier is met
	•	Maturity payoff: If not autocalled, redemption at par if the final index level is above the maturity barrier; otherwise redemption is linked to final index performance



Dear Fragomen Billing Team,

This email is to provide remittance details for payment made in connection with the I-907 Premium Processing Service.

Please find the payment details below and/or attached for your reference:

- Service: I-907 Premium Processing Service  
- Payer Name: Yibo Li  
- Payment Date: [MM/DD/YYYY]  
- Amount Paid: [$ Amount]  
- Payment Method: [ACH / Wire / Check]  
- Reference / Confirmation Number: [If applicable]

Please let me know if any additional information is required to properly apply this payment.

Thank you.

Best regards,  
Yibo Li


Insufficient risk capture was identified in the franchise margin shortfall models, where inadequate FX delta treatment for FX swaps contributed to backtesting breaches; the findings have been remediated through model enhancements


Risk underestimation was identified in the AW portfolio risk decomposition model, where ongoing monitoring reports showed realized volatility exceeding ex-ante model estimates for certain accounts in short-duration, CLO, and emerging markets strategies; model developers are investigating root causes and implementing modeling enhancements where appropriate
	•	Performance deterioration was observed in classification metrics for the Engineering machine-learning model used to detect unauthorized access to production environments; the finding has been remediated through model retraining using additional, more recent data
	•	Insufficient risk capture was identified in the franchise margin shortfall models, including missing interest rate volatility shocks for swaptions and inadequate FX delta treatment for FX swaps that contributed to backtesting breaches; the findings have been remediated through model enhancements



Risk underestimation was identified in the portfolio risk decomposition model used at total portfolio, strategy, and security levels, where ongoing monitoring reports showed realized volatility materially exceeding ex-ante model estimates for certain accounts in short-duration, CLO, and emerging markets strategies; remediation is in progress
	•	Performance deterioration was observed in a firmwide machine-learning model used to detect unauthorized access to production environments, with declines in key classification metrics including accuracy, F1 score, precision, and recall identified through ongoing monitoring during the 2025 additional validation; remediation is in progress
	•	Gaps in risk capture were identified in the margin shortfall model, including missing interest rate volatility shocks for swaptions, inadequate FX delta treatment for FX swaps contributing to backtesting breaches, and incorrect application of default charges for bonds with pricing errors or missing base prices; remediation is in progress




o the model used to monitor incremental netting and enforceability (N&E) risk to extend coverage to franchise and Synthetic Products Group (SPG) businesses, and enhancements to the model used for calculating credit exposure under stress scenarios for margined funds to address validation findings

US government shutdown, including approval of the implementation of US Consumer Price Index (CPI) fallback methodologies aligned with formulas published by the US Treasury and ISDA
** Fallback CPI values are required for US Treasury inflation-protected securities (TIPS) and CPI swaps referencing the October US CPI, which was not published due to the government shutdown

Risk management enhancements, including approval of a new volatility surface calibration methodology for Monte Carlo-based pricing of multi-cross binary options, rainbow options, either-or options, and basket options with four or more crosses
** The new methodology replaces a prior model with frequent short-end calibration failures, resulting in more stable risk calculations, faster performance, and reduced Monte Carlo noise

Valuation adjustments, including approvals of:
** A new Tier 1 model to calculate skew liquidity valuation adjustment (LVA) for the US Volex desk covering European swaptions and interest rate cap and floor options, supporting Controllers’ determination of liquidity reserves
** Enhancements to the Tier 1 equity bid-offer spread reserve model to include equity-equity and equity-FX correlation reserves that were previously not captured, resulting in more stable reserves during market rallies

Extension of the Tier 1 model used to monitor incremental netting and enforceability (N&E) risk to franchise and Synthetic Products Group (SPG) businesses, following prior approval for Futures, Derivative Clearing Services, and Securities Lending, enabling consistent netting-node calculations as part of the ERMF uplift

Enhancements to the V30 version of the CREST credit model used for shortfall benchmarking in Derivative Clearing Services (DCS), addressing a validation finding on divergence relative to other business lines

margin shortfall modeling enhancements for franchise benchmark models, including decomposition of repo cash legs and inclusion of collateral in worst case loss and shortfall calculations, addressing validation findings

Approval of a new Tier 1 model to calculate net interest income (NII) and sensitivity for the Prime Services banking book, developed as part of the ERMF uplift and supporting integration into the centralized firmwide Earnings at Risk (EaR) framework

Model Risk approved a new Tier 2 model to estimate optimal uplend amounts (excess liquid assets lent back to the parent as a short-term loan) to maximize parent company liquidity benefits, replacing previous manual calculation
 * This is part of a broader Corporate Treasury initiative to improve efficiency and systematize inventory funding calculations through integration with the Delphi platform

Liquidity Risk: Approval of enhancements addressing supervisory findings on secured and internalization funding risk limits, including:
** Enhancements to the Tier 1 internalization risk model to measure spot internalization risk from synthetic and physical equity collateral
*** Two high-severity findings related to testing and documentation were remediated prior to approval
** A new Tier A qualitative approach to establish limits for managing maturity concentration risk of secured funding liabilities under stress

Market Risk: Approval of a new Tier 1 model to capture profit and loss profiles under a range of equity risk factor shocks for risk and limit management purposes
** Implemented on the new GSRisk infrastructure as part of a strategic initiative to migrate from RockBox and enable more efficient risk calculations


On January 5, 2026, GS completed the acquisition of Industry Ventures, a venture capital platform investing across all stages of the venture capital lifecycle

To support continued business operations following the acquisition, the Head of Model Risk Management (MRM) granted three-month policy exceptions for the use of existing models and qualitative approaches, during which gaps to GS standards will be assessed and uplift plans established, including:
** Asset & Wealth Management (AWM) will finalize the model inventory and define the uplift plan
** MRM will assign risk tiers to the models and qualitative approaches and establish a validation plan
** Based on the scope of required uplift, MRM will either:
*** Extend the policy exception to cover the uplift period, or
*** Address the items through business-as-usual exception processes, such as waivers or Risk Appetite Statement (RAS) limits, where appropriate

Models from the acquired business are not included in GS RAS metrics until policy exceptions are resolved and required uplifts are completed


There is continued growth in Artificial Intelligence (AI) models and use of new techniques, including approval of enhancements to the personally identifiable information (PII) and prompt injection detection components of a generative AI model that serves as a monitoring framework for the GS AI Platform, used to identify potentially unsafe interactions between users and large language models

There is continued focus on validation work supporting Counterparty Credit Risk (CCR) management enhancements under the ERMF uplift, including approvals of enhancements to the netting and enforceability (N&E) risk monitoring model to extend coverage to franchise and Synthetic Products Group (SPG) businesses, and enhancements to stressed credit exposure models for margined funds to address validation findings

US government shutdown related model enhancements, including approval of US Consumer Price Index (CPI) fallback methodologies prescribed by the US Treasury and the International Swaps and Derivatives Association (ISDA), addressing data unavailability resulting from the shutdown























The desk considers the model assumptions to be conservative, with pricing and charges providing sufficient buffer for model uncertainty:
	•	Removing the call features results in an issuance price of approximately –1% PV (–$120k), indicating that optionality is not driving excess value
	•	Implied volatility is bid near historical lows, while skew is marked at the steeper end of observable G3 and EMEA IRS volatility markets, limiting upside bias
	•	The model assumes deterministic GS spreads, which is conservative, as historically the realised volatility of HUF cross-currency rates plus GS spreads has exceeded the realised volatility of HUF cross-currency rates alone



Breaches were observed in select sub-entities (GSCO, GSFM), for which findings were raised related to the use of proxy time series instead of entity-specific data for certain equity names and the absence of certain new equity risk factors in the VaR model.


Market Risk
	•	Scope of review: MR reviewed Q3 2025 backtesting results across the GS Group and all legal entities subject to standalone capital requirements, including desk-level sub-portfolios where relevant
	•	Review approach: For observed breaches, MR assesses potential drivers including risk-factor data quality, proxy usage, unmodeled risk factors, and portfolio-level conservatism, and evaluates whether under-performance in specific sub-portfolios is offset by acceptable performance elsewhere
	•	Q3 outcomes: No new Group-level backtesting breaches were observed in Q3 2025; breaches were observed in select sub-entities (GSCO, GSFM)
	•	Findings and conclusion: Findings were raised for the affected sub-entities; based on the full review, MR continues to conclude that the VaR framework remains fit for purpose at the Group level, noting increased distance between VaR and P&L in Q3 following two breaches in April

⸻

Credit Risk
	•	Scope of review: MRM reviewed Q3 2025 backtesting results across credit portfolios, including Securities Financing Transactions (SFTs) and interest rate potential exposure (PE) models
	•	Review approach: For observed breaches, MRM evaluates whether excessions are attributable to model assumptions or parameterization, Monte Carlo noise, or market-driven effects, and assesses consistency of results across frameworks and regions
	•	Q3 outcomes: Q3 2025 backtesting results were shared with MRM on January 5 and are currently under review; preliminary results indicate stable overall model performance
	•	Findings and next steps:
	•	SFTs: MRM is investigating the persistently high frequency of small-magnitude backtesting breaches (less than 5% excessions), which are disproportionately observed in SFTs, including cross-checks against EMEA backtesting under the new framework
	•	Outstanding finding: One medium-severity finding remains open as of March month-end related to the interest rate PE model for inflation-linked products, where increased long-horizon backtesting exceptions during inflation regime transitions indicate model limitations; remediation is in progress


Market Risk
	•	Scope of review: MR reviewed Q3 2025 backtesting results across the GS Group and all legal entities subject to standalone capital requirements, including desk-level sub-portfolios where relevant
	•	Backtesting outcomes: No new Group-level backtesting breaches were observed in Q3 2025; breaches were observed in select sub-entities (GSCO, GSFM), for which MR raised findings
	•	Breach diagnostics: Where breaches occur, MR assesses potential drivers including risk-factor data quality, proxy usage, unmodeled risk factors, and model conservatism at the portfolio and sub-portfolio level
	•	Model assessment: Despite increased distance between VaR and P&L in Q3 (following two April breaches), MR continues to find the VaR framework fit for purpose at the Group level, noting that isolated sub-portfolio under-performance did not outweigh acceptable performance elsewhere

⸻

Credit Risk
	•	Backtesting status: Q3 2025 backtesting results were shared with MRM on January 5 and are currently under active review
	•	Overall performance: Preliminary review indicates stable model performance across credit portfolios
	•	Securities Financing Transactions (SFTs): MRM is investigating the persistently high frequency of small-magnitude backtesting breaches (less than 5% excessions), which are disproportionately observed in SFTs
	•	The investigation is focused on assessing whether these breaches are driven by model parameterization rather than Monte Carlo noise or market events, including cross-checks against EMEA backtesting results under the new framework
	•	Outstanding finding: One medium-severity finding remains open as of March month-end
	•	Interest Rate PE Model (Inflation-Linked Products): An increase in long-horizon PE backtesting exceptions during inflation regime transitions indicates limitations in capturing risk during such phases; remediation is in progress




Pricing Models: Significant validation effort focused on complex and high-impact pricing models, including:
	•	Validated and approved implementation of US CPI fallback methodologies prescribed by the US Treasury and ISDA, addressing pricing data unavailability arising from the government shutdown
	•	Identified material deficiencies in a Tier 1 pricing model for TRY cross-currency zero-coupon Bermudan cancellable swaps, and approved remediation with material valuation impact
	•	Validated and approved enhancements to Credit Support Agreement (CSA) pricing models enabling recognition of Funding Valuation Adjustment (FVA) at default, addressing previously unmodeled exposure




MRM is investigating whether the statistically elevated frequency of small-magnitude backtesting breaches in Securities Financing Transactions (SFTs) is model-related rather than driven by market events


Continued in-house MRM development leveraging GenAI to enhance validation workflows, with planned capabilities including:
	•	Automated drafting of MRM validation documentation
	•	GenAI-assisted Annual Review commentary
	•	Support for tracking material model changes, including documentation updates and Annual Review narratives
	•	Automated identification of recurring findings patterns and emerging model vulnerabilities




Resolved all FRAC breaches by remediating [#] unvalidated business activities (including [#] aged findings) inherited at transition from Compliance, bringing the population to zero

Model Risk–related activities and controls are assessed as part of the firmwide Risk Control Self-Assessment (RCSA). Model developers and Strats should be aware of how Model Risk metrics and practices are referenced in RCSA and where supporting information can be found. For detailed guidance on RCSA methodology and requirements, please refer to the Operational Risk Confluence page. The guidance below highlights the limited set of Model Risk considerations relevant for RCSA and points to authoritative sources, including PRISM, to help ensure controls are appropriately reflected in the assessment.



Here is a concise 4–5-bullet version without formulas, keeping only the key points:

⸻

USD CPI Fallback Approval
	•	BLS confirmed the October US CPI will never be published due to the government shutdown; November CPI will be released with a short delay but does not trigger fallback usage.
	•	Fallback CPI values are required for US TIPS and CPI swaps referencing the October fixing, with two fallback methodologies applied (TIPS fallback and ISDA fallback).
	•	Applicability: TIPS use the TIPS fallback; cleared inflation swaps use the ISDA fallback; bilateral trades may use either, though most are using the TIPS fallback in practice.
	•	MRM validated and approved the modelling of the USD CPI fallback methodologies, raising two findings (one implementation bug, now remediated, and one on documentation/regression testing enhancements).
	•	P&L impact is minimal as inflation curves have already been remarked consistent with the fallback values.

⸻

Let me know if you want it even tighter for a slide.



•	Other material findings expected to require MRM involvement relate to outsourcing granularity, absence of a framework for RNIEPE, IMM backtesting, and initial margin modeling for cleared business
	•	Less material findings include weaknesses in validation, ST-portfolio modeling, representative-portfolio construction, treatment of hard-to-replace trades, infrastructural testing, and documentation


Establishes limits to manage maturity concentration risk that arises when large portions of secured funding mature in a short window and may not roll over under stress.

Liquidity Risk Models
MRM revalidated and approved enhancements to the Internalization Grid model (Risk, Tier 1) and the new Maturity Concentration Limits (MCL) qualitative approach (Risk, Tier A), closing supervisory findings on secured and internalization funding risk limits.
• Internalization Grid: Added spot-risk measurement; remediated two high-severity testing and documentation findings prior to approval
• MCL Qualitative Approach: Establishes limits to manage concentrated secured funding maturities during stress

Asset Secured Lending Models
Recent Tier 1 model enhancements approved for the business include:
• Facility-Level Rating (FLR): Adopted CECL-based PD/LGD framework for direct CRE, replacing judgmental methodology and addressing validation findings
• Collateral Valuation & Tail Risk (PECC): Incorporated fund-level recovery into valuation and tail-risk models for PECC loans
• CLO Warehouse Tail Risk: Added hedge-benefit recognition to the CLO warehouse tail-risk model



Here are 4–5 simplified bullets:
	•	Financial-services AI PoCs are still concentrated in fraud detection, customer engagement and service automation; broader adoption remains early
	•	Prompt-injection remains a real risk — Apexon shared a case that temporarily shut down their site and led to new safety controls
	•	Agentic AI can break easily from vendor upgrades, implying heavy ongoing-monitoring and change-review needs
	•	Allowing AI to write data significantly heightens bias risk; industry is cautious and still mostly using GenAI for partial drafting (GS may be ahead on full-doc use)
	•	External examples (e.g., aerospace) show GenAI succeeding in high-stakes processes, and AWS noted ~11-month time-to-value for enterprise AI initiatives


Here is a tight, slide-ready version with clean bullets and no excess text:

⸻

Industry Meeting on Agentic AI – Summary

Agentic AI Adoption
	•	Early stages across the industry, but broad consensus it will be a major trend
	•	Initial pilots show strong efficiency gains (e.g., AML processing reduced from ~1hr to ~5mins)

Risks, Cost, and Governance
	•	Rising compute and infrastructure costs remain a constraint
	•	Difficulties in understanding and controlling autonomous agent behavior
	•	Risk and Compliance (esp. MRM) viewed as central to agentic AI governance

Agentic AI in Control Functions
	•	Risk and Compliance serve as both control owners and early adopters
	•	MRM addresses performance, explainability, and failure modes; Compliance covers policy adherence
	•	Strong traction in AML, fraud detection, and risk monitoring

Managing Agentic AI Risks
	•	Need for robust governance: safety boundaries, role-based permissions, audit logs, approval gates
	•	Continuous monitoring for emergent behavior
	•	Human-override mechanisms (“kill switches”) required for operational resilience

Efficiency and Cost Management
	•	Agentic workflows deliver substantial productivity benefits
	•	Compute costs for agentic systems and vendor LLMs rising quickly
	•	Firms exploring model orchestration and in-house fine-tuning for high-risk or policy-sensitive use cases

⸻

If you want a 1-page executive summary slide or a two-column format, I can generate that as well.




Hi Bill, this is the draft for the December CRO priorities deck. 
Similar to the prior months, we have 2 sections for YTD accomplishments and ongoing priorities.
The accomplishments, we are adding things to the deck month over month. We can focus on the changes which are highlighted in orange color. The black texts are the same as previous months.

We can go through these changes one by one.
First is the MRA remediation, the status is as off last Wednesday. And I added that we are reviewing the enhancements to the Apple Card loss forecasting model to address the CCAR incremental feedback. 

I added ERMF uplift for the IRR calculation here. 

For regulatory accomplishments, I added the submission of the remediation plan under the ACL transformed MRA.

And under PRA, I added the ICR validations under the IRB road map. 

The next slide is mostly stats update. 

Under AI AIRCC, numbers have been updated. 
Under validation, 67 validations completed YTD, up by 6 since last month.

Next on the validation activities, 1180 validations completed as of November 24 , and ~ 10% increase compared to the same period last year. 

We have some updates to the ASL validation last month including extensions of FLR to transition SFR facility. And two enhancements to the tail risk models on the next slide.
The other things stay the same.

Moving on to the ongoing priorities. 
Same update to the MRA remediation for the CCAR incremental feedback.

Under regulatory updates, I put CCAR here considering we are kicking off the 2026 cycle.

And updated the Card origination exam given the meetings have concluded and we are waiting for the soft close.

Under ECB, updated IMM exam and SRAP, given the findings has been formalized, remediation is ongoing.

The last slide, the CCR has been confirmed with Andreza.
The ASL is confirmed with Miao and Shipra. There are more under ASL, but these two new preTrade models and 2 enhancements are confirmed with deadline of YE.

And we have updated significant t1 revalidation. 

187 43% as of Nov 26





“Eight preliminary findings were raised on quantitative modeling, with additional process-related findings expected, notably around local accountability for validation and expectations that validation reports are approved by senior management and the governing body.


FRB MRM MRA remediation remains on track for completion by year-end, with infrastructure enhancements and training completed ahead of the September 30 deadline following Model Risk Control Committee approval in May, and rollout underway with 242 of 751 Q4 reviews completed under the enhanced framework; separately, a remediation plan has been established to address incremental 2025 Comprehensive Capital Analysis and Review (CCAR) feedback related to ongoing monitoring of the credit card loss forecasting model.


Here is a simpler, meeting-minutes-style version consistent with the tone and level used in the rest of the document:

⸻

FRB inquiry on ongoing monitoring for AI models
	•	FRB asked how ongoing monitoring for generative AI models differs from traditional models.
	•	Bill explained that MRM establishes model-specific metrics and thresholds for each higher-tier AI model (for example, recall targets for the Compliance Tier 1 surveillance model), and these metrics are reviewed as part of ongoing monitoring.
	•	For the Compliance model, Bill noted performance targets above 97% recall, with early results around 98%, and Compliance will continue to perform sample-based human QA after go-live.
	•	Bill added that the firm intends to standardize ongoing monitoring for AI models over time, similar to the centralized regression-testing framework used for derivatives models, and engineering is working toward providing firm-wide guidance and tooling to support this.


Absolutely — here’s a version you can drop into the Thematic Update section to capture that specific exchange on AI ongoing monitoring.

⸻

Ongoing monitoring for AI / generative AI models
	•	FRB asked how ongoing monitoring for more complex generative AI models compares to monitoring for traditional models (for example, regression or SecDB-based models), and how Goldman is approaching this across the firm
	•	Bill explained that this is an evolving area, and that while there are only a small number of higher tier generative AI models today, MRM is already setting explicit ongoing monitoring expectations for each approved high-tier AI use case, including
	•	Defining model-specific metrics and thresholds up front (for example, recall targets for surveillance models)
	•	Aligning those metrics and tolerances with the relevant business or risk owner who ultimately accepts residual model risk
	•	Requiring regular reporting and review of these metrics as part of ongoing monitoring
	•	Using the Compliance Tier 1 surveillance model as an example, Bill noted that
	•	The key objective is to capture potential insider trading cases with very high recall
	•	The target recall is set above 97%, and testing and early live results are around 98%
	•	Even after launch, Compliance will maintain QA “below-the-line” testing, where a sample of alerts is reviewed by humans to independently assess model performance over time
	•	Bill added that, longer term, the firm’s goal is to move from a one-off, model-by-model approach to a more standardized framework for AI ongoing monitoring, similar to the centralized regression-testing program that exists for derivatives models
	•	Engineering is expected to provide firm-wide guidance on suitable metrics and thresholds for different types of AI/ML use cases, as well as a common platform to run evaluations and produce consistent reporting
	•	The intent is to build this infrastructure early in the AI lifecycle so that monitoring is scalable and consistent, and to avoid having to retrofit a large number of models later
	•	FRB acknowledged that this is an emerging area and appreciated the explanation of how Goldman is setting expectations for high-tier AI models today while working toward a more centralized, standardized monitoring framework going forward


Here is a tailored script specifically for you as a VP in Goldman Sachs Model Risk Management, reflecting your role, the type of feedback you typically receive, and the expectations at your level.

I’ve kept it polished, concise, and aligned with GS culture.

⸻

🌟 Tailored Performance Review Script (MRM – VP Level)

When your manager reads others’ feedback

1. General Acknowledgment

“Thank you for walking me through the feedback. I really appreciate everyone taking the time to share their observations.”

⸻

When the feedback is positive (strong execution, ownership, stakeholder management)

“I’m glad to hear this aligns with how I’ve been approaching my work. I’ll continue building on these strengths—especially maintaining high-quality validations, producing clear deliverables for regulators, and supporting cross-team priorities.”

⸻

When the feedback is critical or suggests improvement

(communication, prioritization, managing scope, efficiency, pushing back, etc.)

“Thank you—that’s helpful. I understand the theme being raised. I can see how improving in this area would increase my overall impact, and I will make this a priority.”

If you need more clarity:

“Could you share an example so I fully understand the context and expectations?”

⸻

If the feedback is surprising or unclear

“This is very useful to hear. I’d like to understand what strong performance would look like here so I can adjust and make meaningful improvements.”

⸻

🌟 What to Say About Your Development & Goals

When she asks, “What are you looking to focus on going forward?” use this:

1. Strengthen Core Execution

“First, I want to continue strengthening my execution on high-impact validations and regulatory deliverables. Ensuring quality, clarity, and timeliness remains a core priority for me.”

2. Improve Based on Feedback

“Based on the feedback today, I plan to focus on tightening communication loops, driving more efficiency in workstreams, and being more proactive about raising risks or bandwidth constraints early.”

3. Broaden Technical & Leadership Scope

Choose the areas relevant to you:
	•	AI/ML model governance
	•	ICR/CCR uplift
	•	ERMF remediation
	•	FRB/QCC meetings
	•	Ongoing monitoring
	•	Cross-functional leadership

Example line:

“I would like to broaden my scope, especially across AI/ML model governance and ERMF uplift streams, and take on more leadership responsibilities that support the team’s strategic goals.”

4. Increase Strategic Contribution

“I want to operate more consistently at VP level by stepping further into strategic problem-solving—identifying issues early, improving workflows, and helping the team navigate complex regulatory expectations.”

5. Ask for Support (shows maturity)

“I’d appreciate your guidance on which types of projects or responsibilities would help me grow most effectively into the next level.”

⸻

🌟 Closing Statement

Use this near the end:

“Thank you again for going through all of this. I really appreciate the transparency. I’ll continue to build on what I’m doing well, and I’ll focus on the areas where I can sharpen my performance. I’m committed to increasing my impact, supporting the broader MRM agenda, and aligning my work with the team’s priorities.”

⸻

If you’d like, I can also create:

✔ a version for managers expecting more humility
✔ a version for managers expecting stronger assertiveness
✔ a version tailored to your relationship with your manager
✔ scripts for how to respond to common tricky feedback (“needs more leadership,” “needs to be faster,” “needs to improve communication”)

Just tell me which one you want!


Here is a simple, professional, and safe way to respond during your performance review when your manager reads others’ feedback. The goal is to show maturity, openness, and a forward-looking mindset without sounding defensive.

⸻

How to Respond During the Review

Use a calm, concise structure:

1. Acknowledge the feedback
	•	“Thank you for sharing this. I appreciate everyone taking the time to provide feedback.”

2. Show openness and reflection

If the feedback is positive:
	•	“I’m glad to hear this resonates with the team. I’ll continue building on these strengths.”

If the feedback is constructive/critical:
	•	“I understand the point being raised, and I appreciate the candid insight. I can see how improving in this area would help the team.”
	•	Avoid debating or explaining too much. Acknowledge first.

3. Ask clarifying questions (if needed)

This shows maturity and a growth mindset:
	•	“Could you share an example so I understand the context better?”
	•	“What would ‘success’ look like in this area from your perspective?”

4. Demonstrate commitment to improvement
	•	“I’ll incorporate this into my development plan and start making progress immediately.”
	•	“I want to ensure I’m operating at the level expected of me and contributing at the highest impact.”

⸻

What to Look Forward Going Forward (what to say when they ask about your goals)

Keep it structured and aligned with what good performers say.

1. Strengthen core responsibilities
	•	“I want to continue deepening my impact in model risk—especially through stronger end-to-end ownership of validations and clearer communication with stakeholders.”

2. Improve based on feedback
	•	“I’d like to put more focus on the areas highlighted in the feedback—for example, improving efficiency, communication, cross-team coordination, or whatever themes come up.”

3. Expand your role/skills

Tailor to your situation:
	•	“I want to broaden my expertise across AI/ML models and complex CCR/ICR models so I can take on more senior-level responsibilities.”
	•	“I’m looking to improve project management so large deliverables (like FRB decks, MRCC materials) run even more smoothly.”

4. Show alignment with team and firm goals
	•	“I want to ensure my work directly supports the team’s long-term goals—especially MRA remediation, ERMF uplift, and enhancing AI governance.”

5. Ask for support

This is optional but shows maturity:
	•	“I’d appreciate any guidance on prioritization or opportunities you think would help me grow into the next level.”

⸻

A Polished Closing Statement You Can Use

Here is a script you can say toward the end:

*“Thanks for walking me through all the feedback. I appreciate the team’s candid input. I’ll continue building on the strengths highlighted and I’ll focus on improving the areas mentioned today.

Looking forward, I want to deepen my technical contribution, take on more ownership, and continue improving communication and partnership across teams. Please let me know if there are specific opportunities or stretch assignments you think I should target—I want to grow in a way that aligns with the team’s priorities.”*

⸻

If you want, I can also:
✔ create a tailored script for your role in MRM specifically
✔ help prepare answers to likely manager questions
✔ prepare responses depending on the type of feedback (positive vs critical vs surprising)
✔ simulate the performance review so you can practice

Just tell me!



Meeting Minutes: Q4 2025 Quarterly MRM Meeting with FRB – Nov 13, 2025

MRM hosted the Q4 2025 Quarterly Model Risk Management meeting with FRB and FDIC. The agenda covered data challenges stemming from the recent U.S. government shutdown; progress on MRA remediation (including annual review enhancements and incremental CCAR feedback); internal audit findings and issue remediation; status of validation activity and findings; RAS exceptions and aged items; model inventory and AI/ML usage; thematic updates on key model changes; and ongoing monitoring results

⸻

1. MRM plans to mitigate data challenges resulting from the government shutdown
	•	Nature and scope of data disruptions
	•	Bingwen provided an overview of data gaps driven by the government shutdown, including delayed or missing publications for CPI (September delay and risk of no October print), unemployment data used in credit loss projection models, OFR Financial Stress Index, Leading Economic Index, and CFTC commitment-of-traders data used in systematic index strategies
	•	FRB asked about prior disruptions; MRM noted earlier cyber incidents affecting the CFTC/Ion vendor and COT reporting, which were managed without material model issues
	•	Impact assessment and potential pain points
	•	MRM has not identified material model issues or significant business impact to date; data gaps have been manageable using short-term approximations and stable market conditions
	•	CPI-linked products (TIPS and inflation derivatives) and contracts that reference October CPI as an initial fixing were highlighted as potentially most sensitive if the outage had persisted or coincided with large moves in inflation or unemployment
	•	FRB asked at what horizon issues would become binding; MRM noted concerns would rise materially if unemployment or inflation experienced sharp moves without updated data, or if shutdown-related publication delays extended significantly beyond current experience
	•	Mitigation actions and governance
	•	For inflation-linked products, desks are implementing fallback approaches consistent with contractual terms and market standards (Treasury guidance, ISDA inflation definitions, clearing house rules) where such fallbacks are explicitly specified
	•	For systematic trading strategies and indices (including those referencing government data), fallback logic is governed by index rulebooks, which specify when to pause publication or use alternative inputs if data is not available
	•	Where no explicit contractual fallback exists, desks employ internal projections, approximations, or last-available data under approved methodologies, subject to Model Risk Management review and model committee or index governance approvals as appropriate
	•	Desks directly engage clients, clearing houses, and other dealers for CPI-linked contracts where contract terms may need to be adjusted by convention if October CPI is not published; MRM emphasized this is being managed as an industry-wide coordination issue rather than unilateral firm action
	•	Ongoing monitoring and change controls
	•	Existing data quality monitoring and time-series checks remain in place across affected risk and pricing models; MRM and front office monitor for anomalies and missing observations as part of routine controls
	•	FRB asked whether ongoing monitoring is being explicitly enhanced due to the shutdown; MRM explained current monitoring framework is considered sufficient for short gaps, with escalation to desks and MRM if material issues are detected
	•	For urgent production changes required to address data disruptions, preventative change control (PCC) governance allows for fast-tracked reviews when needed, with documentation completed promptly afterward; for anticipated changes (e.g., expected October CPI non-publication), standard approval workflows and timelines are used

⸻

2. MRA Remediation Progress
	•	Annual review framework uplift (MRA)
	•	Caroline reiterated that the enhanced annual review framework previously shared with FRB has been approved by the Model Risk Control Committee, including expanded template questions and clearer expectations for validators
	•	The model risk workflow tool has been uplifted so validators must provide supporting explanation for every yes/no question, regardless of whether an exception is identified, directly addressing prior feedback that commentary should accompany both exceptions and conclusions that “no issues” are observed
	•	Comprehensive training on the enhanced framework and tooling has been delivered to the full MRM team, clarifying expectations for analysis, documentation, and evidence supporting conclusions in annual reviews
	•	Implementation status and milestones
	•	The commitment remains to complete all annual reviews due in Q4 under the enhanced standards by December 19; validators were given an early start by completing the tech release and training ahead of plan
	•	Caroline reported that approximately half of the Q4 population has been completed under the new standard and the program is tracking on schedule to meet the December 19 deadline
	•	Incremental CCAR 2025 feedback
	•	MRM reminded FRB that the firms met separately in September to discuss actions addressing incremental CCAR 2025 feedback; the related plan remains unchanged
	•	Developers have completed ongoing monitoring enhancements required to address this incremental feedback; MRM is now reviewing the enhancements and expects them to be completed and fully embedded in the coming month

⸻

3. Issue Remediation (Internal Audit and other findings)
	•	Internal Audit (IA) overview
	•	Caroline noted there is one open internal audit finding for MRM, rated at the lowest severity level, and no IA findings were closed over the quarter
	•	The open finding relates to preventative change control (PCC) for models implemented in GitLab rather than SecDB, focusing on visibility and control around the “break glass” mechanism for urgent code changes
	•	GitLab PCC and “break glass” remediation
	•	IA identified that for certain GitLab-linked SPR projects, change controls could be disabled in a corner-case configuration, raising concern that model code changes might bypass standard PCC
	•	MRM explained that the population is small (only one model identified in the IA sample) and that approximately 98% of Tier 1 models remain in SecDB, which uses a separate, robust change control framework
	•	Remediation actions include tooling changes so that if PCC is disabled for a relevant GitLab-linked model, the model is automatically “unblessed,” triggering immediate escalation and follow-up by MRM
	•	The workflow is also being updated so PCC no longer depends on a specific GitLab flag; all model changes will be routed through PCC and MRM review irrespective of flag settings, eliminating the identified gap
	•	Context and future state
	•	Bill noted that while the current GitLab population of Tier 1 models is small, the proportion of AI and other models implemented in GitLab is expected to grow; addressing the control gap now avoids larger remediation later
	•	FRB sought clarification on why the disabling configuration had been possible; MRM confirmed the new design removes this dependency and ensures consistent PCC coverage for GitLab models going forward

⸻

4. Status of Validation Findings
	•	Overall validation activity and open findings
	•	Caroline presented the quarter-over-quarter evolution of open validation findings; the total number of open findings declined over the quarter
	•	Validation activity and annual review volumes remain broadly in line with prior quarters, with continued focus on significant Tier 1 models and risk-sensitive areas
	•	As in prior quarters, most open findings reside in the Risk Division and Global Banking & Markets (GBM), reflecting their larger inventory and concentration of Tier 1 models; other divisions have materially smaller inventories and lower finding counts
	•	Annual reviews completed via revalidation
	•	FRB asked about the 12 models “completed through revalidation”; Caroline confirmed these are significant models on a regular revalidation cadence, where the scheduled revalidation is considered to fulfil the annual review requirement for that year
	•	For these models, the next annual review is scheduled one year after the revalidation date, consistent with the “off-year” of the bi-annual revalidation cycle for key Tier 1 models
	•	New vs remediated findings
	•	Slide-level data showed relatively fewer new findings raised in Q3 compared with some prior quarters, while remediation pace remained strong, particularly in Risk and GBM
	•	For qualitative approaches and DRCs, inventories and finding volumes remain smaller, with no notable qualitative trend changes over the quarter

⸻

5. RAS Exceptions and Aged Items
	•	Thresholds and recent policy changes
	•	Caroline reminded FRB that MRM maintains RAS metrics and thresholds for models under waiver and models with aged findings, with oversight by the Board Risk Committee (BRC) and Firmwide Risk Appetite Committee (FRAC)
	•	In April 2024, the firm revised the metric for models with aged findings and set a zero tolerance at the board level for findings aged more than one year beyond the original due date; metrics for models under waiver were also refined
	•	In September 2025, FRAC approved tightening the inner threshold for Tier 1 models with aged findings from 9 months past the original due date to 6 months, effective October 1; the board-level threshold remains at one year
	•	RAS utilization and breaches
	•	MRM presented the same weekly RAS report that is provided to FRAC, showing utilization versus thresholds for unvalidated models in use, unvalidated transactions, and validated but rejected models, segmented by Tier
	•	Utilization of waiver-related metrics remains relatively low across categories, and there were no BRC or FRAC breaches over the quarter for models under waiver or unvalidated transactions
	•	Caroline highlighted that unvalidated Tier 2 models in use are at one of their lower utilization points relative to the last six months, with current levels well below the historical maximum and average
	•	Aged waivers and aged findings
	•	Waivers are generally expected to be remediated within 90 days of issuance; metrics then track items that age beyond this original due date
	•	There were no breaches of aged-waiver metrics
	•	For aged findings on approved Tier 1 models, MRM is currently at the FRAC inner threshold (zero tolerance for findings aged more than six months past original due date), with six counterparty credit risk models and one mortgage pricing model in this category as of October 1
	•	All affected models have new target remediation dates between now and December; MRM does not expect any of these to breach the board-level threshold of one year past original due date
	•	FRB requested a follow-up list of the specific models with aged findings; MRM agreed to provide this information via follow-up

⸻

6. Model Inventory and AI/ML Usage
	•	Overall inventory trends
	•	Caroline noted that inventory remains broadly stable, with approximately 85 new models declared year to date and a similar number in the quarter, spread across divisions
	•	Corporate Treasury contributed to Tier 1 growth primarily through re-segmentation of existing models into more granular representations, rather than entirely new risk exposures
	•	Additional Tier 1 models were added in Risk and GBM, with no single new theme dominating
	•	Tier changes and governance
	•	FRB asked about tier migrations, including a small number of models moving from Tier 1 to Tier 2; MRM explained these were cases where models are no longer used for daily P&L or risk, or where additional information obtained during validation supported a lower risk tier
	•	Risk tier can be adjusted either pre-validation (as more information becomes available after declaration) or post-validation (if usage changes); requirements for documentation, testing, and control intensity adjust accordingly
	•	Caroline noted that when models are down-tiered post-validation, certain Tier 1-like controls often remain in place because the initial setup costs have already been incurred, even if not strictly required by policy for the lower tier
	•	AI/ML and generative AI inventory
	•	AI/ML continues to be an area of development focus but still represents a relatively small share of in-use models (single-digit percentage), with a higher share among models in development
	•	Generative AI models remain concentrated in lower tiers; a small number of higher-tier AI/ML models exist but are not yet a material proportion of Tier 1 inventory
	•	FRB asked whether inventory tables include models in testing/use-case development phases; Caroline confirmed the counts include both in-development and in-use models
	•	Example: Equinox Equity Derivatives model
	•	FRB inquired about the Equinox AI model used in Equity Derivatives
	•	Bo explained that Equinox is a Tier 2 model that converts natural language client requests (e.g., “quote 200 Apple call options with strike X”) into GS’s internal structured quoting format to feed pricing systems
	•	Traders remain in the loop and are responsible for verifying the structured output before responding to clients, preserving human oversight and accountability

⸻

7. Thematic Update – Model Changes and Enhancements
	•	AI and agentic models
	•	Shipra reported continued growth in AI models, highlighting the first Tier 1 model with agentic components approved in September for Compliance
	•	The Compliance model is used to assist with insider trading surveillance: it automatically closes approximately 25% of alerts and provides reasoned summaries to support human review of the remaining alerts
	•	The model runs in production parallel for roughly two months, during which 100% of alerts continue to receive human review; performance targets focus on recall of potential insider trading cases, with a target above 97% and observed performance around 98% in testing and early live usage
	•	Compliance will maintain ongoing monitoring and QA, including sample-based “below the line” human testing post go-live; metrics and thresholds are explicitly defined as part of the validation and governance framework
	•	Other AI/ML approvals
	•	GBM received approval for Tier 1 generative AI models used to classify mortgage and credit loan exposures into credit and liquidity categories for regulatory reporting
	•	Several lower-tier AI/ML models aimed at productivity (e.g., summarizing financial and legal documents from larger corpora of texts) were also approved
	•	Asset-secured lending models
	•	In asset-secured lending, MRM approved enhancements to Tier 1 models owned by GBM and Risk, extending asset-specific coverage to positions previously treated under fallback methodologies as additional data became available
	•	Key approvals included tail-risk and FLR module extensions for home equity lines of credit and second-lien loans, as well as updated calibrations for “fix-and-flip” portfolios and related segments to improve performance and remediate existing findings
	•	Counterparty credit risk (CCR) enhancements
	•	MRM approved a new Tier 1 CCR model to monitor incremental netting and legal enforceability risk for futures, tri-party collateral arrangements, and securities lending businesses
	•	Joyce explained that the model quantifies additional shortfall risk arising when “all-or-nothing” enforceability assumptions do not hold, aligning with broader work to digitize and integrate legal enforceability opinions into risk models
	•	The model is currently used for monitoring rather than limit-setting; MRM and the business are working to extend coverage to additional businesses under defined validation timelines
	•	Other divisional changes
	•	Asset & Wealth Management (AWM): MRM approved migration of private wealth management mortgages models to an enhanced prepayment framework consistent with GBM practice, remediating an open MRM finding
	•	Platform Solutions: Approvals included new credit decisioning models used to support credit line increase decisions and rank customers based on risk
	•	Risk Division: New models were approved for liquidity (broad monitoring of structural risk under mark-to-market tail scenarios) and credit (a CECL model for held-for-investment risk retention positions in the RMBS portfolio)

⸻

8. Ongoing Monitoring
	•	Overall results
	•	Shipra reported that no high-severity findings were raised from ongoing monitoring in Q3
	•	Backtesting results for credit and market risk models for Q2 were generally in line with expectations
	•	Medium-severity findings
	•	A medium-severity finding was raised for transportation facilities shortfall monitoring in the collateralized lending business, where inconsistent shock calibration methodology in tail-risk measures led to notable differences between production and benchmark results and backtesting breaches; remediation is in progress
	•	A medium-severity finding was raised for models estimating probability of default and loss given default for student loan portfolios, driven by backtesting breaches that will require re-estimation of risk parameters; remediation is underway
	•	A medium-severity finding with low materiality was raised for inflation modeling during the index transition process, due to potential minor risk measurement inaccuracies; MRM is tracking remediation of this issue

⸻

9. Closing and Follow-Ups
	•	FRB and FDIC participants thanked the firm for the updates and discussion, noting particular interest in ongoing monitoring and governance for generative AI models and data-challenge mitigation
	•	MRM agreed to provide:
	•	A follow-up list of Tier 1 models with findings aged more than six months (the six CCR models and one mortgage pricing model discussed under the RAS section)
	•	No additional formal actions were requested during the meeting beyond the agreed follow-ups










Here’s a restructured and refined version of your content that directly aligns with the two topics — focusing on review and approval of internal swap valuation models and adjustments to model inputs and outputs.
It preserves all original information but organizes it under clearer, topic-relevant sections and removes duplication for flow and clarity.

⸻

1. Review and Approval of Internal Swap Valuation Models

Purpose and Governance
Model Risk Management (“MRM”) is part of the Risk Division, composed of modeling experts who are functionally and structurally independent from Model Owners, Developers, and Users. The Global Head of MRM reports directly to the Chief Risk Officer, ensuring independence and objectivity in the oversight of model risk.

Scope of Review
MRM independently reviews and approves all models used for:
	•	Computation of market value of swaps
	•	Computation of associated capital charges

These include both new model implementations and any proposed changes to existing models. MRM ensures that all models comply with the Firmwide Model Risk Policy and associated Standards, which require comprehensive documentation and evidence of effective challenge.

Validation and Approval Process
	•	MRM performs independent validation of each model’s conceptual soundness, methodology, implementation, and intended use.
	•	Upon satisfactory validation, MRM grants formal approval for production use.
	•	Any change to model code or regression tests—regardless of materiality—must be reviewed and approved by MRM before release to production.
	•	Pricing and Capital Models, including swap valuation models, are classified as Tier 1 Models, which are subject to the highest development, validation, and control standards.

Change Control and Documentation
Model code is maintained in a version-controlled source repository with preventative control over model changes (PCC).
All changes are automatically tracked, and any violations of control policies are escalated to MRM and relevant stakeholders.

Ongoing Oversight
MRM conducts annual reviews and ongoing performance monitoring to assess model accuracy, robustness, and alignment with intended use.
In cases of inadequate performance or control issues, MRM may issue validation findings or revoke prior approvals until deficiencies are remediated.

⸻

2. Review and Approval of Adjustments to Model Inputs and Outputs

Assessment of Inputs
As part of model validation, MRM evaluates the appropriateness and quality of input data used in swap valuation models. This includes:
	•	Assessing relevance and representativeness of internal and external data sources
	•	Reviewing model assumptions, parameterizations, and calibrations
	•	Considering conservatism in input parameters and overlays in light of identified limitations

Where input data or parameter issues are identified, MRM raises validation findings and communicates them to Model Owners, Developers, and independent control functions.

Approval of Adjustments
Any adjustment to model inputs or outputs—including pricing parameters, yield curves, volatility surfaces, or valuation overlays—must be:
	•	Supported by clear rationale and documentation
	•	Independently reviewed and approved by MRM prior to implementation
	•	Assessed for impact on valuation and capital outcomes

Ongoing Monitoring and Escalation
The appropriateness of inputs and resulting outputs is reviewed regularly as part of ongoing monitoring and annual review processes. If deviations, anomalies, or breaches are identified, MRM will:
	•	Investigate root causes
	•	Escalate issues through validation findings
	•	Require corrective actions or revalidation where necessary

⸻

Would you like me to make this version more formal and regulatory-facing (e.g., for submission to the FRB or an internal governance policy document), or slide-ready (shorter and bullet-based for presentation use)?



Here is a concise, plain-language summary in bullet form:
	•	Patomak issued a report identifying two observations relating to the Standard Initial Margin Model (SIMM): (i) inconsistent documentation of materiality assessments when changes to SIMM are evaluated, and (ii) the need to enhance training for model developers on regulatory requirements and materiality thresholds.
	•	Goldman has previously enhanced the process for identifying material changes to SIMM, but Patomak noted that documentation of the materiality assessment is not consistently maintained.
	•	Patomak also recommended strengthening training to ensure model developers understand SIMM regulatory expectations and thresholds.
	•	Goldman is currently evaluating action plans to address these observations.
	•	Feedback on the report will be provided to Patomak by October 30.




Previously only surviving Limited Partner payments and unsecured recovery were considered; the model now also includes recovery from fund assets after fund debt obligations are paid


Sure — here is a revised version with a clear introductory sentence added, while keeping everything else consistent and formal:

⸻

Due to the recent government shutdown and related data release delays, we have experienced interruptions in the publication of several government data series, including Consumer Price Index (CPI), unemployment rate, Financial Stress Index, Leading Economic Index, and Commodity Futures Trading Commission (CFTC) position reports. There has been no material impact on business activities, and no significant model issues have been identified to date as a result of these data availability challenges. The firm has managed similar data disruptions in the past, and several businesses have already established mitigation processes. Key mitigation approaches include:
	•	Fallback Approaches
	•	For fixings in Treasury Inflation-Protected Securities (TIPS) and inflation derivatives, fallback logic is being implemented in accordance with prescribed methods published by the U.S. Department of the Treasury, the International Swaps and Derivatives Association (ISDA) Inflation Derivative Definitions, or relevant clearing houses
	•	Within the Systematic Trading Strategies (STS) business, the firm designs and publishes investment strategies as indices, some of which reference U.S. government data. Where fallback provisions are specified in an index rulebook, the fallback logic is applied consistent with the rulebook requirements
	•	Internal Projection or Approximation Approaches
	•	Where fallback logic is not specified in an STS index rulebook, an internal roll-forward method may be applied, subject to Index Committee review and approval
	•	The Current Expected Credit Loss (CECL) model uses the unemployment rate as an input to forecast credit losses. In the absence of the September unemployment release, internal unemployment projections would be used
	•	For missing observations in market data time series, internal data completion methods (forward-fill or backward-fill) are applied based on established procedures
	•	Direct Engagement with Clients and Industry Participants
	•	Certain derivative contracts reference published index levels that may be delayed. For example, contracts referencing the October CPI level may require clarification or adjustment. The trading desks are actively engaging with clients and other market participants to align on contractual handling and settlement mechanics

Any model adjustments or implementations to address data availability issues are subject to Product Control Committee (PCC) and Model Risk Management (MRM) review. In addition, ongoing data quality monitoring controls are in place for critical data sources, including those used in market risk calculations.

⸻

If you’d like, I can now convert this into a single slide with concise bulleting for senior audiences (FRB / ERC / MRCC tones).


Here is a revised version that is formal, consistent, and keeps your structure. I also defined acronyms and removed “e.g.” as requested. I assumed “CFC” refers to Commodity Futures Trading Commission (CFTC) position reports; if that is incorrect, I can adjust.

⸻

We have experienced delays or temporary unavailability of several government-published data series, including Consumer Price Index (CPI), unemployment rate, Financial Stress Index, Leading Economic Index, and Commodity Futures Trading Commission (CFTC) position reports. There has been no material impact on business activities, and no significant model-related issues have been identified to date as a result of these data availability challenges. The firm has encountered similar data disruptions in the past, and several businesses have established mitigation processes. Key mitigation approaches include:
	•	Fallback Approaches
	•	For fixings in Treasury Inflation-Protected Securities (TIPS) and inflation derivatives, fallback logic is being implemented in accordance with prescribed methods published by the U.S. Department of the Treasury, the International Swaps and Derivatives Association (ISDA) Inflation Derivative Definitions, or relevant clearing houses
	•	Within the Systematic Trading Strategies (STS) business, the firm designs and publishes investment strategies as indices, some of which reference U.S. government data. Where fallback provisions are specified in an index rulebook, the fallback logic is applied in accordance with the rulebook requirements
	•	Internal Projection or Approximation Approaches
	•	Where fallback logic is not specified in an STS index rulebook, the index may apply an internal roll-forward method, subject to Index Committee review and approval
	•	The Current Expected Credit Loss (CECL) model uses the unemployment rate as an input to forecast credit losses. In the absence of the September unemployment release, internal unemployment projections would be used
	•	For missing observations in market data time series, internal data completion methods (forward-fill or backward-fill) are applied based on established procedures
	•	Direct Engagement with Clients and Industry Participants
	•	Certain derivative contracts reference published index levels that may be delayed. For example, contracts referencing the October CPI level may require clarification or adjustment. The trading desks are actively engaging with clients and other market participants to align on contractual handling and settlement mechanics

Any model adjustments or implementations to address data availability issues are subject to Product Control Committee (PCC) and Model Risk Management (MRM) review. In addition, ongoing data quality monitoring controls are in place for critical data sources, including those used in market risk calculations.

⸻

If you’d like, I can now turn this into one slide or a 3–5 sentence talking point script for regulatory meetings.


Got it — here is the revised sub-bullet in the same style and tone as the Pricing Models sub-bullet:
	•	Potential impact if the Unemployment Rate data is delayed; Current Expected Credit Loss models would instead use internal unemployment projections maintained by Risk Engineering. No material effect on model performance is anticipated.



Here is a clearer and more concise version suitable for the Federal Reserve slide. I kept the language plain, neutral, and factual:

⸻

Data Availability During Government Shutdown

No significant model issues have been identified to date as a result of data publication delays associated with the recent government shutdown. Model Risk is closely monitoring the situation and any potential impacts on models.

Pricing Models
No material impact expected, as pricing models largely rely on market transaction data.
A potential impact exists for products referencing government-published indices, including the October Consumer Price Index. The delay or absence of this data may affect settlements for Treasury Inflation-Protected Securities and inflation derivatives and the reference index used for certain contracts issued in 2026. Developers are implementing fallback logic consistent with prescribed contractual formulas, and Model Risk will review these updates.

Risk Models
No material impact expected at this time.
If the Unemployment Rate data is not released as scheduled, Current Expected Credit Loss models will rely on internal unemployment projections maintained by Risk Engineering. No significant effect on model performance is anticipated.

Systematic Trading Strategies
Some data sourcing challenges have been observed due to temporary pauses in index publications. The affected strategies will apply fallback logic under the index rulebooks or use the latest available data subject to approval by the Index Oversight Committee. No material impact is expected.

⸻

If you want, I can now format this into one slide, with bullet hierarchy and no full sentences at the sub-bullet level.


Here is a polished, plain-language, FRB-appropriate version. I preserved your key points and tightened clarity, structure, and tone. No unnecessary adjectives, no technical jargon, no claims of “zero risk,” just factual statements.

⸻

Data Availability Challenges and Model Impacts

No significant model impacts have been identified to date related to data availability constraints from the recent government shutdown. Model Risk is closely monitoring the situation and will continue to assess any effects on pricing, valuation, and risk measurement.

Pricing Models
	•	No material impact is expected for pricing models that rely on market transaction data, which remains available
	•	For products that directly reference government-published economic indexes, potential delays in the October CPI release may affect settlements for TIPS and inflation-linked derivatives
	•	Front office developers are implementing documented fallback logic consistent with contract and index rulebooks (e.g., use of most recently published CPI level); these changes will be reviewed and approved through the standard Model Risk governance process

Risk Models (CECL and Forecasting)
	•	No material impact is expected for CECL or macro-sensitive risk models
	•	If the Unemployment Rate is not released on schedule, internal unemployment projections will be used as a temporary input, consistent with established model procedures
	•	Current assessment indicates no meaningful change to model performance or expected loss estimates

Index-Based Systematic Strategies
	•	Systematic Trading Strategies has identified delays in certain index publications
	•	The desk will apply fallback logic specified in the index methodologies or use the latest available data, subject to Index Committee review and approval
	•	No material impact to strategy performance or controls is expected

⸻

If you’d like, I can now convert this directly into a one-slide PowerPoint with:
	•	GS / FRB-appropriate formatting
	•	Bullet indentation and spacing matched to Fed supervisory materials style

Just tell me which template style you prefer:
	1.	Simple White / Black
	2.	Blue Federal Reserve Style
	3.	Goldman Internal Blue/Grey




Got it. The transcript is largely fragmented, but the clear themes are:
	1.	GBM Private / Private Placements in Technology Firms:
	•	Concern about concentration risk in certain technology clients and product structures.
	•	Reinforcement to ensure common stock / plain equity where appropriate and avoid unnecessarily complex convertible structures.
	•	Confirmation that Model Risk is aligned on reviewing complexity and suitability when these structures are proposed.
	2.	CPI Index Publication / Data Availability:
	•	Discussion relates to CPI data reliance for certain pricing models, fallback logic, and operational impacts in the event of data disruptions (e.g., government data delays).
	•	No material model valuation or capital impact expected, given fallback logic and transaction-based pricing in relevant markets.
	•	Ongoing monitoring continues and any delays in CPI publication would primarily impact downstream index-linked operational processes, not valuation reliability.

Below is a clean, plain-English, FRB-facing slide:

⸻

Discussion Summary – Data Availability and Product Considerations

Private Placement / Technology Sector Activity
	•	Recent internal discussions highlighted concentration considerations in private placements for certain technology-sector clients
	•	The focus is on ensuring use of plain equity instruments where appropriate, and avoiding unnecessary structuring complexity
	•	GBM and Model Risk continue to coordinate to ensure product suitability and documentation transparency, particularly where valuation relies on bespoke terms
	•	No identified model deficiencies, and governance controls remain in place for review of new or non-plain-vanilla structures

CPI Index Data Availability and Model Implications
	•	Some pricing models reference government-published CPI data, which may be subject to temporary publication delays
	•	Where this occurs, fallback logic is used to reference alternative data sources or prior index levels, consistent with documented governance
	•	The majority of market-based pricing in these portfolios relies on transaction data, not CPI publication timing, limiting valuation impact
	•	No material impact has been observed to date on pricing, model outputs, or capital calculations
	•	Model Risk is continuing to monitor index publication timeliness and will escalate if any material effects emerge

⸻

If you want, I can also convert this into a one-page PowerPoint with layout and formatting.
Just tell me:
	•	Template preference: GS style / neutral / FRB minimal
	•	Color: Blue/gray / black-and-white
	•	Title tone: More formal vs. more brief

And I’ll generate a downloadable .pptx you can directly use.

Would you like the slide to include a short “No supervisory action requested” statement at the bottom?There were no significant model performance issues resulting in high-severity findings based on ongoing monitoring during the quarter. However, medium-severity findings were raised in connection with recent backtesting results, including:
Inconsistent shock calibration methodology was identified in the model used to estimate tail risk for transportation facilities within the Collateralized Lending business, resulting in large differences between the production model and the benchmark approach and leading to breaches in the second-quarter backtesting results. Remediation is underway.

Backtesting breaches were identified in the models used to estimate Probability of Default and Loss Given Default during the review of first-quarter results, requiring a re-quantification of the risk parameters used in the models. Remediation is underway.

Understood — here is a more formal, concise version appropriate for Federal Reserve review. Tone is neutral, factual, and avoids internal shorthand:


Here is a clean, plain-language slide version. No extra wording, neutral and factual:

⸻

Impact of Recent Government Shutdown on Data Sourcing

No significant model issues have been identified to date. Model Risk is monitoring the situation and applying existing fallback procedures where necessary.
	•	OFR Financial Stress Index (daily, OFR): Publication paused for 3 days in early October; index publication was paused for 1 day in line with rulebook procedures
	•	Leading Economic Index (monthly, Conference Board): Delay in underlying Census/BEA/BLS data; using latest available data under extraordinary event fallback with Index Committee approval
	•	NY Fed Multivariate Core Trend Inflation (monthly, NY Fed): Potential delays due to reliance on BEA inputs; plan to use latest available data with CISC approval if needed
	•	CFTC Position Reports (weekly, CFTC): Stopped since late September; relevant strategy defaulted to zero positions and obtained Commodity CISC approval
	•	CEC Model Inputs (unemployment rate): If data is unavailable, plan is to use model projections; no material impact expected and no adjustment to uncertainty planned

⸻


⸻

Impact of Federal Government Shutdown on Data Sourcing

Model Risk is monitoring the data availability challenges arising from the recent government shutdown, and the potential implications for model inputs and outputs. The Front Office has identified the following sourcing issues, and established fallback procedures have been applied where necessary:
	•	OFR Financial Stress Index (daily, Office of Financial Research): Publication was temporarily halted for three days in early October. As a result, the index calculation was paused for one day in accordance with documented methodology.
	•	Leading Economic Index (monthly, The Conference Board): The release relies on underlying Census, BEA, and BLS data, which experienced delays. The latest available data is being used under the extraordinary event fallback provision, with Index Committee approval.
	•	NY Fed Multivariate Core Trend Inflation (monthly, Federal Reserve Bank of New York): While the NY Fed continues to publish, certain inputs sourced from BEA may be delayed. If necessary, the latest available data will be used, subject to Committee approval.
	•	CFTC Position Reports (weekly, Commodity Futures Trading Commission): Publication has been suspended since late September. Relevant strategies have defaulted to zero positions, with approval obtained through the appropriate Front Office governance process.
	•	Model Inputs for Labor Market Data: If unemployment rate data is not released as scheduled, the model’s internal unemployment projections will be used. No material impact to model performance is expected at this time.

⸻



Here is a clearer and more polished version, keeping the same content and structure:

⸻

Notable themes identified through the review of ongoing monitoring include:
	•	Insufficient monitoring coverage and effectiveness, including uncaptured risks, lack of comprehensive metrics, and missing monitoring mechanisms
	•	Implementation deficiencies, such as incorrect product mappings, manual steps required for balance sheet reconciliations, and infrastructure limitations
	•	Data quality issues, including monitoring failures caused by deprecated databases and data unavailability
	•	Required enhancements and justifications to address identified breaches
	•	Insufficient documentation and controls, including gaps in regression testing and model code governance

⸻
https://credentials.cfainstitute.org/45919b20-5357-4076-97ed-cede8e675953



https://api.accredible.com/v1/auth/invite?code=4d5221ee14f0876954c4&credential_id=45919b20-5357-4076-97ed-cede8e675953&url=https%3A%2F%2Fcredentials.cfainstitute.org%2F45919b20-5357-4076-97ed-cede8e675953&ident=9173cc26-9941-4759-9f58-7a72ca6ff4e2/


sz2608@columbia.edu

Here’s a refined and professional version of your paragraph — clear, concise, and aligned with committee-style reporting tone:

⸻

Top of Mind
Internal Credit Rating (ICR) models (Risk, Tier 1) for Private Equity Capital Call (PECC), Direct Commercial Real Estate (CRE), and Corporate portfolios were validated and approved ahead of the October 31 deadline
• This completes Phase 1 of the ICR model uplift under the ERMF enhancement program, addressing FRB feedback on improving model repeatability, transparency, and sustainability
• Seven high-severity findings related to poor model fit, non-representative data, counterintuitive outputs, and unjustified treatment of censored entities were remediated through targeted model enhancements

⸻

Would you like me to make it slightly more executive-summary style (shorter and more headline-driven) for a slide, or keep it in this committee-note format?


https://www.cfainstitute.org/membership/become-member?s_cid=eml-cfa-GLOBAL-global-oct25-Generic-X-b2c-X-email-retention-All-candidates-LIII_Passed_Aug_25-401095


Here’s a clear bullet-point summary of the information you provided:
	•	Event: US PT Index Rebalancing resulted in a ~$125mm loss
	•	Trading tactic:
	•	Long new SPX entrants to build inventory for client flows
	•	Short positions expecting post-rebalancing price normalization
	•	Context: Robinhood and AppLovin were added to SPX; index rebalance occurred on Sep 19
	•	Positions: GS established ~$1bn short in AppLovin and ~$400mm short in Robinhood after setup
	•	Outcome: On Sep 29, both stocks rose sharply (~+12% Robinhood; ~+6% AppLovin), driving ~$125mm loss
	•	Next steps: Strats proposed additional portfolio loss limits of -$150mm to constrain rebalancing trade exposures; MRM will review the proposal

Do you want me to make this more executive-level (shorter, plain language, focus only on what matters for senior stakeholders), or keep the technical detail for risk/strats audiences?

Sure — here’s a clearer, more logical flow in one sentence:

Validation is in progress for the qualitative approach to size a post-model adjustment (PMA) on RWA, required under the PRA regime to hold capital until the new firmwide ICR rating system is approved, with completion due by 10/31



Here’s a more concise and polished version of your two bullets:
	•	Ongoing monitoring control improved across the board versus 2022, with Risk division now fully effective (previously ineffective/adequately effective for MR and CR)
	•	Model development control worsened in GBM, as FX and Commodities desk strats moved from adequately effective to ineffective due to aged findings

Would you like me to make them even shorter, “headline-style,” for slide use?


Here’s a more streamlined version of your second bullet:
	•	As part of the exam, MRM will present updated assessments of remediation and investigation thresholds, as well as the conservatism of SIMM model thresholds, in response to preliminary findings from the NFA capital and margin inquiry in May

Would you like me to make it even shorter—something you could use as a one-liner in a slide?


Here’s a smoother and more concise version of your draft:

Market Risk: MRM approved the new EQ Topsheet model (Risk, Tier 1), which captures the P&L profile under a range of equity risk factor shocks
	•	The model is implemented in GRisk and will replace the current framework as part of a strategic initiative to strengthen equity measures, enabling more timely, optimized, and robust metric calculations

Do you want me to make it even more neutral—removing words like strengthen and optimized—so it reads strictly as a factual update?


Here’s a tightened and consistent rewrite of that second bullet for Collateralized Lending, combining your points and keeping it neutral/clear:
	•	Extension of the Tier 1 Risk Engineering-owned FLR model for asset-based loans, and the Tier 1 FLR and tail risk models for home equity line of credit (HELOC)
	•	Extension of the Tier 1 business-owned collateral valuation model to cover transitional single-family rental facilities within the Capital Solutions Group, enabling use by downstream FLR and tail risk models that currently rely on a fallback model, and enhancements to prepayment and default modeling for fix-and-flip loans to address a validation finding on performance deterioration

⸻

Would you like me to merge these into one composite bullet (to keep the list shorter) or keep them as two separate but parallel bullets under Collateralized Lending?Extension of the Tier 1 Risk Engineering-owned FLR model for asset-based loans, and Tier 1 Risk Engineering-owned FLR and tail risk models for home equity line of credit (HELOC
- Extension of the tier 1 business owned collateral valuation model to include transitional single-family rental facilities within the Capital Solutions Group, to be leveraged downstream by facility-level rating (FLR) and tail-risk models (currently rely on the fallback model), and to enhance prepayment and default modeling for fix & flip loans, addressing validation finding on performance deterioration



Here’s
Got it — here’s the Economic Risk bullet revised to include both HFI and business-as-usual (BAU) clearly, while keeping it concise and neutral:
	•	Economic Risk: Approval of a new Tier 1 model estimating current expected credit losses (CECL) on first-lien residential mortgage-backed security (RMBS) loans held for investment (HFI), under the risk retention regulation and using business-as-usual (BAU) economic assumptions
** A high-severity finding on underestimation of default probability is being addressed through model enhancements

Do you want me to also mirror this style for the Liquidity Risk bullet, so both appear fully parallel in the report?



a cleaner, neutral rewrite that keeps the hierarchy style and avoids long winding phrasing:
	•	Current Expected Credit Losses (CECL): FRB has concluded the remediation validation event and closed one supervisory finding on inadequate risk capture and ongoing monitoring, while converting the other into a narrower finding focused on the Apple Card Allowance for Credit Loss (ACL) model, with remediation due by June 30, 2026
** A remediation plan is in progress

Would you like me to also shorten this further into a two-line Executive Summary version (e.g., “One CECL finding closed; remaining narrowed to Apple Card ACL model with remediation due June 2026”)?pricing model for European options embedded in structured notes

Enhancements to the Tier 1 stochastic volatility reserve model, with additional calibration tests of parameter combinations and penalties to limit sharp week-over-week swings, resulting in improved fit quality and reduced volatility noise

Executive Summary

Validation activity over the quarter
** Continued growth in Artificial Intelligence (AI) models and use of new techniques, including approvals of:
*** The first Tier 1 generative AI model with agentic components, owned by Compliance, used to close insider trading alerts that would otherwise require human review
*** Tier 1 generative AI models owned by Global Banking & Markets (GBM) Public to classify loan proceeds as "credit" or "liquidity" for 6G reporting for the back book, as part of efforts to address supervisory feedback
** Continued focus on validation work related to Counterparty Credit Risk (CCR) management enhancements in line with the Enterprise Risk Management Framework (ERMF) uplift, including approval of a Tier 1 model developed to monitor incremental netting and enforceability (N&E) risk across Futures, Derivative Clearing Services, and Securities Lending
** Ongoing validation work in the Collateralized Lending business, with recent approvals of enhancements to Tier 1 models owned by Risk Engineering and GBM to calculate facility level ratings (FLR) and tail risk measures, extending coverage to asset classes previously handled by fallback models and addressing validation findings

Regulatory updates
** Federal Reserve Board (FRB) Model Risk Management (MRM) Matter Requiring Attention (MRA) remediation remains on track for completion by year-end
*** Infrastructure enhancements and training completed ahead of September 30 deadline, following Model Risk Control Committee approval of framework changes in May
*** Rollout in progress, with reviews of approximately 700 models to be completed under the enhanced framework by December 19
*** A remediation plan established to address incremental feedback from the 2025 Comprehensive Capital Analysis and Review (CCAR) exam on ongoing monitoring of the credit card loss forecasting model

Program updates
** Model Risk has established the Firmwide Standard on AI to formalize existing controls and oversight, including AI risk assessment and approval
*** Standard approved by the AI Risk and Controls Committee (AIRCC) as part of broader actions to address a Firmwide Enterprise Risk Committee (ERC) follow-up and an internal audit finding on RCSA integration and AI usage monitoring

Artificial Intelligence / Machine Learning (ML) Models

Continued growth in development and use of AI/ML models, including approvals of:
** The first Tier 1 Compliance generative AI model (Surveillance AI) with agentic components that shape review workflow and execute tasks, used to close insider trading alerts that would otherwise require human review
*** The model closes about 25% of alerts and provides reasoning to help humans process the rest more efficiently
** The Tier 1 GBM Private generative AI model (Loans AI) used to classify loan proceeds as "credit" or "liquidity" for 6G reporting for the back book, supporting supervisory feedback
*** Three high-severity issues on accuracy, performance, and fragility were addressed through out-of-sample testing, prompt refinements, and added guardrails, resulting in improved performance
** Enhancements to neural network-based pricing models, including approvals of:
*** Extension of the Tier 1 GBM Public equity share buyback pricing model to add features frequently requested by clients
*** Enhancements to Tier 2 fast pricers for equity structured products, with architectural and feature changes, expanded product coverage, and improved performance, while addressing validation findings
** Lower-tier generative AI models for tasks such as data extraction, search enhancement, and information retrieval, developed mainly for productivity gains

Collateralized Lending

Continued focus on validation and development work supporting the collateralized lending business, including:
** Extension of Tier 1 Risk Engineering-owned FLR model for asset-based loans, and Tier 1 Risk Engineering-owned FLR and tail risk models for home equity line of credit (HELOC)
** Enhancements to Tier 1 business-owned collateral valuation models used in downstream mortgage FLR and tail risk models, extending coverage to transitional single-family rental facilities previously handled by fallback methods, and improving prepayment and default modeling for fix-and-flip loans, addressing findings on performance deterioration
** Enhancements to the Risk Engineering-owned tail risk fallback model to increase coverage of bespoke deal features

Global Banking & Markets

Validation activity during the period included:
** Risk management enhancements, including approvals of:
*** Enhancement to the Tier 1 structured note European options pricing model to incorporate adjustments for market alignment, reducing simulation variance and improving stability in risk calculations
*** New Tier 2 models for bid and offer quotes on GS-issued American warrants on the Halo platform, replacing the prior quoting function with improved stability and adjustments for illiquid options markets
** Valuation adjustments, including approvals of:
*** Enhancements to the Tier 1 stochastic volatility reserve model, with additional parameter testing and calibration penalties to reduce week-over-week noise and improve fit quality
*** A new Tier 2 equity volatility reserve model for systematic trading and London exotic trades, capturing jump dynamics of underlying assets and strengthening risk management
** CCR model enhancements, including approvals of:
*** A new Tier 1 model to monitor incremental N&E risk across Futures, Derivative Clearing Services, and Securities Lending, enabling consistent netting calculations as part of the ERMF uplift
*** Enhancements to shortfall calculations for Synthetic Products Group portfolios in the Unified Benchmark Model (UBM), improving consistency across business lines following this year’s migration
*** Other margin shortfall modeling enhancements covering interest rate scenario design, loss aggregation, liquidation charges, and stress testing for repo transactions, addressing validation findings
** Efficiency and architecture initiatives, including a new simulation method for equity exotics pricing that allows faster convergence, error calculation, and reduced memory usage

Asset and Wealth Management

Migration of the Private Wealth mortgage pricing model to an enhanced prepayment framework, aligning methodology with GBM while maintaining distinct parameters for each use
** Change addresses a validation finding and expands the model’s ability to capture borrower behavior

Platform Solutions

Ongoing development of credit decision models for the Apple Card portfolio, with approvals including:
** A new Tier 1 logistic regression-based scorecard model ranking applicants by delinquency risk, supporting credit line management and portfolio monitoring
** A new Tier 1 XGBoost regression-based model ranking existing customers by expected utilization increase after a proactive credit limit increase (PCI), supporting customer selection and credit line adjustments

Risk

Liquidity Risk: Approval of a new Tier 1 commodities tail risk model to monitor exposures under price rally scenarios
** Complements the rates liquidity tail risk model approved in July 2025, broadening monitoring of structural exposures

Economic Risk: Approval of a new Tier 1 model estimating expected credit losses on first-lien residential mortgage-backed securities under risk retention regulation
** A high-severity finding on underestimated default probability is being addressed through model enhancements



Here’s a simplified and structured bullet version of your note:
	•	Meeting Purpose: Discussed PRA’s views on potential discounting of VaR backtesting breaches caused by idiosyncratic single-name moves, in cases where no VaR model deficiencies are identified.
	•	Context: Concern relates to the capital impact from the backtesting multiplier, despite sufficient capitalization already held in IRC (which covers credit migration and default risks in the trading book).
	•	Specific Case: A May 12 VaR breach was reviewed, driven by hedge break between the Beigene block trade and its HSI hedges.
	•	PRA Feedback: PRA emphasized that VaR and IRC capital requirements are not interchangeable, as the risks they cover are distinct, and adjustments for potential double-counting require like-for-like measures.

Would you like me to make this even more executive-summary style (just 2–3 bullets, very high-level), or keep the current 4-bullet detail?



Here’s a simplified version in 4 bullets, keeping it crisp but still covering the key points:
	•	Overall: The paper reflects many SR11-7 design principles, which are already embedded in GS MRM and AIRCC processes.
	•	Common Ideas: Topics like model lifecycle management, guardrails, and stress testing are already incorporated in Surveillance AI model development and validation.
	•	Partially Implemented at GS: Concepts like confidence scoring, automated learning loops, and work graphs are applied only for higher-risk models; Surveillance AI currently uses confidence scores.
	•	GS Additions Beyond the Paper: GS has more detailed policies and templates, and MRM validation applies advanced AI techniques such as agentic benchmarking, hallucination detection, and AI robustness scoring.

Do you want me to make it even more concise (2–3 bullets) for an exec-level audience?



Here’s a 2–3 bullet summary focusing on the observations:
	•	Training & awareness gaps: Patomak observed that FICC Strats are conservative when flagging SIMM model changes as material, partly due to limited understanding of SIMM regulatory requirements and materiality thresholds; enhanced training is recommended.
	•	Incomplete model inventory: The Firm has not fully identified all feeder/pricing models impacting SIMM. While PCC controls exist, Patomak noted the lack of comprehensive documentation showing all pricing model changes are consistently evaluated for SIMM materiality.
	•	Execution/documentation inconsistencies: Although the Firm reviewed 13,509 PCC tickets, Patomak found rationale for why changes were not material to SIMM was not consistently documented, preventing them from concluding that PCC controls are operating effectively.

Would you like me to also propose how to phrase this as a regulatory response draft (i.e., showing acknowledgment + remediation steps), or keep it purely as observation notes?



Here’s a simplified 3-bullet version:
	•	Continued adoption of AI models, including the first Tier 1 generative AI with agentic components (Compliance) to automate surveillance alert closure.
	•	Tier 1 generative AI (GBM) approved for classifying loan proceeds for regulatory reporting, alongside enhancements to neural network pricing models for equity products.
	•	Lower-tier generative AI models deployed for data extraction, search, and information retrieval to boost productivity.

Would you like me to make each bullet even shorter (one-liners) for slide-style use?



Here’s a cleaner, sharper rewrite of the table content you shared. I kept the same structure (Stripe / Focus Area / Description / Risk Management Action & Next Steps), but tightened the language, removed redundancy, and made it more “executive-ready”:

⸻

Stripe: MRM

Focus Area: AI Model Validations
	•	Description: Continued growth in AI model usage, including the recent approval of a Tier 1 generative AI model with agentic components (owned by Compliance) to resolve surveillance alerts without requiring human review.
	•	Risk Management Action / Next Steps: Validation focuses on governance of generative AI and large language models, ensuring adequacy of controls, oversight, and risk management coverage.

Focus Area: AI Governance
	•	Description: Model Risk established the Firmwide Standard on AI to formalize controls and oversight, including AI risk assessment and approval processes.
	•	Risk Management Action / Next Steps: Standard approved by the AI Risk & Controls Committee (AIRCC) as part of a broader program to address Enterprise Risk Committee (ERC) follow-up and remediate internal audit findings. Next steps include integration into risk and control self-assessments (RCSA) and enhancement of monitoring and testing of AI usage.

⸻

Would you like me to also restructure this into a bullet-point slide format (shorter phrases, easier for presentation), or keep it in this more formal “reporting” table style?



Here’s a rewritten transaction waiver summary based on your new information — simplified, structured, and with jargon explained inline where useful.

Special Event (Fixing Mechanism): The trade structure allows the client to start the inflation leg on a floating basis, defined as NTN-B bond yield + spread. The bond yield fixing date is predetermined at trade inception but only locked at a future date. This creates a “Notional Fix Swap,” distinct from vanilla fixed-vs-float swaps.

	
⸻

Transaction Waiver Summary

Product: Brazil Inflation Notional-Fix Swap (BRL 300m)

Structure
	•	Swap where Goldman Sachs pays fixed (IPA leg) and receives floating (BRR leg).
	•	Notional: BRL 300m.
	•	Notional-fix feature: The notional for the inflation leg is converted into Brazilian reals upfront.
	•	Day-1 PnL: ~$500k.

Special Feature (Fixing Event)
	•	The inflation-linked leg begins as floating:
	•	Defined as NTN-B bond yield + spread.
	•	The bond yield is only fixed at a future date (already known at trade inception).
	•	This makes it different from standard swaps — it requires a “fixing event” (system event that locks the yield on the scheduled date).

Day-1 Booking
	•	Correct model exists and is already approved by MRM.
	•	However, DTP systems do not yet support the new fixing event.
	•	Interim booking: trade entered as a vanilla fixed vs floating swap (as if yield already fixed), with daily amendments to mimic the correct exposure.
	•	Risk workaround: Trading receives correct risk calculations offline from the approved model, but FO systems show incorrect risk until DTP mapping is in place.

Reason for Waiver
	•	Temporary workaround needed due to missing DTP system support for the fixing event.
	•	Without waiver, trade would require repeated rebooking and client re-confirmations (ETIs), creating operational friction.

Remediation Plan
	•	DTP Tech team to map the new fixing event in booking systems.
	•	Once complete, the trade can be booked directly in the approved model.
	•	ETI reference: SDBB7MM3334P6WWTZK.

⸻

Jargon Definitions
	•	IPA fixed / BRR floating: Swap legs — one side pays fixed in IPA terms, the other receives floating in BRL.
	•	Notional-fix: Swap structure where the notional is converted into local currency upfront.
	•	NTN-B bond: Brazilian government inflation-linked bond (benchmark for these swaps).
	•	Spread (spd): Additional fixed margin added on top of the reference yield.
	•	Fixing event: A scheduled system event to lock a floating yield into a fixed rate on a future date.
	•	Vanilla swap: A plain fixed vs floating swap, without optional features.
	•	FO systems: Front-office risk and booking platforms used by trading.
	•	ETI confirmation: Standardized electronic client trade confirmation.

⸻

Do you want me to also condense this into a short 3-bullet “tracker” version (like for waiver decks), alongside this detailed write-up?



Here’s a transaction waiver summary in the same structure as the TWL STRIPS one — simplified, structured, and with jargon explained. I also gave the trade a name: Brazil Inflation-Linked Swap Package.


	

⸻

Transaction Waiver Summary

Product: Brazil Inflation-Linked Swap Package (~$7m max PnL across 4 swaps)

Structure
	•	Trades involve Brazil inflation-linked swaps where the inflation leg starts as floating (linked to NTNB yield + spread) and later becomes fixed using Anbima’s closing yield (official Brazilian bond index).
	•	Four swaps to be executed with clients:
	•	Client A: BRL 1bn, 15y, ETA today
	•	Client B: BRL 1bn, 12–15y, ETA next week
	•	Client C: BRL 500m, 15y, ETA October
	•	Client D: BRL 2bn, 10–12y, ETA October

Day-1 Booking
	•	Trades booked as vanilla swaps (standardized swaps) due to system limitation.
	•	Risk in front-office (FO) systems will be shown incorrectly, but corrected risk can be run offline using the proper model and shared daily with the desk.
	•	Expected resolution in less than a week once DTP Tech team enables the fixing event mapping.

Reason for Waiver
	•	The correct model exists, but system mapping of the fixing event (date when inflation leg rate is locked) is not yet supported in DTP.
	•	Booking workaround (vanilla swaps) avoids rebooking later with new confirmations (ETI).

Remediation Plan
	•	DTP Tech team (led by Felipe Carvalho) has prioritized fixing event mapping.
	•	Target completion in under a week; waiver requested to cover interim trades.

⸻

Definitions of Jargon
	•	Inflation-linked swap: A swap where payments depend on inflation index (here, Brazilian NTNB bond yields).
	•	NTNB: Long-term Brazilian government bonds indexed to inflation (benchmark for swaps).
	•	Spread: Additional fixed margin added to a reference rate.
	•	Anbima close yield: Official end-of-day yield from Anbima (Brazilian financial market association), used to fix swap rates.
	•	Fixing event: The point when a floating rate is locked and becomes fixed in the trade.
	•	Vanilla swap: A plain, standard interest rate swap (used here as a placeholder).
	•	FO systems: Front-office systems used by traders for pricing and risk.
	•	ETI confirmation: Standard client trade confirmation; avoids rebooking.

⸻

Do you also want me to condense this into a 3-bullet executive tracker version (like I did with the STRIPS deal), for easier inclusion in a waiver deck?



Understood — here’s a very simplified version of your trade structure summary, with jargon kept minimal and explained in brackets:

⸻

Simplified Trade Structure Summary

Product: TWL STRIPS Forward Repack ($275mm)
	•	Day 1: Client invests $285m into a vehicle (SPV).
	•	~$85m goes into a zero-coupon bond (a bond that grows in value but pays no coupons) and a forward contract (agreement today to buy later) on U.S. Treasury principal STRIPS (Treasury bonds stripped of coupons).
	•	~$200m goes into a fund obligation note (CFO subordinated note; treated as passthrough).
	•	Years 0–10: Goldman provides a swap (cash-flow pass-through agreement). If the New York Life bond defaults during this period, the deal is unwound at market value.
	•	At Year 10: The zero-coupon bond matures; proceeds are used to settle the forward, giving the client $285m of Treasury STRIPS.
	•	Years 10–26: Client holds the STRIPS with another passthrough swap. At Year 26, the STRIPS mature and $285m is returned to the client.

⸻

This keeps the structure easy to follow without too much technical detail.

👉 Do you want me to make this even shorter (3 bullets) for something like a waiver tracker slide, or is this level good for now?Here’s a clean transaction waiver summary draft you can use. I also gave the trade product a name: TWL STRIPS Forward Repack.

⸻

Transaction Waiver Summary

Product: TWL STRIPS Forward Repack ($275mm)

Structure
	•	Day 1: Client invests USD 285mm into SPV.
	•	~$85mm allocated to 26y zero-coupon component:
	•	10y NYL zero-coupon bond accreting to ~$135mm.
	•	10y forward purchase of $285mm UST P-strip (05/15/51).
	•	~$200mm allocated to subordinated note of a CFO (pure passthrough, not modeled).
	•	Year 0–10: GS provides passthrough swap.
	•	Year 10: NYL bond matures; redemption funds settle the UST P-strip forward, delivering $285mm P-strip to SPV.
	•	Year 10–26: GS provides zero-coupon passthrough swap until UST P-strip matures.
	•	Year 26: $285mm UST P-strip matures and returned to client.
	•	Credit Event: Default of NYL bond (0–10y) → unwind at MtM, GS claims up to NYL bond value.

Day-1 Booking
	•	Underlying: short CT Discrete Lock (UST P-strip forward).
	•	FVA: CT CVA Participation with exposure defined by underlying.
	•	Day-1 economics: ~$2.9mm PV (1mm PnL + 800k XVA + 1.1mm SPV fee).
	•	All PnL reserved Day 1.

Reason for Waiver
	•	Repack tradable system does not support bond forwards as underlyings.
	•	CVA requires enhanced repo curve modelling not yet available in repack calculator.

Remediation Plan
	•	Enhance exposure generation logic under CD CLN Bond Switch MC framework.
	•	Target timeline: 60 days for development + 30 days for MRM approval review.

⸻

Would you like me to also prepare a short version (3-bullet summary) that could be dropped directly into a waiver tracker deck, alongside this detailed version?


Here’s a smoother version of your text, with tighter phrasing and more consistent structure:

⸻

There is continued growth in the use of artificial intelligence (AI) models and new techniques, including recent approvals of:
	•	A Tier 1 generative AI model to classify loan proceeds as “credit” or “liquidity” for 6G reporting of the back book, as part of efforts to address supervisory feedback
	•	Enhancements to neural network–based pricing models, adding new features and products for large equity accelerated share buybacks and structured product valuation adjustments
	•	Lower-tier generative AI models for data extraction, search enhancement, and information retrieval, developed primarily to improve productivity and strengthen the GS AI Assistant

⸻

Would you like me to make this even more concise (one line per bullet, stripped of context like “part of efforts to address supervisory feedback”), or keep the fuller explanations?The new approach aligns with Legal/Reg Policy and RWA treatment but is not applied in credit shortfall analysis, since clients can recall collateral absent default or dispute.

Counterparties may post excess collateral in securities borrowing/lending, held with third-party custodians and enforceable on default.


Here’s a refined 3-bullet version focusing on model risk and keeping it simple:
	•	Model risk validated inclusion of excess financial collateral (equities/govies above margin/haircut, enforceable on default) into Large Counterparty Default calculations feeding GMS stress capital.
	•	Previous approach excluded these excess collaterals, driving outsized RAS losses ($54bn California, $3bn Ohio vs $1.3bn CCAR) and forcing trade reductions to manage stress buffer.
	•	New approach recognizes enforceable excess collateral, lowering modeled top counterparty losses toward ~$1.5bn, easing stress capital buffer pressure (note: not included in credit shortfall/CPE).

Would you like me to also prepare a “before vs after” mini-table version (previous vs new approach) so you can drop it straight into your deck?



Here’s a refined 3-bullet version focusing on model risk and keeping it simple:
	•	Model risk validated inclusion of excess financial collateral (equities/govies above margin/haircut, enforceable on default) into Large Counterparty Default calculations feeding GMS stress capital.
	•	Previous approach excluded these excess collaterals, driving outsized RAS losses ($54bn California, $3bn Ohio vs $1.3bn CCAR) and forcing trade reductions to manage stress buffer.
	•	New approach recognizes enforceable excess collateral, lowering modeled top counterparty losses toward ~$1.5bn, easing stress capital buffer pressure (note: not included in credit shortfall/CPE).

Would you like me to also prepare a “before vs after” mini-table version (previous vs new approach) so you can drop it straight into your deck?


Here’s the updated version with previous vs. current approach built in:
	•	Model risk validated and approved incorporation of third-party custodian collateral (equities/govies, enforceable on default) into GMS stress capital, consistent with Legal/Reg Policy and RWA treatment.
	•	Change was due to outsized RAS counterparty default losses ($4bn California, $3bn Ohio vs $1.3bn CCAR-2025), with the previous approach requiring trade reductions to manage stress buffer impacts.
	•	Current approach recognizes enforceable third-party collateral, reducing modeled top counterparty losses toward ~$1.5bn, mitigating stress capital buffer pressure, with no concerns on PCC or methodology.

Do you want me to separate the “previous vs. current approach” into two distinct bullets, or keep it blended as above for brevity?Got it — here’s the streamlined 3-bullet flow using your structure:
	•	Model risk validated and approved incorporation of third-party custodian collateral (equities/govies, enforceable on default) into GMS stress capital, consistent with Legal/Reg Policy and RWA treatment.
	•	Change was due to outsized RAS counterparty default losses ($4bn California, $3bn Ohio vs $1.3bn in CCAR-2025), largely from stock loan exposures with state pensions.
	•	Impacts include reducing modeled top counterparty losses toward ~$1.5bn, mitigating stress capital buffer pressure, with no concerns on PCC or methodology.

Do you want me to keep the numbers in the second and third bullets, or make them more high-level for CRO slides?Perfect — here’s a refined 4-bullet version that emphasizes validation outcome and clearly describes the change + impact:
	•	Model risk validated and approved changes to incorporate third-party custodian collateral (equities/govies, enforceable on default) into GMS stress capital, consistent with Legal/Reg Policy and RWA treatment.
	•	The change allows collateral to offset stress losses, reducing modeled top counterparty default losses from ~$4bn (CA) / ~$3bn (OH) toward ~$1.5bn or lower.
	•	RAS still shows outsized losses versus CCAR-2025 ($1.3bn), largely driven by stock loan exposures with state pensions.
	•	Approval is targeted before October to mitigate stress capital buffer impacts, with no concerns on PCC or methodology.

Would you like me to keep the state-level detail (California/Ohio) in the bullets, or simplify it into a generic “large state pension exposures” for senior audiences?


Here’s a 3-bullet model risk–focused summary you can use:
	•	RAS highlights outsized counterparty default losses (California ~$4bn, Ohio $3bn) versus CCAR-2025 ($1.3bn), largely driven by stock loan exposures.
	•	Proposed approach leverages third-party custodian collateral (equities, govies) for GMS stress capital; approved by Legal/Reg Policy and aligned with RWA treatment.
	•	Model risk has no concerns with methodology or PCC; approval is targeted before October to reduce stress capital buffer impacts.

Do you want me to also simplify the counterparty/state details for a CRO-level audience?Here’s a refined CRO-level version starting with “Model Risk has been validating…”:
	•	Model Risk has been validating Constant Maturity Treasury (CMT) products, which are linked to U.S. Treasury yields and are more intuitive for investors than swap-based products.
	•	Approvals now cover USD 10-year CMTs and Euro CMTs, with Spain CMTs approved but not yet traded.
	•	The largest exposure is in USD 10-year CMTs (~$1.4bn notes), with risk concentrated in the New York desk.
	•	Euro CMTs are smaller (~$127mm) and mainly used in structured products, providing portfolio diversification.

Do you want me to shorten further into 3 bullets (focusing only on validation progress, USD concentration, and EUR diversification), or keep this 4-bullet structure?



Here’s a detailed structured summary of the transcript you provided:

⸻

URC / Deck Preparation
	•	First draft of the URC deck will be ready next week, along with Bryan’s and CR updates.
	•	Previous issue about findings not appearing on the landing page/exported document has been fixed.
	•	Clarification needed on PRC topics: emails from Bill suggest possible content/style changes vs original format; action item is to confirm expectations with Jalen/coordination team.

AI Governance & ETSC Policy
	•	Question raised on whether ETSC policy and firmwide AI standards should be presented to the Board.
	•	Historically, detailed ETSC policy updates were given to the Board; AI governance was reported to FRAC, but unclear if to the Board—need to verify past precedent.
	•	Newly published firmwide AI standard should be confirmed with Phil (owner of AI governance publications).

CRO / AI Updates
	•	Discussion on whether repeating “in-progress” AI model updates every 2 weeks is useful.
	•	Agreement to focus on notable milestones: e.g., surveillance AI approved by RCC and referred to ERC (likely ERC-approved by next week).
	•	Validation progress should only be highlighted once per milestone (e.g., approval or completion).

Regulatory Updates
	•	Alex and regulatory engagement team are consolidating updates across divisions.
	•	MRM should continue to provide updates but focus only on items directly relevant to MRM (avoid generic or tangential regulatory topics).
	•	IMM exam and ECPU updates should be framed through an MRM lens if mentioned.

CR Update / Inventory
	•	Kenan is working on inventory materials for ETSC; final content is TBD but will be included once available.

CRO Update – Broader Themes
	•	Discussion on CMP-related product validation—question of whether it is worth including for Alex.
	•	Bill emphasized desire for more reporting on major model categories (pricing, market risk, credit risk, liquidity risk, IRM).
	•	Current issue: large teams (40+ per area) but little visibility into themes/trends. Need more “stories” or thematic insights.
	•	Suggestion to brainstorm with David or Beau on how to surface themes across thousands of models.

IRR / Control Metrics Slides
	•	Updates needed on thresholds and outcome tables in the IRR/control metrics slides.
	•	Bill requested format improvements (logical ordering, possible additional column).
	•	Clarification that methodology is already defined in policy, so slides only need to show logical presentation of metrics and thresholds.

Risk Model Performance Updates (FRAC)
	•	Missed quarterly FRAC risk model performance update; responsibility now consolidated under one person to upload updates.
	•	Hui and Sergei will feed content, but one owner will handle submissions to avoid surprises for Bill.
	•	Emphasis: Bill must never be caught off guard by MRM material presented externally; tighter coordination with Chris and others required.

⸻

✅ Key Action Items Identified
	1.	Confirm PRC/URC deck expectations with Jalen or coordinators.
	2.	Check historical precedent for presenting AI governance/ETSC updates to Board.
	3.	Confirm AI standard publication with Phil.
	4.	Ensure CRO update only highlights milestone AI approvals (e.g., ERC).
	5.	Prepare regulatory updates focusing on MRM-relevant items; coordinate with reg engagement consolidation.
	6.	Incorporate Kenan’s inventory work once available.
	7.	Brainstorm with David/Beau on surfacing broader thematic insights from pricing/risk models.
	8.	Update IRR/control metrics slides to Bill’s preferred format.
	9.	Tighten coordination for FRAC risk model performance reporting (one owner, consistent updates).

⸻

Would you like me to also reformat this into a “meeting minutes” style (with attendees, topics, decisions, and follow-ups) so you can use it directly for circulation?Here’s a polished version of your draft. I kept the same structure (with the “There is continued…” phrasing) and ensured each bullet is one sentence:

⸻

Validation Activity
There is continued growth in the use of artificial intelligence (AI) models and new techniques, including recent approvals of:
	•	Two generative AI models to classify ~3,000 corporate loans and ~300 mortgages as “credit” or “liquidity” for regulatory reporting.
	•	A new neural network–based fast pricer for equity structured products, improving speed and expanding the existing family of FX and equity fast pricers, with further extensions planned.

There is continued focus on validation work related to Counterparty Credit Risk (CCR) management enhancements under the firm’s Enterprise Risk Management Framework uplift, including recent approval of volatility scenario design and interest rate loss aggregation updates for the Franchise shortfall model, addressing validation findings.

⸻

Regulatory Updates
FRB Model Risk Management (MRM) Matter Requiring Attention (MRA) remediation is on track for year-end completion:
	•	Enhancements to the annual review framework were approved by the Model Risk Control Committee in May, with infrastructure upgrades and training completed ahead of the September 30 deadline.
	•	Rollout is progressing, with reviews of ~700 models scheduled for completion under the enhanced framework by December 19.

⸻

Program Updates
There is continued progress in formalizing AI oversight, with Model Risk establishing the Firmwide Standard on AI to codify controls, risk assessment, and approval processes.
	•	The standard has been reviewed with AIRC and supports both an Enterprise Risk Committee follow-up and remediation of an internal audit finding on ERMF integration and AI usage monitoring.

⸻

Would you like me to make it even tighter (fewer words, almost “board-level headline style”) or keep this polished but still detailed tone?Here’s a clear summary of the key points from the image you shared:

⸻

CMT Validation Overview
	•	Context: MRM validating extensions to CMT tradables (popular in IRP this year).
	•	Rationale: Clients prefer CMT over CMS since investors are more familiar with treasury yields vs. swap rates.
	•	Activity: Most trading occurred earlier in the year, driven by treasury issuance appetite.

⸻

Current Configurations
	•	10y USD CMT
	•	Reference: US Treasuries
	•	Forward: Forward 10y USD Swap rate + Spot Spread + Forward basis
	•	Vol: 10y USD Vol + Vol & Skew (basis benchmarked)
	•	EUR Approved and Traded
	•	Reference: France OATs, Germany Bunds, EU Commission Bonds
	•	Forward: Linear interpolation between nearest shorter and longer maturity bonds relative to 10y
	•	Vol: 10y EUR Vol + Basis of (France/Germany/EU) Bond Options
	•	EUR Approved (Not Traded Yet)
	•	Reference: Spain Bonds (SPGB)
	•	Forward & Vol: Same as EUR traded

⸻

Portfolio Size
	•	10y USD CMT
	•	Portfolio Notional: ~USD 1.4bn
	•	Total Vega: ~700 $K/bp
	•	Risk concentrated in NYC Volex desk (~528 $K/bp Vega on CMTs).
	•	Remaining portfolio split across Asia and EMEA desks.
	•	EUR CMTs
	•	Portfolio: ~$127mm Notional
	•	Total Vega: ~90 $K/bp
	•	Products: Mainly autocallables on Tec10 (France’s CMT).

⸻

Would you like me to also prepare a 1-page executive version (very short bullets with only the most material numbers and facts) for senior management circulation?



Likelihood:
S = SUM(w[n], n=1..M)    where w[n] = weight of model n, M = number of models

Likelihood(S) = {
   Systemic     if S ≥ 101
   Repeated     if 41 ≤ S ≤ 100
   Occasional   if 16 ≤ S ≤ 40
   Remote       if 0 ≤ S ≤ 15
}


Impact (per dimension i: financial, regulatory, reputational...):
T[i] = SUM(x[i,n], n=1..M)    where x[i,n] = 1 if model n has High impact on dimension i, else 0

Impact[i] = {
   Critical     if T[i] ≥ 401
   High         if 101 ≤ T[i] ≤ 400
   Moderate     if 51 ≤ T[i] ≤ 100
   Low          if 0 ≤ T[i] ≤ 50
}

Overall Impact = worst( Impact[i] across all dimensions )





Here’s a clearer, more structured version of your email draft. I kept the tone professional but collaborative, made the points sharper, and grouped them into clear sections for Bill and others to follow easily:

⸻

Subject: Summary of Validator Feedback on MRM AI Assistant

Hi all,

Starting a thread to summarize validator feedback on the MRM AI Assistant. Please add any insights you’ve received from your regions so we can provide Bill with a comprehensive summary.

Positive Feedback
	•	Proofreader: Most frequently used feature. Validators highlighted improved clarity and concision in validation documents, saving hours of effort.
	•	Synopsis: Well-received for summarizing key attributes, risks, and recommended analyses.
	•	Example: During the SPG→UBM Migration validation, a validator used Synopsis to compare methodology and assumptions across migration documents, effectively summarizing differences.
	•	In other cases, it was used to suggest potential analyses for deployment.

Areas for Improvement
	•	Awareness/Usability: Some validators are not familiar with basic functions (e.g., toggle switch). Misuse of plugins has led to error messages, causing frustration and abandonment. More training/promotion needed.
	•	Narrow Scope: For general editing/chatbot tasks, validators prefer GS AI Assistant. Feedback suggests the MRM AI Assistant’s current use cases feel limited, though additional functionality is being developed.

Suggestions from Validators
	•	Enable ability to chat with the LLM even when plugins are switched on, to allow continued discussion of responses within the same session (noted as technically challenging).
	•	Allow documentation upload for plugins to expand applicability.

Thanks, and please add any additional feedback you’ve gathered.

Best,
[Your Name]

⸻

Would you like me to make a shorter “executive-style” version as well (3–4 bullets total), in case Bill prefers a high-level snapshot instead of detailed notes?



Here’s a refined version of your summaries, keeping the same structure but making each bullet exactly one sentence:

⸻

Tier 1 Compliance surveillance AI
Tier 1 Compliance surveillance AI is used to review insider trading cases and reduce escalations for human review, currently under MRM validation and in the pipeline for AIRCC and ERC review.
	•	This is the first AI model with agentic components, enabling the system to both shape the review workflow and execute tasks.

Notable recent model validations include:
Revalidation of the Equity Share Buyback pricing model (Tier 1 GBM Public ML pricer) with approval of 13 exotic features frequently requested by clients.
	•	This update deprecates the slang pricer and migrates all features to Python.
	•	The model leverages a neural network to fair-value equity share buyback transactions, improving execution and pricing competitiveness.

Fast Quoting
MRM approved the Agni Sharkfin model (Tier 2 GBM Public), a neural network pricer reducing quoting time by 72% (from 3 minutes to 50 seconds) for equity structured product charges.
	•	This improvement addresses client feedback that quoting latency above two minutes is increasingly unacceptable as peers accelerate.

Private Wealth mortgages
MRM approved the migration of Private Wealth mortgages from Cyprus to Delphi, aligning methodology across AWM and GBM with distinct parameters for different uses, impacting $12Bn of notional.
	•	The change remediates a validation finding and enables the model to capture a wider set of borrower behaviors.

⸻

Would you like me to make this even tighter (e.g., merge the sub-bullets into one line each) so that the whole section reads like a set of concise highlights?



Alright, here’s a structured response to the first question about Caroline:

1. What is one thing your manager does well and should continue doing?

Caroline excels in recognizing the potential in her team members and nurturing their professional growth. One standout instance of this was when she involved me in the Deterministic Regulatory calculations (DRCs) project. Her decision to include me not only showcased her trust in my abilities but also provided me with a valuable opportunity to enhance my skill set and understanding. I sincerely hope she continues with this approach, as it’s been instrumental in my personal and professional development.


For Ariana as a colleague:

1. What are this person’s top strengths that make them effective in their role?

Ariana’s prowess in coordination stands out distinctly. She seamlessly interacts with various teammates within Model Risk and liaises effectively with other divisions. Her ability to guide and assist, especially evident from my personal experience as a new joiner last year, is truly commendable. Her support has been instrumental in my smooth integration into the team.

2. What is at least one thing this person should consider doing to increase their effectiveness?

Considering Ariana’s strength in coordination and liaison, she might benefit from occasionally attending inter-departmental workshops or seminars. By broadening her network and understanding of the intricacies of other divisions, she can further hone her liaison skills, ensuring even more streamlined communication and collaboration across divisions.


Here’s a concise structured summary of your text:

⸻

LN NM Callable Activity & Issues
	•	Business Activity
	•	Entered SSA callable market in Oct 2023 with EBRD Bermudans.
	•	Started in TRY (waiver 8759), expanded to ZAR & MXN. TRY remains largest.
	•	~$60mm PnL generated to date.
	•	Trade Structure
	•	Typical: 10y NC1y with annual calls, TRY zero vs USD floating.
	•	GS holds call option; notional exchanged at call.
	•	Earlier trades had ~40% accretion (called early); new trades ~20%.
	•	Desk also trades smaller GS-issued callables (ZAR, HUF, PLN, RUB).
	•	March 2024 Issue (+$1.7mm)
	•	Non-continuous MEE window used (Oct24/26/28), mis-reflecting early-call likelihood.
	•	MRM required continuous MEE windows; remarking added +$1.7mm.
	•	August 2025 Issues (-$2.8mm est.)
	•	-$1.3mm: Incorrect mean reversion mark (default vs trading value).
	•	-$0.3mm: Unstable calibration (LMFS parameter inherited, unsuitable for short trades).
	•	-$1.2mm: Approximate calibration for zero-coupon Berms inaccurate under TRY OIS–Xccy basis; MRM alternative reduced value.

⸻

Do you want me to simplify this further into just 4–5 bullets (like a high-level “executive summary”), or keep the current slightly more detailed breakdown?


LDN NM Bermudan Callables Summary
	•	Since Oct 2023, desk trades SSA callables with EBRD, mainly in TRY; also expanded to ZAR and MXN. Business generated ~$60mm PNL.
	•	Typical structure: 10yNC1, GS pays TRY zero coupon, receives USD floating, holds call option; new trades accrete ~20%.
	•	Early trades (7yNC1y) had ~40% accretion, almost always called at first date.
	•	Smaller GS-issued callable notes in ZAR, HUF, PLN, RUB traded pre-EBRD, minor size.
	•	Mar 2024: +$1.7mm from correcting MEE window pricing; Aug 2025: -$2.8mm modeling losses (mean reversion, calibration, zero-coupon Berm approach).

Would you like me to make an even shorter 3-bullet executive version for senior management decks?



I apologize for the oversight. Let’s correct that.

For Kainan as a colleague:

1. What are this person’s top strengths that make them effective in their role?

Kainan exhibits an exceptional technical aptitude that has been foundational to our team’s accomplishments. Her ability to communicate complex ideas succinctly is noteworthy. Her invaluable contributions, especially in areas such as transaction waivers, various reporting decks, and Model IT matters, underline her comprehensive skill set.

2. What is at least one thing this person should consider doing to increase their effectiveness?

While Kainan’s collaborations within the team are commendable, a minor suggestion would be for her to further extend her interactions with colleagues beyond our direct team. By broadening her outreach, she can glean diverse insights and viewpoints, potentially enriching our team’s approach and solutions. This slight expansion in networking can further enhance her already significant impact.


This structure is intended as flexible guidance. You do not need to strictly follow it — adapt bullets and ordering depending on the model or context.


Perfect — thanks for sharing the full draft and the screenshots. I’ve polished your prompt engineering template to make it more formal, structured, and comprehensive, while staying close to your intent. I also expanded the guidance where helpful (e.g., wording discipline, optional additions, handling multiple models).

Here’s an improved version you can use:

⸻

📑 Prompt Engineering Template for MRM Validation Summaries

[ROLE / CONTEXT]

You are a Risk Manager in Goldman Sachs’ Model Risk Management (MRM) team, preparing a bi-weekly update for senior management. The material summarizes validation approvals and related activities for models used by the Global Banking & Markets (GBM) division.

⸻

[TASK]

Summarize the validation information provided into structured, professional bullet points suitable for reporting.

⸻

[FORMAT]
	•	Start with one clear title (model approval, extension, or enhancement).
	•	Follow with bullet points (and sub-bullets if needed).
	•	Maintain a consistent, professional tone.

⸻

[CONSTRAINTS]
	•	Keep each bullet point under 30 words.
	•	Keep factual; avoid subjective or extreme terms (e.g., avoid “significant”, “critical”).
	•	Use consistent tense (“We have approved…”, “During validation, MRM conducted…”).
	•	Acronyms (e.g., CLN, IRP, CVA) may be used without definition, assuming senior audience familiarity.
	•	Where findings are noted, mention their severity (Sev1–3) and the theme (documentation, calibration, etc.), but avoid unnecessary detail.

⸻

[CONTENT STRUCTURE]

Title Options:
	•	Approval of the [Model Name] Model
	•	[Model Name] Model Extension for [Coverage/Payoff]
	•	Enhancements to the [Model Name] Model

Bullets:
	1.	Approval Statement
	•	“We have approved the Tier [1/2/3] [Model Name] model used to [primary purpose].”
	•	OR “We have approved the extension to the Tier [1/2/3] [Model Name] model to support [coverage].”
	•	OR “We have approved enhancements to the Tier [1/2/3] [Model Name] model to [change].”
	2.	Purpose / Business Rationale
	•	“The model was developed to [replace old model / enable business / align with program / remediate waiver].”
	•	OR “This extension resolved [waiver/limitation].”
	•	OR “These enhancements improve [specific model feature, e.g., calibration consistency, hedging accuracy].”
	3.	MRM Validation Analysis
	•	“During validation, MRM conducted independent analyses, including:”
	•	Sub-bullets: benchmarking, back-testing, sensitivity, replication, documentation review.
	•	OR “MRM’s analysis focused on [specific tests].”
	4.	Findings Raised (Optional)
	•	“MRM raised [number] [severity] findings related to [theme].”
	•	If applicable: note whether remediation is closed, in progress, or planned.

⸻

[EXAMPLES]

# Approval of the CD CLNICSL Model
	•	We have approved the Tier 1 CD CLNICSL model, used to price Credit-Linked Notes (CLNs) and implemented in CSL.
	•	The purpose of this model is to price callable CLNs using hazard rate and interest rate dynamics.
	•	During validation, MRM conducted sensitivity analysis across risk factors and parameters.
	•	MRM raised one Sev1 finding on documentation (remediated) and two Sev2 findings on validation checks and IR calibration (remediation in progress).

⸻

# Approval of IRP CVA Cxl Berm and IRP CVA Ctl Berm Swo Models
	•	We have approved two Tier 1 models for XVA computation in USD swaps and Bermudan swaptions.
	•	The models address XVA exposure of life trades by computing XVA for such trades.
	•	During validation, MRM independently assessed exposures, tradeability, MEE windows, and option valuation.
	•	MRM raised two Sev2 findings on implementation and regressions; remediation is ongoing.

⸻

🔧 Additional Guidance
	•	Consistency across multiple approvals: If reporting several models in one update, ensure uniform formatting to improve readability.
	•	Optional grouping: Where multiple approvals belong to one theme (e.g., Callable Structures, XVA Models), a grouped title with sub-sections may be used.
	•	Tone discipline: Keep the voice neutral (no marketing language). Use “enable,” “support,” “address,” “remediate,” instead of “enhance competitiveness” or “significantly improve.”
	•	Flexibility: The template is guidance; adapt wording for clarity but keep structure intact.

⸻

👉 This version is formal, precise, and extensible — you can apply it to any validation summary, whether approvals, extensions, or enhancements.

Would you like me to also create a “bad vs. good” side-by-side example sheet (e.g., too vague vs. properly structured) so your team can quickly see how to apply the template?



[ROLE / CONTEXT]  
You are a risk manager preparing material for a senior executive.  

[TASK]  
Write one sentence describing the root cause of a $1.2m operational risk loss.  

[FORMAT]  
Respond in one sentence, plain English.  

[CONSTRAINTS]  
Keep it under 25 words. Emphasize the system mismatch (fast vs. slow).  

[EXAMPLE]  
Example of a good output:  
“Connecting a fast auto-hedging system with a slow risk feed caused timing mismatches and duplicate trades.”  


[ROLE / CONTEXT]  
You are [who should the AI act as? e.g., risk manager, Python tutor, travel guide].  

[TASK]  
Your task is to [specific action: summarize, explain, draft, calculate].  

[FORMAT]  
Respond in [bullets / table / one sentence / paragraph / code].  

[CONSTRAINTS]  
Keep it [under X words / formal tone / plain English / include examples / no jargon].  

[EXAMPLES (optional)]  
Example of a good output: “...”  



Great question — think of prompt engineering as designing instructions for an AI the way you’d design requirements for a junior analyst: clear, structured, and contextual.

Here’s a practical framework you can use:

⸻

🔑 Steps to Construct a Good Prompt
	1.	Set the Role / Context
	•	Tell the model who it should act as and what the situation is.
	•	Example: “You are a risk manager summarizing an operational loss for senior management.”
	2.	Specify the Task Clearly
	•	State exactly what you want (summarize, draft, translate, compute, etc.).
	•	Example: “Write a one-sentence description of the root cause.”
	3.	Define the Format / Style
	•	Indicate whether you want bullets, tables, headlines, code, formal/informal tone.
	•	Example: “Respond in 3 concise bullets, using plain English.”
	4.	Add Constraints / Rules
	•	Set length, scope, or exclusions.
	•	Example: “Keep under 20 words. Do not mention technical system names.”
	5.	Provide Examples (if possible)
	•	Show the model what “good” looks like.
	•	Example: “Good example: ‘System integration caused a timing mismatch leading to losses.’”
	6.	Iterate & Refine
	•	Start broad, then tighten.
	•	Treat it like coaching: you give feedback, and the prompt evolves.

⸻

🧩 Prompt Template You Can Reuse

Role/Context: “You are [X] working on [Y]…”
Task: “Please [do Z]…”
Format: “Respond in [bullets / table / one sentence / code].”
Constraints: “Keep under [N words / no jargon / include examples].”
Examples (optional): “For example: [give 1-2 good outputs].”

⸻

✅ Example for your op risk case:
“You are a risk manager preparing material for a senior exec. Write one sentence describing the root cause of the $1.2m op risk event. Keep it plain English, under 25 words, and emphasize system mismatch (fast vs. slow).”

⸻

Do you want me to create a cheat sheet of reusable prompt templates (e.g., summarize, draft, explain, code, translate) that you can copy-paste for different tasks?

Here’s a slightly tightened and polished version of your draft. I kept your structure but improved flow, readability, and consistency:

⸻

Top of Mind®
	•	MRM MRA Remediation (Annual Review): Remediation remains on track, with infrastructure enhancements and training completed ahead of the Sep 30 deadline
	•	Rollout is underway, with reviews for ~700 models to be completed under the enhanced framework by Dec 19
	•	We plan to schedule time with the FRB in the coming weeks to review the approach for addressing incremental CCAR feedback

Artificial Intelligence
	•	Validation is in progress for the Tier 1 Compliance surveillance AI used to review insider trading cases and narrow the scope of matters escalated for human review
	•	First AI model with fully agentic components, where the system both determines workflow and executes tasks
	•	Notable recent validations include:
	•	Equity Share Buyback Pricer: Revalidation of the first Tier 1 GBM Public machine-learning pricer; approval of 13 additional exotic features frequently requested by clients
	•	Model leverages a neural network to fair-value equity share buyback transactions, improving execution and client pricing competitiveness
	•	Fast Quoting (Agni Sharkfin): Approval of Tier 2 GBM Public neural network pricer that reduces quoting time by 72% for equity structured product charges

Validation Activities
	•	Approved migration of the mortgage prepayment model to the Delphi framework for pricing PWM mortgages
	•	Addresses a validation finding and aligns methodology across AWM and GBM
	•	Approved enhancements to the commodity margin shortfall model for GSEC clients, following annual review assessments in Q1
	•	Enhancements include recalibrated Cocoa shocks after recent volatility, plus new ongoing monitoring for missing Delta and Vega liquidation charges

Regulatory Updates
	•	FRB held the soft-close call last week for the Transaction Banking AML Remediation Verification Event (RVE)
	•	Confirmed all findings, including one on Compliance models requiring development and testing enhancements, are expected to close with no new findings
	•	NFA 2025 Swap Dealer Exam: Initial response submitted Sep 5
	•	Questionnaire requested pricing/risk model inventory and policy breaches; awaiting scope clarification from NFA
	•	Compliance expects heightened focus on model governance in this year’s exam
	•	PRA Periodic Summary Meeting (PSM): E&Y audit of model changes under IMM and IRB approaches completed
	•	Six preliminary findings identified on model change notification process, covering missing notifications, process scope, governance, and documentation

⸻

Would you like me to make this more executive-friendly (shorter, more headlines, fewer details), or keep it in this technical but polished format for internal tracking?




Here’s a concise draft you can paste into Outlook/Gmail:

⸻

Subject: Updates & asks: AI tooling feedback, surveillance AI, and PRC cadence change

Hi Bill,

Quick heads-up and a few asks based on this week’s check-ins:

1) AI tooling – candid feedback (early read)
	•	MRM AI Assistant (tone & format): Summaries skew too “adjectival.” We’ll tighten prompts to enforce factual tone and fixed bullet counts (e.g., 3–4 bullets).
	•	Plugins UX: Validators prefer plugins default OFF so they can start in general chat and opt-in per task.
	•	Governance-Check AI: Useful for batch doc scans, but not live/UAT; currently run locally by Bo for batch use. We’ll track readiness before wider use.
	•	Usage & efficiency logging: The “time-saved” spreadsheet has low adoption (many zeros/unused). Team feedback suggests clearer comms and expectations would help.

Asks:
	•	Are you supportive of (a) default-OFF plugins and (b) a short guidance note from you to reinforce logging of efficiency/time-saved? I can draft the note for your review.

2) Surveillance AI
	•	Recommend including a brief update for Brian and in the CO update. I’ll prepare a crisp paragraph unless you’d like a slide instead.

3) PRC cadence change (FYI)
	•	PRC moving from 6 to 8 meetings next year, with requests for updates from each risk stripe per meeting → net increase in our update workload.
	•	We’re engaging with Ross’s team to see where supplementary info can be streamlined (e.g., quarterly cadence for certain metrics).

Asks:
	•	Any guidance on where to push hardest on burden reduction before we revert to Ross’s team?

4) Near-term follow-ups
	•	EIA/UI preliminary findings: I’ll coordinate with George for a summary.
	•	IMM exam: Awaiting update from Sandra.
	•	AI feedback summary: Phil and I will send you a one-pager by Monday covering: what we’re tracking, early sentiment, concrete examples, and adoption hurdles.

Happy to adjust any of the above—please let me know preferences (e.g., plugin default stance, comms tone, slide vs. paragraph for Surveillance AI).

Thanks,
Yibo

CC: Phil, Bo, (add others as needed)

⸻

Want me to tailor this for a senior-leadership tone (even tighter, with a 5-line executive summary at the top), or draft the “time-saved logging” note in your voice for Bill to send?



Here’s a concise draft you can paste into Outlook/Gmail:

⸻

Subject: Updates & asks: AI tooling feedback, surveillance AI, and PRC cadence change

Hi Bill,

Quick heads-up and a few asks based on this week’s check-ins:

1) AI tooling – candid feedback (early read)
	•	MRM AI Assistant (tone & format): Summaries skew too “adjectival.” We’ll tighten prompts to enforce factual tone and fixed bullet counts (e.g., 3–4 bullets).
	•	Plugins UX: Validators prefer plugins default OFF so they can start in general chat and opt-in per task.
	•	Governance-Check AI: Useful for batch doc scans, but not live/UAT; currently run locally by Bo for batch use. We’ll track readiness before wider use.
	•	Usage & efficiency logging: The “time-saved” spreadsheet has low adoption (many zeros/unused). Team feedback suggests clearer comms and expectations would help.

Asks:
	•	Are you supportive of (a) default-OFF plugins and (b) a short guidance note from you to reinforce logging of efficiency/time-saved? I can draft the note for your review.

2) Surveillance AI
	•	Recommend including a brief update for Brian and in the CO update. I’ll prepare a crisp paragraph unless you’d like a slide instead.

3) PRC cadence change (FYI)
	•	PRC moving from 6 to 8 meetings next year, with requests for updates from each risk stripe per meeting → net increase in our update workload.
	•	We’re engaging with Ross’s team to see where supplementary info can be streamlined (e.g., quarterly cadence for certain metrics).

Asks:
	•	Any guidance on where to push hardest on burden reduction before we revert to Ross’s team?

4) Near-term follow-ups
	•	EIA/UI preliminary findings: I’ll coordinate with George for a summary.
	•	IMM exam: Awaiting update from Sandra.
	•	AI feedback summary: Phil and I will send you a one-pager by Monday covering: what we’re tracking, early sentiment, concrete examples, and adoption hurdles.

Happy to adjust any of the above—please let me know preferences (e.g., plugin default stance, comms tone, slide vs. paragraph for Surveillance AI).

Thanks,
Yibo

CC: Phil, Bo, (add others as needed)

⸻

Want me to tailor this for a senior-leadership tone (even tighter, with a 5-line executive summary at the top), or draft the “time-saved logging” note in your voice for Bill to send?





Got it — thanks for clarifying. You meant the posting email to Bill about the PRC/BRC cadence change (last part of the transcript). Here’s a clean draft you can send:

⸻

Subject: Heads-up: PRC/BRC cadence change for 2026

Hi Bill,

Quick FYI on the committee schedule:
	•	PRC cadence will increase from 6 to 8 meetings per year starting next year. Each meeting will now request updates from every risk stripe, which means our team’s updates will also increase from ~6 to 8 times annually.
	•	BRC remains on the annual review cycle (December). As part of that session, the MCP change will be included for review.

We are engaging with Ross’s team to explore ways to reduce the incremental burden (e.g., moving certain supplementary metrics to a quarterly cadence). Will keep you posted once we have confirmation.

Let me know if you’d like me to prepare a short slide for MRCC/FRAC to note this change explicitly.

Thanks,
Yibo

⸻

Do you want me to also prepare a 1-liner “executive summary” version that you can use if Bill wants to forward this directly to senior leadership?



Here’s a cleaner, streamlined version of your text:

MRM identified issues during revalidation of the TRY cross-currency zero-coupon Bermudan cancellable swaps model for the LDN New Markets desk.
• Problems included incorrect mean reversion, skew calibration, and calibration instruments, with a total impact of -$2.8mm; the first two have been remediated, while the calibration instruments issue is tracked as a validation finding.
• Review confirmed no material impact on other desks, though analysis is being extended to ensure full coverage.

Do you want me to also create a one-sentence exec summary version of this for quick updates?

Here’s a simplified bullet-point version of your text:
	•	Scope: MRM revalidated the pricing model for TRY xccy zero-coupon Bermudan cancellable swaps (LDN New Markets). Found modelling issues and built improved benchmark model.
	•	Total impact: -$2.8mm, broken down as:
	•	Incorrect Mean Reversion (-1.3mm): Default MR of ~7% used instead of 1%, overstating optionality value.
	•	Inaccurate skew calibration (-0.3mm): CorrRatio mis-marked at -1.1 vs correct -0.1, causing unstable skew calibration.
	•	Inaccurate calibration instruments (-1.2mm): Approximate LGM calibration replaced with near-exact approach; steep TRY curve makes impact large.
	•	Remediation:
	•	First two issues fixed, offset by reserve release from Controllers.
	•	Last issue needs modelling enhancements → raised as a finding.
	•	Impact across desks:
	•	No other desks affected by mean reversion issue.
	•	Other issues exist in desks trading zero Berms on LGM, but smaller impact (lower accretion rates than TRY).
	•	MRM extending analysis to those desks.

Do you want me to make this even shorter (2–3 lines) for quick talking points, or keep this level of detail?


Here’s a detailed structured summary of the updates (framed so you can take them to Brian tomorrow at 9am). I’ve organized them into clear sections, with bullets under each for ease of use:

⸻

1. Brian Meeting – Key Notes to Raise
	•	Due dates / Deliverables
	•	IRR proposal due mid-September → artifact is presentation to MRCC, not full implementation.
	•	Implementation with divisions will run through November.
	•	AU Applicability / Formula
	•	Need Brian’s alignment on AU applicability scoping (strapped vs non-strapped AUs).
	•	Proposal: show examples (GBM, Public Shared Services) → highlight controls (5-control strapped vs minimal control non-strapped).
	•	Include rough counts for context.
	•	Traceability Effort
	•	Regulators are mapping regulatory guidance → policies → AUs/risks/controls.
	•	Issues: CCR rules (e.g. SR 11-10) bring prescriptive requirements not always in templates (e.g. counterparty backtesting).
	•	Clarify whether model obligations are explicitly in scope.

⸻

2. Regulatory Engagements
	•	ECB / IM Exam
	•	Onsite kicked off this week (Frankfurt → Warsaw → London).
	•	Need Sandra’s latest readout from recent ECB conversations.
	•	Concerning feedback: ECB suggests “inventory of non-modeled risks” (risks excluded from capital). → Feels like risk ID vs model inventory. Pushback needed.
	•	MIA Capital Proposal
	•	Simon proposing DRC-like framework for “holes.”
	•	Split views: Leslie supportive, Gopi strongly opposed, Monique neutral.
	•	Worth raising with Brian – outcome will affect broader capital treatment.
	•	EY / Exam Status
	•	No recent noise; possibly due to summer schedules.
	•	ACL MRIA
	•	Examiner meeting today canceled; they indicated they have all materials needed.
	•	Likely next step = soft close and final confirmation.
	•	Other Exams
	•	Fed data controls exam: focus is on inputs rather than model logic.
	•	Example: country code assignment in ETL.
	•	MRM clarified: tested independently, prior finding closed (thresholds).
	•	Compliance Eng. described UAT testing; regulators probing sufficiency of controls.

⸻

3. AI / Model Governance
	•	AI Intake Form
	•	Targeting end-September.
	•	Streamlining: merge “streamlined” + AISG forms → new two-tier form:
	•	Stop at simple “No” answers.
	•	If “Yes,” full form required.
	•	Trimming duplicative RM/MRM questions.
	•	Still Word format → tooling digitization TBD (ModelIT not guaranteed).
	•	Governance Enhancements
	•	Alexis presenting Thursday.
	•	Roles/responsibilities unclear; Brian should be briefed.
	•	AI Project Mapping (Bo / Schley / Alley)
	•	Mapping AI projects to business processes + headcount to measure impact.
	•	Idea: link AI initiatives to risk/control processes and scale of people impacted.
	•	Risk overlay concept still fuzzy. Need Brian’s steer.
	•	Other AI Updates
	•	Guardrail model approved last week.
	•	Loans AI largely wrapped up.
	•	KPI work: Bo pulled validated models’ metadata (thresholds, KPIs) → can aggregate for comparability.

⸻

4. Other Risk / Model Updates
	•	Market Risk Metrics
	•	Limit changes scheduled to go live Oct 1 (FAC approval Sept 16).
	•	Daily calculations; comms should start now in weekly/strat updates.
	•	Validation Activities
	•	GBM validation in London: Turkey bonds model → identified issues, material PnL ($3m).
	•	Not formally in “offs,” but still material – highlight to Brian.
	•	72 Findings
	•	Targeting October 23 closeout.
	•	Market Risk carefully tracking; GBM/risk still exposed.

⸻

5. Action Items Before Brian
	•	Align with Sandra for ECB / IM exam feedback.
	•	Confirm with Simon details on MIA capital proposal.
	•	Get from Bo the latest KPI mapping + AI process linkage work.
	•	Review Alexis’ Thursday AI governance draft.
	•	Finalize IRR AU applicability examples (strapped vs non-strapped) → bring to Brian.
	•	Prep comms on Oct 1 market risk limit changes.
	•	Flag material GBM validation issue (Turkey bonds) for transparency.

⸻

✅ This way, tomorrow you’ll have:
	1.	A clear structure for Brian (regulators → AI governance → model/risk updates).
	2.	Talking points on contentious items (ECB inventory, MIA capital, AU applicability).
	3.	Action items to chase before the meeting.

Do you want me to also draft a one-page “Brian prep note” in bullet format that you could paste directly into an email?



Got it — here’s a tighter 3-bullet version:
	•	Aug 21: MRM call with Fed on ETL country-code logic, $1k filter threshold, and rule replicability; MRM clarified these as standard or FCC-driven, with validation support.
	•	Fed requested details on independent validation of critical data inputs; MRM cited a remediated 2023 data-quality finding, with Compliance/FCC noting first-line testing.
	•	Response provided to Fed on Aug 25.



345. Reverse Vowels of a String
Easy
Topics
premium lock icon
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """


151. Reverse Words in a String
Medium
Topics
premium lock icon
Companies
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """


238. Product of Array Except Self
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


























1071. Greatest Common Divisor of Strings
Easy
Topics
premium lock icon
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

1431. Kids With the Greatest Number of Candies
Easy
Topics
premium lock icon
Companies
Hint
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """


605. Can Place Flowers
Easy
Topics
premium lock icon
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """










Here’s a clearer and more concise rewrite of your section, with the 4 changes simplified:

⸻

SPG to CREST UBM Migration
We have approved the following enhancements to the SPG to CREST UBM Migration:
	•	Eq Delta methodology: Replaced CREST Delta Liquidation with SPIRE V30 Eq Delta functional form, reducing WCL by $1.5Bn.
	•	Currency scenarios: Removed CNO/CNH/CNY and SGD from de-pegging scenario and recalibrated shocks, reducing WCL by $845MM (aligned with prior FX Benchmark Model change).
	•	USD Forwards: Redirected to IR stress (instead of default EQ charge), reducing WCL by $645MM.
	•	MPS swaps: Corrected treatment of swap underliers to prevent default CREST charge, reducing WCL by $240MM.

⸻

Would you like me to condense this further into just a headline + one-liner per change (e.g., 4 short bullets only with action + impact)?



Here’s a cleaner, simplified version:

⸻

Approvals of New Execution Algos
We have approved the TargetClose and Canada Trailblazer Algos within the Atlas Execution Algorithms (Tier 2) and Atlas SOR (Tier 2).
	•	TargetClose Algo: A schedule-based strategy designed to trade into the market close, aiming to minimize slippage by executing near the auction while trading earlier if needed to limit market impact.
	•	Canada Trailblazer Algo: A hidden liquidity-seeking strategy (mirroring the US SOR version) that searches dark and gray pools to maximize fill rates while minimizing market impact.

During validation, MRM raised a Sev2 finding requiring regular recalibration of Transaction Cost Model (TCM) coefficients.

⸻

Do you want me to make it even shorter, like 2–3 bullets only?



•	MRM validated and approved the SVT Quoting (ID 25381) and SVT Volatility (ID 26432) Tier 2 models, resolving the prior waiver.
	•	SVT Quoting generates bid/offer quotes for American warrants via Halo Streaming, using adjusted volatility surfaces from SVT Volatility for market making, including out-of-hours quoting.



•	MRM validated and approved enhancements to EqSp Koala and EqSp YMCA models (Tier 1) to support Project Solaris, a reinsurance agreement with a Japanese insurer on a new VA product.
	•	FX hedge is booked in EqSp YMCA, while the GMAB hedge and swap hedge on SPV notes are booked in EqSp Koala.
	•	Both models are used for pricing, risk management, and stress testing of the hedges and swap related to the reinsurance agreement.


Here’s a cleaned-up, detailed summary of the transcript you shared:

⸻

Review of RC Draft Responses
	•	Managers are reviewing RC responses; each section already has an assigned reviewer:
	•	CCR – Bo / Natalia
	•	LRM – R
	•	MRA – Reviewed
	•	Market Risk – David (with Marcus’s input)
	•	Last section – S
	•	Procedure: Bill’s approval is required before sending to the Fed.
	•	If no major issues, Bill can be sent the reviewed package now instead of waiting until the 21st.
	•	Messaging to Bill should note that all relevant managers have reviewed and ask if he wants any changes before submission.

⸻

Items for STR Meeting (During Out-of-Office)
	•	MRA Remediation – Keep at the top of updates.
	•	Secar Feedback – Mention to the Fed without revealing detailed action plans; note that a targeted plan will be submitted for that model.
	•	RCSA – Include remaining 2025 tasks.
	•	Policy Uplift – Not critical to highlight.
	•	GBM Q2 Results – Include results excluding CCR models; send to Bill now for potential inclusion in STRAP partner meeting.
	•	AI Section – Add any incremental updates.
	•	Worth flagging Devon (E-Trading AI) to the Fed as they would be interested.
	•	ESG/EG model items – optional, depending on Bill’s preference.
	•	AI App Approval Task Force – include, along with AI efficiency task force updates.
	•	E-Trading OpRisk Event – Likely to be included; flag to Bill to confirm.
	•	AI Model KPI Performance – Already covered under AI task force.
	•	Residual Risk Rating – No strong need to re-calculate for results without IDR models; let Bill decide.

⸻

Monday P&L Call Prep
	•	Mention that the ACL meeting has concluded (with follow-up meeting on Aug 26).
	•	Fed is focusing heavily on handling of past-due findings — worth making the group aware.
	•	ECB SERP finding – to be mentioned; also IMM status (check with Cassandra).
	•	New MRM AI Assistant applications in EC and ANR – mention to the group.
	•	CR Feedback – note that a project plan is being prepared.
	•	FRB follow-up – to be included in the discussion.

⸻

Other Notes
	•	No major additional items to include beyond regular updates.
	•	CSG AI (public and private) impressed GBM; may be worth adding.
	•	For ETSC metrics, remove the first two tables — all relevant data is already in the third table.
	•	Bill will be sent RCSA results and asked if he wants them included for RAT updates.

⸻

If you’d like, I can also turn this into a condensed bullet-only “ready-to-send” version for your internal minutes so it’s easier to drop into your tracking doc. Would you like me to prepare that?



https://click.mail.cfainstitute.org/?qs=f0565be3c13e00d25eb5054550c449e43b74dce2552a2a5c18e799b4cecb5d89ed4971f331177b4bc9edb8204a2f4f532359bf59a5445633

ECB IMM Onsite Exam – Starts Aug 25, runs until Nov, covering Frankfurt, Warsaw, and London.
	•	Preparation: 48 pre-exam requests submitted Aug 8, including model and validation documentation; 13 meetings set in first two weeks, with a dedicated validation session.
	•	Focus Areas: Model changes from prior ECB inspection remediation and topics with limited previous coverage.


Here’s the simplified summary with the proposal and next steps included:
	•	Overview – Bermuda-based GS reinsurance entity with formal governance (Board, council, underwriting panel) and regular cross-divisional updates.
	•	Portfolio – $8bn across 11 deals with Japanese insurers:
	•	VA – market risk hedged, keeps mortality/lapse risk.
	•	FIA – reinsurance on STS-linked option upside.
	•	Composite VA – hybrid of VA and FIA (1 active deal).
	•	Risk – Most market risk passed to GSI; small residual (~$50k VaR). Mortality/lapse risk unhedged but monitored; not yet in VaR or credit models.
	•	Credit – ~$192mm exposure to 2 IG Japanese insurers, collateralized; trades count toward ~$170mm RWA.
	•	Proposal & Next Steps – Seeking NAC approval (Aug 6) for Project Vista, a Hong Kong deal using Value in Force (VIF) monetization—a pre-paid derivative linked partly to lapse risk. Originally planned as a broader HK/Singapore rollout, now narrowed to one transaction for approval. Market and Credit Risk teams are setting new mortality/lapse limits and developing models to capture these risks before further expansion.


Here’s a simpler 4–5 bullet version:
	•	Overview – Bermuda-based GS reinsurance entity with formal governance (Board, council, underwriting panel) and regular cross-divisional updates.
	•	Portfolio – $8bn across 11 deals with Japanese insurers:
	•	VA – market risk hedged, keeps mortality/lapse risk.
	•	FIA – reinsurance on STS-linked option upside.
	•	Composite VA – hybrid of VA and FIA (1 active deal).
	•	Risk – Most market risk passed to GSI; small residual (~$50k VaR). Mortality/lapse risk unhedged but monitored; not yet in VaR or credit models.
	•	Credit – ~$192mm exposure to 2 IG Japanese insurers, collateralized; trades count toward ~$170mm RWA.
	•	Expansion – Seeking approval for HK deal (Project Vista, VIF monetization). Broader HK/Singapore expansion under review; would raise mortality/lapse risk, so new limits and modelling are in progress.

Here’s a simplified bullet version:
	•	ECB IMM onsite exam starts 25 Aug, runs until Nov, covering FFT, WSW, and LDN.
	•	48 pre-exam requests sent 8 Aug (includes model and validation docs).
	•	13 meetings in first two weeks, including a validation session.
	•	Focus on changes from previous inspection remediation and areas with limited prior coverage.
	•	ECB SREP feedback: draft letter includes finding on model inventory completeness; 4-week response period.
	•	While policy/governance is strong, execution gaps remain in some divisions.
	•	Finding relates to models not in inventory until ECB flagged them, meaning no independent review occurred.
	•	Examples: previously remediated AVA declaration gaps, and cases where risks were not quantified or capital was not taken (latter not considered an inventory gap under policy).

Here’s your simplified short bullet version:
	•	ECB IMM Onsite Exam
	•	Kick-off: 25 Aug → runs until Nov; covers FFT, WSW, and LDN.
	•	48 pre-exam requests submitted (8 Aug), incl. model/validation docs.
	•	13 meetings in first two weeks; one dedicated to validation.
	•	Focus: remediation of past ECB findings + topics with limited prior coverage.
	•	ECB SREP Feedback
	•	Draft SREP letter includes finding on model inventory completeness; 4-week response window.
	•	Policy/governance is robust, but execution by Divisions may need improvement.
	•	Finding triggered by:
	•	Models not in inventory until ECB feedback.
	•	Remediated AVA declaration gaps.
	•	Risks without quantification/capital (not considered inventory gaps per policy).


Here’s a much simpler version of your text:

⸻

E-Trading Oprisk Event – $1.2m Loss in US Rates (7/28/2025)
	•	The Rates Central Risk Book (CRB) recently began internalizing hedge orders from IRP desks to lower costs, trading only residual risk on the exchange.
	•	On July 28, a pilot linked CRB to the Optex auto-hedging algorithm to offset risks between the two. CRB relied on Heracles system data to track net risk.
	•	A 15-second data delay in Heracles meant Optex’s risk reduction wasn’t shown in time, causing CRB to trade the same risk again.
	•	Within 7 seconds, traders noticed a spike and used the kill switch. By then, CRB had traded 106 times (~1.5m/bps DV01), leading to a $1.2m loss.
	•	The CRB–Optex link was cut. CRB will resume its original standalone flow, with tighter exposure controls to be validated by ETSC, which is also reviewing all CRB control parameters.

⸻

If you want, I can also make a one-sentence “headline” version for a report. That would make it even sharper.

Here’s a much shorter, simpler version of your text:

⸻

E-Trading Oprisk Event – $1.2m Loss in US Rates (7/28/2025)
	•	A pilot trade linked the Rates Central Risk Book (CRB) hedger with the Optex auto-hedging algo to net interest rate risk.
	•	Due to a 15-second delay in the Heracles risk update, CRB Hedger repeatedly traded the same risk, executing 106 times and building an excessive position.
	•	Traders stopped the algo within 7 seconds, but closing the position caused a $1.2m loss.
	•	Connection between CRB and Optex was removed. Additional exposure controls will be added and validated before any future integration.

⸻

If you want, I can also make a one-sentence ultra-condensed version for quick slide updates.



Here’s a detailed summary of the transcript with emphasis on what to draft/include for Brian’s updates:

⸻

Key Topics Covered

1. MRA / Remediation Updates
	•	Training will be completed after tomorrow.
	•	Tech enhancements for MRMT are progressing, nearing UAT phase.
	•	Incremental CR feedback received from last week’s Fed meeting to be incorporated.
	•	Plan to show Brian a draft modified remediation plan that reflects this feedback.
	•	Timeline: Aim to implement annual monitoring enhancements by Nov 1, review by year-end (aligned with SECARD timelines).

Include for Brian:
	•	Status of training completion.
	•	UAT readiness for tech enhancements.
	•	Fed feedback incorporated into remediation plan (show draft).
	•	Target dates for implementation/review.

⸻

2. EMF Uplift – Open Issues
	•	Inherent risk rating formula still WIP; tied to OpRisk’s reconsideration of excluding divisions based on materiality.
	•	Two separate scoping questions:
	1.	Which divisions/AUs can be excluded entirely.
	2.	Within included AUs, which processes can be excluded.
	•	Internal Audit’s role unclear; OpRisk may be revising approach.
	•	Processes and controls now aligned with MRM AUs, but scoping still unsettled.
	•	Plan to get latest from OpRisk in tomorrow’s touchpoint.

Include for Brian:
	•	Clarify two separate scoping decisions.
	•	Flag that OpRisk is rethinking criteria; Internal Audit involvement unclear.
	•	Note dependencies for inherent risk formula completion.

⸻

3. AI / GenAI Validation and Controls
	•	26 GenAI model validations completed (Tier 1–3).
	•	Grouped by function (e.g., summarization, extraction).
	•	Capture KPIs, thresholds; note that some models have multiple KPIs.
	•	Highlight big-ticket items: CGI model, Devin.
	•	Related RCSA work for AI controls follows same timeline as model controls.
	•	Additional AI initiatives:
	•	W Pager plug-in and ETSC tools for ANI writeups.
	•	Early testing of agentic AI for committee material gathering.
	•	Interest from other divisions (OpRisk, Ross’s group) to replicate MRM AI setup — MRM will provide templates but not build or staff their work.
	•	AISG policy change expected in September; current API access still gated via RSD.

Include for Brian:
	•	Summary of 26 validations, grouped by category, with KPI/threshold status.
	•	Key models (CGI, Devin) and ongoing RCSA/controls work.
	•	New tools/pilots (W Pager, agentic AI).
	•	Divisional interest in replication; MRM role limited to template/advice.
	•	AISG process changes and current API approval requirements.

⸻

4. Policy & Governance Issues
	•	EY Europe “change notification” misunderstanding — now clarified that MRM not part of the process.
	•	Internal confusion on policy linkages and ownership — risk of divisions writing MRM requirements without MRM involvement.
	•	Example: ILST tracker policy derived from incorrect sources; guidance given to list as “related policies” instead.
	•	Need for training across division on how to read and link policies correctly.
	•	Possible role for divisional risk governance group (RPOG) to enforce linkage/approval rules.

Include for Brian:
	•	Awareness item: policy linkage confusion persists, risk of MRM requirements being added without review.
	•	Recommendation: divisional training on policy linkage/approval.

⸻

5. CCR & Regulatory Updates
	•	Current ACL and TxB exams ongoing.
	•	Participation in CCR and trading quarterly meetings.
	•	Mention CCR validation updates in CO report.

⸻

6. Market Model Topics for Awareness
	•	Central risk book in ALCO — unclear if model involved; recent operational event shut it down.
	•	Equity buyback model switching from GAXA to Constant model.
	•	Suggest MRM track modeling developments across all asset classes (commodities, rates, FX, derivatives, cash, GSS).
	•	Arrow project — possible business opportunity; Brian’s perspective may be useful.

Include for Brian:
	•	Flag central risk book issue and equity buyback model change.
	•	Propose systematic tracking of modeling developments by asset class.
	•	Arrow project awareness.

⸻

7. Draft CO Update Content (to show Brian)
	•	MRA remediation status (training, tech enhancements, Fed feedback).
	•	AI updates (validations, controls, new tools, key models).
	•	CCR validation updates.
	•	ACL MRIA/MRA progress.

⸻

✅ If you want, I can also draft the actual Brian’s update talking points from this, in a concise, presentation-ready format so you can drop them into your meeting notes or slides. This would make it much easier for him to hit all points without wading through detail.

Do you want me to prepare that next?



Here’s a cleaned-up, more concise version while keeping the meaning intact:

⸻

Notable recent approvals for CCR model enhancements include:
	•	Updated shortfall calculation for SPG on the Unified Benchmark Model (UBM), following the migration earlier this year, improving model consistency across business lines and reducing total worst-case loss (WL) by $3.2Bn.
	•	Implementation of collateral stress monitoring for WL and shortfall calculations in DCS and Futures, approved in April, replacing the prior counterparty shortfall limit framework.
	•	These changes deliver more robust benchmark stress loss/shortfall metrics, mitigate wrong-way risk, and address regulators’ prior inquiries on including collateral in stress testing.

⸻

If you want, I can also make it even tighter and more “regulatory-update style” so it’s easier to drop into a meeting minutes or a deck.



Here’s a tightened, clearer rewrite of your text while keeping all details intact:

⸻

Artificial Intelligence
	•	GBM Private Tier 1 Loan Classification Models – Validation nearing completion for generative AI models classifying ~3,000 corporate loan back book records as liquidity or credit.
	•	Findings – Two high-severity issues identified and remediated:
	1.	Accuracy below target and inconsistent performance between seen/unseen samples.
	2.	High output fragility.
Both were addressed through model enhancements and have been closed.
	•	AI Risk & Controls Committee (AIRCC) – [TBU for Devin update after tomorrow’s meeting].
	•	Recent Approvals – Integration of Doc AI into the Tier 1 ESG AI model for extracting ESG data from public company disclosures.
	•	Enhancement improves handling of tables, numerical data, and complex layouts, and incorporates the latest LLM capabilities.

ERMF Integration – [TBU]

⸻

Regulatory Updates
	•	Allowance for Credit Loss MRIA 1 & MRA 2 – Scheduled meetings concluded this week [TBU for final outcome].
	•	Validation focus areas: independent analyses for CRE, ASL, and Apple Card; model uncertainty evaluation; QRF validation approach; and validation findings, including overdue finding extensions.

⸻

If you’d like, I can also make a more concise “headlines-only” version so it fits into a compact meeting deck without losing impact. That would make it feel cleaner for an executive audience. Would you like me to prepare that?



Certainly — here is a bullet-point summary of the positional stress test discussion:

⸻

Positional Stress Test – Swap Spread vs. Bond Basis
	•	Caleb asked for clarification on the new stress test capturing basis risk between Treasuries, swaps, and bond futures, and whether it aligns with Market Risk’s “deleveraging stress scenario.”
	•	David explained:
	•	The test was developed for the NY rates trading portfolio, which held long Treasuries hedged with short bond futures and receiver swaps.
	•	Previously, exposure was monitored using a simple DVO1-based metric, which didn’t fully capture basis risk.
	•	The new test uses historical stress scenarios to simulate losses based on:
	•	OAS spreads on Treasuries,
	•	Net basis on bond futures (CTD),
	•	And swap spreads.
	•	Positions across bonds, swaps, and futures are treated as a commingled exposure.
	•	Bond-specific time series (e.g., on-the-run vs. off-the-run) are used to increase precision.
	•	Caroline noted the team will confirm whether the model is internally referred to as the “deleveraging stress scenario.”

⸻

Let me know if you’d like all these bullet summaries compiled into a single meeting recap.


Certainly — here is a bullet-point summary of the MRA remediation discussion from the end of the Q2 2025 meeting:

⸻

MRA Remediation – Summary of Discussion
	•	Makaylah asked for an update on remediation progress and whether CCAR feedback (Apple Card model’s ongoing monitoring) would be incorporated.
	•	Caroline explained:
	•	Phases 1.1 and 1.2 (enhanced templates and standards) were completed and approved by MRCC.
	•	Phases 1.3 and 1.4 (workflow tool updates and validator training) are underway.
	•	Enhanced annual reviews will begin in Q4 2025, with all due reviews completed by mid-December.
	•	Makaylah emphasized:
	•	CCAR feedback must be formally addressed in the MRA remediation.
	•	This will be a key focus during the Fed’s Remediation Validation Examination (RVE).
	•	Caroline confirmed:
	•	Internal discussions are ongoing to determine how to incorporate the CCAR feedback.
	•	The firm will follow up with the Fed once the approach is finalized.
	•	Makaylah noted she will discuss the firm’s remediation materials with David Palmer and others and will provide feedback.
	•	She offered to invite David to the next quarterly meeting and encouraged the firm to send any questions in advance.

⸻

Let me know if you’d like a version combining this with other section summaries.


Certainly — here is the expanded version of the positional stress test discussion, incorporating more detail while keeping the Q&A format consistent:

⸻

10. Positional Stress Test for Swap Spread vs. Bond Basis

Caleb asked for clarification on the new positional stress test covering swap spread vs. bond basis risk. He sought to understand what the model measures, how it differentiates from existing approaches, and whether it aligns with what Market Risk refers to as a “deleveraging stress scenario.”

David explained that the new stress test was developed by Market Risk in response to observed concentrations in the New York rates trading portfolio, where the desk was:
	•	Long U.S. Treasuries
	•	Hedging with short bond futures and receiver swaps

Previously, the desk was monitored using a simple DVO1-based stress, which compared the size of bond futures positions against the underlying treasury positions. However, this did not capture the full basis risk between:
	•	Treasuries and futures (CTD basis)
	•	Treasuries and swaps (swap spread risk)

The new stress test includes:
	•	OAS spreads on the Treasury securities
	•	Net basis on the cheapest-to-deliver (CTD) bond futures
	•	Historical stress scenarios that simulate joint movements in these metrics

The stress test uses percentile-based historical losses (e.g., 95th percentile) rather than static sensitivities, making it more risk-sensitive and reflective of historical co-movements.

Caleb followed up to ask how the swap spread component was modeled and whether the different hedging instruments were commingled.

David confirmed that:
	•	The swap spread component is captured through changes in the OAS of the bond (i.e., the difference between the bond yield and discount curve derived from swaps).
	•	The overall position — combining Treasuries, futures, and swaps — is modeled as a commingled exposure, with risk captured through co-movements in those spread relationships.
	•	Time series are bond-specific, accounting for on-the-run/off-the-run status, and adjusted accordingly.

David noted that this test helps better capture basis risk across instruments and replaces simplistic metrics with a robust stress-driven approach.

Caroline added that the team would follow up to confirm whether this model is referred to internally as the “deleveraging stress scenario.”

⸻

Let me know if you’d like this paragraph dropped into the full minutes document or exported in a preferred format.



Absolutely — here is the revised Q2 2025 Fed Meeting Minutes, written exclusively in Q&A format, using “Makaylah asked/inquired” and “Caroline explained” (or other names where appropriate). The content remains detailed and structured around the key discussions.

⸻

Meeting Minutes: Q2 2025 Quarterly MRM Meeting with FRB – August 5, 2025

On August 5, 2025, the firm hosted the Q2 2025 Quarterly Model Risk Management (MRM) meeting with the Federal Reserve Board (FRB). The meeting covered supervisory feedback, validation activity, internal audit findings, RAS exceptions, AI/ML model usage, and MRA remediation progress. Below summarizes the FRB’s questions and the firm’s responses.

⸻

1. CCAR Feedback on Ongoing Monitoring and MRA Remediation

Makaylah asked how the firm plans to incorporate CCAR feedback on ongoing monitoring, particularly related to the Apple Card loss forecasting model, into its MRA remediation efforts.

Caroline explained that the feedback was received only the prior Friday, and internal discussions are ongoing. The firm expects to address the Apple Card feedback in addition to the existing MRA remediation plan, and will provide further updates once internal alignment is reached.

⸻

2. Internal Audit Finding and Validator Training

Makaylah inquired about a recently closed internal audit finding related to comprehensiveness of validation documentation, and asked for details on the training conducted for validators, including whether ongoing monitoring was covered.

Caroline explained that the finding was low severity and focused on validation documentation—not monitoring effectiveness itself. The training emphasized:
	•	The importance of clearly documenting how validators assess developer monitoring plans.
	•	Ensuring validation documents remain up to date through model changes and annual reviews.
	•	Comprehensive coverage of assumptions, limitations, and monitoring assessments.

Oliver added that the training was delivered as live sessions and completed across the validator group.

⸻

3. Revalidations and Additional Validation

Makaylah asked whether any of the 13 revalidations were triggered by performance or monitoring issues and requested clarification on “additional validation.”

Caroline explained that the 13 revalidations were triggered by annual review outcomes—not by performance concerns. Additional validation refers to targeted reviews of specific model aspects (e.g., monitoring or a key assumption) rather than a full revalidation.

She noted that the team would follow up with more detail on themes across the 13 revalidations.

⸻

4. RAS Thresholds and Aged Findings

Makaylah asked how often the firm revisits RAS thresholds and how the aged Tier 1 findings are being addressed.

Caroline explained that thresholds are revisited annually. Following the 2018 model uplift, thresholds were gradually tightened to reflect a steady-state framework. The remaining breach relates to Tier 1 counterparty credit risk models within GBM, which are actively being remediated.

⸻

5. AI/ML Inventory and Usage

Makaylah inquired about the firm’s current usage of AI/ML models and requested ongoing quarterly updates on AI inventory in light of broader topical reviews at the Fed.

Caroline explained that AI/ML models remain concentrated in lower tiers, with only a small number of Tier 1 models such as Guardrails. AI platforms (e.g., underlying LLMs) are included in inventory but are validated only in the context of specific use cases.

She confirmed that AI/ML inventory updates will be included in future quarterly meetings.

⸻

6. Validation Findings for Guardrails Model

Makaylah asked whether the Guardrails model update referenced in the deck was intended to remediate validation findings.

David explained that validation had identified the model’s inability to detect issues embedded in the middle of long prompts. The enhancement improved detection across full input texts and addressed the finding. The model is not used for model validation purposes.

⸻

7. FX Algo Model Usage

Caleb asked whether the FX algo model is currently used in production, what markets it applies to, and how bid/offer spreads are adjusted.

David explained that the model is used in cash FX trading, specifically G10 currencies, within the firm’s automated market-making system. It predicts next-tick price direction to guide quoting. Follow-up will be provided regarding execution venues and trading specifics.

⸻

8. Credit Contagion and CCR Model Enhancements

Makaylah and Caleb asked for more detail on the new CCR models and how exposure to un-margined counterparties is tracked.

David explained that:
	•	The enhanced Credit Contagion Model now allows for:
	•	Multiple collaterals per trade.
	•	Default-driven price jumps to better capture wrong-way risk.
	•	Two new coherent CCR models were developed:
	•	One for margined hedge funds, using symmetric historical VAR scenarios.
	•	One for un-margined counterparties, applying 6-month CCAR stress scenarios.

David confirmed that the firm will follow up with exposure data for un-margined counterparties (e.g., energy clients).

⸻

9. LRM Reclassification and Liquidity Impact

Caleb asked whether enhancements to the Liquid and Readily Marketable (LRM) classification impacted capital or liquidity metrics.

Caroline explained that the enhancements—primarily the reclassification of convertible bonds—reduced RWAs by $6–7B. The impact on liquidity metrics (e.g., HQLA and GCLA) was limited. The team will follow up with specific impacts and any planned refinements to LRM classification.

⸻

10. Positional Stress Test for Swap Spread vs. Bond Basis

Caleb asked for clarification on the new positional stress test that monitors the swap spread vs. bond basis risk, and how basis risk between treasuries, swaps, and futures is captured.

David explained that the new model was designed to replace simple DVO1-based measures. It uses historical stress scenarios to capture movements in:
	•	Bond OAS spreads.
	•	Net basis on bond futures.
	•	Swap spreads embedded in bond leg pricing.

The model addresses concentrations in NY rates trading books, particularly those hedging long treasury positions with futures and swaps. David will confirm whether this aligns with what market risk refers to as the “deleveraging stress scenario.”

⸻

11. Execution Status of MRA Remediation Plan

Makaylah asked for an update on execution of the MRA remediation plan and whether CCAR feedback is being incorporated.

Caroline explained that:
	•	Templates and policy enhancements (Phases 1.1 and 1.2) were approved by MRCC.
	•	Infrastructure enhancements and validator training (Phases 1.3 and 1.4) are in progress.
	•	Execution of enhanced annual reviews will begin in Q4, targeting completion by mid-December.
	•	The CCAR feedback will be addressed as part of the broader remediation plan, and the firm will circle back once a path forward is finalized.

⸻

Let me know if you’d like this saved to Word or PDF format — or if you’d like a version with only the most critical questions summarized.



You’re right — Makaylah did follow up with a question during the Internal Audit Findings section regarding the training conducted for validators. Here’s the updated Section 4: Internal Audit (IA) Finding Status, with a detailed sub-bullet on training in response to her question:

⸻

4. Internal Audit (IA) Finding Status
	•	All IA findings are general or low severity and model-specific rather than thematic.
	•	Two findings remain outstanding, both related to enhancements in validation documentation (no issues with model soundness or monitoring frameworks).
	•	Several findings were closed in Q2, including:
	•	Developer monitoring scope was broadened in response to feedback.
	•	Sensitivity analysis and parameter recalibration were introduced in specific models.
	•	Validation documentation was enhanced to address staleness and completeness concerns.

Makaylah inquired about the training conducted for validators, specifically:
	•	Whether the training addressed the importance of ongoing monitoring, as well as documentation expectations.
	•	Caroline clarified:
	•	The internal audit finding was not about deficiencies in monitoring practices but about how monitoring was documented in validation reports.
	•	The training emphasized:
	•	Clear articulation of how validators assessed the completeness and appropriateness of developers’ ongoing monitoring plans.
	•	Comprehensive documentation of all aspects of validation, including monitoring, assumptions, limitations, and model changes.
	•	Importance of maintaining and updating validation documentation over time — especially during annual reviews or following any model changes.
	•	The training was conducted as live sessions and completed across the validation team.
	•	Makaylah acknowledged the clarification and appreciated the focus on documentation integrity, noting that many of the IA findings were indeed documentation-related.

⸻

Let me know if you’d like me to integrate this directly into the full draft again or export it as a document.



Thank you for sharing the Q2 transcript. Based on the Q1 format and the extensive Q2 discussion, here is a draft of the Q2 2025 Quarterly MRM Meeting Minutes with the FRB, following the same structure:

⸻

Meeting Minutes: Q2 2025 Quarterly MRM Meeting with FRB – August 5, 2025

On August 5, 2025, the firm hosted its Q2 2025 Quarterly Model Risk Management (MRM) meeting with the Federal Reserve Board (FRB). The discussion focused on supervisory feedback received during the 2024 CCAR exam, ongoing MRA remediation efforts, internal audit findings, validation activities, RAS exceptions, AI/ML model developments, and counterparty credit risk model enhancements. Joyce Kim (Regulatory Relations) and Makaylah (FRB) participated in the meeting, which concluded with appreciation for the firm’s transparency and commitment to ongoing improvement.

⸻

Key Discussions:

1. MRA Remediation and Ongoing Monitoring Feedback
	•	Makaylah opened the meeting by referencing CCAR feedback related to the Apple Card loss forecasting model’s ongoing monitoring and asked how this would be incorporated into MRA remediation plans.
	•	Caroline confirmed that internal discussions were underway and that stakeholders would convene to determine how to address the incremental feedback. Additional updates will be shared with the FRB once a remediation plan is finalized.
	•	Makaylah emphasized the importance of incorporating CCAR feedback into MRA remediation, especially ahead of RVE.

2. Internal Audit Findings
	•	Makaylah also flagged a recently closed internal audit finding related to model validation documentation and ongoing monitoring.
	•	Caroline clarified that:
	•	The finding was general/low severity.
	•	The issue was not about weaknesses in ongoing monitoring, but rather comprehensiveness of validation documentation.
	•	MRM responded by conducting live training sessions to reinforce expectations around documentation completeness and maintenance over time.

3. Validation Activities
	•	MRM provided updates on validation findings and trends:
	•	336 findings closed during the period; highest volume in GBM and Risk, in line with their large inventories.
	•	13 models were revalidated based on annual review outcomes, not due to external triggers. MRM will follow up on whether any themes emerged from these revalidations.
	•	Additional validations were explained as targeted deep dives into specific aspects of a model when full revalidation is not warranted.
	•	Qualitative Approaches (QAs) and Deterministic Regulatory Calculations (DRCs) saw an increase in findings due to new developments, primarily across Controllers, Treasury, and Risk.

4. Internal Audit (IA) Finding Status
	•	All IA findings are low severity and model-specific.
	•	Two findings remain outstanding (documentation enhancements only).
	•	Several findings were closed in Q2 following actions such as:
	•	Broadening developer monitoring scope.
	•	Enhancing sensitivity analysis.
	•	Strengthening documentation to reflect ongoing monitoring and model changes.

5. RAS Exceptions and Aged Items
	•	No breaches at the Board or firm-wide risk appetite committee (FRAC) thresholds for models under waiver.
	•	Aged waiver breaches noted in prior quarters have been resolved.
	•	Breach remains for Tier 1 models with aged findings (related to CCR), which are under active remediation.
	•	Makaylah inquired about the frequency of RAS threshold reviews. MRM explained that departments revisit them annually and that thresholds have been ratcheted down over time to reflect a steady state post-2018 uplift.

6. Model Inventory and AI Usage
	•	Model inventory has remained stable overall.
	•	AI/ML model inventory was presented by:
	•	Business unit
	•	Risk tier
	•	GenAI vs. non-GenAI
	•	AI platforms (LLMs used as infrastructure)
	•	AI usage remains concentrated in lower-tier models, with Tier 1 models being exceptions (e.g., Guardrails).
	•	Makaylah acknowledged the utility of the update and asked that AI/ML inventory be included in future meetings.

7. AI/ML Model Developments

Highlighted developments:
	•	FX Algo (Tier 3): Transformer-based neural network model for predicting next-tick FX price movement in auto-quoting. Validated using benchmark models.
	•	Guardrails Model (Tier 1): Enhanced to improve detection of prompt injection and hallucination, particularly for issues embedded mid-text.
	•	AI Web Grounding (Tier 2): New model leveraging vetted web search results to reduce hallucination in chatbot responses.

Clarifications:
	•	Guardrails enhancements addressed validation findings, not used for model validation itself.
	•	Most lower-tier AI models referenced fall under Tier 3 (not Tier 4).

8. Counterparty Credit Risk (CCR) and Other Model Enhancements

Key enhancements:
	•	Credit Contagion Model (CVA): Now supports multiple collaterals and jump-to-default effects for wrong-way risk.
	•	Bermudan Product CVA Modeling: Enhanced for FRTB standard approach and treatment of FVA at default.
	•	Unified CCR Short Form Model (EBM Crest): Standardized across SPG and Equities, enabling combined exposure analysis and improved concentration charge modeling.
	•	New Coherent CCR Models:
	•	One for margined hedge funds (symmetric historical VAR).
	•	One for unmargined counterparties (natural resources) applying CCAR-based 6-month stress scenarios.
	•	LRM Enhancements: Reclassified convertible bonds as LRM, reducing ~$6–7B in RWAs; impact on liquidity metrics (e.g., HQLA) expected to be limited, with follow-up promised.
	•	Swap Spread vs. Bond Basis Risk: New positional stress test introduced to enhance monitoring of hedging imbalances in the NY rates book.

9. MRA Remediation Execution Plan
	•	MRM confirmed:
	•	Phase 1.1 and 1.2 completed (enhanced templates approved by MRCC).
	•	Phase 1.3 (infrastructure uplift) and 1.4 (training) are underway.
	•	Execution of enhanced annual reviews scheduled to begin in Q4 with completion expected by mid-December.
	•	Makaylah reiterated the importance of ensuring CCAR feedback on Apple Card loss forecasting is incorporated.

⸻

Closing and Next Steps:
	•	Makaylah thanked the firm for its transparency and proactive approach.
	•	Caleb and other FRB members will send follow-up questions in writing for firm response.
	•	FRB will review MRA remediation materials with David Palmer and others; feedback to be shared in due course.
	•	Next quarterly meeting expected in Q3. FRB encouraged submission of questions in advance to facilitate participation from senior staff.

⸻

Would you like this version as a Word or PDF document as well?




Great — I’ve reviewed both the Q1 example and your full Q2 transcript.

Here’s a draft of the Q2 2025 Quarterly MRM Meeting Minutes, aligned with the structure, tone, and level of detail used in the Q1 version but adapted to reflect the longer and more substantive Q2 meeting:

⸻

Meeting Minutes: Q2 2025 Quarterly MRM Meeting with FRB – August 5, 2025

MRM hosted the Q2 2025 Quarterly Model Risk Management meeting with the FRB on August 5. The meeting covered updates on MRA remediation efforts, validation findings, RAS exceptions, AI/ML model usage, and model development. Joyce Kim from Regulatory Relations introduced herself as the new engagement lead. Michaela from the FRB requested the meeting begin with updates on ongoing monitoring and its connection to the open MRA.

⸻

Key Discussions:

1. MRA Remediation and Ongoing Monitoring Feedback (Primary Focus)
	•	Michaela requested an update on how the firm plans to incorporate CCAR feedback into the MRA remediation, particularly concerns around ongoing monitoring of the Apple Card projection model.
	•	Caroline acknowledged the feedback was received recently (prior Friday) and is under internal discussion with model developers. Next steps will include a plan to address this incremental feedback.
	•	Caroline confirmed the remediation plan remains on track:
	•	Milestones 1.1 and 1.2 (enhanced templates and MRCC approval) have been completed.
	•	Milestones 1.3 and 1.4 (system enhancements and validator training) are in progress.
	•	Live training sessions for validators have commenced; Q4 annual reviews will be executed under the enhanced framework with completion targeted by mid-December.
	•	Michaela emphasized the importance of addressing CCAR feedback within the remediation to ensure it is trusted during RVE. The Fed expects follow-up once the firm aligns internally on remediation approach.
	•	Caroline confirmed willingness to follow up and noted FRB feedback had already been socialized with the MRCC.
	•	Michaela noted a broader Fed review of the remediation effort was upcoming and that she had circulated Goldman’s deck and templates to David Palmer and others for internal discussion.

⸻

2. Internal Audit (IA) Findings
	•	Caroline clarified that recent IA findings were all low severity and model-specific, with no thematic weaknesses.
	•	Of note:
	•	A general IA finding was issued regarding comprehensiveness of validation documentation (not deficiencies in ongoing monitoring).
	•	This was remediated by conducting live training for all validators focused on documentation practices, including how to assess developer-provided monitoring plans and maintain validation documentation as models evolve.
	•	Several IA findings were closed during the quarter, including:
	•	Expanded developer monitoring requirements following IA feedback.
	•	Enhancements to parameter monitoring and documentation for specific models.
	•	Closure of a finding related to monitoring limitations and uncertainties in a loan settlement risk model, remediated via additional monitoring requirements and parameter recalibration.

⸻

3. Validation Findings
	•	336 findings were closed during the quarter, primarily within Risk and GBM, which hold the largest share of Tier 1 models.
	•	13 models were triggered for revalidation as a result of annual review outcomes; these were not routine cadence revalidations.
	•	Michaela inquired whether any of the revalidations were triggered by specific issues (e.g., ongoing monitoring). Caroline committed to following up with details.
	•	Caroline clarified the distinction between full revalidations and “additional validations” — the latter refers to targeted validation work focused on specific areas, e.g., model performance or monitoring, rather than full-scope revalidations.

⸻

4. RAS Exceptions
	•	Utilization of models under waiver remained low across all tiers, with no breaches of BRC or firm-wide RAS thresholds.
	•	All aged waiver breaches noted in prior meetings have been resolved.
	•	One RAS breach remains outstanding: Tier 1 approved models with aged findings, primarily in the counterparty credit risk area (e.g., margin shortfall calculations).

⸻

5. AI/ML and Generative AI Inventory
	•	AI inventory remains concentrated in lower risk tiers (Tier 3 and 4).
	•	Few Tier 1 models exist; guardrails and ESG AI models were highlighted as examples.
	•	Inventory updates now include “AI platforms” (e.g., underlying LLMs used across multiple applications), which are tracked but not validated standalone.
	•	Michaela requested that this AI inventory breakdown be included in future meetings for ongoing monitoring of AI/ML model usage across the industry.

⸻

6. AI/ML Model Enhancements

David summarized recent developments, including:
	•	FX Algo Model (Tier 1): First deployment of a transformer-based deep learning model to auto-quote FX crosses. Validated using benchmark models and feature attribution analyses. The model outperformed simpler neural networks and demonstrated low hallucination risk.
	•	Guardrails Model Enhancements: Detection performance was improved to address prompt injection vulnerabilities occurring mid-text. Enhancements were in response to initial validation findings.
	•	AI Web Grounding Model (Tier 2): Introduced a model leveraging web search engines to reduce hallucinations in LLM responses by grounding outputs in vetted, real-time sources. Significant reduction in hallucination observed during validation.

⸻

7. Model Inventory
	•	Overall model inventory remained stable. No thematic shifts were observed in newly added or reclassified models.
	•	Inventory of Qualitative Approaches and DRCs also remained steady.

⸻

8. Model Development Highlights

David highlighted several key developments:
	•	Credit Contagion CVA Model: Enhanced to support multiple collaterals and model jump-to-default contagion effects between counterparty and collateral.
	•	FEA Enhancements: Improvements to modeling recovery of FVA at default in bilateral derivatives, especially relevant for corporate counterparties.
	•	Unified Short-Form CCR Model: Adoption of a consolidated benchmark model across SPG and Equities, enabling more efficient cross-portfolio aggregation and improved concentration charge modeling.
	•	Coherent CCR Models:
	•	Short-form Coherent Model: Developed for margined funds using symmetric historical return scenarios.
	•	Stress Metric Model: For un-margined counterparties (e.g., natural resources), simulating six-month CCAR-like scenarios to capture extended MPOR risk.
	•	LRM Model Enhancement: Classification of convertible bonds as LRM led to ~$6–7B RWA reduction. Limited impact to internal or regulatory liquidity metrics; further enhancements under consideration.

⸻

9. Closing and Follow-Ups
	•	Michaela emphasized the importance of incorporating CCAR feedback into the MRA remediation to avoid duplication during RVE.
	•	The Fed expects follow-up from the firm once internal planning is complete.
	•	Michaela noted an upcoming internal meeting with David Palmer and others to review the firm’s remediation materials.
	•	Caleb will submit trading-specific follow-up questions in writing. Caroline welcomed written follow-ups for clarity and tracking.

⸻

Let me know if you’d like:
	•	a clean Word or PDF version for formal distribution,
	•	shortened bullets for an executive summary,
	•	or help with highlighting changes since Q1.

I’m happy to tailor it.




During Q2, Model Risk identified a P&L breach in the Vega PST for the EMEA Volex portfolio during the monitoring report review. The issue stemmed from static scenario shocks that were not appropriately calibrated to reflect recent market data. A medium-severity finding was raised, recommending shock recalibration. Remediation is currently in progress.



AI Web Grounding, which uses web search to provide real-time context and improve response accuracy and timeliness



Here’s a clearer and more polished version of your text:

⸻

Artificial Intelligence
	•	Loans AI: Validation in progress for the generative AI model that classifies loan document purposes as either credit or liquidity for 6g Liquidity reporting.
	•	Mortgage Loans AI (Tier 1): Approved by MRM; assists the U.S. Mortgage Warehousing Desk by flagging loans likely to be liquidity.
	•	Corporate Loans AI (Tier 1): Validation in progress. Performance and reproducibility issues identified; this model is used across GBM and AWM portfolios and is critical for credit classification.
	•	Other recently approved models:
	•	Funds AI (Tier 2): Extracts NAV of externally administered funds and verifies against alternative sources, reducing manual effort by ~80%.
	•	Wealth AI (Tier 3): Uses LLM to answer PWM advisors’ queries by leveraging internal documentation. Accuracy improved from 61% to 90% after addressing a validation finding.
	•	Agentic AI (Devin):
	•	AIRCC approved expansion of M365 Copilot from 10k users to firmwide.
	•	Staged rollout of Marquee AI Widget-as-a-Tool, enabling users to answer queries, update parameters, and run templatized calculations on Marquee widgets for internal and external use.

⸻

✅ This version:
	•	Improves flow and readability
	•	Groups related items logically
	•	Uses concise, active language
	•	Adds emphasis on outcomes (e.g., reducing manual effort by ~80%)

Do you want me to make it even more executive-friendly for a senior management or board update (shorter bullets, business impact emphasized), or keep it detailed for an internal MRM/AI governance update?


NFA issued follow-up requests from the May 2025 Capital Enquiry, mainly on P&L breaches, positional P&L construction, and VaR model; while MRM is not the main focus, NFA requested our input on some topics.



Here’s a cleaner and more concise version of your text while keeping “went well” and combining sentences where appropriate:

⸻

Regulatory Updates

Supervisory Finding Remediation:
	•	MRM MRA Remediation: On track, with infrastructure enhancements and training to be completed by Sep 30 ahead of the enhanced annual review framework rollout.
	•	Allowance for Credit Loss (MRIA 1: Risk Capture & Ongoing Monitoring; MRA 2: Weaknesses in MRM): Development and validation meetings on Apple Card, Asset Secured Lending (ASL), and Commercial Real Estate (CRE) went well.
	•	TxB AML MRIA 2 (Optimization, Testing & Risk-Based Monitoring): FRB has initiated validation, with the kickoff meeting completed.

Quarterly Meetings with FRB:
	•	FRB-MRM Quarterly Meeting: Scheduled for Aug 7. In addition to the usual agenda, the Fed requested updates on open IA findings, AI/ML inventory segmentation, and MRM MRA remediation progress.
	•	CCR Modeling Quarterly Meeting (Jul 22): Went well, focusing on the commodities potential exposure (PE) model. Follow-up includes modeling choices and a list of PE models across asset classes.
	•	Market Risk Trading Model Quarterly Meeting (Jul 30): Went well; we reviewed notable pricing model enhancements approved during H1.

⸻

Would you like me to make it more executive-friendly (shorter, for senior management) or slightly more technical (for internal risk/regulatory audiences)?


Enhancement to Credit Contagion Model
	•	MRM approved improvements enabling multiple collaterals in a single trade and modeling correlated defaults.
	•	Enhances CVA and gap risk calculations by capturing diversification and default correlations.
	•	Paired with the multi-credit jump model, this is a key milestone for CSG model development.
	•	Benefits include better risk representation for private credit SPV notes and on-balance sheet lending, improving accuracy of trade risk depiction.



Here’s your original text with all changes highlighted. I’ll show original → revised differences in bold so you can easily see what I changed.

⸻

Title
	•	Original: Model Performance Under Tariff Uncertainty: During the volatile market period, the trading valuation models performed well and robustly overall.
	•	Revised: Model Performance Under Tariff Uncertainty: During the volatile market period, the trading valuation models performed well and remained robust overall.
(✔ Added “remained” for better flow)

⸻

Section 1: Basket Options
	•	Original: There was calibration issues observed under multi-FX model:
	•	Revised: However, calibration issues were observed under the multi-FX model:
(✔ Fixed plural agreement: “issues were” instead of “issues was”; ✔ Added “However,” for readability; ✔ Added “the” before multi-FX model)
	•	Original: For basket option with large number (5 or more) of crosses, there was calibration issues at the short end and observed unstable Vega risk.
	•	Revised: For basket options with a large number (five or more) of crosses, calibration issues were noted at the short end, resulting in unstable Vega risk.
(✔ Pluralized “option” → “options”; ✔ Added “a” before large number; ✔ Spelled out “5” → “five” for formal tone; ✔ Changed “there was calibration issues” → “calibration issues were noted”; ✔ Changed “and observed unstable Vega risk” → “resulting in unstable Vega risk” for smoother grammar)
	•	Original: The model implies local correlations from the local volatilities of underlying crosses.
	•	Revised: The model infers local correlations from the local volatilities of the underlying crosses.
(✔ “implies” → “infers” for technical accuracy; ✔ Added “the” before underlying)
	•	Original: Due to increased volatility/skew, it led to implied correlations out of the bounds.
	•	Revised: Due to increased volatility/skew, this led to implied correlations falling outside acceptable bounds.
(✔ Replaced “it led” → “this led”; ✔ Added “falling outside acceptable bounds” for clarity)
	•	Original: The model has an internal calibration check to make sure the impact from the bounding is not too large.
	•	Revised: The model has an internal calibration check to ensure the impact of bounding is not too large.
(✔ “make sure” → “ensure”; ✔ “from the bounding” → “of bounding” for grammar)
	•	Original: The check failed for some basket trades. The issue was temporarily fixed with limited impact, and further model enhancement is in progress.
	•	Revised: This check failed for some basket trades. The issue was temporarily fixed with limited impact, and further model enhancements are in progress.
(✔ Added “This” for continuity; ✔ Changed “enhancement” → “enhancements” since multiple changes are likely)

⸻

Section 2: Control Variates
	•	Original: Control Variates (CVs) for Monte Carlo Pricer: For multi-asset barrier trades in Equity, control variates have been introduced within the Monte Carlo pricing framework to reduce MC noise, which can better match prices for vanilla payoffs and enhance risk calculation stability for Vega and high order risk. Currently it’s rolled out for Eq MA Barriers (As of May 30, 2025, the P&L impact was ~ $445K), and additional ongoing work is underway to roll it out to other tradables.
	•	Revised: Control Variates (CVs) for Monte Carlo Pricer: For multi-asset barrier trades in Equity, control variates have been introduced within the Monte Carlo pricing framework to reduce MC noise. This improves price alignment for vanilla payoffs and enhances risk calculation stability for Vega and higher-order risks. Currently, it has been rolled out for Eq MA Barriers (as of May 30, 2025, the P&L impact was approximately $445K), and additional work is underway to extend it to other tradables.
(✔ Split long sentence into two for readability; ✔ Changed “which can better match” → “This improves price alignment”; ✔ Changed “high order risk” → “higher-order risks”; ✔ Added comma after “Currently”; ✔ Replaced “~” with “approximately” for formal tone; ✔ Changed “roll it out” → “extend it” for variety)

⸻

Section 3: XVA Pricing
	•	Original: XVA Pricing Enhancement: XVA pricing has been enhanced to better model Credit Support Agreements (SAs) which allow for claiming of FVA value at default and presents in LATAM market. The market price quotes suggested trades were priced with such CSA and cases of actual defaults confirmed such close out amount calculation. In the enhanced model, the FVA exposure at default will be netted with NPV at default, and this is beneficial for liability FVA. With this change, there were ~$14mm XVA reserve release, which was mainly from liability FVA benefit with LATAM counterparties.
	•	Revised: XVA Pricing Enhancement: XVA pricing has been enhanced to better model Credit Support Agreements (CSAs) that allow for claiming FVA value at default, which is present in the LATAM market. Market price quotes suggested trades were priced with such CSAs, and cases of actual defaults confirmed such close-out amount calculations. In the enhanced model, the FVA exposure at default will be netted with the NPV at default, which is beneficial for liability FVA. With this change, there was an approximate $14mm XVA reserve release, mainly from liability FVA benefit with LATAM counterparties.
(✔ Changed “SAs” → “CSAs” for accuracy; ✔ Changed “and presents in LATAM market” → “which is present in the LATAM market” for grammar; ✔ Added commas for clarity; ✔ “such close out amount calculation” → “such close-out amount calculations”; ✔ Added “the” before NPV; ✔ Changed “there were ~$14mm” → “there was an approximate $14mm”)

⸻

Section 4: Forward Risk Dividend Logic
	•	Original: Forward Risk Dividend Logic[Q1]: There was an implementation issue on projecting future dividends in forward risk calculations. It only affects the risk calculations at the year end. Specifically, dividend projection logic references the pricing date year as start point to determine marked dividend period by adding fixed number of years. When shifting pricing date forward during forward risk calculations, it added additional year without dividend data in back end of dividend marks, and it resulted in incorrect future dividend projection under the risk scenario. This resulted in an equity delta misstatement of ~ $50mm, no PL impact. The issue has been fixed with MRM review.
	•	Revised: Forward Risk Dividend Logic [Q1]: An implementation issue occurred in projecting future dividends in forward risk calculations. This only affected risk calculations at year-end. Specifically, the dividend projection logic referenced the pricing date year as the starting point to determine the marked dividend period by adding a fixed number of years. When shifting the pricing date forward during forward risk calculations, it added an additional year without dividend data at the back end of the dividend marks, resulting in incorrect future dividend projections under the risk scenario. This caused an equity delta misstatement of approximately $50mm, with no P&L impact. The issue has been fixed with MRM review.
(✔ Changed “There was an implementation issue on projecting” → “An implementation issue occurred in projecting”; ✔ Changed “It only affects” → “This only affected”; ✔ Added “the” before start point → “the starting point”; ✔ Added “a” before fixed number; ✔ Changed “added additional year without dividend data in back end” → “added an additional year without dividend data at the back end”; ✔ “it resulted in incorrect future dividend projection” → “resulting in incorrect future dividend projections”; ✔ Changed “This resulted in” → “This caused”; ✔ “~” → “approximately”; ✔ “no PL impact” → “with no P&L impact”)

⸻

✅ Summary of edits:
	•	Fixed subject-verb agreement
	•	Improved readability by breaking up long sentences
	•	Changed informal phrasing (e.g., “make sure” → “ensure”)
	•	Added missing articles (“the,” “a”)
	•	Adjusted technical word choice for accuracy (“implies” → “infers”)
	•	Standardized currency and numeric expressions
	•	Added commas for clarity and consistency

⸻

Would you like me to produce a clean final version with all changes accepted and also a separate executive summary version (short and clear for reporting)?




Here is your text with minor grammar and clarity improvements only (no major restructuring):

⸻

Model Performance Under Tariff Uncertainty: During the volatile market period, the trading valuation models performed well and remained robust overall. However, calibration issues were observed under the multi-FX model:
	•	Basket Options with Multiple Crosses: For basket options with a large number (five or more) of crosses, calibration issues were noted at the short end, resulting in unstable Vega risk. The model infers local correlations from the local volatilities of the underlying crosses. Due to increased volatility/skew, this led to implied correlations falling outside acceptable bounds. The model has an internal calibration check to ensure the impact of bounding is not too large. This check failed for some basket trades. The issue was temporarily fixed with limited impact, and further model enhancements are in progress.
	•	Control Variates (CVs) for Monte Carlo Pricer: For multi-asset barrier trades in Equity, control variates have been introduced within the Monte Carlo pricing framework to reduce MC noise. This improves price alignment for vanilla payoffs and enhances risk calculation stability for Vega and higher-order risks. Currently, it has been rolled out for Eq MA Barriers (as of May 30, 2025, the P&L impact was approximately $445K), and additional work is underway to extend it to other tradables.
	•	XVA Pricing Enhancement: XVA pricing has been enhanced to better model Credit Support Agreements (CSAs) that allow for claiming FVA value at default, which is present in the LATAM market. Market price quotes suggested trades were priced with such CSAs, and cases of actual defaults confirmed such close-out amount calculations. In the enhanced model, the FVA exposure at default will be netted with the NPV at default, which is beneficial for liability FVA. With this change, there was an approximate $14mm XVA reserve release, mainly from liability FVA benefit with LATAM counterparties.
	•	Forward Risk Dividend Logic [Q1]: An implementation issue occurred in projecting future dividends in forward risk calculations. This only affected risk calculations at year-end. Specifically, the dividend projection logic referenced the pricing date year as the starting point to determine the marked dividend period by adding a fixed number of years. When shifting the pricing date forward during forward risk calculations, it added an additional year without dividend data at the back end of the dividend marks, resulting in incorrect future dividend projections under the risk scenario. This caused an equity delta misstatement of approximately $50mm, with no P&L impact. The issue has been fixed with MRM review.

⸻

✅ Would you like me to make this more concise and executive-friendly (for reporting) while keeping the technical details accurate? Or keep this detailed version as is?


Certainly! Here’s a clearer, more concise rewrite of your bullet points:

⸻

Validation Activities
	•	MRM approved enhancements to the credit contagion model for CVA and gap exposure in secured funding trades, now allowing multiple collateral assets and the use of a benchmark whose default can trigger correlated price jumps in other collaterals.
	•	These changes allow the model to capture diversification benefits, account for default correlations among collaterals, and support CVA and gap exposure calculations for trades with bond or loan portfolios as collateral.
	•	Validation completed for models used in the ECB Counterparty Credit Risk Exploratory Scenario (ECB CCR-ES) exercise.
	•	This exercise, run in parallel with the EU-wide Stress Test, tests banks’ ability to model CCR under stress and risks from connections to non-bank financial institutions like hedge funds.
	•	Key improvements include better justifications for leverage metric selection across counterparties and improved documentation for specific wrong-way risk.

⸻

Let me know if you want this made even shorter or have other edits!




Here’s a simplified and clearer version of your bullet points:

⸻

Validation Activities
	•	Enhancement to Credit Contagion Model
MRM approved improvements to the credit contagion model for CVA and gap exposure in secured funding trades. The enhancement allows:
	•	Inclusion of multiple collateral assets in one trade
	•	Designation of a benchmark name whose default can trigger correlated price jumps in other collateral assets
	•	Better modeling of diversification benefits and default correlations, enabling CVA and gap exposure calculations for secured lending and TRS trades with collateral portfolios
	•	ECB Counterparty Credit Risk Exploratory Scenario (ECB CCR-ES)
Validation completed for models used in this exercise, which runs alongside the EU-wide Stress Test to evaluate CCR modeling under stress and vulnerabilities linked to non-bank financial institutions (e.g., hedge funds).
	•	Key improvements include clearer justification for leverage metrics across counterparties and stronger documentation on wrong-way risk

⸻

Would you like me to make this even shorter (one sentence per bullet) for a high-level executive summary?



This includes approvals of Mortgage Loans AI, used in the U.S. Mortgage Warehousing Desk to assist by flagging loans that may be for liquidity, and Corporate Loans AI, used across GBM and AWM portfolios and relied on more heavily to classify loans as credit or liquidity.A new Tier 2 generative AI model designed to extract and validate Net Asset Values (NAV) of externally administered investments from financial statements, streamlining operations and strengthening the accuracy and reliability of accounting processes.


Here’s a refined and more professional version with improved flow and grammar:

⸻

Regulatory Updates
	•	FINRA/GSCO 2024 Cycle Exam:
The final report was issued in May with no findings for Model Risk. The exam, spanning from September 2024 to May 2025, placed significant focus on Model Risk. A total of 59 requests were addressed, including written responses and eight onsite/Zoom meetings. These covered all aspects of the firm’s model risk management framework, including policies and standards, model inventory and tiering, model validation, model change management, and ongoing monitoring.
	•	Prudent Valuation / Additional Valuation Adjustments (AVAs):
Model Risk completed initial validation and approved twelve prudent valuation methodologies developed to address ECB findings from an onsite inspection. In total, 33 findings were raised by Model Risk, including three high-severity issues related to unapproved model code, methodologies not meeting regulatory guidance, underestimation of AVAs, and documentation weaknesses. All high-severity findings were remediated and closed prior to approval.
	•	Internal Capital Adequacy Assessment Process (ICAAP):
Model Risk reviewed and approved models used by GSI, GSIB, and GSG UK for the current ICAAP cycle. Validation work focused on reassessing model appropriateness for these entities, including evaluation of limitations, uncertainties, and overlays under ICAAP scenarios and in light of portfolio changes. All model changes introduced since the previous ICAAP cycle underwent MRM validation and approval, including improvements to residual risk add-on quantification within the Economic Capital model to remediate prior findings.
MRM also validated and approved ICAAP usage of two climate risk models to assess physical and transition risks, as well as a new qualitative approach for projecting Prudent Valuation Adjustments (PVA). Seventeen new findings were raised, including one high-severity issue for the PVA projection approach, which was addressed through additional testing and documentation enhancements. Remaining lower-severity findings relate primarily to methodology and implementation of limited materiality, insufficient justification for modeling choices, and gaps in ongoing monitoring.
	•	Asset Quality Review (AQR) Exam:
Remediation of four ECB findings from the AQR exam has been completed. These related to GSBE oversight, annual review and validation practices, and process documentation.
	•	ECB Counterparty Credit Risk Exploratory Scenario (ECB CCR-ES):
Model Risk validated models used for the ECB CCR-ES exercise, conducted in parallel with the EU-wide stress test to assess banks’ ability to model CCR under stress and vulnerabilities from interlinkages with non-bank financial institutions, such as hedge funds. The review resulted in improved documentation on specific wrong-way risk within the submission, additional justification for the selection of leverage metrics across counterparties, and a medium-severity finding regarding shortcomings in FX modeling.

⸻

✅ Key improvements:
	•	Fixed grammatical inconsistencies and repetitive phrasing.
	•	Consolidated redundant phrases like “Model Risk has validated and approved” → Model Risk validated and approved.
	•	Organized content into structured, readable bullet points for clarity.
	•	Formalized language for regulatory readiness.

⸻

Would you like me to apply the same editing style to your entire draft so that it reads consistently professional and regulator-friendly?



Model Risk validated and approved a new positional stress test (PST) within the interest rate stress testing framework to capture basis risk across futures, bonds, and swaps. This enhancement was introduced following observed P&L volatility during the April Trump tariff announcements, where previous limits accounted only for bond–futures basis, while losses were primarily driven by bond–swap basis risk.
new model for estimating Delta risk in commodity products, using an improved numerical implementation for greater accuracy and deployed on the Griffin infrastructure for faster computation, relative to the previously used CNPL platform.


Low-tier generative AI models, including Tier 2 and Tier 3 tools, were developed to support productivity across businesses by summarizing market and research content, extracting financial data, generating visualizations from natural language queries, analyzing portfolio exposures, enhancing search relevance, and assisting advisors with curated content.
Low-tier generative AI models were developed to enhance productivity across businesses, including summarizing market and research content, extracting financial data, generating visualizations from natural language queries, analyzing portfolio exposures, improving search relevance, and assisting advisors with curated content.



During Q1 2025, a modeling issue was identified by the Exotios trading desk:
At year-end, the desk observed that forward risk calculations did not correctly incorporate dividend impacts. The issue arose because dividend projections were dropped when the forward date was adjusted in the risk calculation. This occurred due to the projection logic referencing the pricing date year as the starting point for dividends; when this shifted during forward risk calculations, it pointed to a year with no dividends, resulting in incorrect inputs.

Impact: Equity delta was misstated by approximately $50 million.

Resolution: The issue was remediated through model changes, which were validated and approved by Model Risk.

Here’s the improved version with each item as a separate paragraph for readability, while maintaining clarity and completeness:

⸻

Trading Model Performance and Valuation Updates

Market Context:
No significant model performance issues were observed during tariff-driven market volatility at the end of March and early April. However, the following notable changes and breaches occurred:

⸻

USD Yield Curve Range Accrual (YCRA) Callable Notes:
Model Risk validated and approved a methodology change for marking callable prices (MEE) in the USD YCRA book, reverting to the pre-Dec 2022 approach used for other callables. This change was driven by two factors: (1) pricing in earlier call options eliminates the need to hedge later coupons, and (2) market observations showed YCRAs priced at the system-optimal call. As of April 8, the impact included Delta of –$0.6MM and Vega of +0.3MM per abp.

⸻

Commodity Volatility Calibration:
Calibration failures were observed in Gold volatility, particularly for structured exotic trades. These issues were caused by record-high spot prices during tariff uncertainty and heavily skewed volatility. The problem was addressed by temporarily disabling short-tenor calibration, which had a limited overall impact.

⸻

FX Model Calibration:
Volatility and correlation calibration failures occurred in multi-cross FX trades due to increased volatility/skew and difficulty sourcing reliable market data for marking. A temporary solution was implemented with limited impact, and further investigation is ongoing.

⸻

Forward Risk Dividend Logic:
At year-end, the Exotics trading desk discovered an error in forward risk calculations caused by incorrect dividend projections. The logic referenced the pricing date year as the starting point, and when adjusted for forward risk, it pointed to a year with no dividends, leading to omitted dividends in risk calculations. This resulted in an equity delta misstatement of approximately $50MM. The issue was corrected through a model change, which has been validated and approved by Model Risk.

⸻

Approved Modeling Enhancements (H1 2025)

Dynamic Barrier Shift for Multi-Asset Equity Autocallables:
Model Risk approved a new methodology enabling barrier shifts to dynamically adjust based on volatility. Previously, barrier shifts were static, either set by traders or calculated only at trade inception. This enhancement allows desks to tighten widths during low volatility, improving competitiveness, and ensures caps on large barriers scale with volatility. The change released approximately $1.7MM from the Barrier Shift Reserve on October 7, 2024, and resulted in a DP impact of –$7K and a Vega impact of –$374K on January 22, 2025.

⸻

Control Variates for Monte Carlo Pricer:
Model Risk approved the application of control variates (CV) within the Monte Carlo pricing framework using local volatility for multi-asset barrier options (Eq MA Barrier). Currently, this enhancement is limited to European-style payoffs, where European calls, puts, and/or digital options serve as CV instruments based on the original payoff structures. The primary goal is to reduce Monte Carlo variance, particularly for Vega, thereby improving risk calculation stability. As of May 30, 2025, enabling CV resulted in a cumulative P&L impact of approximately $445K.

⸻

XVA Pricing Enhancement:
Enhancements were approved for CVA pricing under Credit Support Agreements (CSAs), specifically allowing the claim of FVA value at default. Key updates include: (1) modeling FVA exposure at default within the same netting node as related trades (previously in a separate node), and (2) increasing the claimable portion (“haircut”) of FVA from 62.5% to 70%. These changes align MTM and FVA when their signs differ and reflect agreed adjustments between Controllers and Trading. For FX Latam counterparties—where CSAs are concentrated—this change resulted in an approximate $14MM increase in XVA exposure on an overall exposure of about $130MM as of May 2, 2025.

⸻

✅ Do you want me to make it even more concise for a regulatory response (shorter paragraphs, less technical jargon), or keep this detailed version but add an executive summary on top?




During Q3, several trading model performance enhancements were implemented that impacted valuation:
	1.	Control Variates (CV) for Monte Carlo Pricer (Multi-Asset Barrier Options):
Model Risk approved the application of control variates within the Monte Carlo pricing framework using local volatility for multi-asset barrier options (Eq MA Barrier). This enhancement is applied exclusively to European-style payoffs. Control variates—European calls, puts, and/or digital options—are selected based on the original option and barrier structures specified in the trade’s payoff. The primary objective is to reduce Monte Carlo variance, particularly for vega sensitivities, thereby improving risk calculation stability. As of May 30, 2025, the cumulative P&L impact from enabling CV functionality was approximately $445K.
	2.	Close-Out Modeling Enhancements for CVA Pricing under CSAs:
Model Risk approved updates to the close-out modeling for CVA calculations where Credit Support Agreements (CSAs) permit claiming of FVA value at default. Key changes include:
	•	(a) FVA exposure at default is now modeled within the same netting node as related trades (previously modeled separately).
	•	(b) The claimable haircut on FVA at default has been revised from 62.5% to 70%, reflecting agreement between Controllers and Trading.

These adjustments ensure consistent alignment of MTM and FVA when their signs differ and update the haircut to match current contractual terms. For FX Latam counterparties as of May 2, 2025, this change resulted in an increase of approximately $14MM on an overall XVA exposure of ~$130MM.




Counterparty Credit Risk (CCR)

There is continued focus on enhancing CCR management capabilities as part of the firm’s ERM uplift plans. Recent approvals include extensions to credit exposure models under stress scenarios to cover (1) all margined funds and (2) all unmargined counterparties firmwide.
Key improvements include updates to margin determination logic, incorporation of client-level defaults, assessment of previously unmodeled risk factors, and strengthened documentation and testing to address validation findings.

Recovery and Resolution Planning (RRP)

Model Risk validated and approved seven Tier 1 models and four qualitative approaches to estimate liquidity needs post-parent bankruptcy and support the firm’s RRP submission to the FRB and FDIC.
Enhancements were driven by FRB feedback on business-level segmentation, validation findings, and developer-identified issues. Outstanding medium-severity findings relate to intraday liquidity risk methodology, unjustified runway assumptions, uncaptured contingent pricing features, and incomplete reflection of recent stressed scenarios in deposit modeling.

Liquid & Readily Marketable (LRM) Classification

Model Risk validated and approved a new qualitative approach for classifying securities as “Liquid & Readily Marketable” for liquidity metrics and capital requirements, improving upon prior simpler methods. All seven high-severity findings were remediated through enhanced analysis and justification of model choices. Medium-severity issues remain, requiring refinements to classification logic, mitigation of unintuitive outcomes, and addressing uncertainty in volume thresholds and Bloomberg data quality.

Asset Secured Lending (ASL)

Development of new models to support ASL continues, with recent approvals of 11 Risk Engineering-owned usages of Facility Level Rating (FLR) models for underwriting. Common outstanding issues include inconsistencies with post-trade model assumptions and required enhancements to documentation, monitoring, and platform user interface






A new model for estimating Delta risk in commodity products, replacing the previous forward difference method with a central difference method for improved accuracy, implemented within the advanced Griffin infrastructure to enhance computational speed.



A new model for estimating Delta risk in commodity products, utilizing a central difference method for improved accuracy, implemented within the advanced Griffin infrastructure to enhance computational speed.


Validation activities during the period primarily focused on:

Risk management enhancements, including approvals of:
	•	An enhancement to the Monte Carlo-based credit contagion model used for calculating Credit Valuation Adjustment (CVA) and gap exposure in secured funding trades. This update allows multiple collateral assets within a single trade and designates a benchmark collateral asset whose default triggers correlated price jumps in other counterparties’ collateral assets. This enhancement captures diversification benefits and collateral default correlations, supports multiple CVA bookings within a single trade, and enables gap CVA modeling for secured lending and Total Return Swap (TRS) trades involving portfolios of bonds or loans as collateral.
	•	A new model for estimating Delta risk in commodity products, utilizing a central difference method implemented within the advanced Griffin infrastructure, replacing the previous forward difference method to improve accuracy and computational speed.
	•	Two new models for calculating X-Valuation Adjustment (XVA) on USD-denominated cancellable swaps and Bermudan swaptions, which were previously not modeled.
	•	An enhancement to the multi-asset barrier options pricing model to incorporate control variates (adjustments to align with market prices) for European-type payoffs, thereby reducing Monte Carlo variance and enhancing stability in risk calculations.
	•	Enhancements to the electricity price prediction model, including adjustments to load inputs accounting for load ramp-up periods, input restrictions to mitigate outlier impacts, and unified battery dispatch post-load adjustment to ensure consistency across prediction blocks.

Counterparty Credit Risk (CCR) model enhancements, including recent approvals of:
	•	Migration of the Equities franchise business to the Unified Benchmark Model for margin shortfall calculations, following the earlier migration of Synthetic Products Group (SPG) portfolios, supporting ongoing standardization and consistency efforts across Prime and Franchise businesses.
	•	An enhancement to the Prime Brokerage (PB) SPIRE margin model, now incorporating eligible bank loans into worst-case loss calculations, previously benchmarked at 100% of market value for all bank loans.
	•	Additional improvements to margin shortfall modeling, including collateral inclusion, repurchase agreement treatment, recalibration of interest rate shocks, and migration of the franchise credit model to the “V30” version, addressing model validation findings.

London Interbank Offered Rate (LIBOR) transition-related enhancements, including:
	•	Approval of fallback logic for trades linked to the Israel Tel Aviv Inter-Bank Offered Rate, now referencing the Shekel Overnight Interest Rate (SHIR) plus a fixed spread.




An enhancement to the Monte Carlo-based credit contagion model for calculating Credit Valuation Adjustment (CVA) and gap exposure in secured funding trades, allowing multiple collateral assets in a single trade and the designation of a benchmark collateral whose default triggers correlated price jumps among other collateral assets.

This enhancement captures diversification benefits and default correlations among collateral assets, supports multiple CVA bookings within a single trade, and enables modeling of gap CVA for secured lending and Total Return Swap (TRS) trades involving portfolios of bonds or loans as collateral.




An enhancement to the Monte Carlo-based credit contagion model for calculating Credit Valuation Adjustment (CVA) and gap exposure in secured funding trades. The update allows multiple collaterals in a single trade and designates a benchmark credit name whose default triggers correlated defaults among other collateral names.
This enhancement captures diversification benefits and correlations between collateral defaults, supports multiple CVA bookings in a single off-balance sheet trade, and enables modeling gap CVA for secured lending and Total Return Swap (TRS) trades involving portfolios of bonds or loans for both private credit SPVs and on-balance sheet lending.





Artificial Intelligence (AI) / Machine Learning (ML) Models

There continues to be significant growth in the development and adoption of AI/ML models, including recent approvals and implementations.

Non-generative AI models:
	•	The first Tier 2 transformer-based deep learning neural network model, developed to analyze FX trading data, predict price movement directions for major currency pairs, and dynamically adjust bid-offer spreads in FX algorithmic trading.
	•	A new Tier 2 Global Banking & Markets (GBM) public neural network model, designed to calculate valuation adjustment charges for multi-asset snowball autocallables, expanding the coverage of the Agni fast pricer suite across FX and Equities, while significantly reducing computational time.

Enhancements to the GS AI Platform monitoring framework:
	•	Improvements addressing model validation findings, including advanced detection of hallucinations and enhanced performance when analyzing longer documents.
	•	The model detects potentially unsafe interactions with large language models (LLMs), specifically targeting issues such as hallucinations, profanity, prompt injection, and exposure of personally identifiable information.

Generative AI productivity tools utilizing Large Language Models (LLMs):
	•	Tier 2 Engineering models developed to (1) summarize trends and patterns from equity market data, news articles, and industry research and (2) extract and validate Net Asset Values (NAV) from externally administered investment financial documents.
	•	Tier 3 Global Banking & Markets (GBM) models designed to (1) convert natural language queries into relevant market data series and visualizations and (2) summarize earnings call transcripts to support investment banking activities.
	•	Tier 3 Asset & Wealth Management (AWM) models used to (1) evaluate portfolio exposure to specific themes such as tariffs, inflation, or AI and (2) respond to advisors’ queries by selecting and presenting the most relevant Private Wealth Management (PWM) content.
	•	A Tier 3 Global Investment Research (GIR) model developed to contextually reorder search results to enhance relevance and usability.





Certainly! Here’s a refined version with improved clarity and flow, while preserving your original structure and content:

⸻

Artificial Intelligence (AI) / Machine Learning (ML) Models
There continues to be growth in the development of AI/ML models and adoption of new techniques, including the recent approval of the following:

Non-generative AI models, including:
	•	A Tier 2 deep learning neural network (transformer)-based AI signal, trained on FX trading data to predict directional price movements for a basket of major FX currency pairs, used to dynamically adjust bid-offer spreads in FX algorithmic trading.
	•	A new Tier 2 Global Banking & Markets (GBM) Public neural network-based model, designed to calculate valuation adjustment charges for multi-asset snowball autocallables, expanding the Agni fast pricer suite across FX and Equities while significantly reducing computational time.

Enhancements to the GS AI Platform monitoring framework
	•	Improvements address prior model validation findings and enhance hallucination detection, particularly in longer documents.
	•	The model continues to monitor and flag unsafe interactions between users and LLMs, including hallucinations, profanity, prompt injection, and exposure of personally identifiable information.

Generative AI productivity tools leveraging large language models (LLMs), including:
	•	Tier 2 Engineering models that (1) identify trends and patterns in equity market data, news articles, and industry research, and (2) extract and verify Net Asset Value (NAV) of externally administered investments from financial documents.
	•	Tier 3 GBM models that (1) translate natural language queries into market data series and visualizations, and (2) summarize earnings call transcripts for investment bankers.
	•	Tier 3 Asset & Wealth Management (AWM) models that (1) assess portfolio exposures to specific themes such as tariffs, inflation, or AI, and (2) respond to advisor queries using AI to retrieve the most relevant content from Private Wealth Management (PWM) materials.
	•	A Tier 3 Global Investment Research (GIR) model that reorders search results contextually based on relevance, improving both usability and informational value.

⸻

Let me know if you’d like this reformatted for a slide or summary version.






Guardrail Model Enhancements

MRM approved a significant upgrade to the Guardrail Model (now Tier 1) used to safeguard the firm’s Generative AI platform, including real-time hallucination blocking capabilities. This marks a transition from a monitoring-only tool to a preventative control.

Key improvements in the newly validated Guardrail 3.0 include:
	•	Enhanced detection of hallucinations and prompt injection
	•	Improved processing of long documents
	•	Integration of a new LLM with better reasoning capabilities
	•	Expansion of the training dataset for broader coverage

Since the model’s initial approval in early 2024, MRM has raised 16 findings across the Guardrail family (covering hallucinations, bias, prompt injection, PII, and unsafe use), with 13 already remediated — resulting in measurable performance gains.

MRM’s validation included independent benchmarking against Guardrail 2.0. One Sev2 finding was raised regarding limited ability to retrieve and synthesize information across multiple documents, requiring further enhancement.

Despite progress, MRM continues to monitor three key limitations:
	•	21.6% of hallucinations remain undetected
	•	Detection may be biased by the LLM’s own stereotypes
	•	Performance degrades in tasks requiring logical inference or big-picture understanding




Trade Description:

Goldman Sachs intends to acquire bilaterally a Mandatory Exchangeable Bond (MEB) from an issuer, collateralized by a pledged share position. Economically, the trade resembles a funded equity collar, with embedded structuring features including:
	•	An averaging period for final settlement (similar to a tranched collar),
	•	A voluntary acceleration right allowing the issuer to settle early,
	•	Reverse Asian-style payoff elements, including a daily cap/floor and harmonic mean calculation.

Key Terms:
	•	Notional: ~$300 million USD
	•	Maturity: 4.5 months from trade date
	•	Target Return: ≥3.5% pre-fee (with potential for ~2% fee uplift via GBM Private)


					      
					      Reason for Waiver:
The current booking model (Eq CASB Threshold) does not support all features required for this trade—specifically, it lacks functionality for:
	•	Reverse averaging (reverse ASB),
	•	Daily cap/floor, and
	•	Harmonic mean averaging.

Booking Approach During Waiver Period:
	•	Trade will be booked under Eq CASB Threshold, wrapped via SP Shadow, which will represent all features except daily cap/floor and harmonic mean.
	•	Reverse ASB support will be enabled in production under the waiver.
	•	Local code modifications will be used to approximate P&L and Greeks, which will be taken into account in trading’s risk management.

Model Enhancement Plan:
	•	Full support for daily cap/floor and harmonic mean averaging will be added to Eq CASB Threshold during the waiver period.
	•	Enhancements will be documented and submitted for model approval and deployment post-trade.





Trade Description:

The proposed transaction is a 5-year Contractual Dividend Autocallable on a worst-of basket of South African bank stocks (ABG1.J, NEDJ.J, OMUJ.J) with a notional equivalent of approximately $15 million (3 tranches of ZAR 90 million each). The trade is structured to pay fixed dividends and includes an Asian-style observation feature for autocall triggers, intended to mitigate liquidity concerns around spot fixing on observation dates.

This trade combines two features—fixed dividend handling and Asianing of autocall observations—which are individually supported in existing tradeable templates:
	•	EQ Auto Callable MA supports Asianing without fixed dividends
	•	EQ Auto Callable MA CS supports fixed dividends without Asianing

However, the system currently does not support both features simultaneously within a single tradeable template, hence the need for a model waiver.

Rationale:
	•	Asianing on autocall observations is introduced to address liquidity challenges in the South African equity market.
	•	Fixed dividend treatment aligns with client expectations and economic modeling assumptions.

Booking Approach:
	•	The trade will be booked initially without the Asianing feature.
	•	If the trade is executed, we plan to implement and stratify a new tradeable version that incorporates both features by the end of this week.
	•	The trade will be rebooked into the updated version once available. The Asianing period spans only a few days and is not expected to materially impact P&L at inception.

Remediation Plan:
	•	Feature enhancement in EQ Auto Callable MA CS to support Asianing will be completed by end of this week.
	•	Full documentation, testing, and submission to MRM for review and model approval will be completed by end of next week.


Transaction Model Waiver Summary

Terms:
	•	Trade Type: Contractual Dividend Autocall on Worst-off South African Banks
	•	Notional: ~$15 million (3 x 90mm ZAR)
	•	Maturity: 5 years
	•	Underliers: ABG1.J, NEDJ.J, OMUJ.J
	•	Expected P&L: ~$1 million
	•	Client: Abax

Economic Description:
	•	Classical Fixed Dividend Autocall structure with the additional Asianing feature for autocall observations. Asianing is introduced to mitigate liquidity concerns.

Reason for Waiver:
	•	Existing tradables separately support autocall with Asianing (eq auto callable ma) and fixed dividend (eq auto callable ma cs), but no single tradable supports both simultaneously. Immediate trading capability required as the transaction is imminent.

Booking During Waiver Period:
	•	Initially booked without the Asianing feature.
	•	The Asianing impact is minimal for the first few days, thus negligible initial impact.
	•	Rebooking planned once the Asianing-enabled strat is available, anticipated by end of the current week.

Compensating Controls:
	•	Implementation of Asianing feature into “EQ Auto Callable ma CS” to be completed by end of this week.
	•	Documentation, testing, and formal submission to Model Risk Management (MRM) to occur by end of next week to remediate the waiver promptly.





Please let me know if any further adjustments are required!
AIL FRAC Breaches Resolved
	•	All remaining breaches have been resolved, including:
	•	4 unvalidated activities
	•	1 rejected activity
	•	1 activity under waiver
	•	20 activities with medium severity findings aged over 6 months
	•	Since ETSC risk metrics were established in FRAC (Oct ’24), all metrics have been reduced to zero

E-trading Policy / Standard Update
	•	The E-trading Policy and Standard have been updated to establish ETSC validation and approval as a standalone requirement
	•	Applies to all new or modified E-trading activities before trading can commence
	•	Formalizes ETSC validation as a parallel process to ATRACG review
	•	Supports greater efficiency in approvals and better aligns with the model validation framework



AIL FRAC Breaches Resolved
All outstanding breaches were resolved, including aged medium-severity items related to E-trading.
Since launching ETSC risk metrics in FRAC in Oct ‘24, we’ve reduced all key breach categories to zero:
	•	Unvalidated Activities: 4 → 0
	•	Rejected Activities: 1 → 0
	•	Activities under Waivers: 1 → 0
	•	Aged Medium Severity Findings (>6 months): 20 → 0

E-trading Policy / Standard Update
The policy now requires ETSC validation and approval for all new or modified E-trading activities before trading begins.
This formalizes ETSC as an independent approval path alongside ATRACG, improving efficiency and aligning with model validation practices.


CRO Update

Top of Mind
	•	RCSA: Central guidance for divisions approved today by the Model Risk Control Committee (MRCC).
	•	IDR Assessments: Wrapping up assessments; thematic finding raised regarding timely remediation of GBM validation findings.

Artificial Intelligence
	•	Loans AI: Leveraging Large Language Models (LLMs) to classify loan proceeds as “credit” or “liquidity” for 6G reporting.
	•	Validation in progress following AIRCC’s conditional approval, pending verification of testing data and alignment with ORR leadership.
	•	Current accuracy stands at 95%, with 16% flagged for human review and approximately 12.5% disagreement between AI and human evaluations.
	•	Consistency remains a concern; around 10% of classifications vary upon retesting. Remediation underway to address this before the November regulatory deadline.

Regulatory Updates
	•	MRM MRA Remediation: On track with infrastructure improvements and training scheduled for completion by September 30, ahead of the rollout of the enhanced annual review framework.
	•	ACL MRIA/MRA Remediation: Submitted required materials to the FRB addressing ACL MRIA 1 (Inadequate Risk Capture and Ongoing Monitoring for ACL Models) and MRA 2 (Weaknesses in Model Risk Management).
	•	Submitted documents include model and validation reports, ongoing monitoring updates, policies and templates, finding extensions, and MRM reporting materials. Kickoff scheduled for July 21.
	•	AQR Findings: Completed remediation of all four MRM-owned Asset Quality Review (AQR) findings, covering enhancements in GSBE oversight, annual review processes, significant Tier 1 revalidations workflow, and related policies and procedures.





I’ve refined the updates for clarity and conciseness. Let me know if further adjustments are needed!




Loans AI leverages Large Language Models (LLMs) to classify the purpose or use of loan proceeds as either “credit” or “liquidity” for 6G reporting purposes.

Model validation is currently underway, following AIRCC’s conditional approval pending human verification of ground truth data for the testing sample and subsequent discussion with ORR leadership.

The current model demonstrates approximately 95% accuracy, with 16% of loans flagged for human review due to complexity or uncertainty. Within this subset, there is roughly a 12.5% disagreement rate between AI-generated results and human assessments.

Consistency and repeatability remain concerns, as approximately 10% of loan classifications produce different outcomes upon retesting. Remediation efforts are ongoing, targeting resolution before the November regulatory submission deadline.



Halo (Agni Framework) – Summary Updates:
	•	The Agni AI framework is transitioning training responsibilities directly to trading desks, enabling business-specific customization across equities, FX, and bond markets.
	•	Halo aims to enhance adaptability by allowing desks to independently develop tailored AI models, leveraging the core Agni infrastructure provided centrally.


Here’s a simplified version suitable for non-technical readers:

Loans AI – Summary Updates:
	•	Current AI testing shows 95% accuracy overall, with 16% of loans flagged for human review due to complexity or unclear information.
	•	For loans requiring human review, there is around 12.5% disagreement between AI results and human assessments, indicating these loans are generally more challenging.
	•	Consistency remains a concern, as about 10% of loan assessments produce different results when repeated; improvements are underway to resolve these issues before the November regulatory deadline.




Here’s a detailed yet concise summary suitable for the CRO updates based on the last part of the transcript:

CRO Updates:
	•	MRCC and RCSA:
	•	MRCC reviewing the central RCSA guidance, with ongoing discussions about IDDR assessment calibration.
	•	Market Risk showed improved effectiveness in Q2 assessments; GBM continues to lag.
	•	AI and Model Validation:
	•	Validation in progress for Loans AI (mortgage and wholesale loans) targeting resolution of repeatability issues ahead of the November regulatory deadline.
	•	GitHub Copilot and agentic AI implementations progressing, with engineering planning to deploy three agentic use cases by year-end.
	•	Generative AI (Content AI) now active in GIR, improving client search result relevance through contextual reordering.
	•	Remediation and Findings:
	•	Ongoing remediation efforts for ACL RVE and AQR completions are advancing.
	•	Attention required for overdue model validations, ensuring accurate reporting and adherence to newly adjusted timelines.







•	Content AI: GIR portal now leverages Generative AI to contextually reorder search results, enhancing relevance and usability.Loans AI – Summary Updates:
	•	Model accuracy currently at 95%, with 16% of loans requiring human review.
	•	12.5% disagreement rate between AI and human reviewers in the flagged subset.
	•	10% repeatability issue due to code inconsistencies; fixes targeted before November submission.

Loans AI – Summary Updates:
	•	Current testing indicates 95% accuracy for automated AI review, with 16% of loans flagged for human review due to uncertainty or loan complexity.
	•	Of the loans undergoing human review, there is approximately a 12.5% disagreement rate between AI and human assessments, highlighting higher complexity in the manually reviewed subset.
	•	Repeatability remains a key concern, with roughly 10% of classifications switching outcomes upon retesting, primarily due to inconsistent code logic; ongoing development efforts aim to address these issues before the November regulatory submission deadline.






Here is a detailed, structured summary of the provided transcript:

AI Loan Review and Model Accuracy Discussion:
	•	Model Performance:
	•	The AI model accuracy is currently around 95% based on the P-metric.
	•	84% of loans are processed entirely by AI without human review; 16% require human review.
	•	Of the loans reviewed by humans, 12.5% show disagreement between human reviewers and AI results.
	•	Error Rates:
	•	Approximately 3% of total loan processing is incorrect, based on ground-truth validation.
	•	Discrepancy noted: the 16% of loans flagged for review are inherently more complicated, thus having a higher error rate.
	•	Data Sampling and Validation:
	•	Humans performed detailed sampling on 285 loans to estimate error rates.
	•	Clarification was needed about the sampling method as initial understanding was unclear.
	•	Challenges with Repeatability:
	•	There is a significant repeatability issue: approximately 10% of cases flip classification results (e.g., between equity and credit) when tests are repeated multiple times.
	•	Main cause: poorly structured code with redundant logic paths and inconsistent prompt usage.
	•	Developers are actively updating the model, causing instability in the validation results.
	•	Timeline:
	•	Initially, the deadline for Fed submission was set for the end of the month but later extended to November.
	•	An internal push exists to resolve mortgage-related components sooner.
	•	Oversight and Approval:
	•	MRM approval is critical, yet there was confusion about why the DR (Designated Reviewer) was involved.
	•	Normally DR does not directly involve itself in the approval of models validated by MRM.

⸻

MRM and Control Framework Updates:
	•	IDR Control Assessment:
	•	Discussion highlighted significant pushback from business areas regarding IDR control assessments.
	•	Market Risk showed improved performance in Q2, but GBM’s scores remain problematic.
	•	RCSA Assessments:
	•	Assessments were due recently, but operational challenges arose related to permission issues for accessing confidential findings.
	•	Concerns raised about inappropriate modifications made by other teams to the provided metrics and tables.
	•	Emphasized the need for accuracy and consistency in self-assessment reporting.

⸻

AI Developments and Updates:
	•	Generative AI (GenerVI) Implementation:
	•	Implemented in GIR web portal, enhancing relevance by reordering search results contextually.
	•	Positive reception from users with limited resistance from GIR, who generally prefer minimal oversight over their IP.
	•	Copilot and Agentic AI:
	•	Updates provided on GitHub Copilot and agentic AI initiatives.
	•	Engineering planning to roll out 3 agentic use-cases by year-end from a total of 5 candidates.
	•	Agni Framework:
	•	Training ownership of the Agni framework shifting to the trading desks, allowing customized model training across various business areas (equities, FX, bond market).

⸻

Administrative and Reporting Notes:
	•	Metrics and Reporting:
	•	Discussed appropriate coloring schemes for tables and metrics highlighting urgency or overdue items (e.g., white, yellow).
	•	Noted ongoing cleanup efforts for reporting clarity, specifically regarding overdue findings and waiver-related items.
	•	Q2 Updates and Meetings:
	•	Preparation of summaries and bullet points required for Brian and MRCC updates, covering:
	•	MRA remediation status.
	•	MRCC review of central RCSA guidance.
	•	Updates on IDDR and ongoing validation activities.
	•	ACL, RVE (Reserve Verification Exam), and AQR completion updates.

⸻

Miscellaneous:
	•	Concerns expressed about unclear naming conventions for models (e.g., mortgages, wholesale loans, liquidity).
	•	Brief mention of client-related implications of GIR AI updates, noting that no major complaints or risks emerged from their rollout.

⸻

Key Actions and Next Steps:
	•	Clarify data sampling methods and ensure repeatability issues are resolved before Fed submission deadline.
	•	Reinforce clarity and permissions related to RCSA assessments to prevent inappropriate data modification.
	•	Finalize and clearly document Q2 performance and IDR results for MRCC and Brian updates.
	•	Ensure proper oversight, and accurate documentation is maintained as model updates continue, especially regarding AI loan reviews.






Key drivers of ongoing validation work:
AI continues to show growth, with increasing adoption of new techniques that present novel risks. This spans both the generative AI space—such as enhancements to the Guardrails model, which supports the GS AI Platform monitoring framework—and the non-generative space, highlighted by the first deep learning neural network-based model deployed for algorithmic trading.
Strategic enhancements to risk management capabilities, particularly in counterparty credit risk, remain a focus as part of the firm’s ERMF uplift plans and efforts to address model validation findings.
Additional drivers relate to the firm’s regulatory capital and liquidity requirements, which continue to shape validation priorities.
A key area of focus for 2025 is the planned enhancement of the annual review process to address supervisory feedback. The associated remediation remains on track for year-end completion.






Thanks for the clear feedback. Here’s a revised version of the callout box, incorporating all your points:

⸻

The firm’s AI governance framework builds on and complements existing model risk management practices. All AI is included in the model inventory to ensure appropriate governance standards are applied.

AI use cases are classified into model risk tiers, which determine the scope and intensity of applicable controls. All AI use cases are treated as individual models and require Model Risk validation and approval prior to use.

While AI-related models continue to grow in number, they remain a small portion of the overall model inventory and are primarily concentrated in lower risk tiers.

⸻

Let me know if you’d like a more concise version or to tailor it for a specific format (e.g., memo, slide, report).




The firm’s AI governance framework is built on—and complements—the existing model risk management framework. As AI adoption continues to grow significantly across business lines, the framework ensures consistent oversight through model inventory, tiering, and validation standards.

	Here’s a refined and more concise version of your bullet points:
	•	The firm’s AI governance framework builds upon and complements the existing model risk management framework.
	•	Per the Firmwide Policy on Artificial Intelligence, all AI platforms, applications, and their specific use cases must be captured in the firmwide model inventory and included in the quarterly attestation process to ensure completeness and accuracy.
	•	To strengthen oversight and ensure consistent governance of AI use, Model Risk enhanced the control framework in late 2023 to:
– Align the definition of AI with the Firmwide Policy and mandate its inclusion in the model inventory
– Introduce a Tier 4 model risk classification to cover very low-risk AI use cases that were not previously in scope
	•	All AI use cases are treated as individual models and are subject to Model Risk Management (MRM) validation, in line with the firm’s standards for model approval.Enhancements to margin shortfall modeling, such as (1) inclusion of collateral in the worst-case loss and shortfall calculations for CREST Derivative Clearing Services (DCS) and Futures business to capture risk more accurately, and (2) methodology enhancements to address validation findings relating to the treatment of triparty repos and recalibration of interest rate shocks in shortfall




We presented 10 real-life approval/rejection case studies and, in partnership with Engineering, GBM, and AWM, showcased four strong first-line use cases.



Here’s a detailed summary of the transcript, organized clearly by topic, including all discussion points and additional items intended for Brian’s updates:

⸻

Topics Discussed for Brian’s Update:

1. MRA Remediation
	•	Included, but limited updates available.
	•	Mention tech-related questions circulating regarding the practical implementation process.

2. ER Mesh Uplift
	•	Plans for 2025: Establish a centralized Assessment Unit (AU) for firmwide programs such as Model Risk.
	•	Highlight that the current effectiveness metrics were set intentionally harshly, resulting in many “reds,” even in IDDR areas.
	•	Potential feedback from GBM anticipated due to these strict ratings.
	•	Important to verify Brian’s comfort level with the severity calibration; emphasize that CCR metrics currently appear worst-performing, potentially prompting a recalibration.

3. Control Effectiveness Finalization
	•	Finalization expected this or early next week, but possible delays due to unclear accountability within O-Risk.

4. Encouraging Self-Identified Issues
	•	Discuss with Brian the idea of promoting self-raised issues (thematic findings) by business lines.
	•	Clarify how this would interact with credit received under the RCSA process.

5. LRM and ETSC Updates
	•	Confirm LRM model approval completion.
	•	Clarify the governance around ETSC, as there’s uncertainty if controls are centrally imposed by Compliance or Risk.
	•	Need to discuss with Compliance whether ETSC controls should be standardized and centrally imposed, possibly enhancing consistency in governance.

6. Validation Findings and Metrics
	•	For recent major validations (Items C and D), highlight the notably large number of findings identified.
	•	Emphasize these as indicators of poor model-development practices, reinforcing the need for stronger upfront controls.

7. AI Models and LLM Versioning
	•	Discuss concerns related to frequent LLM version updates (e.g., OpenAI moving from 4.0 to 4.1).
	•	Suggest a more scalable solution, potentially through automated testing like “AI regression tests,” run by the first line.
	•	Emphasize first-line responsibility for ongoing tests, with second-line focusing on ensuring the testing program itself remains robust.
	•	Propose that frequent LLM updates (every 2-3 months) need automated handling rather than manual re-validation approvals.

8. AI Code Repositories and Development Practices
	•	Highlight concerns over fragmentation in AI development practices (e.g., multiple repositories with differing library versions, reduced visibility, and inconsistent testing practices).
	•	Emphasize the importance of maintaining transparency and open-code testing, akin to historical Goldman Sachs practices (e.g., STV’s success).
	•	Flag concerns around proprietary patents filed by GBM and Engineering, possibly creating silos and further complicating transparency and validation efficiency.

9. GSI/GSIB Board Updates
	•	Include updates related to Brian’s role on the GSIB board.
	•	Mention any significant updates from the GSI and GSIB board meetings.

10. Training and Issues Management Terminology
	•	Clarify confusion around “issues management” terminology, as current terminology is creating unnecessary ambiguity internally and externally.
	•	Highlight MRM-specific items relevant to MRAs, especially weaknesses in validation practices and findings management.

11. SR Inventory Completeness Feedback
	•	Note concerns raised by SR about the completeness of model inventories, specifically the Controllers’ decision to exclude certain risks (e.g., strategic or business risk) from capital calculations without a documented methodology.
	•	Clarify ECB’s recommendation: even decisions not to calculate capital (effectively “zero capital”) should be formally documented in inventory.
	•	Consider raising thematic findings against Controllers for not fully ensuring completeness in inventory identification processes.

12. EMA Updates
	•	Include updates on upcoming EMA items:
	•	AQR (Asset Quality Review)
	•	ProVal model updates
	•	UK ICAP completion
	•	Recent ECB submission adjustments (residual risk reclassification from DRC to qualitative approaches).
	•	Mention upcoming EY audit for Purely PSM, noting it will significantly involve MRM documentation review.
	•	Flag differences in regulatory compliance notification responsibility in MRM for UK entities versus the global group.

13. EmoLex DVA Error
	•	Confirm if EmoLex DVA error warrants a formal mention or escalation.

⸻

Additional Items to Include for Brian’s Awareness:
	•	CCR Lotus Completion: Finalize CCR work related to Lotus (including model migration and LRM validation).
	•	AI Committee Meeting Updates: Recent approvals and ongoing issues related to AI/ML models.
	•	Validation Activities: Updates on CCR equities migration to the unified benchmark model and completion of UK ICAP.
	•	Regulatory Updates: MRAs and ongoing CECL model validations.

⸻

Next Steps:
	•	Clarify accountability and timelines for control effectiveness reviews.
	•	Confirm Brian’s comfort level with the severity calibration of model control effectiveness ratings.
	•	Pursue clarification from Compliance on centralized control imposition for ETSC.
	•	Implement scalable testing solutions for managing frequent AI/LLM updates.
	•	Consider a thematic finding on Controllers regarding inventory completeness issues.
	•	Verify and clearly document the ECB’s expectations for model inventory completeness and zero-capital approaches.

This structured summary should provide clear guidance for preparing Brian’s updates and next steps for addressing identified issues.










Sure, here’s a simplified and clearer version:

Firmwide AI/ML Development Training 2025:
MRM organized a training program for all AI/ML developers to promote best practices, improve model quality, and support more efficient reviews.
The session included 10 real-life approval/rejection case studies and featured four strong first-line use cases in partnership with Engineering, GBM, and AWM.
Firmwide AI/ML applications grew to ~200, and the number of model owners increased from ~200 to 300 over the past nine months, reflecting growing interest and engagement.Liquidity Risk Enhancements: Validation efforts continue to focus on improving liquidity risk models. Recent key approvals include a new qualitative approach for classifying liquid and readily-marketable (LRM) assets, aimed at optimizing capital and liquidity metrics, reducing risk-weighted asset (RWA) requirements, and meeting regulatory expectations, as well as models and qualitative approaches supporting our Recovery and Resolution Planning (RRP) submissions to the Federal Reserve Board (FRB) and Federal Deposit Insurance Corporation (FDIC).




Enhancements to the models used for calculating credit exposure under stress scenarios, extending coverage from hedge funds to all margined funds and firmwide unmargined counterparties within the natural resources industry.
	•	Migration of equities franchise business to the Unified Benchmark Model for calculating margin shortfall, aligning with broader ongoing efforts to standardize and ensure consistency across Prime and Franchise businesses.Artificial Intelligence (AI)/Machine Learning (ML) Models: We continue to see significant growth in AI/ML model development and the adoption of new technologies. Recent notable approvals include:
	•	The first AI model utilizing transformer-based deep learning techniques to predict price movements for FX algorithmic trading.
	•	Expansion of our neural network-based pricing tool to include multi-asset structured products.
	•	Enhancements to the generative AI monitoring framework supporting our GS AI Platform, which improves performance, enables the GS AI Assistant to handle multiple document uploads, and provides real-time alerts for detected inaccuracies (pending deployment).

Counterparty Credit Risk (CCR): We remain focused on enhancing and validating our CCR management models in alignment with our Enterprise Risk Management Framework (ERMF) improvement initiatives. Recent significant approvals include:
	•	Extending our stress scenario credit exposure models beyond hedge funds to encompass all margined funds and firmwide unmargined counterparties within natural resources.
	•	Transitioning our equities franchise business to the Unified Benchmark Model, standardizing margin shortfall calculations and ensuring consistency across our Prime and Franchise operations.

Liquidity Risk Enhancements: Validation efforts continue to focus on improving liquidity risk models. Recent key approvals include:
	•	A new qualitative approach for classifying liquid and readily-marketable (LRM) assets, aimed at optimizing capital and liquidity metrics, reducing risk-weighted asset (RWA) requirements, and meeting regulatory expectations.
	•	Models and qualitative approaches supporting our Recovery and Resolution Planning (RRP) submissions to the Federal Reserve Board (FRB) and Federal Deposit Insurance Corporation (FDIC).



Does this revised draft meet your needs, or would you like further Model sensitivity noted regarding “high trading volume” thresholds and Bloomberg data quality, with future enhancements planned to refine classifications and address unintuitive outcomes.




Weekly CRO Update

Top of Mind

CCR Validations:
	•	Coherent Shortfall Model: Validation completed ahead of the June 30 Lotus deadline.
	•	Model scope extended from hedge fund clients to all margined funds.
	•	Six new medium-severity findings identified, addressing unjustified parameters, modeling choices, unidentified risk factors, testing deficiencies, and gaps in ongoing monitoring.
	•	Stressed CCE Model: Extended validation completed ahead of the deadline.
	•	Scope expanded from unmargined natural resources counterparties to firmwide implementation.
	•	Four new medium-severity findings noted, focused on implementation issues and ongoing monitoring gaps.

Liquid & Readily-Marketable (LRM) Classification:
	•	Validation completed prior to June 30 commitment.
	•	Successfully remediated all seven high-severity findings relating to insufficient development evidence, implementation, testing, and documentation.
	•	Model sensitivity noted regarding the threshold determination for “high trading volume” and dependency on Bloomberg data quality. Future enhancements planned to refine Equities classification and address unintuitive outcomes (low materiality or overly conservative results).

⸻

Validation Activities

CCR:
	•	Migration of Franchise Equity Benchmark Model (FEBM) to Unified Benchmark Model (UBM) approved by MRM for shortfall calculations.
	•	This migration aligns with previous SPG model transitions and contributes to broader standardization and consistency across Prime and Franchise segments.

⸻

Regulatory Updates

MRM MRA Remediation:
	•	On track for completion of infrastructure enhancements and training by September 30, ahead of rolling out the enhanced annual review framework.

CECL RVE Examination:
	•	The FRB initiated validation steps for remediation of existing ACL MRIA1 (Inadequate Risk Capture and Ongoing Monitoring for ACL Models) and MRA2 (Weaknesses in Model Risk Management).
	•	Meetings scheduled to occur over a 3–4 week period from July 15 to August 15, prioritizing Wholesale followed by Retail.






Here’s a detailed summary organized by key points discussed:

1. Personal Updates (Vacation and Family)
	•	Carol recently returned from vacation on the U.S. West Coast.
	•	Traveled to three major cities and five national parks, covering about 3,000 miles.
	•	Carol’s parents enjoyed the trip and have returned safely to Shanghai.
	•	Tried visiting the office on the weekend but forgot passwords, took photos around the building instead.
	•	Mentioned long flights (10 hours to San Francisco and 20+ hours returning from New York).

2. Preparation of BRC Deck and Upcoming Reports
	•	Carol is preparing the BRC deck for review on Monday.
	•	Planning for BRC involves selecting thematic topics rather than deep technical details.
	•	Agreed on major topics for the BRC deck:
	•	AI Guardrail 3.0 (keep thematic, not overly technical)
	•	CCR model enhancements
	•	Liquidity Risk Management (LRM)
	•	Potential inclusion of Resolution and Recovery Plan (RRP) and GSI Trading Wind-down updates
	•	Incremental updates on MRM MRA remediation

3. Updates for Brian and CRO
	•	Brian’s update will include CCR and LRM completions.
	•	Possible inclusion of the recent Op Risk (EMMA equity delta hedging) event.
	•	CRO update may mention CCR and LRM completions and the upcoming validation of CECL MRIA/MRA by the Fed.
	•	GSII Capital review status needs verification with the EM team.

4. Regulatory Interactions and Upcoming Meetings
	•	Discussed regulatory engagements:
	•	Fed topical study explicitly restricted AI and recording tools.
	•	Upcoming regulatory meetings related to trading models scheduled for the end of next month and October.
	•	Preliminary impact analysis for the SLR/LR regulatory changes by the research team.
	•	Potential regulatory finding related to a broken link in a TRC model; the team is currently pushing back.

5. Efficiency and AI Initiatives
	•	Emphasized importance of AI and automation for the second half of the year.
	•	Highlighted need for efficiency improvements and automation in processes, especially:
	•	Reporting workflows (Strat PMMD update, Brian update, and RCSA automation).
	•	Encouraging team experimentation and ideation for practical AI uses.
	•	Mentioned the recent AI Hackathon event that aimed at creating efficient prompt engineering examples.
	•	Carol noted ongoing efforts to automate manual reporting burdens, especially inventory and findings pages.

6. M365 Copilot Functionality and Team’s Transition
	•	Carol and the team expect to receive access to Microsoft 365 Copilot soon.
	•	Discussed anticipated capabilities of Copilot:
	•	Assisting in finding and summarizing emails/documents.
	•	Potential functionalities in Excel and PowerPoint.
	•	Noted feedback from peers about Teams Meetings having significant AI utility (summarizing and transcribing meetings).
	•	Firm may eventually transition from Zoom to Teams Meetings, although there’s uncertainty about confidentiality concerns in regulatory contexts.

7. Planning for the Second Half of the Year
	•	Emphasis on:
	•	AI initiatives and efficiency improvements.
	•	Regulatory interaction skills and preparation.
	•	Scheduled follow-up discussion for further strategic planning.

8. Upcoming Key Dates and Deliverables
	•	BRC on July 31st (first draft due around July 8th).
	•	MRCC meeting scheduled for August 16th.
	•	FRA meeting on August 5th and another critical meeting on August 6th.
	•	Ongoing MRA implementation planning.

Overall Focus:
	•	Prioritizing thematic updates to senior management and board.
	•	Continued focus on AI-driven efficiency enhancements.
	•	Ensuring clear communication and preparedness for regulatory interactions.
	•	Planning ongoing automation and improving processes for reporting and internal operations.





You’re absolutely right — the actual Op Risk event referred to by Youness occurs later in his section and relates to DVA (Debt Valuation Adjustment). Here’s a corrected and focused summary of that specific Op Risk event:

⸻

✅ Operational Risk Event (Youness – DVA Issue)
	•	Event Description:
	•	Two risk-free notes incorrectly showed non-zero DVA exposure.
	•	These trades were expected to have zero DVA, but due to a code logic error, DVA was calculated and booked.
	•	Root Cause:
	•	The DVA calculation relies on a hardcoded filter that excludes certain trades by ID.
	•	These two trades were not added to the exclusion list, so the system treated them as having credit risk.
	•	This resulted in an incorrect DVA of approximately -$3 million being booked.
	•	Discovery:
	•	The issue was identified in Q1 2025.
	•	It was brought to MRM’s attention recently by the desk.
	•	Remediation Actions:
	•	The desk is conducting a global check to ensure no other risk-free notes are impacted.
	•	MRM recommended replacing the hardcoded filter with a systematic, programmatic solution.
	•	The suggestion was also made to reflect risk-free status directly in the trade booking, reducing reliance on manual filters.
	•	Follow-up:
	•	It was unclear during the meeting whether the issue was formally logged as an Op Risk event, but it was flagged as having operational risk implications.
	•	A follow-up was proposed to determine if it should be logged and tracked accordingly.

⸻

Let me know if you’d like this turned into a formal Op Risk event report or if you need other sections summarized.




Here is a bullet-point summary of the Operational Risk (Op Risk) Event spoken by Youness in the transcript:

⸻

Op Risk Event (Youness):
	•	Event Description:
	•	Due to a market move, the 30-year minus 2-year rate spread widened to 50 basis points.
	•	This triggered the early call of about 20 callable range accrual notes that were nearing maturity (within 1–2 years).
	•	Cause:
	•	High spread levels increase the cost of future coupon payments, which made it uneconomical for the firm to continue holding the trades.
	•	As a result, the issuer called the notes early to avoid paying further high coupon costs.
	•	Impact:
	•	The operational event primarily involved trade cancellations to avoid further coupon payments, not a model or system error.
	•	Additional Notes:
	•	The issue was flagged due to financial impact from changing interest rate spreads.
	•	It’s unclear whether this was formally logged as an operational risk event, but a follow-up was requested in the meeting.

⸻

Let me know if you’d like summaries of other speakers or model changes as well.





Yibo Li
200 Angelo Cifelli Dr, Apt 263
Harrison, NJ 07029
Phone: (571) 269-7933
Email: yiboli@gwu.edu

June 1, 2025

To: U.S. Customs and Border Protection

Dear Immigration Officer,

I am writing to confirm that my parents, Mr. Guanyao Li and Mrs. Yafang Li, are visiting the United States as tourists. They hold valid B2 visitor visas and are traveling here to spend time with me, visit multiple cities, and experience American culture.

They are scheduled to stay from June 2, 2025, to June 24, 2025, and have confirmed return flight tickets. During their visit, they will initially stay in San Francisco at the Holiday Inn San Francisco-Golden Gateway, located at 1500 Van Ness Ave, San Francisco, CA 94109, before continuing their travels to other destinations. Later in the trip, they will also stay with me at my residence listed above in New Jersey.

I am currently employed under an H-1B visa at Goldman Sachs in New York City. I will be fully responsible for their accommodation and daily living expenses throughout their visit. They do not intend to work, study, or remain in the U.S. beyond their authorized stay.

As they do not speak English, I kindly request your patience and understanding during their entry process. The details of their return flight itinerary are included on the following page for your reference.

If you need any further information, please feel free to contact me using the information provided above.

Thank you very much for your time and assistance.

Sincerely,
(signature if printed)
Yibo Li


Travel Itinerary for Mr. Guanyao Li and Mrs. Yafang Li
U.S. Visit: June 2, 2025 – June 24, 2025

June 2 – Arrival flight: PVG → SFO, arriving at 9:05 AM
Stay in San Francisco, California

June 3 – Stay in San Francisco, California

June 4 – Travel from San Francisco to San Luis Obispo, California

June 5 – Travel from San Luis Obispo to Los Angeles, California

June 6 – Stay in Los Angeles, California

June 7 – Travel from Los Angeles to Las Vegas, Nevada

June 8 – Travel from Las Vegas to Zion National Park, Utah

June 9 – Travel from Zion to Bryce Canyon to Page, Arizona

June 10 – Travel from Page to Grand Canyon South Rim, Arizona

June 11 – Travel from Grand Canyon to Las Vegas, Nevada

June 12 – Travel from Las Vegas to Fresno, California via Death Valley

June 13 – Travel from Fresno to San Francisco, California via Yosemite

June 14 – Fly from San Francisco to New York

June 15–23 – Stay in Harrison, New Jersey
Address: 200 Angelo Cifelli Dr, Apt 263, Harrison, NJ 07029
June 24 – Return flight: JFK → PVG







Here’s a clearer and more concise version of your update:

⸻

Artificial Intelligence Updates
	•	Graph Retriever Model: Approved for retrieving relevant data from knowledge graphs to support Q&A on MD Bios. The model improves semantic search by leveraging structured relationships and contextual understanding. Benchmarking against MRM models confirmed its robustness, though two findings were raised on insufficient ongoing monitoring and code control.
	•	Agni Snowball Autocallables: The neural network-based fast pricer and RFQ tool has been extended to support multi-asset underliers, expanding the Agni suite beyond last year’s single-asset approval. Four medium-severity findings were raised, primarily concerning model performance and implementation.








Here is a draft for the second page summary on how model risk is incorporated into the RCSA (Risk and Control Self-Assessment), including definitions, assessment steps, and implications of ineffective controls:

⸻

RCSA Model Risk Assessment Summary

Background

Model Risk is formally integrated into the Risk and Control Self-Assessment (RCSA) process under the GBM Public Strats Assessment Unit (AU), specifically within the “Develop & Maintain Models” process. This includes two key model risk types:
	•	Risk 1: Incorrect Model Design / Implementation
	•	Risk 2: Incorrect or Inappropriate Model Usage

Each risk is assessed across defined control suites, with resulting ratings impacting firmwide risk visibility and action plans.

⸻

Definitions of Key Terms
	•	IRR (Inherent Risk Rating): The level of risk present assuming no controls are in place.
	•	CSR (Control Suite Rating): An aggregate control effectiveness rating derived from the effectiveness of individual controls.
	•	RRR (Residual Risk Rating): The remaining level of risk after controls have been applied. It is a function of both IRR and CSR.

⸻

Assessment Steps
	1.	Inherent Risk Rating (IRR):
Each model-related risk is evaluated based on its potential impact and likelihood, assuming no controls are present. Both risks currently carry a High IRR.
	2.	Control Rating:
Each control associated with the risk is individually rated as:
	•	Fully Effective
	•	Adequately Effective
	•	Ineffective
	3.	Control Suite Rating (CSR):
The CSR is calculated based on thresholds:
	•	Fully Effective: ≥70% of controls are Fully Effective and <15% are Ineffective
	•	Adequately Effective: Combined (FE + AE) ≥85%, with FE <70% and IE <15%
	•	Ineffective: ≥15% of controls are Ineffective
	4.	AU Assessment / Residual Risk Rating (RRR):
Based on the CSR and IRR, the residual risk is mapped using the RRR matrix. For example:
	•	R1 (with a CSR of Ineffective and IRR of High) results in a High RRR
	•	R2 (with a CSR of Fully Effective and IRR of High) results in a Low RRR

⸻

Implications of Ineffective Controls
	•	Risks assessed with Ineffective CSR lead to formal Issues being raised.
	•	These issues are recorded as Thematic Findings in ModelIT, which automatically feeds into Enterprise Issue Repository (EIR) for central issue tracking, governance, and remediation oversight.

⸻

Let me know if you’d like this in presentation format or want to include visual excerpts from the image.






Here’s the detailed methodology and a downloadable Excel-style table shown above:

⸻

🧮 Detailed RCSA Model Control Rating Methodology (3-Point Weighted)

Step 1: Input Data Structure

Each Assessment Unit (AU) includes:
	•	Number of models
	•	Three control effectiveness ratings:
	•	Model Development Control
	•	Model Change Control
	•	Model Ongoing Monitoring Control

Step 2: Convert Ratings to Numeric Scale

We assign a numeric score for qualitative control ratings:

Rating Label	Numeric Score
Ineffective	1
Adequately Effective	2
Fully Effective	3

Step 3: Compute Average Score per AU

\text{Average Control Score}_{AU} = \frac{\text{Dev Score} + \text{Change Score} + \text{Monitoring Score}}{3}

Step 4: Apply Model Weighting

\text{Weighted Control Score}_{AU} = \text{Average Score} \times \text{# Models}

\text{Overall Weighted Score} = \frac{\sum (\text{Weighted Control Score})}{\sum (\text{# Models})}

Step 5: Map Overall Score to Qualitative Rating

Weighted Score Range	Final Rating
1.00 – 1.66	Ineffective
1.67 – 2.33	Adequately Effective
2.34 – 3.00	Fully Effective


⸻

The displayed table shows:
	•	Each AU’s scores
	•	The model-weighted contribution
	•	A calculated final qualitative rating
	•	A summary row with the overall weighted rating

Let me know if you’d like this exported as an Excel file or extended to include more AUs. ￼





Here’s a trimmed and simplified version of your update:

Resolution Recovery Plan (RRP):
MRM approved seven Tier 1 models and four Tier A qualitative approaches for the RRP Title 1 bi-annual submission. Key enhancements included:
	•	Business-level segmentation for trading wind-down in response to FRB feedback
	•	Alignment of intercompany repo/reverse repo treatment with Modeled Liquidity Outflow (MLO), following a reassessment by modelers and MRM
	•	Additional updates based on MRM findings and developer-identified issues, including alignment of runway assumptions with MLO
	
		
			
				
					
							•	Resolution Recovery Plan (RRP):
	•	MRM validated and approved 7 Tier 1 models and 4 Tier A qualitative approaches, including 2 initial validations, for the RRP Title 1 bi-annual submission.
	•	Key enhancements included:
	•	Added business-level segmentation for trading wind-down, addressing FRB feedback, resulting in a $9bn reduction in Peak Funding Need (PFN).
	•	Implemented various improvements and bug fixes based on MRM findings and developer self-identified issues.
	•	Adjusted treatment of intercompany repo/reverse repos to align with MLO, reducing PFN by $10bn, which required Board approval due to its impact.
	•	GSI Trading Activity Wind-Down (TWD):
	•	Validated and approved 26 models and 6 qualitative approaches as part of enhancements to comply with PRA’s TWD requirements effective from March 3.
	•	Of 57 findings identified, 26 have been resolved and closed, including all high-severity issues. One qualitative approach is currently under validation and used with a waiver.
	•	Submission to PRA included findings from MRM validations and self-assessment against SS 3/18 model risk management principles.
	•	Held a 4-hour meeting with PRA on May 15, addressing questions on validation approaches and open issues. PRA expects to finalize their review by January.



Here’s a clear, concise draft for the footnote:

Footnote:
For Development Control and Model Control, metrics are calculated based on IR model scope with data as of May 16. For Inventory OM and Change Control, metrics reflect data as of the end of Q1 at the assessment level, not specifically scoped to TI models.




Detailed Transcript Summary

RTSA Results for IDDR Models
	•	Results were presented in a summarized table format, printed concisely onto one page.
	•	Metrics are based on a four-point scale defining thresholds clearly.
	•	Specific clarifications requested:
	•	Footnote required:
	•	Metrics for Development Control and Model Control based on IR model scope data as of May 16.
	•	Inventory OM and Change Control metrics calculated as of end of Q1 at the assessment (uter) level, not scoped specifically to TI models.
	•	The “IDDR” models discussed are a one-time ad hoc exercise for July; thus, additional detailed clarifications for these are unnecessary.
	•	Confirmation that ineffective remediation findings and excessive indicators should not be assumed as fully effective and should be excluded.

Table Ranking and Additional Analysis
	•	Current ranking in tables is based on the number of models.
	•	Received a request from Bill to rank Assessment Units (AUs) by “badness” (risk level).
	•	An additional table will address Bill’s specific request.
	•	The team agreed sorting by number of models is currently practical, pending Bill’s feedback.

Brian’s Update
	•	Progress ongoing; feedback gathering from various stakeholders continues.
	•	Recommendation given to simplify and make internal feedback notes less formal and more direct, highlighting essential actions clearly.
	•	Confirmed the recalibration of the threshold scale from a four-point to a three-point scale may be considered going forward, but verification is required on whether to show Q1 results again using the new scale to Brian, pending Bill’s decision.

Regulatory and Audience-specific Communications
	•	Acknowledgment that updates for Brian should differ significantly from broader audience updates.
	•	Communication to general stakeholders (excluding detailed audience like Alex, Bryant, Gopi, who have already received extensive information) needs to be concise, high-level, and clear.
	•	Main points for the broader audience include:
	•	Enhancements reviewed positively with the Fed and MRCC.
	•	Next steps clearly outlined.
	•	Simplified bullet points recommended for communicating Fed feedback.

Additional Suggested Topics
	•	ERMF uplift: Include recalibration to a three-point scale and preliminary results on model risk metrics.
	•	Regulatory updates: Briefly mention ongoing initiatives:
	•	Capital model approval requests.
	•	Preparations for the 2025 examinations.

Next Steps
	•	Aim to finalize a clear and concise draft for Brian’s update by the following morning.





Please review and let me know if any adjustments are needed!




Here’s the simplified and refined summary:

AI Guardrail 3.0: MRM has approved the enhanced AI Guardrail 3.0 (Tier-1), enabling the GS AI Assistant to handle larger and multiple documents, supporting up to 500,000 tokens (~750 pages). Guardrails include both monitoring and preventative controls, applicable across the firmwide AI platform. A new feature is under development to indicate hallucinated content to users before enabling preventative blocking.

AI FX Algo Trading Signal: MRM approved a transformer-based AI model for the FX eDealing Client Pricing algorithm, enhancing the FX algorithmic market-making business. The model effectively predicts the direction of price movements for a basket of major FX currency pairs, demonstrating strong performance in high-frequency trading scenarios.




Sure, here’s a concise version in two sentences:

Assessment Units are ranked from worst to best based on the number of Ineffective ratings, followed by Adequately Effective ratings. If there is a tie, the unit with more models is ranked worse.





Here’s a structured summary for Brian’s update based on the provided discussion transcript:

1. MRM / MRA Remediation
	•	Update Brian on the recent Fed meeting outcomes and immediate next steps.
	•	MRCC review scheduled before Thursday; highlight importance of MRCC engagement given the substantial nature of framework changes.
	•	Plan to distribute review materials to MRCC today to encourage pre-meeting familiarization.

2. Enterprise Metrics Framework (EMF) Uplift
	•	Progressing on using a three-point scale for IDR (Issue, Deficiency, and Risk) areas; summary to be prepared in Brian’s preferred new format.
	•	Solicit Brian’s view on consistency between three-point vs. four-point scales across different areas (e.g., issues management vs. RCSA).
	•	Consider additional metrics for tracking, e.g., attestation lateness.
	•	Initiate preliminary discussions on metrics for Electronic Trading Supervision and Control (ETSC), to be established by year-end.
	•	Clarify current state and completeness of the risk taxonomy, specifically regarding electronic trading risks and associated control effectiveness metrics.

3. ERM and Breach Response Plan
	•	Provide status update on the breach response plan submissions to FRAC (Financial Risk and Control Committee).
	•	Start with weekly updates on breach response submissions, transitioning to bi-weekly once established processes stabilize.

4. EMEA Capital Governance
	•	Summarize key points from Simon’s planned EMEA capital governance sessions, noting current delay/rescheduling.
	•	Outline intended discussion topics clearly for Brian’s concurrence.

5. EMEA Data Governance (DGO)
	•	Recap previous skepticism from Brian regarding the materiality of perceived gaps.
	•	Provide update on recent gap assessment by KPMG, specifically their findings on data usage in model development/calibration.
	•	Clarify KPMG’s involvement scope and the sponsoring party for their assessment.

6. CCR (Counterparty Credit Risk)
	•	Provide updates on recent validations and findings.
	•	Highlight status on larger, firm-wide CCR model projects.
	•	Prepare explanations addressing Brian’s consistent concern about delays, particularly focusing on historical context rather than recent extensions.

7. Resolution Planning
	•	Summarize internal audit (IA) findings related to implementation review obligations for QA (Quality Assurance) tasks.
	•	Propose approach to manage the transfer of these tasks to the team, focusing on robust implementation validation, following IA’s raised concerns.
	•	Clarify and confirm with Brian and Alex the interpretation and adequacy of current QA policy vs. actual practices.

8. AI / Guardrail Updates
	•	Update Brian on recent Guardrail 3 approval, emphasizing enhancements (improved detection capabilities, explainability, preventative blocking plans).
	•	Provide outlook on testing plans (initially observational, transitioning to preventative blocking).
	•	Discuss preliminary ideas or future roadmap considerations for Guardrail 4 (though currently no defined plans exist).

9. Copilot and Generative AI Tools
	•	Inform Brian on the pilot rollout of Microsoft 365 Copilot, highlighting user feedback on interface convenience and general usability.
	•	Provide updates on the streamlined approval of Anthropic as an additional LLM provider.
	•	Briefly note recent IRCC discussions and debates around AI implementations, control vs. engineering perspectives.
	•	Mention upcoming FRB AI-focused meeting (June 18); seek attendee list clarification.

10. Pricing Models / Market Risk Updates
	•	Review current discussions with market risk specialists, particularly:
	•	Positional stress tests around funding spreads in equities.
	•	Private equity valuation discrepancies, especially in tech and fintech sectors.
	•	Verify with specialists if current developments warrant Brian’s attention from a model risk perspective.

11. Electronic Trading Incident
	•	Detail recent critical issue in Equity Delta Hedging Facility (EDHF) involving stale risk data caused by overloaded servers.
	•	Clearly explain the risks posed by incorrect hedging, implications if incident duration was longer, and highlight gaps in existing controls.
	•	Propose steps for deeper analysis and possibly enhancing electronic trading control infrastructure.

12. Other Regular Updates
	•	Highlight recent validation of pricing models, if noteworthy.
	•	Include brief mention of the National Futures Association (NFA) updates, subtly indicating ongoing irritations/issues without explicit detail.

13. MRCC Administrative Items
	•	Announce upcoming MRCC membership changes (Ken leaving; additions include Giuseppe, David Jeria, Ariana).

This structured outline captures all major topics discussed, clearly delineating items to update Brian on, questions requiring his input, and key points needing further action or clarification.















Here’s a detailed summary of key items to include for Brian’s update and the Alex/CRO update based on the provided transcript:

For Brian’s Update:
	•	ERMF Uplift: Include detailed updates on the Enterprise Risk Management Framework (ERMF).
	•	DRC Program: Summarize key issues regarding the DRC extension, including uncertainties around capital governance, regulatory implications, and proposed paths forward.
	•	Capital Governance: Emphasize the proposed approach involving three key programs: M&T (Model & Testing), Data Governance, and DRC, highlighting Simon’s recommended approach.
	•	CCR (Counterparty Credit Risk): Provide detailed updates, noting that substantial CCR content has not been given recently and should now be addressed.

For Alex/CRO Update:
	•	MRA Remediation: Highlight recent feedback from the Fed meeting, noting particularly positive feedback on the progress and detailed enhancements discussed in MRCC.
	•	AI Guardrail 3.0: Emphasize recent updates or developments, given its importance.
	•	CCAR: Provide any recent updates or notable items, acknowledging that significant changes or updates might be minimal.

General Guidance for Updates:
	•	Include specific summaries where the information is confirmed and clear.
	•	For uncertain topics, use placeholders pending further confirmation or input from Bill.
	•	Clearly highlight the positive feedback from recent regulator interactions to underscore progress.

This structure will ensure both Brian and Alex/CRO updates are comprehensive and aligned with current strategic priorities and recent developments.







Certainly! Here’s a direct quote from the transcript you can include to reflect that addition clearly:

“We’ll also provide you with those MRCC materials once they’re finalized and after the meeting. So you can actually see the exact changes that we’re proposing.”

“We’re also happy to provide you with those examples once they’re ready. And we, of course, would welcome any feedback.”

You can incorporate this into your notes to explicitly document MRM’s offer to share both MRCC materials and annual review mock-up examples once available.



MRM offered to submit finalized MRCC materials following their review meeting, as well as detailed annual review mock-up examples once ready. These materials aim to clearly demonstrate the proposed changes and enhancements to the regulator, and feedback was specifically invited.






Does this structured summary meet your expectations, or would you like any refinements?

Meeting Minutes – Regulator Meeting

Invalidated and Rejected Models:
	•	Regulator inquired about unvalidated models in use and whether there were thematic issues.
	•	MRM responded:
	•	Tier 1 Models: Utilization is low, mainly due to significant model changes implemented before validation.
	•	Tier 2 Models: Primarily driven by GBM, AWM, and Controllers. Controllers’ issues relate to capital add-on calculations for EMEA legal entities.
	•	Tier 3 Models: Utilization relatively low.
	•	Regulator asked about rejected models.
	•	MRM explained rejections were due to regression testing failures exceeding 14 days, triggering model rejections and escalations, which have since been resolved.

Threshold Breaches (Page 10):
	•	Regulator inquired about breaches related to invalidated Tier 2 models aged over six months and Tier 1 models with findings aged over nine months.
	•	MRM responded:
	•	Tier 2: Breaches related to capital add-on calculations delays, with one resolved and two expected to be approved shortly.
	•	Tier 1: Issues were primarily in the counterparty credit risk area (margin shortfall calculations) with significant management attention and ongoing remediation efforts.

Generative AI (Gen AI) Usage:
	•	Regulator asked about increased usage and governance of generative AI models.
	•	MRM explained proactive steps initiated in 2023, establishing firm-wide AI governance and the AI Risk and Controls Committee. Growth has been gradual, focusing on low-risk productivity-enhancing tools.
	•	MRM highlighted two Tier 1 AI models: one for AI platform monitoring (guardrail model), and one related to ESG metrics.
	•	Regulator asked about committee composition and risk coverage.
	•	MRM explained committee membership includes stakeholders from Legal, Compliance, Operational Risk, Tech Risk, Engineering, and MRM, ensuring comprehensive risk review and monitoring of all AI use cases.

MRA Remediation Progress:
	•	Regulator requested an update on MRA remediation.
	•	MRM provided an overview:
	•	Completed first milestone (enhanced annual review templates) with external consultant input.
	•	Scheduled to review enhancements with MRCC.
	•	Created differentiated templates for Tiers 1-3 and Tier 4 models, enhanced question structure and guidance, requiring detailed commentary for all questions.
	•	Proposed exemption from annual reviews in revalidation years, aligning with industry practice.
	•	Next steps include system enhancements and team-wide training, starting with mock reviews.

Tier 4 Model Reviews:
	•	Regulator asked about newly introduced Tier 4 models (low-risk AI/ML models).
	•	MRM explained:
	•	Tier 4 specifically addresses low-risk AI/ML models recently included in inventory.
	•	Annual reviews focus on ongoing monitoring and maintaining low risk, elevating tier and review rigor as necessary.

Conclusion:
	•	Regulator acknowledged remediation progress, expressing satisfaction with proposed enhancements.
	•	MRM committed to providing further documentation (examples, MRCC materials) and remaining available for additional meetings.
	•	Regulator agreed to have additional internal review by David Palmer for final feedback.




Key Guardrail 3.0 Improvements:
	•	Better hallucination detection, including subtle cases.
	•	Improved processing of longer documents.
	•	Upgraded LLM to Gemini Flash 2.0.
	•	Clearly separated Prompt Injection detection from PII/Harmful content detection.
	•	Expanded proprietary dataset for improved fine-tuning.




220 models underwent additional validation or revalidation in Q1, primarily driven by:
	•	The annual review process, notably including (1) implementation of the multi-risk-factor stress methodology for the credit risk scenario design model, (2) enhancements to risk factors and applicable markets for the investment decision model used for interest rate swaps across markets, (3) improvements to equity volatility risk models ensuring consistent proxy granularity and refining the volatility surface shock methodology, and (4) enhancements related to the Interest Rate Risk (IRR) model, including backtesting improvements.
	•	Insufficient documentation, testing, and ongoing monitoring.




I’ve combined the numbered items into one sentence as requested. Let me know if further adjustments are needed!



I’ve combined the numbered items into one sentence as requested. Let me know if further adjustments are needed!



I’ve combined the numbered items into one sentence as requested. Let me know if further adjustments are needed!
	
		
			
					•	Participated in CCAR exam meetings this week covering market risk, credit card provisions, and PPNR.
	•	Regulators emphasized reviewing and validating assumptions and qualitative adjustments, especially ensuring robust governance and challenge processes.
	•	Discussions on PPNR particularly addressed modeling approaches in GBM Public and Private sectors, focusing on adjustments related to firm-specific risks.

Continue regulatory engagement, including recent follow-ups from the FRB CTO quarterly on ESG AI, preparation for the upcoming Generative AI meeting with SEC/FINRA, and responses to FCA inquiries related to the GS AI Assistant.
	
		
			
				
						•	A loss of $121k occurred due to incorrect market data used by an automated trading system for equity risk management in Japan.
	•	The issue was caused by a system failure; the error was manually corrected by a trader, as existing controls didn’t detect this specific scenario.
	•	New automated controls have been implemented to prevent similar incidents, with additional risk assessment planned.



https://www.atlassian.com/data/charts/stacked-bar-chart-complete-guide

“One important consideration in building a stacked bar chart is to decide which of the two categorical variables will be the primary variable (dictating major axis positions and overall bar lengths) and which will be the secondary (dictating how each primary bar will be subdivided). The most ‘important’ variable should be the primary; use domain knowledge and the specific type of categorical variables to make a decision on how to assign your categorical variables.”

In your case:

Model Tier reflects hierarchy or domain importance (Tier 1–4), and likely drives the structure of validation efforts.

Validation Outcome is a dependent result of the process.

Therefore, the guidance suggests that Model Tier is the more appropriate variable for the x-axis (primary category), while Outcome is suited for stacking (secondary category).

Also relevant is:

“Variables with more levels are generally better as primary variables; we want to limit the number of secondary levels to a fairly small amount to make the stack breakdowns easier to read.”

Since your Model Tier variable has 4 levels and Outcome has 2, the document supports placing Model Tier on the x-axis, with Outcome as the stacked segments.

Let me know if you'd like a one-page summary or visual aid referencing this guidance.




That’s a very good question — and it touches on an important nuance in data visualization: chart titles describe what is being measured, but not necessarily how the data must be structured.

📌 Key Consideration: What is the primary comparison you want to show?
Let’s break it down:

🟦 Chart Title: "Model Validation Outcomes"
This tells the viewer what the chart is about — i.e., the result of the validation process — but it doesn’t dictate whether outcomes or tiers belong on the x-axis. That decision depends on what dimension you want to compare across:

Option 1: X-axis = Model Tiers
Interpretation: “Here’s how outcomes (Approved/Rejected) differ across model tiers.”

Viewer takeaway: Outcome patterns by tier

Typical for internal model inventory reviews or governance presentations

✅ Recommended when your goal is:

"How do validation outcomes vary across different tiers?"

Option 2: X-axis = Outcomes
Interpretation: “Here’s how the number of models from each tier contributes to each outcome.”

Viewer takeaway: Tier contribution within each outcome

Less common unless focused on categorizing models by outcome

✅ Valid when your goal is:

"What tiers are most represented in Approved vs. Rejected categories?"

🧠 Visualization Practice Consensus
Most data visualization guidelines (e.g., from Atlassian, Storytelling with Data, and Datawrapper) emphasize that:

The x-axis should represent the categorical variable you're comparing (e.g., Tiers)

The stacks or bars should reflect composition or outcome breakdown

So even though the chart is named “Model Validation Outcomes,” that does not mean the x-axis must be “Outcomes.”



Here’s a cleaner and more polished version of your sentence:

There is continued growth in the development of generative AI models, including the recent approval of enhancements to the model serving as a monitoring framework for the GS AI Platform, designed to detect potential unsafe conversations between users and a large language model (LLM) (e.g., hallucination, profanity, prompt injection, personally identifiable information), and now extended to enable real-time hallucination blocking, shifting its role from monitoring to preventative control.

Would you also like an even slightly more concise option?





Issue-Management Talking Points
	•	Clarify the remit
	•	Issues Management (IM) is a first-line tool to record and remediate model-performance or control gaps; Model Risk remains a facilitator, not the owner.
	•	Avoid “model-risk cutting” perceptions by keeping ownership with Liquidity/Res Engineering, Finance Risk, etc.
	•	Current coverage & pain points
	•	IDDR AUs: controls stand-up targeted for end-Q2 2025; firm-wide by year-end 2025.
	•	Controls not yet embedded ⇒ IM metrics red-flag many items that are actually implementation lag, not true defects.
	•	Overdue inventory (Apr-29-2025 cut): GBM 156 / Risk 90 models (~10–12 % of their inventories) driving the red status.
	•	Metrics & thresholds
	•	Draft severity thresholds (count & aging) complete; ready for production once controls are live.
	•	Proposal: announce a go-live date now (e.g., 1 Oct 2025) and a grace period during which AUs must clear or formally waive aged items.
	•	Escalation path
	•	Models breaching thresholds auto-generate High-Severity findings with predefined remediation milestones.
	•	Mid-May Controller CVA waiver is a test-case: if timeline slips, AU must table a revised plan immediately.
	•	Regulatory & audit backdrop
	•	Fed exam teams already probing link between ER tracker and IM; mixed vocabulary is causing confusion.
	•	Internal Audit likely to raise a finding if systematic IM isn’t demonstrated in 2H 2025.
	•	Actions for Brian
	1.	Endorse the proposed go-live date and grace-period message.
	2.	Signal to AU heads that overdue backlogs will trigger automatic High-Severity findings post–go-live.
	3.	Support resource allocation to the two heaviest offenders (Market-Risk Strats & Risk-Economic Strats) to reduce red items before Q4.




Executive-level take-away

Brian’s next update needs to knit together three threads: (1) growing regulatory/exam pressure around model performance vs. model‐control governance, (2) near-term deliverables and deadlines across validation, waivers, and AI governance, and (3) the emerging need to escalate overdue models and findings through a more systematic issues-management playbook.  The talking points below are ordered the way the team suggested presenting them to Brian.

⸻

1. Exam response & “IRR/IDDR confusion”
	•	Clarify the purpose of the Liquidity-Risk/Engineering tracker – it is first-line performance monitoring, not a Model Control Policy artefact.
	•	Stress that Model Risk is coordinating but must not become the de-facto owner of exam findings; ownership stays with first line.
	•	Flag risk of leaving the exam with an unintended “model-risk cutting” finding; action: align vocabulary and responsibilities before the next Fed touchpoint.

2. Model-Control & RCSA roll-out
	•	Status by division
	•	IDDR AUs fully stood-up target → end-Q2 2025
	•	Firm-wide roll-out target → end-2025
	•	Show-and-tell for Brian
	•	One-pager matrix: all Risk AUs with their Model-Risk controls, RCSA mapping, primary/secondary sign-offs.
	•	If possible, a parallel view for Controllers (IPV vs. RevCap split still under discussion).
	•	Note GBM–Model-Control meeting likely to move forward (check new date).

3. Personnel / capacity
	•	Introduce Emma (May intake) now assisting the team.

4. AI / Generative-model governance
	•	MRM AI Assistant pilot and related regulatory threads – bundle under one bullet.
	•	VerCopilot (S-1 generation) status; highlight AWS-Hosting & Engineering pushback (WM driven).
	•	Two weeks until FID-T Explainability & Data-Science submission → offline working session to finalise, then release to Compliance.

5. Validation pipeline & “Lotus” deadlines
	•	US vs. PRA divergence
	•	US models will stick to 2025 Lotus timeline; PRA path still undecided but will likely rely on current QAs/manual processes in the interim.
	•	Provide Brian any colour on feasibility of running parallel rating methodologies.
	•	Early validation themes – data representativeness, conceptual soundness (e.g., Antonas Ray conceptual issue).

6. CCAR & firm-wide stress metrics
	•	New Firm-Wide Asset Loss Metric (extension of un-margined metric) moving from exposure to loss basis.
	•	Validation working to reconcile weak- vs. six-month shocks; need written methodology.
	•	Confirm June deliverables and any further phases for Canal and related projects.

7. Controller CVA waivers (critical path)
	•	Mid-May target at risk; Controllers still refining justification language.
	•	Action for Controllers: if the date will slip, surface a revised plan immediately with root-cause detail.
	•	Escalate to Brian that this waiver is closely tracked by Zero Committee.

8. Inventory, metrics & issues-management escalation

Area	Total models	Overdue / waiver	%
GBM (all)	~1,500	156	≈10%
Risk	~750	90	≈12%

	•	Most overdue Risk models sit in Market-Risk Strats & Risk-Economic Strats AUs.
	•	Proposed next steps
	1.	Finalise severity thresholds (already drafted) and set a go-live date for systematic raising in Issues Management.
	2.	Communicate grace period end to AU owners; remediation playbooks ready.
	3.	Prepare for potential Internal Audit scrutiny if delays persist.

9. Miscellaneous regulatory items (one-line bullets)
	•	ILST methodology updates – ready to brief.
	•	SEC NPR (new market-risk rules) – no immediate action for Model Risk; monitor.
	•	FIS code exam wrap-up – largely handled by MRM; worth a closing remark.
	•	ETSC findings – four on-track for June closure; credit-mark negotiation completed.

⸻

Suggested deck structure for Brian
	1.	Exam & Ownership Clarification (slide)
	2.	Model-Control / RCSA Map – Risk & Controllers (tables)
	3.	Key Deliverables Calendar (timeline graphic)
	4.	AI Governance Snapshot (bullet slide)
	5.	Validation & Lotus Status (narrative + heat-map)
	6.	Waivers & Overdue Models – Metrics & Next Steps (chart)
	7.	Regulatory Odds-and-Ends (overflow slide)

This coverage should equip Brian to answer likely questions on governance scope, upcoming deadlines, and the plan to impose more disciplined issue escalation.








Got it — keeping your original start (“new model for pricing callable credit-linked notes (CLNs),”), here’s the improved version:

New model for pricing callable credit-linked notes (CLNs), using dynamics that incorporate both stochastic hazard rates and stochastic interest rates, addressing the limitations of existing approved models that assume deterministic hazard rates.

Would you also like an even slightly smoother version with minimal change, like adding just one word to make it read even more naturally (e.g., “has been introduced”)?



Implementation Requirements by Phase:

The initial implementation of the Deterministic Regulatory Calculation (DRC) framework for the calculation of U.S. Standardized Approach Risk-Weighted Assets (RWA), addressing direct regulatory feedback, must comply fully with all requirements specified in this Policy.

Any subsequent extension of this framework to include calculations related to the Global Systemically Important Bank (GSIB) surcharge and the Supplementary Leverage Ratio (SLR), as part of the firm's Enterprise Risk Management Framework (ERMF) enhancement initiatives, must also fully comply with all requirements outlined in this Policy.

A detailed plan for the remaining implementation activities concerning U.S. regulatory capital ratios under the Federal Reserve Board’s risk-based and leverage capital regulations will be provided during the Policy's annual review. This plan will include clearly defined timeframes within which the DRC implementation will achieve full compliance with this Policy.



Thank you — that’s a very important clarification.
You’re saying the issue isn’t traders randomly picking marks, it’s that there’s no reliable market price available for them to mark to.
This needs to be worded carefully to reflect that.

Here’s the revised version staying very close to your structure with “and”, now properly reflecting mark-to-market difficulties:

⸻

Volatility and correlation calibration issues were observed in multi-cross FX trades due to increased volatility and skew, and challenges in sourcing reliable market prices for marking; a temporary solution with limited impact has been approved, and further investigation is in progress.

⸻

Another polished version, a little more formal but still matching your original structure:

Volatility and correlation calibration issues were observed in multi-cross FX trades due to increased volatility and skew, and difficulty identifying reliable market levels for marking; a temporary solution with limited impact has been approved, and further investigation is in progress.

⸻

Small but important details fixed:
	•	“Challenges in sourcing reliable market prices for marking” = focuses exactly on mark-to-market.
	•	“Difficulty identifying reliable market levels” = another variation if you want slightly more formal tone.
	•	Preserved your “and”, your structure, your meaning, without making it sound alarming (“unreliable market data” sounded bad — now it’s more professional).

⸻

Would you like me to also show a super crisp version for an executive deck or slide, if you want an even sharper cut?
(Only if you need.)





Got it — you want a version that defines not just AMC, but also CM, MC, SFL, etc.
Here’s a much clearer rewrite where I lightly define the acronyms in-line:

⸻

Efficiency and strategic risk architecture initiatives, including recent approval of enhancements to the American Monte Carlo (AMC) regression framework — a simulation-based approach for valuing options with early exercise features — to improve the numerical implementation for credit products, particularly for Monte Carlo (MC) simulations of credit multi-coupon (multi-CM) payoffs used across Strategic Financing Lending (SFL) businesses, including public and private transactions and exotics, with future plans to extend usage to other asset classes such as CVA tradables, as part of a broader optimization effort.

⸻

Summary of what I did:
	•	AMC → American Monte Carlo (simulation-based approach for early exercise options)
	•	MC → Monte Carlo (simulation method)
	•	multi-CM → multi-coupon (multi-CM) payoffs
	•	SFL → Strategic Financing Lending (SFL)

Quick check:
	•	AMC = American Monte Carlo = simulation approach used when valuing American-style options (early exercise possible)
	•	MC = Monte Carlo simulation = random sampling to simulate price paths
	•	CM = multi-coupon structures = multiple cash flows/payoffs at different times
	•	SFL = Strategic Financing and Lending = business segment handling specialized financing (including public/private side)

⸻

Would you also like a version that’s even a little shorter, in case you need to make it even more compact?
(Depends if you’re writing for a deck, email, or formal memo.)




Got it — keeping your structure and phrasing for the first part exactly, and fitting everything into one clean sentence, here’s the improved version:

Enhancements to the approach for adjusting barrier levels (“barrier shift”) used for pricing multi-asset equity autocallables to be dynamically updated based on volatility versus the previous approach of determining the adjustments at the time of the trade, while also capturing the additional Vega introduced by applying a cap and floor to volatility-based shifts that was previously not reflected in trader-marked values.

⸻

Would you like a second version that’s slightly more formal (just in case you need it for a very polished memo)?



Model Risk has approved the change to re-mark US Volex’s USD YCRA book, restoring the pre-December 2022 MEE-window pricing methodology used for other callables after validating the supporting code update.



Here’s an expanded and detailed summary specifically highlighting the PR call items:

⸻

PR Call Items (Detailed):
	•	CCAR Updates:
	•	Provide a briefing on recent internal CCAR-related meetings held this week.
	•	Update the team on the NPR (Notice of Proposed Rulemaking) issued by the Federal Reserve (Fed):
	•	The Fed is seeking industry comments regarding potential changes to the CCAR process.
	•	Expectation set that this NPR is part of broader adjustments anticipated later this year.
	•	Industry groups, including possibly GS, are preparing detailed responses, coordinated by EO and Controllers teams, on proposed CCAR-related regulatory changes.
	•	Other Regulatory Updates:
	•	Mention that FRB exams recently concluded a follow-up meeting, specifically discussing updates and follow-ups regarding ALST (Asset Liability Stress Testing).
	•	Highlight any critical points from the exam follow-ups, stressing continued regulatory engagement and ongoing compliance requirements.
	•	General acknowledgment of active regulatory oversight, potentially noting positive developments or progress in addressing prior regulatory feedback.
	•	General Expectations:
	•	Reinforce awareness of ongoing regulatory developments relevant to the firm, emphasizing preparedness and proactive management.
	•	Clarify that although no immediate action items from the NPR for CCAR are currently assigned to the team, staying informed remains important due to potential future implications.

⸻

This expanded version ensures clarity on the CCAR-related NPR, highlighting the regulatory engagement’s strategic relevance, and explicitly notes the ongoing follow-ups from recent FRB meetings as important discussion points.







Here’s a concise summary of the provided transcript, emphasizing the final part titled “PL Call Items”:

⸻

Policy Update (DRC Policy)
	•	The team is updating the DRC policy to align with the required “policy on policies” format.
	•	Carly instructed to include an “implementation plan,” referencing a data governance policy as an example.
	•	The policy applies to US regulatory capital under FED rules, specifically the standardized approach. Scope needs to reflect completed and pending implementations clearly.

CRO Update
	•	Reviewing CI and shortfall breaches; no significant model issues identified despite VAR breaches.
	•	Team clarified the placement of EBS stress tests under validation activities, noting consistency with IR and CCR validation activities. Focus remains on MRA remediation rather than ERMS.

Risk Weekly Review
	•	Responsibilities split clearly: GBM updates by the speaker, Ariana manages ENA updates with inputs from Y and Cedra.
	•	Sandra raised queries for FR updates and is independently tracking these updates.

FRAC/BRC and FED Materials
	•	First drafts for FRAC/BRC updates nearly ready.
	•	FED material updates pending; additional model performance issues and market risk model updates likely required, especially MR remediation.
	•	IA updates planned for completion shortly.

Jury Duty Schedule
	•	Uncertainty over jury duty on Monday; unable to commit to specific scheduling for BRC/FRAC meetings until after confirmation.
	•	Speaker to communicate their availability after confirming their jury schedule.

Other Meetings and Upcoming Schedules
	•	Next week’s Scraps meeting scheduled; Brian’s meeting scheduled for the following week.
	•	Alex’s meeting occurs bi-monthly; not due soon.

Front Deck and Regulatory Updates
	•	Front deck content includes AI model performance, regulatory updates, and coherent risk items.
	•	Consideration about combining regulatory updates (IAP, ILA, EBS) into fewer paragraphs; team to review.

PR Call Items for Next Week
	•	Discussion points to include:
	•	CCAR updates and recent NPR requesting industry comments on proposed changes.
	•	Updates from the recent FRB meeting follow-ups on ALST.
	•	General awareness of regulatory activities.

Platform Solutions Insights
	•	Mentioned recent internal developments:
	•	Platform Solutions experiencing no layoffs due to earlier Apple Card exits.
	•	Confirmed a significant retention incentive for remaining staff until the Apple Card sale.

⸻

This summary captures all essential points, particularly around the policy implementation updates, scheduling uncertainty due to jury duty, regulatory update plans, and key topics for upcoming meetings.





















Below is a detailed script you can use (or adapt) for your YouTube video review of the Flexispot E2 standing desk. Feel free to customize it based on your personal experience, style, and preferences.

---

## [INTRO]

**Video opens with a wide shot of you in front of the desk or an overview shot of the Flexispot E2.**  
**Energetic background music plays softly.**

**On-Camera/Voiceover (VO)**:  
> Hey everyone, welcome back to my channel! Today I’m super excited to bring you a review of the **Flexispot E2** standing desk. Whether you’re working from home, streaming, or just looking to upgrade your workspace, a standing desk can make a huge difference for comfort and health. So let’s dive in!

---

## [CHAPTER 1: UNBOXING & SETUP]

**Transition to unboxing footage: Show clips of opening the packaging, removing parts, skimming through instructions, etc.**

**On-Camera/VO**:  
> The Flexispot E2 arrived well-packaged. Inside the box, I found all the necessary parts neatly organized:  
> - Two desk legs and the crossbeam  
> - A control box and handset  
> - All the screws, tools, and accessories needed  
> - And of course, the desktop itself (if you got the Flexispot desktop option).  

> The instructions were straightforward, and the entire setup took me about [insert your time] minutes. I recommend using a power drill if you have one, but everything can be done with the supplied Allen wrench. Just be sure to follow the instructions carefully.

**[Optional: Include any tips or tricky parts you encountered while assembling.]**

---

## [CHAPTER 2: FEATURES & DESIGN]

**Cut to you demonstrating the desk. Show close-ups of different parts: the control panel, the legs, underside, etc.**

**On-Camera/VO**:  
> Once assembled, the desk feels sturdy. The E2 model is known for:
>
> 1. **Height Range**: It has a height range from [X to Y inches/cm (depending on the model)] – accommodating most users whether sitting or standing.  
> 2. **Motor & Speed**: The E2 features a single/dual motor system (depending on your exact E2 variant) that’s relatively quiet. I measured the noise level at around [insert approximate decibels if you did a test], which is pretty discreet.  
> 3. **Controller**: The control panel is simple. You press up or down to adjust the height, and some versions include memory presets so you can save your favorite sitting and standing heights.  
> 4. **Stability**: There’s minimal wobble at standing height, especially for a desk in this price range.  
> 5. **Weight Capacity**: The E2 can hold up to [insert approximate weight capacity], so whether you have a dual monitor setup or a heavy desktop tower, it should handle it well.  
> 6. **Desktop Options**: Flexispot offers different desktop sizes and finishes. I went with [describe your choice], which fits my space perfectly and looks sleek.

---

## [CHAPTER 3: USER EXPERIENCE / DAILY USE]

**Show B-roll of you working, adjusting the desk height, typing, placing items on the desk, etc.**

**On-Camera/VO**:  
> I’ve been using the Flexispot E2 for [insert timeframe] now, and here’s what I’ve noticed in everyday use:
> - **Ergonomics**: Standing for parts of the day definitely helps reduce back pain and makes me feel more energized.  
> - **Ease of Adjustment**: The transition from sitting to standing is smooth and takes only a few seconds. This makes me more likely to actually use the standing feature instead of sticking to one position all day.  
> - **Cable Management**: Flexispot includes some basic cable ties, but you might want to invest in additional solutions if you have multiple monitors and peripherals.  
> - **Desktop Space**: The version I have offers enough room for my dual monitors, keyboard, and a few accessories.

---

## [CHAPTER 4: PROS & CONS]

**On-Camera/VO**:  
> Let’s break it down:
>
> **Pros**:  
> 1. **Affordability**: Compared to other standing desks on the market, the E2 is competitively priced, making it a solid entry-level option.  
> 2. **Sturdy Construction**: The steel frame and stable design inspire confidence.  
> 3. **Customizable Height**: Good height range and memory presets (if your model includes them) make it user-friendly.  
> 4. **Health Benefits**: Encourages movement and reduces the monotony of sitting for long periods.

> **Cons**:  
> 1. **Basic Controller (on some variants)**: If you want advanced features like mobile app control or advanced memory settings, you’ll need a higher-end model.  
> 2. **Limited Aesthetic Options**: While there are some desktop colors and finishes, you might find fewer customization options compared to more premium brands.  
> 3. **Cable Management**: The included solutions are minimal, so you’ll likely need additional accessories for a clean setup.

---

## [CHAPTER 5: COMPARISONS (OPTIONAL)]

**You can add this section if you have personal experience with other standing desks, or just skip it.**

**On-Camera/VO**:  
> Compared to other standing desks in a similar price range, the Flexispot E2 stands out for its sturdy frame and relatively quiet motor. Some desks in this price category can be wobbly at higher settings or have slower motors. Flexispot strikes a nice balance between performance and cost.

---

## [CHAPTER 6: FINAL THOUGHTS & RECOMMENDATION]

**Return to a medium shot of you sitting or standing at the desk.**

**On-Camera/VO**:  
> Overall, the Flexispot E2 is a fantastic entry-level standing desk. It’s sturdy, reliable, and doesn’t break the bank. If you’re looking to upgrade your workspace without jumping to the higher-priced standing desks, this is a great option. As always, consider your needs—like the size of your room, your preferred desktop finish, and desired features—before you buy.  

---

## [OUTRO / CALL-TO-ACTION]

**On-Camera**:  
> Thanks so much for watching! If you found this review helpful, please **hit that like button** and **subscribe** for more reviews and productivity tips. Drop a comment below if you have any questions or if you already own a Flexispot desk—let me know your thoughts!  

> Until next time, this is [Your Name], signing off. Happy standing (and sitting)!

---

### [END CARD / CREDITS]

- **Show channel logo or social media handles.**
- **Mention any affiliate links or discount codes if relevant.**
- **Remind viewers to check the description for more info.**

---

**That’s it!** You now have a structured, step-by-step script to guide your Flexispot E2 standing desk review. Adjust the specifics—like exact height measurements, price, and personal anecdotes—to reflect your genuine experience. Good luck with your video!










Here’s a detailed summary of the key points discussed, structured clearly by topic, for drafting purposes:

⸻

Meeting Agenda Items for Brian:

1. AI Updates & Audit
	•	Provide updates on current AI-related initiatives.
	•	Include status on the ongoing audit concluding this week and key opinions or findings.

2. Board Presentation
	•	Include the board presentation deck and summarize any relevant items.

3. MRA Remediation
	•	Summarize recent clarifications from regulatory meetings.
	•	Possibly include estimates previously provided to Alex.
	•	Update status on broader regulatory commitments.

4. Regulatory Updates
	•	Briefly update on CCAR developments.
	•	Provide updates on other regulatory items, specifically:
	•	ILST Exam currently in progress.
	•	Pearl Street Initiative (Commodities Business Review):
	•	Clarify which models (Tier 1 and Tier 2) are associated with battery storage in UK energy markets.
	•	Outline model inputs, specifically predictive power prices and operational schedules for charging/releasing energy.
	•	Explain associated derivatives markets and risk exposures.

5. DRC (Data Risk Controls)
	•	Address confusion regarding DRCs, particularly where issues exist (possibly related to 6G or LCR).
	•	Highlight uncertainty regarding next steps due to unclear regulatory guidance.
	•	Note concerns from controllers and Finance regarding capital implications and the strategic alignment of DRC usage.
	•	Address potential European regulatory impacts or discussions on similar matters.

6. EMF-related Updates
	•	Clarify responsibility around breach response plan due to an upcoming deadline.
	•	Note interactions with Tom’s team to minimize unnecessary processes, possibly adjusting meeting frequency and sign-off responsibilities.
	•	Consider pragmatic approaches suggested by Tom regarding minimum viable processes.

7. Operational Risk Issues
	•	Discuss concerns over adoption and mapping of Assessment Units (AUs) between Model Risk Management (MRM) and Operational Risk.
	•	Highlight that Jenny’s team is responsible, but offer assistance due to complexities.
	•	Emphasize risks involved in restructuring or remapping AUs unnecessarily, suggesting pragmatic alternatives.

8. RCSA (Risk and Control Self-Assessment)
	•	Expectation of a second review round by Ross’s team informed by other risk areas.
	•	Consider whether the team should officially be recognized as independent Model Monitoring Team (MMT) versus divisional MMT, noting implications for being viewed as a key control versus a second-line review function.
	•	Clarify if RTG and other divisions are labeled as independent or divisional MMT and implications for MRM.

9. Thematic Findings
	•	Discuss planned launch (targeted for April 1) of thematic finding processes, starting potentially with Risk division.
	•	Address the operational readiness for this step, noting manual aspects that might require automation.
	•	Suggest initiating weekly summary emails highlighting problematic areas, with links to dashboards in ModelIt for visibility.

10. Metrics and Waivers
	•	Highlight metrics showing an increase in overdue findings now affecting Tier 1 and Tier 2 models, including AVA models.
	•	Note current issues around unvalidated waivers sitting with Controllers, emphasizing Bo’s rejection recommendation due to significant gaps.
	•	Clarify that a validated rejection is preferable to unvalidated status from a risk management perspective.

11. Internal Audit (IA)
	•	Summarize ongoing IA issues, specifically related to intake forms for AI.
	•	Note continuing frustrations and time-consuming interactions with IA, highlighting IA’s use of audits as learning opportunities, creating inefficiencies.
	•	Seek a pragmatic resolution with IA, involving Gareth for support.

12. Data Governance Issues
	•	Highlight concerns around model input, development, and production data as raised by Engineering.
	•	Identify ambiguity regarding boundaries between data governance and model governance frameworks, specifically:
	•	Whether models must strictly source data from authorized data services (ADS).
	•	Clarify if data governance expectations explicitly cover data used for model development or only production inputs and outputs.
	•	Anticipate challenges with the ECB guidance on model data governance and potential implications from upcoming examinations.
	•	Suggest reviewing the model control framework and data governance standards for clarity around model data handling requirements.

⸻

These structured points can serve as a solid basis for drafting materials and subsequent discussions with Brian.








Detailed Breakdown of ECB Submissions: ICAAP, ILAAP & Prudential Valuation

1. ECB Submissions Overview
	•	Submission of key regulatory documents to the ECB, focusing on risk management, capital adequacy, and liquidity.
	•	The primary focus areas are:
	•	ICAAP (Internal Capital Adequacy Assessment Process)
	•	ILAAP (Internal Liquidity Adequacy Assessment Process)
	•	Prudential Valuation (PV) Review & Follow-Ups

⸻

2. ICAAP (Internal Capital Adequacy Assessment Process)

Purpose:
	•	Ensures that the institution holds sufficient capital to cover all material risks.
	•	Aligns with Basel III/CRR requirements and ECB’s SREP (Supervisory Review and Evaluation Process).

Key Deliverables & Updates:
	•	Submission of ICAAP methodology documents and models.
	•	Includes 30 key documents submitted today, with 16 major ones sent to PCB for IAP.
	•	Focus on:
	•	Risk identification & materiality assessments for Pillar 2 risks.
	•	Stress testing framework—covering both base and adverse scenarios.
	•	Capital planning under different scenarios to ensure resilience.
	•	Alignment with latest ECB guidelines and expectations.

Challenges & Follow-Ups:
	•	ECB has raised questions on the risk-weighted asset (RWA) calculation methodology.
	•	Next steps: Provide detailed breakdowns of the risk appetite framework and stress testing assumptions.

⸻

3. ILAAP (Internal Liquidity Adequacy Assessment Process)

Purpose:
	•	Ensures the institution can withstand liquidity stress and meet obligations under various scenarios.
	•	Aligned with ECB’s Liquidity Stress Testing and Contingency Funding Plan requirements.

Key Deliverables & Updates:
	•	Submission of ILAAP documents, liquidity stress test models, and funding plans.
	•	Emphasis on:
	•	Liquidity buffer calculations and resilience assessment.
	•	Survival horizon analysis under different stress conditions.
	•	Net Stable Funding Ratio (NSFR) and Liquidity Coverage Ratio (LCR) compliance.
	•	Intraday liquidity risk assessment based on ECB’s expectations.

Challenges & Follow-Ups:
	•	ECB has requested further details on liquidity stress assumptions and outflow scenarios.
	•	Next steps include refining the liquidity risk framework documentation to align with ECB’s latest supervisory expectations.

⸻

4. Prudential Valuation (PV) Review & Follow-Ups

Purpose:
	•	Ensures institutions apply fair value adjustments (FVA) properly, reflecting valuation uncertainty.
	•	Aligns with CRR Article 105 and ECB’s Prudential Valuation Guidelines.

Key Deliverables & Updates:
	•	Submission of valuation adjustments methodology and impact analysis.
	•	Covers FVA across Level 1, Level 2, and Level 3 assets, ensuring compliance with regulatory standards.
	•	Addressing ECB’s concerns:
	•	Valuation model risks and uncertainty calibration.
	•	Methodology for market price uncertainty, close-out costs, and concentrated positions.
	•	Independent price verification (IPV) processes.
	•	Alignment with Basel requirements and IFRS 13 fair value hierarchy.

Challenges & Follow-Ups:
	•	BCP has raised concerns about specific methodologies used for prudent valuation adjustments.
	•	Next week: Detailed response to BCP follow-up questions, focusing on:
	•	Justification for valuation methodologies.
	•	Additional stress test results to support prudent valuation adjustments.
	•	Potential recalibration of specific valuation adjustments for Level 3 assets.

⸻

5. Next Steps & Ongoing Monitoring
	•	ICAAP & ILAAP:
	•	Address ECB’s RWA calculation and liquidity stress testing methodology concerns.
	•	Refine the capital and liquidity risk framework documentation.
	•	Prudential Valuation:
	•	Respond to BCP’s methodology concerns with additional data and supporting analysis.
	•	Align prudent valuation adjustments with ECB’s supervisory expectations.
	•	Governance & Reporting:
	•	Ensure ongoing ECB compliance through quarterly validation updates.
	•	Monitor evolving ECB regulatory guidance for potential future refinements.

Let me know if you need further details or specific refinements!

In the transcript, the acknowledgment letter comes up when the Federal Reserve representative confirms that they have received and reviewed the firm’s recent project plan/response and notes that an official acknowledgment letter will be sent soon. Here’s the relevant excerpt in context:

	Regulator (Fed): “We did … and I was able to review those and also I wanted to let the firm know that we did render the process of reviewing the response. So … we should be sending acknowledgment letters soon—just wanted to let you know that.”

The key points regarding the acknowledgment letter are:
	1.	Purpose: It is a formal notification from the Fed acknowledging receipt and initial review of the firm’s submission (such as a supervisory response or project plan).
	2.	Timing: The Fed representative explains that the letter will go out “soon” but does not specify an exact date.
	3.	Next Steps: The letter generally confirms that regulators have reviewed the material and outlines whether there will be any follow-up questions or additional steps expected from the firm.

So, in short, the acknowledgment letter is the official communication from the Fed that they have received the firm’s materials and are moving forward with their supervisory review process.





Below is a concise “Q&A style” summary of the data quality discussion that took place during the transcript, highlighting the question from the regulator and the response from the firm’s Model Risk Management (MRM) team.

⸻

1. Regulator’s Question on Data Quality
	1.	Context of the Inquiry
	•	The regulator observed mentions of data quality issues in the revalidation process and asked how the firm is addressing data governance—particularly as it expands into Generative AI (GAI).
	2.	Core Question
	•	“How is the firm thinking about data quality issues, especially around Generative AI? Are there new or enhanced data management and governance frameworks in place to handle the heightened data risk from advanced AI models?”

⸻

2. Firm’s Response on Data Quality
	1.	Enterprise Data Governance Uplifts
	•	The firm noted that it is already engaged in enterprise-wide data governance enhancements, partly tied to broader regulatory expectations (e.g., BCBS 239 or internal “EMF uplift” efforts).
	•	These ongoing programs aim to improve data lineage, data quality controls, and overall consistency of data usage across the firm.
	2.	Model Risk Perspective
	•	From an MRM viewpoint, data validation is already a core requirement. The firm emphasized that it verifies not only the input data but also the accuracy of the “ground truth” or reference data used to train or benchmark models.
	•	Particularly for AI/ML models, validators focus on how raw inputs are processed into features and whether the labeled outcomes (ground truth) are reliable.
	3.	Generative AI-Specific Measures
	•	Generative AI models must follow the same model validation framework, but with additional scrutiny around:
	•	Data provenance: Where the training data or reference data is coming from.
	•	Comparison across AI engines: For instance, using two different Large Language Model (LLM) providers to cross-check results for consistency or potential drift.
	•	The firm’s newly formed AI Risk & Controls Committee adds supplemental reviews of data usage, model outputs, and risk to ensure that these models comply with legal, compliance, and privacy standards.
	4.	Real-World Example
	•	For the ESGAI model (the first Tier 1 “generative AI” model at the firm), MRM paid close attention to:
	•	Data labeled by humans: Ensuring labels or reference data were validated.
	•	Potential mismatch among multiple AI engines: Identifying if different LLMs yield divergent outputs, which might point to data or labeling inconsistencies.
	5.	Ongoing Controls and Monitoring
	•	Daily or frequent performance tests ensure that if data streams degrade or become inconsistent, the model’s performance metrics will flag it.
	•	The firm also proactively watches for unexpected code changes—a spike in urgent code fixes may signal data or model under “pressure” that warrants closer review.

⸻

Final Takeaway
	•	The regulator asked how the firm is managing data quality—especially in the Generative AI realm.
	•	The firm explained that it has robust data governance efforts in progress, validates ground truth and feature processing for AI/ML, and employs ongoing monitoring plus a specialized AI Risk & Controls Committee to address new challenges posed by advanced models. The focus is on ensuring reliable inputs and consistent labeling so that AI and other models remain accurate, even under heightened market or operational “pressure.”




What “Pressure” Means in This Setting
	1.	Market Volatility or Stress Events
	•	Large swings in interest rates, foreign exchange rates, or credit spreads can introduce unexpected behaviors in a model’s inputs or outputs.
	•	Sudden shocks can reveal gaps in model assumptions or calibration.
	2.	Model Performance & Stability
	•	Models under “pressure” may exhibit higher-than-expected errors, fail certain back-tests, or produce outputs that do not align with market observations.
	•	In risk management terms, a model might be at risk of “breaking” (e.g., generating unrealistic valuations or risk measures) when real-world conditions deviate sharply from the historical data it relies on.
	3.	Operational or Business Changes
	•	Rapidly evolving products, new lines of business, or emergency trading strategies can stress a model if it has not been recalibrated for those changes.

⸻

2. How the Firm Monitors Models Under Pressure

When asked about recent market and interest-rate volatility, the firm’s representatives explained:
	1.	Daily Risk Testing
	•	Many of the front-office and risk models (e.g., pricing, Value-at-Risk, counterparty exposure) undergo daily “re-tests” or real-time performance checks.
	•	If unusual outputs or back-test exceptions surface, those prompt immediate investigation.
	2.	Code Change Monitoring
	•	A sudden increase in developer “hot fixes” or emergency code changes can be a red flag. It might indicate a model is struggling under current market conditions.
	•	The Model Risk Management (MRM) team watches for spikes in code deployments as an early-warning sign.
	3.	Enhanced Scrutiny During Events
	•	If global markets experience a big shock (e.g., a large interest-rate jump or extreme volatility), MRM and the business lines perform ad hoc or forward-looking scenario analyses.
	•	They compare model outputs to alternative benchmarks or “ground truth” data to see if performance is degrading.
	4.	Regular Governance Touchpoints
	•	Any sign of model underperformance triggers Model Risk Control Committee or FRAC reviews. If severe, it escalates to the Board Risk Committee.

⸻

3. Current Observations

From the transcript, the firm indicated:
	•	They have not identified any major breakdowns or anomalies despite recent rate and FX fluctuations.
	•	Ongoing monitoring has not revealed big spikes in back-test exceptions or model failures, so no immediate “pressure” issues were flagged at the time of that conversation.

⸻

4. Why This Matters
	1.	Preemptive Risk Management
	•	By actively searching for “pressure points,” the firm can adjust models (e.g., recalibrate, update assumptions) before problems become critical.
	2.	Regulatory Expectations
	•	Regulators expect that banks detect early signs of model stress and proactively mitigate. If the firm fails to do so, it might face supervisory findings or require urgent remediation.
	3.	Business Continuity and Accuracy
	•	Accurate models under all market conditions reduce the risk of trading losses, mispriced products, and poor strategic decisions.

⸻

Final Takeaway

“Pressure” refers to the stresses placed on a model by volatile or unexpected market conditions. The firm’s process—daily testing, code-change monitoring, ongoing validation checks, and escalations to senior committees—aims to catch any emergent model issues promptly. As of the conversation in the transcript, no significant “pressure” had manifested in the firm’s models, but they continue enhanced 



In the context of the transcript, “pressure” primarily refers to external market or business conditions that could stress or challenge the firm’s models—especially when there is heightened market volatility or significant economic shifts. Here is how that concept of “pressure” surfaced and was addressed:

⸻

1. What “Pressure” Means in This Setting
	1.	Market Volatility or Stress Events
	•	Large swings in interest rates, foreign exchange rates, or credit spreads can introduce unexpected behaviors in a model’s inputs or outputs.
	•	Sudden shocks can reveal gaps in model assumptions or calibration.
	2.	Model Performance & Stability
	•	Models under “pressure” may exhibit higher-than-expected errors, fail certain back-tests, or produce outputs that do not align with market observations.
	•	In risk management terms, a model might be at risk of “breaking” (e.g., generating unrealistic valuations or risk measures) when real-world conditions deviate sharply from the historical data it relies on.
	3.	Operational or Business Changes
	•	Rapidly evolving products, new lines of business, or emergency trading strategies can stress a model if it has not been recalibrated for those changes.

⸻

2. How the Firm Monitors Models Under Pressure

When asked about recent market and interest-rate volatility, the firm’s representatives explained:
	1.	Daily Risk Testing
	•	Many of the front-office and risk models (e.g., pricing, Value-at-Risk, counterparty exposure) undergo daily “re-tests” or real-time performance checks.
	•	If unusual outputs or back-test exceptions surface, those prompt immediate investigation.
	2.	Code Change Monitoring
	•	A sudden increase in developer “hot fixes” or emergency code changes can be a red flag. It might indicate a model is struggling under current market conditions.
	•	The Model Risk Management (MRM) team watches for spikes in code deployments as an early-warning sign.
	3.	Enhanced Scrutiny During Events
	•	If global markets experience a big shock (e.g., a large interest-rate jump or extreme volatility), MRM and the business lines perform ad hoc or forward-looking scenario analyses.
	•	They compare model outputs to alternative benchmarks or “ground truth” data to see if performance is degrading.
	4.	Regular Governance Touchpoints
	•	Any sign of model underperformance triggers Model Risk Control Committee or FRAC reviews. If severe, it escalates to the Board Risk Committee.

⸻

3. Current Observations

From the transcript, the firm indicated:
	•	They have not identified any major breakdowns or anomalies despite recent rate and FX fluctuations.
	•	Ongoing monitoring has not revealed big spikes in back-test exceptions or model failures, so no immediate “pressure” issues were flagged at the time of that conversation.

⸻

4. Why This Matters
	1.	Preemptive Risk Management
	•	By actively searching for “pressure points,” the firm can adjust models (e.g., recalibrate, update assumptions) before problems become critical.
	2.	Regulatory Expectations
	•	Regulators expect that banks detect early signs of model stress and proactively mitigate. If the firm fails to do so, it might face supervisory findings or require urgent remediation.
	3.	Business Continuity and Accuracy
	•	Accurate models under all market conditions reduce the risk of trading losses, mispriced products, and poor strategic decisions.

⸻

Final Takeaway

“Pressure” refers to the stresses placed on a model by volatile or unexpected market conditions. The firm’s process—daily testing, code-change monitoring, ongoing validation checks, and escalations to senior committees—aims to catch any emergent model issues promptly. As of the conversation in the transcript, no significant “pressure” had manifested in the firm’s models, but they continue enhanced scrutiny as part of standard risk oversight.







In the context of the transcript, “pressure” primarily refers to external market or business conditions that could stress or challenge the firm’s models—especially when there is heightened market volatility or significant economic shifts. Here is how that concept of “pressure” surfaced and was addressed:

⸻

1. What “Pressure” Means in This Setting
	1.	Market Volatility or Stress Events
	•	Large swings in interest rates, foreign exchange rates, or credit spreads can introduce unexpected behaviors in a model’s inputs or outputs.
	•	Sudden shocks can reveal gaps in model assumptions or calibration.
	2.	Model Performance & Stability
	•	Models under “pressure” may exhibit higher-than-expected errors, fail certain back-tests, or produce outputs that do not align with market observations.
	•	In risk management terms, a model might be at risk of “breaking” (e.g., generating unrealistic valuations or risk measures) when real-world conditions deviate sharply from the historical data it relies on.
	3.	Operational or Business Changes
	•	Rapidly evolving products, new lines of business, or emergency trading strategies can stress a model if it has not been recalibrated for those changes.

⸻

2. How the Firm Monitors Models Under Pressure

When asked about recent market and interest-rate volatility, the firm’s representatives explained:
	1.	Daily Risk Testing
	•	Many of the front-office and risk models (e.g., pricing, Value-at-Risk, counterparty exposure) undergo daily “re-tests” or real-time performance checks.
	•	If unusual outputs or back-test exceptions surface, those prompt immediate investigation.
	2.	Code Change Monitoring
	•	A sudden increase in developer “hot fixes” or emergency code changes can be a red flag. It might indicate a model is struggling under current market conditions.
	•	The Model Risk Management (MRM) team watches for spikes in code deployments as an early-warning sign.
	3.	Enhanced Scrutiny During Events
	•	If global markets experience a big shock (e.g., a large interest-rate jump or extreme volatility), MRM and the business lines perform ad hoc or forward-looking scenario analyses.
	•	They compare model outputs to alternative benchmarks or “ground truth” data to see if performance is degrading.
	4.	Regular Governance Touchpoints
	•	Any sign of model underperformance triggers Model Risk Control Committee or FRAC reviews. If severe, it escalates to the Board Risk Committee.

⸻

3. Current Observations

From the transcript, the firm indicated:
	•	They have not identified any major breakdowns or anomalies despite recent rate and FX fluctuations.
	•	Ongoing monitoring has not revealed big spikes in back-test exceptions or model failures, so no immediate “pressure” issues were flagged at the time of that conversation.

⸻

4. Why This Matters
	1.	Preemptive Risk Management
	•	By actively searching for “pressure points,” the firm can adjust models (e.g., recalibrate, update assumptions) before problems become critical.
	2.	Regulatory Expectations
	•	Regulators expect that banks detect early signs of model stress and proactively mitigate. If the firm fails to do so, it might face supervisory findings or require urgent remediation.
	3.	Business Continuity and Accuracy
	•	Accurate models under all market conditions reduce the risk of trading losses, mispriced products, and poor strategic decisions.

⸻

Final Takeaway

“Pressure” refers to the stresses placed on a model by volatile or unexpected market conditions. The firm’s process—daily testing, code-change monitoring, ongoing validation checks, and escalations to senior committees—aims to catch any emergent model issues promptly. As of the conversation in the transcript, no significant “pressure” had manifested in the firm’s models, but they continue enhanced scrutiny as part of standard risk oversight.




Below is an expanded explanation of how granular the reporting is—particularly what information the firm’s Board Risk Committee (BRC), the Firmwide Risk & Controls Committee (FRAC), and other senior groups see with respect to model risk.

⸻

1. Board-Level Reporting
	1.	High-Level Risk Appetite Metrics
	•	The Board primarily sees aggregate Model Risk metrics—these are the same top-level Key Risk Indicators (KRIs) that form part of the firm’s Risk Appetite Statement (RAS).
	•	Examples include the number of unvalidated or rejected Tier 1 models in use, breaches of model risk thresholds (e.g., how many models have been “aged” past one year), and any zero-tolerance threshold violations.
	2.	Model Inventory Overview
	•	The Board is given a snapshot of the total number of models, categorized by business unit (Risk, GBM, etc.) and by approval status (validated, unvalidated, rejected).
	•	This helps them gauge the overall size and complexity of the firm’s modeling landscape.
	3.	Significant Updates and Thematic Issues
	•	For important emerging topics—like Generative AI, stress-testing enhancements, or high-profile regulatory findings—the Board receives summary updates or short thematic discussions.
	•	These overviews give them a sense of why certain issues are arising, where potential risks are concentrated, and how management is remediating them.
	4.	Escalation of Major Problems
	•	Any “high-severity” or Tier 1 model concerns (e.g., a large breach or a critical supervisory finding) is escalated immediately to the Board.
	•	If a threshold is breached at the Board level—for instance, if a model’s unvalidated status goes beyond one year—this is highlighted in the Board materials as a zero-tolerance breach.

	Key Takeaway: The Board sees top-level model risk metrics, major trends, and serious exceptions. They do not typically see the full granular “line-by-line” detail for every finding or model.

⸻

2. FRAC and Model Risk Control Committee Reporting
	1.	More Detailed Breakdowns
	•	The FRAC and Model Risk Control Committee (MRCC) get the same top-level metrics the Board sees, plus more granular reporting.
	•	For instance, they might see a breakdown of the exact number of findings by severity, open vs. closed status, and how many days past due each item is.
	2.	Qualitative Approaches, Deterministic Reg Calculations
	•	Beyond typical quantitative models, these committees also see detailed metrics on qualitative approaches and deterministic regulatory calculations (such as certain capital or compliance calculations).
	•	This ensures coverage of all tool types under the broader “model” or “model-like” umbrella.
	3.	In-Depth Thematic Reviews
	•	If there is a specific area of heightened focus—e.g., new large language models, a revalidation wave for stress-testing, or interest-rate volatility—FRAC/MRCC may receive a deeper “spotlight” analysis or a short write-up showing key observations and any open issues.
	4.	Focus on Remediation and Progress
	•	These committees track whether open findings are being closed on schedule and monitor areas with higher volumes of new findings.
	•	They also see trend analyses (e.g., quarter-over-quarter changes in the number of open findings, average days to close a finding, etc.).

⸻

3. Subcommittees and Working Groups
	•	Working-Level Detail
	•	At the most granular level—within MRM or specialized working groups—teams might review the individual findings line by line. This includes severity scores, root causes, and exact remediation steps.
	•	These working groups feed summarized information up to FRAC and eventually to the Board, so the level of detail filters appropriately based on the audience.

⸻

4. Why Different Audiences See Different Levels of Detail
	1.	Audience and Purpose
	•	Board: Oversees risk at a strategic level. They want to know if there are large or systemic issues jeopardizing the firm’s risk appetite.
	•	FRAC/MRCC: Operate at a more tactical and operational level, ensuring robust controls are actually implemented and that meaningful issues or rising trends are handled before they become Board-level breaches.
	•	Working Groups / Validation Teams: Perform the day-to-day analysis, root cause identification, model reviews, and produce the raw data that rolls up to the committees.
	2.	Escalation Tiers
	•	The firm’s governance model sets out which types of issues must be escalated to which committee—and on what timetable—to prevent any critical or overdue items from going unnoticed.

⸻

Final Summary
	•	The Board receives a high-level, strategic view: key metrics, risk appetite thresholds, serious exceptions, and thematic summaries.
	•	The FRAC/Model Risk Control Committee sees a more detailed breakdown of open findings, model statuses, business-line splits, and thematic deep-dives.
	•	Working groups handle the most granular, line-by-line model details, feeding that information upward as summarized reports for senior stakeholders.

In essence, the reporting grows more granular as you move from the Board (highest level) down to the committees and working groups.




In the transcript, there is a reference to six Tier 1 unvalidated models “quarter over quarter.” The concern was whether these six were the same models staying unvalidated too long or if the number “6” simply reappeared each quarter for different reasons (new models, model updates, etc.).

Key Points
	1.	It is not necessarily the same six models
	•	During the quarter, some Tier 1 models get validated and come off the unvalidated list, while new or changed models are added to the unvalidated list. So the figure may remain around six each quarter, but it reflects different models over time.
	2.	New Model Development & Significant Model Changes
	•	Tier 1 models often arise from highly complex or critical areas (e.g., trading, risk management). Whenever the firm introduces new Tier 1 models or makes material changes to existing ones, those models must go through revalidation.
	•	That revalidation process can temporarily increase the number of unvalidated Tier 1 models.
	3.	Waiver & Aging Controls
	•	The firm uses a 90-day waiver for unvalidated models in use, plus tight aging metrics (six or nine months at the FRAC level, one year at the Board level). These thresholds ensure that unvalidated models cannot remain outstanding indefinitely.
	•	If any model is in use without validation past its original remediation date, the firm tracks it as an “aged” item, which triggers increased scrutiny.
	4.	Ongoing ‘Churn’
	•	The firm describes a “churn” or turnover: some Tier 1 unvalidated models in use resolve each quarter and drop off the list, while new ones (due to fresh development or updates) come on. That can keep the number around six, even though they are not the same exact six from quarter to quarter.

⸻

In short, the number “six” showing up quarter over quarter does not imply that the same six Tier 1 models are perpetually unvalidated; rather, it’s a recurring level driven by ongoing model development, enhancements, and validation turnover.




From the discussion, the main reason for the uptick in findings near the end of the year is that new model development, model changes, and scheduled revalidations all came together in Q4. In other words:
	1.	New or Enhanced Models
	•	Whenever the firm introduces a new model or significantly changes an existing one, the Model Risk team performs fresh validation. This typically leads to new findings being raised.
	2.	Revalidations
	•	A large batch of Tier 1 model revalidations was wrapped up at year-end. These reviews can also generate findings—especially around documentation, calibration details, or minor code fixes—even when the model itself is fundamentally sound.
	3.	Close-Out vs. New Findings
	•	In Q4, the number of new findings (from all the model changes and revalidations) slightly outpaced the number of closed findings, causing a net increase (or “uptick”) in open items for that quarter.




Below is a structured, detailed summary of the discussion, based on the transcript provided. The conversation is primarily between representatives from a financial institution’s Model Risk Management (MRM) group (including Caroline, Bill, Bo, Bingwen, OJ, and others) and regulators from the Federal Reserve (“the Fed”) and FDIC (with Michaela and Caleb representing the regulators). The main topics include quarterly model risk updates, threshold tightening for certain metrics, the use of generative AI models, and the status of various validation activities and findings.

⸻

1. Meeting Logistics and Introductions
	•	The call begins with attendees confirming who is present from both the firm and the regulators.
	•	Michaela joins, and the group confirms they have the relevant participants from the Fed, FDIC, and the bank’s MRM team.
	•	The bank’s team mentions that it sent over meeting materials in advance, confirming that the Fed received and reviewed them.

⸻

2. Recent Submissions and Regulatory Review
	•	The Fed acknowledges receipt of the firm’s recent project plan/response to supervisory requests and indicates that an acknowledgment letter will be sent soon.
	•	The firm reiterates it is available to address any questions about the plan or any other materials, either during the meeting or offline.

⸻

3. Updates on Risk Appetite Thresholds and Governance
	•	Tightening of waiver aging thresholds:
	•	The firm explains that it previously established a threshold of nine months for certain model waivers at the FRAC (Firmwide Risk and Controls Committee) level but decided to reduce it to six months.
	•	The Board Risk Committee (BRC) retains a one-year zero-tolerance threshold for these same items, meaning if a waiver is still unresolved after one year (relative to its original due date), it breaches the BRC’s risk appetite.
	•	The shortened six-month threshold provides an earlier escalation path while leaving a three-month buffer before hitting the Board-level one-year limit.

⸻

4. Discussion on Generative AI (GAI) and Large Language Models
	•	A regulator inquires about a recently approved ESG-related large language model (an “ESGAI” model) and the firm’s broader generative AI strategy.
	•	AI governance structure:
	•	The bank has a dedicated AI policy and an AI Risk & Controls Committee, formed in 2023.
	•	The committee includes representatives from various control functions (Model Risk, Operational Risk, Legal, Compliance, etc.) to address potential risks of new AI use cases.
	•	Model Risk Management approach:
	•	Generative AI models are subject to the same core model-risk controls and require model validations similar to traditional models.
	•	The firm uses specialized documentation and validation templates for AI/ML models.
	•	They have introduced a separate AI inventory process so that not only validated AI models but also certain AI “tools” and “platforms” are tracked.
	•	Use cases and outlook:
	•	Most generative AI models so far are in lower-risk, operational efficiency use cases.
	•	The ESGAI model is the first “Tier 1” generative AI model (i.e., of higher materiality/risk) that has gone through full validation.
	•	Additional generative AI expansions are expected, but each is examined under the AI policy and standard model risk controls.

⸻

5. Status of Validation Findings and Internal Audit (IA) Items
	•	Open and closed findings:
	•	The MRM team reviews charts illustrating open findings, newly raised findings, and those closed during the quarter.
	•	They note a slight uptick in total findings for Q4 but highlight a downward trend on a year-over-year basis.
	•	Findings are concentrated where model inventory is largest (e.g., Risk, Global Banking & Markets).
	•	Internal Audit (IA) observations:
	•	Seven IA findings were closed in the quarter, all of them lower-severity (general) items, primarily documentation-related.
	•	A new, low-severity IA finding was raised noting a “pattern” of validation documentation gaps over a few years. IA did not question the firm’s validation conclusions but felt it warranted a broader training initiative.
	•	The firm agreed to roll out training to reinforce comprehensive documentation standards by the end of April.

⸻

6. Board and FRAC-Level Metrics (RAS Utilization)
	•	The firm tracks several risk appetite statement (RAS) metrics around unvalidated or rejected models and the aging of those conditions.
	•	Waiver framework:
	•	If a model is in use without a finalized validation (unvalidated) or with a “reject” rating, it must have a time-bound waiver, typically remedied within 90 days.
	•	Age-based metrics (how long a model or finding remains unresolved past its original due date) are set to zero tolerance at nine months (now shortened to six months) at the FRAC level and one year at the Board level.
	•	Current usage:
	•	There were no Board-level or FRAC-level breaches during the quarter for unvalidated or rejected models.
	•	Some items did breach the age threshold for “severity 2” findings. Two specific GBM models triggered the FRAC threshold, but those findings have since been remediated.

⸻

7. Model Inventory and Ongoing Monitoring
	•	Inventory overview:
	•	The firm reports a stable overall model inventory, noting a modest increase of around 100 models over the past year.
	•	They break it down by tier (materiality) and business line (e.g., Risk Division, GBM, etc.).
	•	Market volatility considerations:
	•	Regulators ask whether the firm has enhanced monitoring due to recent market volatility (particularly interest-rate-related).
	•	The firm explains that its daily risk tests, ongoing performance assessments, and close scrutiny of code changes help identify potential breakage or model underperformance.
	•	As of now, there have been no major issues from volatile conditions.

⸻

8. Model Changes and Significant Revalidations
	•	Enhancements and new approvals:
	•	The firm highlights approvals for collateralized lending models (private equity, direct CRE, etc.), interest rate risk enhancements, and other operational models.
	•	Validation teams identified a few low-severity issues (e.g., minor code bugs) that were fixed pre-approval.
	•	Significant Tier 1 revalidation cycle:
	•	The two-year cycle for the highest-materiality (Tier 1) models concluded at year-end.
	•	No high-severity findings emerged; medium-severity findings primarily involved methodology, parameter calibration, or documentation improvements.
	•	The firm is already beginning the next two-year revalidation cycle for Tier 1 models and is also performing annual validations for CCAR/stress-testing models.

⸻

9. Meeting Conclusion
	•	The regulators express appreciation for the comprehensive materials and clarity of updates.
	•	They confirm they will follow up with any additional questions and will send an official acknowledgment of the firm’s supervisory response.
	•	Both parties end on a positive note, and the meeting concludes with thanks exchanged.

⸻

Overall, the discussion centers on the bank’s continued enhancements to model risk governance—tightening certain thresholds, validating and monitoring advanced AI models, and staying on top of internal audit findings. Regulators appear satisfied with the bank’s progress and reaffirm that they will remain in contact regarding any needed clarifications on model risk and supervisory items.







MEETING MINUTES
Date: [Insert Date of Meeting]
Time: [Insert Time of Meeting]
Location: Virtual Conference

⸻

1. Attendees
	•	Regulatory Representatives
	•	Federal Reserve (Fed): Attendee(s) not fully specified
	•	FDIC: Attendee(s) not fully specified
	•	Michaela (Regulator)
	•	Caleb (Regulator)
	•	Firm Representatives
	•	Caroline (Model Risk Management, “MRM”)
	•	Ajan
	•	Bo
	•	Bill
	•	Ibo
	•	Additional MRM and Risk Team members (names not fully specified)

⸻

2. Meeting Purpose
	•	To provide a quarterly update on Model Risk Management (MRM) to the Federal Reserve and FDIC.
	•	To discuss recent changes to the firm’s model risk thresholds (including waiver aging), internal audit findings, and Generative AI (GAI) models.

⸻

3. Agenda Highlights
	1.	Introductions and confirmation of participants
	2.	Acknowledgment of materials (confirming regulators received the deck)
	3.	Quarterly model risk updates (including waiver threshold changes and status of findings)
	4.	Generative AI model discussion (ESGAI model and broader GAI governance)
	5.	Internal audit findings review
	6.	Revalidation activities and model inventory trends
	7.	Questions, next steps, and action items

⸻

4. Detailed Updates and Discussion

4.1 Waiver Thresholds and Aging

The firm reiterated that it has a zero-tolerance policy at the Board Risk Committee (BRC) level for models or findings aged beyond one year from the original due date. As an intermediate check, the firm’s Model Risk Control Committee (FRAC) threshold was previously set at nine months. To better align with other control functions, the FRAC threshold has been shortened to six months. The firm explained that this adjustment creates an additional buffer, ensuring potential concerns are flagged and addressed before reaching the Board’s one-year threshold.

4.2 Generative AI (GAI) Models

The firm has observed an increase in the number of AI/ML models, including those using large language models (LLMs). While most uses remain low-risk and focused on operational efficiencies, the firm noted its first Tier 1 Generative AI model (ESGAI). The validation approach for GAI follows the firm’s existing model risk framework, supplemented by an AI Risk and Controls Committee. This committee includes representatives from legal, compliance, operational risk, and other control functions to address emerging risks such as data privacy, unintended model behaviors, and compliance considerations.

4.3 Internal Audit Findings

The firm reported that many of the recent internal audit findings were of lower severity, typically related to documentation enhancements. Internal audit had also identified a pattern of documentation inconsistencies over several years. The firm has responded by committing to additional training sessions on comprehensive model validation documentation. Most findings have already been remediated or are in the process of closure, with no impact on the fundamental integrity of any model conclusions.

4.4 Model Inventory and Revalidations

The firm’s model inventory remains relatively stable. A slight uptick in Q4 was attributed to normal development and enhancements in existing models. The firm tracks outstanding waivers carefully and ensures that no waiver is extended indefinitely without proper justification. Significant Tier 1 revalidations, required on a two-year cycle, have been completed for the current period with no high-severity findings. The firm is also in the midst of annual reviews tied to regulatory exercises such as CCAR. Overall, there have been no major performance issues in daily run tests, and no models have experienced unexpected breakage during recent market volatility.

⸻

5. Questions and Responses (in Third Person)
	1.	Regulators inquired about the rationale for tightening waiver thresholds
The firm responded that it sought to align its Model Risk processes with similar frameworks in other control functions (e.g., Internal Audit). By reducing the FRAC threshold from nine to six months, the firm provided additional time to address potential issues well before the Board’s one-year zero-tolerance deadline.
	2.	Regulators asked for an update on the firm’s progress with Generative AI
The firm explained that it continues to see new GAI applications, often focusing on operational efficiencies. It has validated its first Tier 1 GAI model (ESGAI) and uses AI-specific validation templates. The AI Risk and Controls Committee reviews AI models for potential legal, compliance, and operational risks that go beyond traditional model risk.
	3.	Regulators requested information on recent Internal Audit findings
The firm stated that the majority of new findings related to documentation gaps rather than fundamental model performance. Some issues had been self-identified in the course of prior reviews. To address these gaps, the firm is rolling out targeted training for validators, emphasizing thorough documentation standards.
	4.	Regulators inquired about model performance during market volatility
The firm reported that daily run tests remain stable. There have been no noteworthy breakages, code failures, or unusual parameter shifts resulting from market events. The firm also indicated it monitors changes in model code for any signs of stress or anomalies.
	5.	Regulators asked whether any unvalidated Tier 1 models had exceeded their remediation deadlines
The firm confirmed that all unvalidated or rejected models require waivers and are tracked for timeliness. Extended waivers are granted only after a robust internal process, and aging metrics (nine months previously, now six months) ensure issues are escalated before becoming overdue at the Board level.

⸻

6. Next Steps and Action Items
	•	Acknowledgment Letters:
Regulators plan to issue formal letters acknowledging the firm’s recent supervisory response.
	•	Severity 1 Finding Confirmation:
The firm will verify the status of a Severity 1 finding in the Risk division to confirm whether the model is in production or still under development.
	•	Documentation Training Completion:
The firm will finalize and conduct training sessions on validation documentation best practices by the end of April.
	•	Generative AI Oversight:
The firm will continue to provide updates on new GAI models and any significant policy or governance changes under the AI Risk and Controls Committee.
	•	Continued Market Monitoring:
Daily run tests will continue, with attention to volatility and potential code updates that might signal underlying stress.

⸻

7. Conclusion

Regulators expressed appreciation for the comprehensive update and noted that no significant concerns emerged from the quarterly materials. The firm will continue its proactive approach to model risk, especially around new AI applications and any documentation improvements suggested by internal audit. Both parties agreed to maintain open communication on model risk developments and to reconvene at the next scheduled quarterly update (or sooner if needed).

⸻

These minutes summarize the main points of discussion, the firm’s responses to regulators’ questions, and the agreed-upon action items.









Meeting Minutes
Date: [Insert Date of Meeting]
Time: [Insert Time of Meeting]
Location: Virtual Conference

⸻

1. Attendees
	•	Regulatory Representatives
	•	Federal Reserve (Fed): [Name(s) not fully specified in transcript]
	•	FDIC: [Name(s) not fully specified in transcript]
	•	Michaela (Regulator)
	•	Caleb (Regulator)
	•	Firm Representatives
	•	Caroline (Model Risk Management, “MRM”)
	•	Ajan
	•	Bo
	•	Bill
	•	Ibo
	•	Others from the MRM and Risk Teams

(Note: Some names were partially mentioned or not fully introduced in the transcript.)

⸻

2. Meeting Purpose
	•	Quarterly Model Risk Management Update to the regulators (Fed and FDIC).
	•	Review of:
	•	Recent changes to Model Risk thresholds (including waiver aging).
	•	Firm’s approach to Generative AI (GAI) models.
	•	Status of internal audit findings and overall validation progress.
	•	Model inventory trends, revalidation cycles, and key issues.

⸻

3. Agenda & Key Discussion Topics
	1.	Introductions and Confirmation of Attendance
	2.	Acknowledgement of Meeting Materials
	•	Regulators confirmed receipt of the firm’s materials.
	•	The regulators noted an acknowledgment letter regarding a recent supervisory submission would be sent soon.
	3.	Quarterly Model Risk Update
	•	Overview of findings and remediation status.
	•	Discussion of the firm’s Risk Appetite Statement (RAS) thresholds and recent tightening of waiver aging thresholds.
	4.	Discussion on Generative AI (GAI) Models
	•	First Tier 1 GAI model approval (ESGAI).
	•	Broader firm strategy and governance approach for AI and large language models.
	5.	Internal Audit Findings & Closure
	•	Review of recent and ongoing internal audit findings (documentation, validation templates, potential patterns observed).
	•	Discussion of training plans to address documentation consistency.
	6.	Model Inventory & Revalidations
	•	Updates on model inventory statistics.
	•	High-level review of revalidation activities (especially “significant Tier 1” revalidations).
	•	Status of daily run tests/monitoring given market volatility.
	7.	Next Steps & Action Items

⸻

4. Detailed Discussion and Q&A

Below is a summary of questions raised during the meeting and the firm’s responses.

4.1 Changes to Waiver Thresholds
	•	Question (Regulator):
“You recently tightened the waiver aging threshold from nine months to six months. Could you provide background on why you lowered it and how it aligns with the board’s existing threshold?”
	•	Response (Firm):
“Previously, we introduced zero tolerance for waivers older than one year at the Board level. We had an internal (FRAC) threshold of nine months but decided to tighten that to six months for better alignment with other control functions (e.g., internal audit) and to ensure we have ample time to remediate before reaching Board-level thresholds. This gives the FRAC additional buffer to address potential issues before one year elapses.”

4.2 Generative AI (GAI) Model and Future Plans
	•	Question (Regulator):
“We noticed the ESGAI model was recently approved. It’s a large language model. Could you talk about your broader approach to Generative AI? Are you looking at many use cases? Any specific risk governance for GAI?”
	•	Response (Firm):
“Yes, ESGAI is our first Tier 1 GAI model. Most GAI uses here have been low-risk, operational-efficiency tools. All GAI models go through our existing model risk process with dedicated AI/ML validation templates. In addition, we’ve established an AI Risk and Controls Committee, which includes operational risk, legal, compliance, and other relevant control functions. This committee provides an additional oversight layer beyond standard model validation due to heightened concerns like data usage and privacy. We have indeed seen growth in AI models, but many are Tier 2 or Tier 3, and they must follow the same rigorous validation processes.”

4.3 Internal Audit Findings and Documentation
	•	Question (Regulator):
“You mentioned a few internal audit findings related to documentation. How is the firm addressing these gaps? Is there specific training for staff?”
	•	Response (Firm):
“Most findings identified by internal audit focused on documentation clarity, not on the validity of model outputs or effective challenge. We’ve already remedied several of these items. For the most recent one (raised in Q4), we are developing a formal training program for our validators to reinforce comprehensive documentation standards. Our target is to complete this training by the end of April.”

4.4 Model Inventory Trends
	•	Question (Regulator):
“Your inventory is generally stable, but there was a slight uptick in Q4. What drove that, and do you see any issues with timely validations?”
	•	Response (Firm):
“The small increase reflects typical new-model approvals and changes in existing models. We’re closely monitoring them through our waiver process. Each model requiring validation has a remediation timeline, and we track these carefully. We haven’t identified any major delays beyond standard extensions. Our aged metrics help ensure nothing languishes past the original due date.”

4.5 Market Volatility and Model Performance
	•	Question (Regulator):
“Given recent market volatility, have you enhanced your daily model monitoring processes? Notably, are any pricing or risk models showing stress or breakage?”
	•	Response (Firm):
“We conduct daily run tests, and so far, we haven’t seen any unusual breakage or unexpected parameter shifts. Our teams also proactively check for large market shocks. If we see unusual code changes or anomalies, that prompts deeper scrutiny. At this time, we’re not seeing significant performance issues.”

⸻

5. Action Items and Next Steps
	1.	Acknowledgment Letters:
	•	Regulators will send acknowledgement letters regarding the firm’s recent supervisory response.
	2.	Follow-Up on Severity 1 Model:
	•	The firm to confirm details regarding a Severity 1 finding in the Risk division (to clarify if the model was in use or in development).
	3.	Documentation Training:
	•	The firm to complete the new training program for validation staff by end of April.
	4.	Monitoring of Market Volatility:
	•	The firm will continue daily run tests and step up monitoring for any potential volatility-driven model errors or breakages.
	5.	Generative AI Governance:
	•	The firm to keep regulators informed of further developments, approvals, or changes in the GAI framework and usage.

⸻

6. Conclusion
	•	The regulators confirmed receipt of the quarterly update materials.
	•	The firm provided detailed updates on the model risk inventory, waiver threshold changes, and the status of internal audit findings.
	•	Generative AI governance remains a focus, with new oversight committees and processes in place.
	•	No immediate concerns were raised regarding market volatility or model performance.
	•	Both parties agreed to continue close communication and follow up on open items and training initiatives.

⸻

These minutes capture the primary points of discussion, key questions and responses, and agreed-upon next steps.






Below is a revised version you might find clearer and more concise:

Revised Response:

The CEU calculation is embedded within the Tier D1 SA-CCR DRC. In alignment with the Firmwide Standards for Deterministic Regulatory Calculations, MRM conducts an annual review of all Tier D1 DRCs to confirm their ongoing validity, considering potential changes to the DRC itself or the surrounding operating environment. In addition, Tier D1 DRC developers are required to obtain IRG approval for any DRC modifications before implementing them in production.

Furthermore, continuous monitoring procedures are in place to maintain the accuracy of the DRC. These procedures include daily regression tests and weekly ongoing monitoring reports to verify the CEU determination logic.

This version groups the key points more clearly, highlights responsibilities, and streamlines the language. You can adjust the level of detail or formality to suit your specific needs.





A new 1-month “staple-shaped” instantaneous forward rate (IFR) discontinuity for the USD Secured Overnight Financing Rate (SOFR) curve, which is based on 3-month SOFR International Money Market (IMM) futures, addresses short-end constraints and enables more granular control at the 1-month level.


A new “staple-shaped” IFR discontinuity—two offsetting jumps spaced one month apart—was introduced to the USD SOFR curve to address short-end constraints driven by 3-month SOFR IMM futures and CFR interpolation in IFR space, while preserving CER interpolation and enabling more granular 1-month control, specifically allowing the desk to manage 1-month serial SOFR/FF basis levels previously beyond their reach.



A new “staple-shaped” IFR discontinuity—two offsetting jumps spaced one month apart—was introduced to the USD SOFR curve to address short-end constraints driven by 3-month SOFR IMM futures and CFR interpolation in IFR space, while preserving CER interpolation and enabling more granular 1-month control, specifically allowing the desk to manage 1-month serial SOFR/FF basis levels previously beyond their reach.




The USD SOFR curve is constructed to reflect future financing rates, but in practice, traders often need finer adjustments at shorter intervals—particularly around monthly roll dates—so this new “staple-shaped” IFR discontinuity, composed of two offsetting jumps spaced one month apart, was introduced to allow more precise control at the 1-month point within each 3-month IMM period, ensuring better alignment with market realities and short-term rate movements.


A new “staple-shaped” IFR discontinuity—two offsetting jumps one month apart—was introduced to the USD SOFR curve to provide finer 1-month control within each 3-month IMM period, fulfilling the desk’s need for more precise short-end management.




Below is a detailed, thematic summary of the conversation. It focuses on the main topics discussed, the context behind them, and the next steps or action items that arose.

1. Upcoming Meeting With Brian (Wednesday Morning)
	•	Schedule and Materials
	•	The speakers confirm that a meeting with Brian is still planned for Wednesday morning (referred to as “Wednesday 45”).
	•	They note that materials being circulated are updates that were originally prepared for a prior meeting which “got bumped.”
	•	Topics to Cover
	1.	Emery Remediation: Provide an update and refresh of the remediation bid, given schedule changes.
	2.	AI Topics:
	•	Growth and modality of AI resources (e.g., HPC usage).
	•	“AI acceleration proposal” and a related summary from “AI governance from table.”
	3.	Leslie’s Request:
	•	There is a question about integrating an ask from Leslie.
	•	The group is unclear on the background or context of Leslie’s query and wonders where it originated.
	•	This might be an opportunity to review the DAIS process for Brian, including divisional representation (e.g., Jay, Constantine).
	4.	Additional AI Initiatives:
	•	The team wants to get a comprehensive list of ongoing or potential AI ideas from Jay.
	•	They plan to be “opinionated”—assessing which ideas are more likely to succeed and which are less so, potentially identifying gaps or overlooked opportunities.
	•	They also discuss how success in production (e.g., an AI-driven validation or summarization tool) could reinvigorate interest.
	5.	Resources and Headcount:
	•	Part of the AI discussion centers on highlighting resource constraints, budget (ZPP), and headcount needs.
	•	They mention HPC usage charts, exponential growth, and how to represent (or exclude) certain large allocations (e.g., T204, AI platform) to make the data clearer.

2. Additional AI Updates and Observations
	•	Big Models / AI 2.0
	•	There are bank-wide efforts around large model initiatives.
	•	Upcoming pilot projects (e.g., “blockingination detection”) for GBM public vs. private.
	•	Positioning and Ownership
	•	Speakers note they want it clear that their team is spearheading AI efforts, rather than another department (OAS).
	•	They also mention synergy with AI HPC resources and that there’s ongoing work with other teams (e.g., “AirCC stuff”).

3. Other Agenda Items for Brian
	1.	IRR & CCAR
	•	They plan to refresh Brian on the status of IRR work and CCAR updates.
	2.	Lotus, RCSA, and Issue Management
	•	They have bullets to discuss, given Brian’s ongoing focus on RCSA (Risk and Control Self-Assessment) and issue management.
	•	One point is the milestone reached on some RCSA deliverables (control library sign-off, for instance).
	•	They need final confirmation on a control-library spreadsheet from compliance (“someone in compliance emailed a spreadsheet”).
	•	The group believes the changes align with prior agreements and likely just require official sign-off.

4. Metrics and Findings
	•	Current ‘No Breach’ Moment
	•	The team discusses how for certain key metrics, there are currently no active breaches.
	•	However, there may be potential upcoming breaches (e.g., a repo-related one).
	•	Tracking the Overall Findings Count
	•	They recall the count of open findings used to be quite high (possibly 40–50), and they are now aiming for a lower number (around 22).
	•	They see progress in some areas but mention continued friction in others (e.g., market risk consistently missing deadlines unless escalated).
	•	Possible Thematic Findings
	•	They are considering raising “thematic findings” for any group that remains in persistent metric “red” status.
	•	One idea is to pick a date (e.g., April 1) after which the team will systematically raise findings if certain metrics remain red, ensuring consistent application across GBM and other divisions.
	•	RCSA Integration
	•	Ongoing conversations about how the new RCSA processes (led by the central risk organization) align with day-to-day controls and findings management.
	•	There is mention of how risk teams only do RCSA events semiannually, making control-effectiveness updates slow.

5. “Breach Response Plan” and Workflow Tool
	•	New Policy Requirement
	•	A new policy mandates that any breach must have a response plan (with an ETA) approved by the CRO (Alex).
	•	The group references a “breach workflow tool” originally developed for Market Risk.
	•	Challenges
	•	The tool is not well-suited to ongoing or long-standing breaches (as often happens in this group’s processes, which can remain “over” for extended periods rather than a short event).
	•	Using the tool daily for repeated, unchanged breaches would be an administrative burden.
	•	Seeking Clarification
	•	They want clarity on how detailed Alex wants these response plans to be.
	•	They had initially thought an exemption might be possible, but it appears certain stakeholders (e.g., Motrum) insist on using the new tool regardless.
	•	Next Steps
	•	There is a follow-up call scheduled (moved to “tomorrow”) to discuss a possible exemption or a more streamlined process for these “long-running” or “operational” types of breaches.
	•	They note that other teams (like OpRisk) have similar issues, though some (like Phil’s group) appear to have already acquiesced.

6. Action Items & Points of Emphasis
	1.	AI Resource & Budget Discussion
	•	Finalize HPC usage charts, deciding whether to include or exclude large platform allocations, to clarify the growth story for Brian.
	•	Emphasize how the AI demands and expansions fit into the existing headcount and budget constraints (ZPP).
	2.	List of AI Initiatives
	•	Obtain the comprehensive list from Jay/Constantine.
	•	Formulate opinions on which projects have the highest chance of success or strategic value, plus mention any new opportunities not currently on that list.
	3.	Sign-off on Control Library
	•	Confirm agreement with the recent spreadsheet from compliance and provide official go-ahead.
	4.	Metrics Updates
	•	Refresh the table for Brian, highlight improvement trends, but also outline the areas (e.g., Market Risk) still needing regular escalation.
	5.	Thematic Findings Escalation
	•	Potentially propose a set start date (e.g., April 1) for systematic escalation via thematic findings when certain divisions remain in red status.
	6.	Breach Response Plan Tool
	•	Attend the follow-up meeting to see if an exemption or adapted process can be reached.
	•	Seek Brian’s input on the best approach to manage daily operational/long-term breaches under the new policy.

Overall Takeaways
	•	Preparation for Brian: The team plans to cover AI updates (including acceleration proposals, resource constraints), risk metrics (breaches, findings, and open issues), and RCSA progress.
	•	Administrative & Policy Burdens: New policy requirements (e.g., breach response tool) may be ill-suited to how this team typically manages longer-running issues, prompting them to seek alternatives or clarifications.
	•	Governance & Ownership: They want to highlight clearly where AI efforts truly sit (their team vs. other groups), underscore successes in HPC usage, and clarify budgetary needs.
	•	Ongoing Friction Points: Persistent challenges with market risk’s responsiveness to escalations and confusion over RCSA processes remain important discussion items for Brian’s input.

This summary reflects the key points and context from the transcript. It consolidates who is doing what, where the main pressures or problems lie, and which decisions or clarifications need leadership input.





A new “staple-shaped” IFR discontinuity—two offsetting jumps one month apart—was introduced to the USD SOFR curve to address short-end constraints and enable more granular 1-month-level control within each 3-month IMM period.



Below is a consolidated, detailed summary of the conversation. It organizes the main points and clarifies the various threads that came up during the discussion:

1. Purpose of the Conversation

The speakers are discussing a series of updates and action items related to:
	•	AI-related projects and communications
	•	MRA (Matter Requiring Attention) remediation status
	•	Upcoming meetings with different committees (BRC, FRAC)
	•	Governance and risk-related items (RCSAs, capital risk, expansions, etc.)
	•	Scheduling constraints, especially with one person being out on Tuesday

The conversation centers on making sure that final materials (particularly for BRC and FRAC) are up to date, reflect recent changes, and incorporate feedback from various stakeholders.

2. AI Updates and Communication
	1.	Polished Language / Revised Notes
	•	There are existing AI updates, some of which overlap with emails sent to Alex and Gopi. The idea is to “true up” or refine the wording to match a more polished version already in circulation.
	•	There are also notes from a meeting with Michaela and a governance roundtable (led by or involving Eric Goor) that should be incorporated into the AI section of broader governance or committee materials.
	2.	Continued Improvements in CCR and ASL
	•	The conversation touches on CCR (likely a risk or compliance model/tool) and ASL (possibly another internal system or tool). Both are undergoing continual enhancements. The group wants to decide if these ongoing improvements are significant enough to highlight in upcoming committee materials.
	•	The suggestion is to confirm with team members (e.g., Javarianna or Andresa) which specific enhancements might be noteworthy or relevant for the committees.

3. MRA Remediation Status
	1.	Background
	•	The MRA remediation appears to be a priority topic for multiple committees (BRC, FRAC).
	•	There were originally 19 total findings from some form of audit or review (by ERM or an external body), of which most have been remediated. Three remain open.
	2.	Committee Presentations
	•	The question arises whether MRA remediation should stand on its own as a separate discussion item, especially since some committees have specific agendas that may or may not align with MRA topics.
	•	There is a desire to keep the language very clear about what has been done so far (e.g., the 19 findings, how many were resolved, and the plan for the remaining open items).
	3.	Capital Risk Table Issue
	•	The speakers reference a table or chart that addresses “capitalist challenges” or “capital risk,” which might incorrectly lump MRA remediation into a broader risk discussion.
	•	There is a need to ensure that MRA items are accurately represented and not placed into a table that could suggest a mismatch of issues. One speaker references Kevin’s email, noting that bullet points about MRA have been removed from that particular risk table to avoid confusion.

4. Upcoming Meetings and Materials
	1.	Meeting Schedule
	•	A “stress meeting” is confirmed for Wednesday.
	•	Brian’s meeting is happening on Tuesday afternoon.
	•	The FRAC and BRC materials need to be prepared by Thursday and Friday, respectively, to align with upcoming sessions.
	2.	Committee Packets
	•	The final versions of FRA and BRC decks (or related material) should incorporate big topics: MRA remediation, significant AI updates, CCR/ASL enhancements, and any other noteworthy developments.
	•	There is interest in ensuring the committees receive clear, polished language that reflects current progress on these initiatives.
	3.	RCSAs (Risk & Control Self-Assessments)
	•	The Q4 RCSA results (at least for GBM) will need to be included in the upcoming committee updates or presentations. The speaker intends to finalize these results by Tuesday night to be ready for review on Wednesday.

5. Potential DRC Expansion
	•	There is mention of expanding something called “DRC” to EIA (the acronym is not fully defined in the conversation).
	•	Engineering teams would need to propose an onboarding plan and resource estimates.
	•	It does not appear to be budgeted for this year, so the timeline is still “to be determined” (TBD).

6. Action Items and Next Steps
	1.	Refining Documents
	•	Incorporate polished language from the “already circulated” AI updates, along with notes from Michaela’s meeting and Eric Goor’s governance roundtable.
	•	Clarify the MRA remediation language so that it properly captures the status of the open/closed findings.
	2.	Coordination with Various Stakeholders
	•	Check in with specific team members (e.g., Andresa, Javarianna) to see if the ongoing CCR/ASL upgrades warrant highlighting in committee materials.
	•	Coordinate with Kevin (and possibly others) to ensure MRA references are correctly presented or removed from any confusing risk tables.
	3.	Preparing for a Busy Week
	•	One person will be out on Tuesday, so they plan to work remotely or at night to finalize certain documents, especially the RCSA updates.
	•	Materials for BRC and FRAC should be ready by Thursday/Friday, noting that the MRA remediation will likely be a central topic.

7. Overall Takeaways
	•	Timely Updates: Multiple committees (BRC, FRAC) need accurate, up-to-date information on MRA remediation, AI/CCR/ASL enhancements, and RCSA results.
	•	Clear Communication: The transcript underscores how critical it is to fine-tune the language in presentations, especially around MRA findings and any risk tables, so that committees receive an accurate picture.
	•	Resource Planning: Some items, such as the DRC expansion, remain in a preliminary stage and need budget/resource alignment before proceeding.
	•	Logistics: Owing to schedules (someone being out Tuesday), final reviews will be done quickly—some on Tuesday night, with a final check on Wednesday morning, before the materials go to their respective committees.

In essence, the conversation is a coordination meeting to ensure that various corporate governance and risk materials—especially around MRA remediation and AI—are updated, aligned with stakeholder feedback, and ready in time for important committee sessions.





Below is a concise summary of what was discussed (and planned) for the upcoming Monday “PO” call based on the transcript:

Purpose of the Monday PO Call
	•	Gather and review any pressing regulatory items that need to be communicated or escalated.
	•	Check in on outstanding action items (e.g., T TBP cleanup, Fed submissions, etc.).

Main Discussion Topics
	1.	Regulatory Updates (SEC, FINRA, Fed)
	•	SEC AP Model Request:
	•	A minor submission item; no major concerns expected.
	•	Team will confirm details are finalized or if any clarifications are needed.
	•	FINRA Follow-ups:
	•	There may be outstanding follow-up items to communicate or confirm.
	•	Fed-Related Items:
	•	Briefly mention the upcoming CEU meeting with the Fed.
	•	The team will also touch on the submission of the latest inventory to the Fed (Ariana is handling details).
	2.	T TBP (Trade/Transaction Booking Policy) Cleanup
	•	The group wants to highlight the revamp of the T TBP process.
	•	Open Tickets: People with older booking policy exceptions need to review or close them.
	•	The call is a chance to remind owners of outstanding tickets to address them by a certain deadline.
	•	Follow-up Strategy:
	•	Phil (and possibly Prashant) will help chase updates from London-based or harder-to-reach teams.
	•	If no response is received from owners, tickets may be closed or escalated.
	3.	CCAR / General Fed-Submission Updates
	•	A short update on any CCAR-related progress or requirements if relevant.
	•	Mention if there are any regulatory due dates or deliverables in the next couple of weeks.
	4.	High-Level Reminders
	•	Governance Team Constraints: The governance team is understaffed at the moment (with Lena’s departure and someone else out sick), so be mindful of how much is assigned to them.
	•	Upcoming Committee Meetings: BRC and FRAC are on the same timeline (February 27). The call might briefly confirm any dependencies or next steps related to preparing materials.

Outcome / Next Steps for the PO Call
	•	Finalize which items to present: The group will decide which updates (SEC AP model, FINRA follow-ups, Fed inventory submission) need more attention on the call.
	•	Set a Deadline for T TBP Ticket Closures: Communicate a clear plan for owners to respond or close their tickets.
	•	Coordinate with Key Stakeholders: Ensure people like Ariana, Phil, Prashant, and others are looped in for their respective pieces of work.
	•	Confirm Prep for Regulatory Meetings: Decide if any additional materials or summaries are needed for the Fed or other regulators.

That covers the main points expected to be addressed in the next Monday PO call based on the conversation.





Below is a concise summary of the main points discussed in the transcript:
	1.	Lotus Data Source Changes
	•	There is a plan to move certain Lotus-related calculations from existing (“non-alternative”) data sources to a new, presumably higher-quality data source.
	•	The team expects fewer manual overrides and improved data quality once these new sources are implemented.
	•	Follow-up reviews may be required after the switch, but the team will perform checks to ensure the transition does not worsen data quality.
	2.	Expansion of LCO (Europe Scope)
	•	There is discussion about expanding LCO coverage in Europe.
	•	This expansion was not previously budgeted, so the team needs to determine resource requirements, timeline, and headcount.
	•	Further planning with senior stakeholders (e.g., “BB”) is needed to clarify scope and funding.
	3.	UK’s Stance on Basel 3 and Resulting Budget/Planning Implications
	•	The UK has decided not to proceed with full Basel 3 implementation.
	•	This decision impacts prior plans, budgets, and potentially the technical approach to regulatory calculations.
	•	The team notes that any rework (e.g., rewriting certain calculations) could be as large an undertaking as the initial DRC (Default Risk Charge) build.
	•	They emphasize the need for a strategic discussion on how to manage the additional workload and align resources accordingly.

Overall, the conversation centers on upcoming data-source transitions, regulatory scope expansion in Europe, and the budget/timeline adjustments required in light of the UK’s Basel 3 decision.



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




