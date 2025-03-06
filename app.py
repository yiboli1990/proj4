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




