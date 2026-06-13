# schemes_data.py
# GovAssist - Government Scheme Database
#
# Field structure for each scheme:
#   name        : Scheme name
#   occupation  : Farmer / Student / Laborer / Business Owner / Government Employee /
#                  Private Employee / Self-Employed / Unemployed / Pregnant Women / Senior Citizen / Any
#   category    : General / SC / ST / OBC / EWS / Any  (social category)
#   gender      : Male / Female / Any  (optional, defaults to Any if absent)
#   income_limit: Maximum annual family income in INR for eligibility (None = no limit specified)
#   overview    : Short description of the scheme
#   benefits    : List of key benefits
#   eligibility : List of eligibility conditions
#   documents   : List of documents required to apply

schemes = [

    # ============================================================
    # FARMER SCHEMES (with full details)
    # ============================================================
    {
        "name": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Income support scheme providing direct cash transfer to landholding farmer families to help meet agricultural and household expenses.",
        "benefits": [
            "₹6,000 per year paid in 3 equal installments of ₹2,000 each",
            "Direct Benefit Transfer (DBT) to bank account",
            "No repayment required"
        ],
        "eligibility": [
            "Must be a landholding farmer family",
            "Excludes constitutional post holders, serving/former ministers and MPs/MLAs",
            "Excludes income tax payers and pensioners drawing ₹10,000 or more per month"
        ],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details", "Passport Size Photo"]
    },
    {
        "name": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Crop insurance scheme that provides financial support to farmers in case of crop loss or damage due to natural calamities, pests, or diseases.",
        "benefits": [
            "Low premium rates (2% for Kharif, 1.5% for Rabi, 5% for commercial/horticultural crops)",
            "Coverage for pre-sowing to post-harvest losses",
            "Quick claim settlement via technology-based assessment"
        ],
        "eligibility": [
            "All farmers including sharecroppers and tenant farmers growing notified crops",
            "Compulsory for farmers with crop loans (unless opted out)",
            "Voluntary for non-loanee farmers"
        ],
        "documents": ["Aadhaar Card", "Land Ownership/Tenancy Records", "Bank Account Details", "Sowing Certificate"]
    },
    {
        "name": "Kisan Credit Card (KCC) Scheme",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides farmers with timely access to credit for agricultural and allied activities at concessional interest rates.",
        "benefits": [
            "Short-term credit up to ₹3 lakh at 4% effective interest rate (with timely repayment)",
            "Flexible withdrawal and repayment based on crop cycle",
            "Covers crop production, post-harvest, and allied activities"
        ],
        "eligibility": [
            "All farmers - individual/joint borrowers, tenant farmers, sharecroppers, oral lessees",
            "Self Help Group (SHG) or Joint Liability Group (JLG) members"
        ],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details", "Passport Size Photo"]
    },
    {
        "name": "Pradhan Mantri Kisan Maandhan Yojana (PM-KMY)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Voluntary pension scheme for small and marginal farmers providing social security after the age of 60.",
        "benefits": [
            "Minimum guaranteed pension of ₹3,000 per month after age 60",
            "Government contributes equal matching share to the pension fund",
            "Spouse eligible for continuation of pension"
        ],
        "eligibility": [
            "Small and marginal farmers aged 18-40 years",
            "Landholding up to 2 hectares",
            "Not covered under other statutory social security schemes"
        ],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account/Savings Passbook", "Age Proof"]
    },
    {
        "name": "e-NAM (National Agriculture Market)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Online trading platform that connects existing mandis to create a unified national market for agricultural commodities, helping farmers get better prices.",
        "benefits": [
            "Access to a larger pool of buyers across India",
            "Transparent price discovery through online bidding",
            "Reduced dependency on local middlemen"
        ],
        "eligibility": [
            "Any farmer registered with a participating APMC mandi"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details", "Mandi Registration"]
    },
    {
        "name": "Soil Health Card Scheme",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides farmers with soil nutrient status reports along with recommendations on appropriate dosage of nutrients for crop improvement.",
        "benefits": [
            "Free soil testing every 2 years",
            "Customized fertilizer recommendations to improve yield",
            "Reduces input costs by avoiding over-use of fertilizers"
        ],
        "eligibility": [
            "All farmers across India are eligible"
        ],
        "documents": ["Aadhaar Card", "Land Records"]
    },
    {
        "name": "PM Kisan Urja Suraksha evam Utthan Mahabhiyan (PM-KUSUM)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Promotes solar power generation and use of solar pumps for irrigation to reduce dependency on diesel and grid electricity.",
        "benefits": [
            "Subsidy of up to 60% on solar pump installation",
            "Additional income by selling surplus solar power to grid",
            "Reduced irrigation costs"
        ],
        "eligibility": [
            "Individual farmers, group of farmers, cooperatives, panchayats, FPOs",
            "Must have access to suitable land for solar installation"
        ],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details"]
    },
    {
        "name": "Agriculture Infrastructure Fund (AIF)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides medium-to-long term debt financing for investment in post-harvest management infrastructure and community farming assets.",
        "benefits": [
            "Interest subvention of 3% per annum on loans up to ₹2 crore",
            "Credit guarantee coverage under CGTMSE for eligible borrowers",
            "Supports cold storage, warehouses, and processing units"
        ],
        "eligibility": [
            "Farmers, FPOs, agri-entrepreneurs, cooperatives, and SHGs"
        ],
        "documents": ["Aadhaar Card", "Business/Project Proposal", "Land Documents", "Bank Account Details"]
    },
    {
        "name": "Paramparagat Krishi Vikas Yojana (PKVY)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Promotes organic farming practices through cluster-based approach and certification to improve soil health and farmer income.",
        "benefits": [
            "Financial assistance of ₹50,000 per hectare over 3 years",
            "Support for organic inputs, certification, and marketing",
            "Training on organic farming techniques"
        ],
        "eligibility": [
            "Farmers willing to form clusters of minimum 20 hectares for organic farming"
        ],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details"]
    },
    {
        "name": "Sub-Mission on Agricultural Mechanization (SMAM)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Promotes farm mechanization by increasing access to farm machinery and equipment, especially for small and marginal farmers.",
        "benefits": [
            "Subsidy up to 50% on purchase of agricultural machinery",
            "Higher subsidy (up to 80%) for SC/ST and women farmers",
            "Custom Hiring Centres for machinery access"
        ],
        "eligibility": [
            "All categories of farmers, with priority to small and marginal farmers"
        ],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details", "Caste Certificate (if applicable)"]
    },
    {
        "name": "Namo Drone Didi Scheme",
        "occupation": "Farmer",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides drones to Women Self Help Groups for rental services to farmers for agricultural purposes like spraying fertilizers and pesticides.",
        "benefits": [
            "Subsidy up to 80% for drone purchase by SHGs",
            "Additional income generation opportunity for SHG members",
            "Training on drone operation and maintenance"
        ],
        "eligibility": [
            "Members of registered Women Self Help Groups"
        ],
        "documents": ["Aadhaar Card", "SHG Membership Certificate", "Bank Account Details"]
    },
    {
        "name": "National Mission for Sustainable Agriculture (NMSA)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Promotes sustainable agriculture through climate-resilient practices, integrated farming, and efficient resource use.",
        "benefits": [
            "Support for rainfed area development",
            "Promotion of climate-resilient crop varieties",
            "Financial assistance for water conservation structures"
        ],
        "eligibility": [
            "All farmers, with focus on rainfed and drought-prone areas"
        ],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details"]
    },

    # ============================================================
    # STUDENT SCHEMES (with full details)
    # ============================================================
    {
        "name": "National Scholarship Portal (NSP)",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 800000,
        "overview": "Single-window platform for students to apply for various central and state government scholarships.",
        "benefits": [
            "Access to multiple scholarship schemes through one application",
            "Direct transfer of scholarship amount to bank account",
            "Covers tuition fees, maintenance allowance, and other expenses"
        ],
        "eligibility": [
            "Students enrolled in recognized educational institutions",
            "Family income below specified limits (varies by scheme)"
        ],
        "documents": ["Aadhaar Card", "Income Certificate", "Bank Account Details", "Previous Year Marksheet", "Bonafide Certificate"]
    },
    {
        "name": "PM YASASVI Scholarship",
        "occupation": "Student",
        "category": "OBC",
        "income_limit": 250000,
        "overview": "Scholarship scheme for students from OBC, EBC, and DNT categories to support their education from class 9 onwards.",
        "benefits": [
            "Pre-Matric scholarship of ₹75,000-1,25,000 per year for class 9-10 students",
            "Top Class education scholarship for higher education covering tuition fees",
            "Support for coaching for competitive exams"
        ],
        "eligibility": [
            "Students belonging to OBC, EBC, or DNT categories",
            "Family income below ₹2.5 lakh per annum",
            "Studying in class 9 or above"
        ],
        "documents": ["Aadhaar Card", "Caste Certificate", "Income Certificate", "Previous Marksheet", "Bank Account Details"]
    },
    {
        "name": "Central Sector Scheme of Scholarships for College and University Students",
        "occupation": "Student",
        "category": "General",
        "income_limit": 450000,
        "overview": "Provides financial assistance to meritorious students from economically weaker sections to pursue higher education.",
        "benefits": [
            "₹10,000 per annum for college/university students",
            "Renewable annually based on academic performance",
            "Disbursed directly to bank account"
        ],
        "eligibility": [
            "Students who scored above 80th percentile in class 12 exams",
            "Family income less than ₹4.5 lakh per annum",
            "Pursuing regular undergraduate courses"
        ],
        "documents": ["Aadhaar Card", "Class 12 Marksheet", "Income Certificate", "Bank Account Details", "Admission Proof"]
    },
    {
        "name": "INSPIRE Scholarship (SHE Scheme)",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Encourages students to pursue education and research careers in basic and natural sciences by providing scholarships.",
        "benefits": [
            "₹80,000 per annum scholarship for pursuing science degree courses",
            "Summer research fellowships under affiliated programs",
            "Career counselling for research opportunities"
        ],
        "eligibility": [
            "Students in the top 1% of class 12 board examination",
            "Pursuing BSc/MSc/integrated MS-PhD in natural and basic sciences"
        ],
        "documents": ["Aadhaar Card", "Class 12 Marksheet", "Admission Letter", "Bank Account Details"]
    },
    {
        "name": "Pragati Scholarship for Girls (AICTE)",
        "occupation": "Student",
        "category": "Any",
        "gender": "Female",
        "income_limit": 800000,
        "overview": "Provides financial assistance to girl students pursuing technical education in AICTE-approved institutions.",
        "benefits": [
            "₹50,000 per annum for tuition fees and other expenses",
            "Covers full duration of the technical course"
        ],
        "eligibility": [
            "Girl students admitted to first year of diploma/degree technical courses",
            "Maximum 2 girl children per family",
            "Family income up to ₹8 lakh per annum"
        ],
        "documents": ["Aadhaar Card", "Income Certificate", "Admission Proof", "Bank Account Details"]
    },
    {
        "name": "Saksham Scholarship for Differently Abled Students (AICTE)",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 800000,
        "overview": "Financial support for differently-abled students pursuing technical education to reduce financial barriers.",
        "benefits": [
            "₹50,000 per annum towards tuition fees and incidentals",
            "Covers entire duration of the course"
        ],
        "eligibility": [
            "Differently-abled students (40% or more disability) admitted to technical courses",
            "Family income up to ₹8 lakh per annum"
        ],
        "documents": ["Aadhaar Card", "Disability Certificate", "Income Certificate", "Admission Proof", "Bank Account Details"]
    },
    {
        "name": "Post Matric Scholarship for SC Students",
        "occupation": "Student",
        "category": "SC",
        "income_limit": 250000,
        "overview": "Financial assistance for SC students studying at post-matriculation or post-secondary level to enable them to complete their education.",
        "benefits": [
            "Reimbursement of tuition fees and non-refundable charges",
            "Monthly maintenance allowance ranging from ₹230 to ₹1,200 depending on course",
            "Additional allowances for books, study tours, and thesis"
        ],
        "eligibility": [
            "Students belonging to Scheduled Caste",
            "Family income less than ₹2.5 lakh per annum",
            "Studying in post-matric/post-secondary courses"
        ],
        "documents": ["Aadhaar Card", "Caste Certificate", "Income Certificate", "Previous Marksheet", "Bank Account Details", "Bonafide Certificate"]
    },
    {
        "name": "Post Matric Scholarship for ST Students",
        "occupation": "Student",
        "category": "ST",
        "income_limit": 250000,
        "overview": "Financial assistance for ST students studying at post-matriculation level to support continuation of education.",
        "benefits": [
            "Reimbursement of tuition fees and compulsory institutional charges",
            "Monthly maintenance allowance based on course and hostel status",
            "Book grants and study tour allowances"
        ],
        "eligibility": [
            "Students belonging to Scheduled Tribe",
            "Family income less than ₹2.5 lakh per annum",
            "Studying in post-matric/post-secondary courses"
        ],
        "documents": ["Aadhaar Card", "Tribe Certificate", "Income Certificate", "Previous Marksheet", "Bank Account Details", "Bonafide Certificate"]
    },
    {
        "name": "Merit-cum-Means Scholarship for Minorities",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 250000,
        "overview": "Supports meritorious students from minority communities pursuing professional and technical courses.",
        "benefits": [
            "Course fee reimbursement up to ₹20,000 per annum",
            "Maintenance allowance for hostellers and day scholars"
        ],
        "eligibility": [
            "Students from notified minority communities (Muslim, Christian, Sikh, Buddhist, Jain, Parsi)",
            "Minimum 50% marks in previous qualifying examination",
            "Family income less than ₹2.5 lakh per annum"
        ],
        "documents": ["Aadhaar Card", "Minority Community Certificate", "Income Certificate", "Previous Marksheet", "Bank Account Details"]
    },
    {
        "name": "AICTE Swanath Scholarship",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides financial assistance to technical education students who have lost a parent due to COVID-19 or other circumstances.",
        "benefits": [
            "₹50,000 per annum scholarship",
            "Covers full duration of technical course"
        ],
        "eligibility": [
            "Students who have lost both parents or sole earning parent",
            "Pursuing AICTE-approved technical courses"
        ],
        "documents": ["Aadhaar Card", "Death Certificate of Parent", "Admission Proof", "Bank Account Details"]
    },
    {
        "name": "Vidyanjali Scheme",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Volunteer initiative to enhance the quality of education in government schools through community and corporate participation.",
        "benefits": [
            "Access to additional learning resources and volunteer mentors",
            "Improved infrastructure through CSR contributions",
            "Exposure to skill-based and extracurricular activities"
        ],
        "eligibility": [
            "Students enrolled in government and government-aided schools"
        ],
        "documents": ["School ID/Enrollment Proof"]
    },
    {
        "name": "PM Vidyalaxmi Scheme",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 800000,
        "overview": "Provides collateral-free education loans to students for higher education in top quality institutions with interest subsidy.",
        "benefits": [
            "Collateral-free loans up to ₹7.5 lakh with credit guarantee",
            "3% interest subvention for students from families with income up to ₹8 lakh",
            "Full interest subsidy for students from EWS families with income up to ₹4.5 lakh"
        ],
        "eligibility": [
            "Students admitted to top-ranked higher education institutions",
            "Family income within specified limits for subsidy"
        ],
        "documents": ["Aadhaar Card", "Admission Letter", "Income Certificate", "Bank Account Details"]
    },

    # ============================================================
    # PREGNANT WOMEN / WOMEN SCHEMES (with full details)
    # ============================================================
    {
        "name": "Pradhan Mantri Matru Vandana Yojana (PMMVY)",
        "occupation": "Pregnant Women",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Maternity benefit program providing cash incentives to pregnant and lactating women to improve health and nutrition during pregnancy.",
        "benefits": [
            "₹5,000 cash incentive in three installments for first living child",
            "Additional ₹6,000 for second child if a girl",
            "Promotes institutional delivery and health check-ups"
        ],
        "eligibility": [
            "Pregnant and lactating women (except those in regular government employment)",
            "Benefit available for first living child of the family, with additional support for second child if girl"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details", "Mother and Child Protection (MCP) Card", "Marriage Certificate (if applicable)"]
    },
    {
        "name": "Janani Suraksha Yojana (JSY)",
        "occupation": "Pregnant Women",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Safe motherhood intervention promoting institutional delivery among pregnant women to reduce maternal and neonatal mortality.",
        "benefits": [
            "Cash assistance for institutional delivery (amount varies by rural/urban area)",
            "Free delivery including caesarean section in government facilities",
            "Free transport from home to health institution"
        ],
        "eligibility": [
            "All pregnant women delivering in government or accredited private health facilities",
            "Special focus on women from BPL families and low-performing states"
        ],
        "documents": ["Aadhaar Card", "BPL Card (if applicable)", "Bank Account Details", "Antenatal Checkup Records"]
    },
    {
        "name": "Janani Shishu Suraksha Karyakram (JSSK)",
        "occupation": "Pregnant Women",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides free and cashless services to pregnant women and sick infants in government health institutions.",
        "benefits": [
            "Free delivery including caesarean section",
            "Free medicines, diagnostics, and diet during stay at hospital",
            "Free transport to and from health facility, including referral transport"
        ],
        "eligibility": [
            "All pregnant women delivering in public health institutions",
            "Sick newborn infants up to 1 year of age"
        ],
        "documents": ["Aadhaar Card", "MCP Card"]
    },
    {
        "name": "SUMAN (Surakshit Matritva Aashwasan) Scheme",
        "occupation": "Pregnant Women",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Ensures dignified, respectful, and quality healthcare at no cost for every woman and newborn visiting public health facilities.",
        "benefits": [
            "Zero expense for delivery and related services",
            "Guaranteed services with assured quality and zero tolerance for denial of services",
            "Free treatment for complications during pregnancy and post-delivery"
        ],
        "eligibility": [
            "All pregnant women and newborns up to 6 months at public health facilities"
        ],
        "documents": ["Aadhaar Card", "MCP Card"]
    },
    {
        "name": "Pradhan Mantri Surakshit Matritva Abhiyan (PMSMA)",
        "occupation": "Pregnant Women",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides free, fixed-day antenatal care services to pregnant women on the 9th of every month at government health facilities.",
        "benefits": [
            "Free antenatal checkups including ultrasound and lab tests",
            "Identification and management of high-risk pregnancies",
            "Counselling on nutrition and danger signs"
        ],
        "eligibility": [
            "All pregnant women, especially those in 2nd/3rd trimester"
        ],
        "documents": ["Aadhaar Card", "MCP Card"]
    },
    {
        "name": "Sukanya Samriddhi Yojana",
        "occupation": "Any",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Small savings scheme for the girl child to encourage parents to build a fund for her future education and marriage expenses.",
        "benefits": [
            "High interest rate compared to regular savings accounts (revised periodically)",
            "Tax benefits under Section 80C",
            "Partial withdrawal allowed for higher education at age 18"
        ],
        "eligibility": [
            "Girl child below 10 years of age",
            "Account can be opened by parents or legal guardian",
            "Maximum two accounts per family (exceptions for twins/triplets)"
        ],
        "documents": ["Birth Certificate of Girl Child", "Aadhaar Card of Guardian", "Address Proof"]
    },
    {
        "name": "Beti Bachao Beti Padhao",
        "occupation": "Any",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "National campaign to address declining child sex ratio and promote education and welfare of the girl child.",
        "benefits": [
            "Awareness generation and advocacy for girl child welfare",
            "Convergence with schemes like Sukanya Samriddhi Yojana",
            "Multi-sectoral interventions in select districts"
        ],
        "eligibility": [
            "Applicable to families with a girl child, especially in focus districts"
        ],
        "documents": ["Aadhaar Card", "Birth Certificate"]
    },

    # ============================================================
    # LABOURER / UNORGANIZED WORKER SCHEMES (with full details)
    # ============================================================
    {
        "name": "e-Shram Card Scheme",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Creates a national database of unorganized workers to enable them to access social security and welfare schemes.",
        "benefits": [
            "Unique 12-digit Universal Account Number (UAN)",
            "Accidental insurance cover of ₹2 lakh under PMSBY",
            "Access to various social security schemes through linked database"
        ],
        "eligibility": [
            "Unorganized sector workers aged 16-59 years",
            "Not a member of EPFO/ESIC or an income tax payer"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details", "Mobile Number"]
    },
    {
        "name": "Pradhan Mantri Shram Yogi Maandhan (PM-SYM)",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": 180000,
        "overview": "Voluntary and contributory pension scheme for unorganized workers providing a minimum monthly pension after age 60.",
        "benefits": [
            "Minimum assured pension of ₹3,000 per month after age 60",
            "Government contributes equal matching share",
            "Spouse entitled to continuation of pension"
        ],
        "eligibility": [
            "Unorganized workers aged 18-40 years",
            "Monthly income up to ₹15,000",
            "Not covered under EPFO/ESIC/NPS"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details", "e-Shram Card"]
    },
    {
        "name": "Building and Other Construction Workers (BOCW) Welfare Scheme",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides welfare measures for construction workers including health, education, and financial assistance through state welfare boards.",
        "benefits": [
            "Financial assistance for medical treatment and accidents",
            "Scholarships for children of construction workers",
            "Pension and maternity benefits for registered workers"
        ],
        "eligibility": [
            "Construction workers aged 18-60 years who have worked at least 90 days in a year",
            "Registration with state BOCW welfare board"
        ],
        "documents": ["Aadhaar Card", "Proof of Construction Work (90 days)", "Bank Account Details", "Photograph"]
    },
    {
        "name": "Pradhan Mantri Suraksha Bima Yojana (PMSBY)",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Accidental insurance scheme offering coverage for death or disability due to accident at a very low premium.",
        "benefits": [
            "₹2 lakh cover for accidental death and full disability",
            "₹1 lakh cover for partial disability",
            "Annual premium of just ₹20"
        ],
        "eligibility": [
            "Individuals aged 18-70 years with a bank account",
            "Auto-debit consent for premium payment"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details"]
    },
    {
        "name": "Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Life insurance scheme offering renewable one-year coverage for death due to any reason at an affordable premium.",
        "benefits": [
            "₹2 lakh life cover in case of death due to any cause",
            "Annual premium of ₹436 (subject to revision)",
            "Renewable every year"
        ],
        "eligibility": [
            "Individuals aged 18-50 years with a bank account",
            "Auto-debit consent for premium payment"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details"]
    },
    {
        "name": "Atal Pension Yojana (APY)",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Government-backed pension scheme for unorganized sector workers offering guaranteed minimum monthly pension after age 60.",
        "benefits": [
            "Guaranteed monthly pension of ₹1,000 to ₹5,000 after age 60 based on contribution",
            "Government co-contribution for eligible subscribers (for limited period)",
            "Spouse and nominee benefits in case of subscriber's death"
        ],
        "eligibility": [
            "Indian citizens aged 18-40 years with a savings bank account",
            "Should not be a member of any statutory social security scheme"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details", "Age Proof"]
    },
    {
        "name": "National Pension Scheme for Traders and Self Employed (NPS-Traders)",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": 180000,
        "overview": "Pension scheme for small shopkeepers, retail traders, and self-employed persons providing minimum assured pension at age 60.",
        "benefits": [
            "Minimum assured pension of ₹3,000 per month after age 60",
            "Government matching contribution",
            "Family pension for spouse"
        ],
        "eligibility": [
            "Small shopkeepers and self-employed persons aged 18-40 years",
            "Annual turnover not exceeding ₹1.5 crore"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details", "Shop/Business Registration"]
    },

    # ============================================================
    # BUSINESS OWNER / SELF-EMPLOYED SCHEMES (with full details)
    # ============================================================
    {
        "name": "PM Vishwakarma Yojana",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Supports traditional artisans and craftspeople across 18 trades with recognition, skill training, toolkit incentive, and collateral-free credit.",
        "benefits": [
            "₹15,000 toolkit incentive for upgrading equipment",
            "Free skill training with ₹500 per day stipend",
            "Collateral-free enterprise loan up to ₹3 lakh at 5% interest"
        ],
        "eligibility": [
            "Artisans/craftspeople engaged in one of the 18 notified trades",
            "Aged 18 years or above",
            "Not availed similar schemes like PMEGP, PM SVANidhi, or Mudra in last 5 years",
            "Government employees and their families not eligible"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details", "Trade Proof/Self-declaration"]
    },
    {
        "name": "PM SVANidhi (Street Vendor's AtmaNirbhar Nidhi)",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides affordable working capital loans to street vendors to resume and grow their businesses, with digital payment incentives.",
        "benefits": [
            "First loan up to ₹10,000, with higher subsequent loans up to ₹50,000",
            "Interest subsidy of 7% on timely repayment",
            "UPI-linked RuPay credit card with revolving credit limit up to ₹30,000"
        ],
        "eligibility": [
            "Street vendors with a Certificate of Vending or identified in survey",
            "Vending in urban local body areas"
        ],
        "documents": ["Aadhaar Card", "Certificate of Vending", "Bank Account Details"]
    },
    {
        "name": "Pradhan Mantri Mudra Yojana (PMMY)",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides collateral-free loans to micro and small enterprises for setting up or expanding non-farm income generating activities.",
        "benefits": [
            "Loans up to ₹10 lakh under three categories - Shishu (up to ₹50,000), Kishore (up to ₹5 lakh), Tarun (up to ₹10 lakh)",
            "No collateral required",
            "Flexible repayment terms"
        ],
        "eligibility": [
            "Non-corporate, non-farm small/micro enterprises",
            "Individuals, proprietorship, partnership firms engaged in income-generating activities"
        ],
        "documents": ["Aadhaar Card", "Business Plan/Proof", "Bank Account Details", "Address Proof"]
    },
    {
        "name": "Stand-Up India Scheme",
        "occupation": "Self-Employed",
        "category": "SC",
        "income_limit": None,
        "overview": "Facilitates bank loans for setting up greenfield enterprises in manufacturing, services, or trading sectors for SC/ST and women entrepreneurs.",
        "benefits": [
            "Composite loans between ₹10 lakh and ₹1 crore",
            "Handholding support for application, registration, and credit linkage",
            "Covers 75% of project cost (other contributions from promoter and government schemes)"
        ],
        "eligibility": [
            "SC/ST and/or women entrepreneurs above 18 years of age",
            "Setting up a new (greenfield) enterprise"
        ],
        "documents": ["Aadhaar Card", "Caste Certificate (if applicable)", "Business Plan", "Bank Account Details"]
    },
    {
        "name": "Prime Minister's Employment Generation Programme (PMEGP)",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Credit-linked subsidy program for setting up new micro-enterprises in manufacturing and service sectors to generate self-employment.",
        "benefits": [
            "Subsidy of 15-35% of project cost depending on category and area",
            "Maximum project cost ₹50 lakh for manufacturing and ₹20 lakh for service sector",
            "Higher subsidy for SC/ST/women/ex-servicemen and special category states"
        ],
        "eligibility": [
            "Individuals above 18 years of age",
            "Minimum VIII standard pass for projects above ₹10 lakh (manufacturing) or ₹5 lakh (service)"
        ],
        "documents": ["Aadhaar Card", "Educational Qualification Certificate", "Project Report", "Caste Certificate (if applicable)"]
    },
    {
        "name": "Udyam Registration (MSME)",
        "occupation": "Business Owner",
        "category": "Any",
        "income_limit": None,
        "overview": "Free online registration for Micro, Small, and Medium Enterprises to avail government benefits, subsidies, and priority sector lending.",
        "benefits": [
            "Access to collateral-free loans under credit guarantee schemes",
            "Priority in government tenders and procurement",
            "Eligibility for various subsidy schemes and protection against delayed payments"
        ],
        "eligibility": [
            "Any enterprise meeting MSME investment and turnover criteria"
        ],
        "documents": ["Aadhaar Card", "PAN Card", "Business Address Proof", "Bank Account Details"]
    },
    {
        "name": "Credit Guarantee Fund Trust for Micro and Small Enterprises (CGTMSE)",
        "occupation": "Business Owner",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides credit guarantee cover to banks for collateral-free loans extended to micro and small enterprises.",
        "benefits": [
            "Collateral-free credit up to ₹5 crore",
            "Guarantee cover up to 85% for micro enterprises",
            "Encourages banks to lend to MSEs without security"
        ],
        "eligibility": [
            "New and existing micro and small enterprises (manufacturing or service)"
        ],
        "documents": ["Udyam Registration Certificate", "PAN Card", "Business Plan", "Bank Account Details"]
    },
    {
        "name": "Startup India Scheme",
        "occupation": "Business Owner",
        "category": "Any",
        "income_limit": None,
        "overview": "Initiative to build a strong ecosystem for nurturing innovation and startups, providing tax benefits and easier compliance.",
        "benefits": [
            "Income tax exemption for 3 consecutive years",
            "Self-certification under labour and environment laws",
            "Fast-track patent examination with up to 80% rebate on fees"
        ],
        "eligibility": [
            "Entity incorporated as private limited company, LLP, or partnership firm",
            "Turnover not exceeding ₹100 crore in any financial year",
            "Working towards innovation/improvement of products or processes"
        ],
        "documents": ["Certificate of Incorporation", "PAN Card", "Director/Partner Details", "Business Description"]
    },

    # ============================================================
    # GOVERNMENT EMPLOYEE SCHEMES (with full details)
    # ============================================================
    {
        "name": "National Pension System (NPS) for Government Employees",
        "occupation": "Government Employee",
        "category": "Any",
        "income_limit": None,
        "overview": "Mandatory pension scheme for government employees (joined after 2004) providing market-linked retirement savings.",
        "benefits": [
            "Employer contribution of 14% of basic salary plus DA",
            "Tax benefits under Section 80CCD",
            "Choice of investment options (equity, corporate bonds, government securities)"
        ],
        "eligibility": [
            "Central/state government employees who joined service on or after January 1, 2004"
        ],
        "documents": ["Aadhaar Card", "PAN Card", "Employment ID", "Bank Account Details"]
    },
    {
        "name": "Central Government Health Scheme (CGHS)",
        "occupation": "Government Employee",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides comprehensive medical care to central government employees, pensioners, and their dependents.",
        "benefits": [
            "Cashless treatment at empanelled hospitals and CGHS dispensaries",
            "Coverage for outpatient, inpatient, and emergency care",
            "Coverage continues post-retirement for pensioners"
        ],
        "eligibility": [
            "Serving and retired central government employees and their dependents"
        ],
        "documents": ["CGHS Card", "Aadhaar Card", "Employment/Pension Certificate"]
    },
    {
        "name": "Group Insurance Scheme for Central Government Employees (CGEGIS)",
        "occupation": "Government Employee",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides life insurance coverage along with a savings component to central government employees.",
        "benefits": [
            "Insurance cover based on employee group/grade",
            "Savings fund accumulated with interest, payable on retirement/death",
            "Low monthly premium deducted from salary"
        ],
        "eligibility": [
            "All regular central government employees"
        ],
        "documents": ["Employment ID", "Nomination Form", "Bank Account Details"]
    },
    {
        "name": "Leave Travel Concession (LTC) for Government Employees",
        "occupation": "Government Employee",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides reimbursement of travel expenses for government employees to visit their home town or any place in India during leave.",
        "benefits": [
            "Reimbursement of travel fare for self and dependent family members",
            "Available once in a block of two/four years",
            "Covers travel by air, rail, or road as per entitlement"
        ],
        "eligibility": [
            "All regular central government employees and their dependents"
        ],
        "documents": ["Employment ID", "Travel Tickets/Bills", "LTC Application Form"]
    },
    {
        "name": "Mission Karmayogi (NPCSCB)",
        "occupation": "Government Employee",
        "category": "Any",
        "income_limit": None,
        "overview": "National program for civil services capacity building to enhance efficiency through standardized training and digital learning resources.",
        "benefits": [
            "Access to online learning platform (iGOT Karmayogi) with curated courses",
            "Competency-based training framework",
            "Continuous professional development opportunities"
        ],
        "eligibility": [
            "All central government civil service employees"
        ],
        "documents": ["Employment ID", "iGOT Portal Registration"]
    },

    # ============================================================
    # PRIVATE EMPLOYEE SCHEMES (with full details)
    # ============================================================
    {
        "name": "Employees' Provident Fund (EPF)",
        "occupation": "Private Employee",
        "category": "Any",
        "income_limit": None,
        "overview": "Retirement savings scheme where both employee and employer contribute a percentage of salary towards a provident fund corpus.",
        "benefits": [
            "12% of basic salary contributed by both employee and employer",
            "Tax-free interest on accumulated balance",
            "Lump sum withdrawal on retirement, resignation, or for specific needs"
        ],
        "eligibility": [
            "Employees of establishments with 20 or more employees",
            "Salary-based mandatory enrollment criteria apply"
        ],
        "documents": ["Aadhaar Card", "PAN Card", "Bank Account Details", "UAN Number"]
    },
    {
        "name": "Employees' State Insurance (ESI) Scheme",
        "occupation": "Private Employee",
        "category": "Any",
        "income_limit": 21000,
        "overview": "Self-financing social security scheme providing medical, cash, and other benefits to employees and their dependents.",
        "benefits": [
            "Free medical treatment for employee and family",
            "Cash benefits during sickness, maternity, and disability",
            "Dependent benefits in case of death due to employment injury"
        ],
        "eligibility": [
            "Employees earning up to ₹21,000 per month in covered establishments"
        ],
        "documents": ["Aadhaar Card", "ESI Card", "Bank Account Details", "Employment Proof"]
    },
    {
        "name": "Employees' Pension Scheme (EPS)",
        "occupation": "Private Employee",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides pension benefits to employees of the organized sector after retirement, disability, or to family in case of death.",
        "benefits": [
            "Monthly pension after retirement (minimum 10 years of service)",
            "Disability pension regardless of years of service",
            "Widow/family pension benefits"
        ],
        "eligibility": [
            "EPF members who have completed at least 10 years of contributory service"
        ],
        "documents": ["Aadhaar Card", "UAN Number", "Bank Account Details", "Service Certificate"]
    },
    {
        "name": "Atal Bimit Vyakti Kalyan Yojana (ABVKY)",
        "occupation": "Private Employee",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides cash relief to insured persons under ESI who become unemployed involuntarily.",
        "benefits": [
            "Cash relief up to 50% of average wage for up to 90 days of unemployment",
            "Direct bank transfer of benefit amount"
        ],
        "eligibility": [
            "ESI-insured employees who have contributed for at least 2 years before unemployment",
            "Involuntary loss of employment"
        ],
        "documents": ["Aadhaar Card", "ESI Card", "Bank Account Details", "Unemployment Proof"]
    },

    # ============================================================
    # HEALTHCARE SCHEMES (Any occupation, with full details)
    # ============================================================
    {
        "name": "Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (AB PM-JAY)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "World's largest health assurance scheme providing free health coverage for secondary and tertiary hospitalization to economically vulnerable families.",
        "benefits": [
            "Health cover of ₹5 lakh per family per year",
            "Cashless and paperless access to services at empanelled hospitals",
            "Covers pre and post-hospitalization expenses"
        ],
        "eligibility": [
            "Families identified based on deprivation criteria from SECC database",
            "Covers approximately bottom 50% of the population"
        ],
        "documents": ["Aadhaar Card", "Ration Card", "Ayushman Bharat Card"]
    },
    {
        "name": "eSanjeevani (National Telemedicine Service)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Telemedicine platform enabling patients to consult doctors remotely, especially benefiting people in rural and remote areas.",
        "benefits": [
            "Free online doctor consultations",
            "Reduces travel time and cost for medical consultations",
            "Access to specialists not available locally"
        ],
        "eligibility": [
            "All Indian citizens with access to internet/smartphone"
        ],
        "documents": ["Aadhaar Card", "Mobile Number"]
    },
    {
        "name": "National TB Elimination Programme (NTEP)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to eliminate tuberculosis in India through free diagnosis, treatment, and nutritional support for TB patients.",
        "benefits": [
            "Free TB diagnosis and treatment medication",
            "₹500 per month nutritional support under Nikshay Poshan Yojana during treatment",
            "Free follow-up testing"
        ],
        "eligibility": [
            "Any individual diagnosed with TB and registered under Nikshay portal"
        ],
        "documents": ["Aadhaar Card", "Bank Account Details", "Diagnosis Report"]
    },
    {
        "name": "Rashtriya Bal Swasthya Karyakram (RBSK)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Child health screening and early intervention program covering 4 D's - Defects at birth, Deficiencies, Diseases, and Development delays.",
        "benefits": [
            "Free health screening for children aged 0-18 years",
            "Free treatment and management of identified health conditions",
            "Referral support for further management at higher facilities"
        ],
        "eligibility": [
            "Children aged 0-18 years enrolled in anganwadis and government schools"
        ],
        "documents": ["Aadhaar Card", "Birth Certificate", "School/Anganwadi Enrollment Proof"]
    },
    {
        "name": "Pradhan Mantri Jan Dhan Yojana (PMJDY)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Financial inclusion program providing access to banking services, insurance, and credit to all households.",
        "benefits": [
            "Zero-balance savings account",
            "RuPay debit card with accident insurance cover of ₹2 lakh",
            "Overdraft facility up to ₹10,000"
        ],
        "eligibility": [
            "Any Indian citizen above 10 years of age without a bank account"
        ],
        "documents": ["Aadhaar Card", "Address Proof", "Passport Size Photo"]
    },
    {
        "name": "Ayushman Bharat Digital Mission (ABDM)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Creates a digital health ecosystem with unique health IDs to enable seamless access to health records across providers.",
        "benefits": [
            "Unique Ayushman Bharat Health Account (ABHA) ID",
            "Digital storage and sharing of health records with consent",
            "Easier access to healthcare services across providers"
        ],
        "eligibility": [
            "All Indian citizens"
        ],
        "documents": ["Aadhaar Card", "Mobile Number"]
    },

    # ============================================================
    # HOUSING SCHEMES (Any occupation, with full details)
    # ============================================================
    {
        "name": "Pradhan Mantri Awas Yojana - Urban (PMAY-U)",
        "occupation": "Any",
        "category": "EWS",
        "income_limit": 1800000,
        "overview": "Provides affordable housing to urban poor through credit-linked subsidy, beneficiary-led construction, and affordable rental housing.",
        "benefits": [
            "Interest subsidy on home loans under Credit Linked Subsidy Scheme (CLSS)",
            "Direct financial assistance for construction/enhancement of houses",
            "Priority to women, SC/ST, differently-abled, and senior citizens"
        ],
        "eligibility": [
            "Families without a pucca house anywhere in India",
            "Income criteria: EWS up to ₹3 lakh, LIG up to ₹6 lakh, MIG up to ₹18 lakh per annum"
        ],
        "documents": ["Aadhaar Card", "Income Certificate", "Bank Account Details", "Property Documents (if applicable)"]
    },
    {
        "name": "Pradhan Mantri Awas Yojana - Gramin (PMAY-G)",
        "occupation": "Any",
        "category": "EWS",
        "income_limit": None,
        "overview": "Provides financial assistance for construction of pucca houses to homeless and houseless families in rural areas.",
        "benefits": [
            "Financial assistance of ₹1.2 lakh (plains) / ₹1.3 lakh (hilly/difficult areas)",
            "Convergence with MGNREGA for unskilled labor wages",
            "Toilet construction support under Swachh Bharat Mission"
        ],
        "eligibility": [
            "Houseless families or families living in kutcha/dilapidated houses",
            "Identified through Socio-Economic Caste Census (SECC) data"
        ],
        "documents": ["Aadhaar Card", "MGNREGA Job Card", "Bank Account Details", "Caste Certificate (if applicable)"]
    },
    {
        "name": "Affordable Rental Housing Complexes (ARHC)",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides affordable rental housing to urban migrants and poor, especially industrial workers and migrant laborers.",
        "benefits": [
            "Rental housing units at affordable rates near work locations",
            "Basic civic amenities included",
            "Reduces commute and housing cost burden for migrant workers"
        ],
        "eligibility": [
            "Urban migrants/poor including industrial workers, students, and laborers"
        ],
        "documents": ["Aadhaar Card", "Employment Proof", "Address Proof"]
    },

    # ============================================================
    # SENIOR CITIZEN SCHEMES (with full details)
    # ============================================================
    {
        "name": "Indira Gandhi National Old Age Pension Scheme (IGNOAPS)",
        "occupation": "Senior Citizen",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides monthly pension to elderly persons living below the poverty line to ensure basic financial security.",
        "benefits": [
            "Monthly pension of ₹200-500 (central share, states may add top-up)",
            "Direct bank/post office transfer"
        ],
        "eligibility": [
            "Persons aged 60 years or above belonging to BPL households"
        ],
        "documents": ["Aadhaar Card", "Age Proof", "BPL Certificate", "Bank Account Details"]
    },
    {
        "name": "Pradhan Mantri Vaya Vandana Yojana (PMVVY)",
        "occupation": "Senior Citizen",
        "category": "Any",
        "income_limit": None,
        "overview": "Pension scheme for senior citizens providing assured returns on a lump sum investment through LIC.",
        "benefits": [
            "Guaranteed pension based on chosen payout frequency (monthly/quarterly/annual)",
            "Loan facility available after 3 policy years",
            "Pension for 10 years with return of purchase price on maturity/death"
        ],
        "eligibility": [
            "Senior citizens aged 60 years and above"
        ],
        "documents": ["Aadhaar Card", "Age Proof", "Bank Account Details"]
    },
    {
        "name": "Rashtriya Vayoshri Yojana (RVY)",
        "occupation": "Senior Citizen",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides aids and assisted-living devices to senior citizens belonging to BPL category suffering from age-related disabilities.",
        "benefits": [
            "Free distribution of aids like walking sticks, wheelchairs, hearing aids, spectacles",
            "Improves mobility and quality of life for elderly"
        ],
        "eligibility": [
            "Senior citizens aged 60 years and above belonging to BPL category"
        ],
        "documents": ["Aadhaar Card", "Age Proof", "BPL Certificate"]
    },
    {
        "name": "Senior Citizens Savings Scheme (SCSS)",
        "occupation": "Senior Citizen",
        "category": "Any",
        "income_limit": None,
        "overview": "Government-backed savings scheme offering attractive interest rates for senior citizens to ensure regular income post-retirement.",
        "benefits": [
            "Higher interest rate compared to regular savings accounts (revised quarterly)",
            "Quarterly interest payout",
            "Tax benefits under Section 80C on deposit"
        ],
        "eligibility": [
            "Individuals aged 60 years and above",
            "Retired civilian employees aged 55-60 years (under certain conditions)"
        ],
        "documents": ["Aadhaar Card", "Age Proof", "PAN Card", "Bank/Post Office Account Details"]
    },

    # ============================================================
    # SC / ST / OBC SPECIFIC SCHEMES (with full details)
    # ============================================================
    {
        "name": "National Overseas Scholarship for SC Students",
        "occupation": "Student",
        "category": "SC",
        "income_limit": 800000,
        "overview": "Provides financial assistance to SC students for pursuing higher studies (Masters/PhD) abroad in select fields.",
        "benefits": [
            "Full financial support including tuition fees, living expenses, and travel",
            "Covers approved courses at recognized foreign universities"
        ],
        "eligibility": [
            "SC students with minimum qualifying marks in relevant degree",
            "Family income up to ₹8 lakh per annum",
            "Age limit applicable as per notification"
        ],
        "documents": ["Aadhaar Card", "Caste Certificate", "Income Certificate", "Admission Letter from Foreign University", "Passport"]
    },
    {
        "name": "Dr. Ambedkar Pre-Matric and Post-Matric Scholarship for OBC",
        "occupation": "Student",
        "category": "OBC",
        "income_limit": 250000,
        "overview": "Financial assistance to OBC students at pre-matric and post-matric levels to reduce dropout rates and support continuation of education.",
        "benefits": [
            "Maintenance allowance and reimbursement of tuition/ad-hoc fees",
            "Additional support for hostellers"
        ],
        "eligibility": [
            "Students belonging to OBC category",
            "Family income less than ₹2.5 lakh per annum"
        ],
        "documents": ["Aadhaar Card", "OBC Certificate", "Income Certificate", "Previous Marksheet", "Bank Account Details"]
    },
    {
        "name": "Venture Capital Fund for SC (VCF-SC)",
        "occupation": "Business Owner",
        "category": "SC",
        "income_limit": None,
        "overview": "Provides equity/quasi-equity support to SC entrepreneurs for setting up greenfield ventures and growing existing businesses.",
        "benefits": [
            "Equity investment in viable SC-owned businesses",
            "Support for business expansion and modernization",
            "Mentorship and handholding support"
        ],
        "eligibility": [
            "SC entrepreneurs with viable business plans",
            "Company should have majority SC ownership"
        ],
        "documents": ["Aadhaar Card", "Caste Certificate", "Business Plan", "Company Registration Documents"]
    },
    {
        "name": "Pradhan Mantri Adi Adarsh Gram Yojana (PMAAGY)",
        "occupation": "Any",
        "category": "ST",
        "income_limit": None,
        "overview": "Aims to develop model villages with majority tribal population by providing basic infrastructure and livelihood support.",
        "benefits": [
            "Improved infrastructure - roads, drinking water, electricity",
            "Convergence of schemes for health, education, and livelihood",
            "Skill development and livelihood opportunities"
        ],
        "eligibility": [
            "Residents of villages with significant Scheduled Tribe population identified under the scheme"
        ],
        "documents": ["Aadhaar Card", "Tribe Certificate", "Residence Proof"]
    },
    {
        "name": "Eklavya Model Residential Schools (EMRS)",
        "occupation": "Student",
        "category": "ST",
        "income_limit": None,
        "overview": "Provides quality residential education to tribal students from class 6 to 12 with focus on overall development.",
        "benefits": [
            "Free quality education with hostel facility",
            "Focus on preserving local art and culture along with academics",
            "Sports and skill development opportunities"
        ],
        "eligibility": [
            "Students belonging to Scheduled Tribe communities",
            "Admission through entrance test, primarily in areas with significant ST population"
        ],
        "documents": ["Aadhaar Card", "Tribe Certificate", "Previous School Records", "Birth Certificate"]
    },
    {
        "name": "Stand Up India - Women Entrepreneurs",
        "occupation": "Self-Employed",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Facilitates bank loans for women entrepreneurs setting up greenfield enterprises with handholding support.",
        "benefits": [
            "Composite loans between ₹10 lakh and ₹1 crore",
            "Handholding support for DPR preparation, registration, and credit linkage",
            "Margin money support up to 25% of project cost"
        ],
        "eligibility": [
            "Women entrepreneurs above 18 years of age",
            "Setting up a new (greenfield) enterprise in manufacturing, services, or trading"
        ],
        "documents": ["Aadhaar Card", "Business Plan", "Bank Account Details"]
    },

    # ============================================================
    # ADDITIONAL SCHEMES - Reaching 130 entries
    # (Name + occupation/category for matching; generic overview)
    # ============================================================
    {
        "name": "Pradhan Mantri Kaushal Vikas Yojana (PMKVY)",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Flagship skill development scheme enabling youth to take up industry-relevant skill training to secure better livelihood.",
        "benefits": ["Free skill training in various trades", "Certification recognized by industry", "Placement assistance after training"],
        "eligibility": ["Unemployed youth and school/college dropouts aged 15-45 years"],
        "documents": ["Aadhaar Card", "Educational Certificates", "Bank Account Details"]
    },
    {
        "name": "Deen Dayal Upadhyaya Grameen Kaushalya Yojana (DDU-GKY)",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Skill development and placement program for rural youth from poor families to provide sustainable employment.",
        "benefits": ["Free residential/non-residential skill training", "Placement in jobs with regular wages", "Post-placement support"],
        "eligibility": ["Rural youth aged 15-35 years from poor families"],
        "documents": ["Aadhaar Card", "Income Certificate", "Bank Account Details"]
    },
    {
        "name": "MGNREGA (Mahatma Gandhi National Rural Employment Guarantee Act)",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Guarantees 100 days of wage employment in a financial year to rural households whose adult members volunteer for unskilled manual work.",
        "benefits": ["Guaranteed 100 days of employment per household", "Minimum wages as notified by state", "Work within 5 km of residence"],
        "eligibility": ["Adult members of rural households willing to do unskilled manual work"],
        "documents": ["Aadhaar Card", "Job Card", "Bank Account Details"]
    },
    {
        "name": "Deendayal Antyodaya Yojana - National Urban Livelihoods Mission (DAY-NULM)",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides skill training, self-employment support, and shelter for urban poor and homeless populations.",
        "benefits": ["Skill training and credit linkage for self-employment", "Support for street vendors", "Shelter for urban homeless"],
        "eligibility": ["Urban poor identified through surveys"],
        "documents": ["Aadhaar Card", "Income Certificate", "Bank Account Details"]
    },
    {
        "name": "National Rural Livelihood Mission (NRLM)",
        "occupation": "Self-Employed",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Promotes self-employment and organization of rural poor into Self Help Groups for livelihood enhancement.",
        "benefits": ["Access to low-interest credit through SHGs", "Skill training for livelihood activities", "Market linkage support"],
        "eligibility": ["Rural poor women, preferably members of Self Help Groups"],
        "documents": ["Aadhaar Card", "SHG Membership", "Bank Account Details"]
    },
    {
        "name": "PM Surya Ghar Muft Bijli Yojana",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides subsidy for rooftop solar installation to households to reduce electricity bills and promote renewable energy.",
        "benefits": ["Subsidy up to ₹78,000 for rooftop solar systems", "Up to 300 units free electricity per month", "Reduced dependence on grid power"],
        "eligibility": ["Households with suitable rooftop space for solar installation"],
        "documents": ["Aadhaar Card", "Electricity Bill", "Bank Account Details"]
    },
    {
        "name": "Ujjwala Yojana (Pradhan Mantri Ujjwala Yojana - PMUY)",
        "occupation": "Any",
        "category": "EWS",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides LPG connections to women from BPL households to promote clean cooking fuel and reduce health hazards.",
        "benefits": ["Free LPG gas connection", "Subsidy on LPG cylinder refills", "Improved health due to clean cooking fuel"],
        "eligibility": ["Women from BPL households without an existing LPG connection"],
        "documents": ["Aadhaar Card", "BPL Certificate", "Address Proof", "Bank Account Details"]
    },
    {
        "name": "Jal Jeevan Mission",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to provide functional household tap water connections to every rural household across India.",
        "benefits": ["Piped water supply connection to households", "Improved access to safe drinking water", "Reduced water-borne diseases"],
        "eligibility": ["Rural households without piped water connection"],
        "documents": ["Aadhaar Card", "Address Proof"]
    },
    {
        "name": "Swachh Bharat Mission (Gramin)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to achieve open-defecation-free rural India through construction of household and community toilets.",
        "benefits": ["Financial incentive for toilet construction (up to ₹12,000)", "Improved sanitation and hygiene awareness"],
        "eligibility": ["Rural households without access to toilet facility"],
        "documents": ["Aadhaar Card", "Bank Account Details", "Address Proof"]
    },
    {
        "name": "Deendayal Disabled Rehabilitation Scheme (DDRS)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides financial assistance to NGOs for rehabilitation services to persons with disabilities through education and training.",
        "benefits": ["Access to special schools and vocational training centers", "Rehabilitation aids and assistive devices", "Community-based rehabilitation programs"],
        "eligibility": ["Persons with disabilities accessing services through registered NGOs"],
        "documents": ["Aadhaar Card", "Disability Certificate"]
    },
    {
        "name": "Accessible India Campaign (Sugamya Bharat Abhiyan)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Nationwide flagship campaign to enhance accessibility for persons with disabilities in built environment, transport, and ICT.",
        "benefits": ["Improved physical accessibility in public buildings", "Accessible transport systems", "Accessible websites and digital content"],
        "eligibility": ["Persons with disabilities; benefits accrue to general public infrastructure"],
        "documents": ["Disability Certificate (where applicable)"]
    },
    {
        "name": "National Handicapped Finance and Development Corporation (NHFDC) Loan Scheme",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides concessional loans to persons with disabilities for self-employment and skill development.",
        "benefits": ["Loans at concessional interest rates for income-generating activities", "Support for education loans for disabled students", "Skill development loan support"],
        "eligibility": ["Persons with disabilities (40% or more) above 18 years of age"],
        "documents": ["Aadhaar Card", "Disability Certificate", "Business/Education Plan", "Bank Account Details"]
    },
    {
        "name": "Vishwakarma Vatsalya Yojana (Artisan Credit Card)",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides credit card facility to artisans and weavers to meet their working capital needs at concessional rates.",
        "benefits": ["Credit limit up to ₹2 lakh", "Concessional interest rates", "Simplified documentation"],
        "eligibility": ["Artisans and craftspersons engaged in production activities"],
        "documents": ["Aadhaar Card", "Artisan Identity Card", "Bank Account Details"]
    },
    {
        "name": "Weavers' Mudra Scheme",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides credit at concessional rates to handloom weavers for working capital and investment needs.",
        "benefits": ["Margin money assistance of 20% of loan amount (up to ₹10,000)", "Interest subvention of 6% for 3 years", "Credit guarantee on loans"],
        "eligibility": ["Individual handloom weavers and members of weaver groups"],
        "documents": ["Aadhaar Card", "Weaver ID Card", "Bank Account Details"]
    },
    {
        "name": "National Handloom Development Programme (NHDP)",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Supports the holistic development of the handloom sector including raw material supply, design, and marketing support.",
        "benefits": ["Financial assistance for raw material procurement", "Design and product development support", "Marketing assistance through exhibitions"],
        "eligibility": ["Handloom weavers and weaver cooperative societies"],
        "documents": ["Aadhaar Card", "Weaver ID Card", "Cooperative Society Membership (if applicable)"]
    },
    {
        "name": "Fisheries and Aquaculture Infrastructure Development Fund (FIDF)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides concessional finance for development of fisheries infrastructure to boost fish production and exports.",
        "benefits": ["Concessional loans for fisheries infrastructure projects", "Interest subvention of up to 3%", "Support for cold chain and processing units"],
        "eligibility": ["Fish farmers, fishery cooperatives, and entrepreneurs in fisheries sector"],
        "documents": ["Aadhaar Card", "Project Proposal", "Bank Account Details"]
    },
    {
        "name": "Pradhan Mantri Matsya Sampada Yojana (PMMSY)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to enhance fish production and productivity through targeted interventions across the fisheries value chain.",
        "benefits": ["Financial assistance for fish farming infrastructure", "Insurance coverage for fishers and fishing vessels", "Support for cold storage and processing"],
        "eligibility": ["Fish farmers, fishers, fish workers, and fisheries cooperatives"],
        "documents": ["Aadhaar Card", "Land/Pond Records", "Bank Account Details"]
    },
    {
        "name": "National Livestock Mission",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to improve livestock productivity through breed improvement, fodder development, and entrepreneurship support.",
        "benefits": ["Subsidy for setting up poultry, sheep/goat, and piggery units", "Financial support for fodder cultivation", "Insurance support for livestock"],
        "eligibility": ["Farmers and entrepreneurs engaged in livestock rearing"],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details"]
    },
    {
        "name": "National Mission on Edible Oils - Oil Palm (NMEO-OP)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Promotes cultivation of oil palm to reduce import dependency on edible oils and increase farmer income.",
        "benefits": ["Financial assistance for planting material and inputs", "Viability price support for fresh fruit bunches", "Support for irrigation infrastructure"],
        "eligibility": ["Farmers in notified oil palm growing states/regions"],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details"]
    },
    {
        "name": "Rashtriya Krishi Vikas Yojana (RKVY)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides flexible funding to states for agriculture and allied sector development based on local needs and priorities.",
        "benefits": ["Funding for state-specific agricultural infrastructure projects", "Support for innovative agri-startups", "Promotes value chain development"],
        "eligibility": ["Farmers benefit through state-implemented projects under this scheme"],
        "documents": ["Aadhaar Card", "Land Records (project-dependent)"]
    },
    {
        "name": "Formation and Promotion of 10,000 FPOs Scheme",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Promotes formation of Farmer Producer Organizations to provide collective bargaining power and economies of scale to small farmers.",
        "benefits": ["Financial support for FPO formation and management cost", "Equity grant matching member equity (up to ₹15 lakh)", "Credit guarantee facility for FPO loans"],
        "eligibility": ["Groups of farmers willing to form a Farmer Producer Organization"],
        "documents": ["Aadhaar Card", "Land Records", "FPO Registration Documents"]
    },
    {
        "name": "Mission Amrit Sarovar",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to develop and rejuvenate water bodies in rural areas to improve water availability for irrigation and groundwater recharge.",
        "benefits": ["Improved irrigation water availability", "Groundwater recharge benefiting nearby agricultural land", "Employment generation during construction"],
        "eligibility": ["Farmers in villages where Amrit Sarovars are developed"],
        "documents": ["Aadhaar Card", "Residence Proof"]
    },
    {
        "name": "Integrated Scheme for Agricultural Marketing (ISAM)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Develops agricultural marketing infrastructure to provide farmers better access to markets and reduce post-harvest losses.",
        "benefits": ["Subsidy for cold storage and warehouse construction", "Grading and standardization facilities", "Market information services"],
        "eligibility": ["Farmers, FPOs, agri-entrepreneurs, and market committees"],
        "documents": ["Aadhaar Card", "Land/Project Documents", "Bank Account Details"]
    },
    {
        "name": "Direct Benefit Transfer (DBT) in Fertilizer",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Ensures fertilizer subsidy benefits reach farmers directly by linking subsidy to point-of-sale transactions.",
        "benefits": ["Subsidized fertilizer available at point of sale", "Transparent and leakage-free subsidy delivery"],
        "eligibility": ["All farmers purchasing fertilizers from registered retailers"],
        "documents": ["Aadhaar Card"]
    },
    {
        "name": "Interest Subvention Scheme for Short Term Crop Loans",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides interest subvention to make short-term crop loans more affordable for farmers.",
        "benefits": ["2% interest subvention on crop loans up to ₹3 lakh", "Additional 3% incentive for prompt repayment"],
        "eligibility": ["Farmers availing short-term crop loans through KCC or other channels"],
        "documents": ["Aadhaar Card", "KCC/Loan Account Details", "Land Records"]
    },
    {
        "name": "Production Linked Incentive (PLI) Scheme for Food Processing",
        "occupation": "Business Owner",
        "category": "Any",
        "income_limit": None,
        "overview": "Incentivizes food processing companies to enhance manufacturing capabilities and create global champions in select food categories.",
        "benefits": ["Incentives linked to incremental sales of eligible products", "Boosts processing infrastructure and export potential"],
        "eligibility": ["Food processing companies meeting minimum investment and turnover criteria"],
        "documents": ["Company Registration", "PAN Card", "Investment Proposal"]
    },
    {
        "name": "Make in India Initiative",
        "occupation": "Business Owner",
        "category": "Any",
        "income_limit": None,
        "overview": "Encourages domestic and foreign companies to manufacture in India through ease of doing business reforms and sector-specific incentives.",
        "benefits": ["Sector-specific investment incentives", "Simplified regulatory processes", "Access to dedicated investment facilitation cells"],
        "eligibility": ["Manufacturing enterprises across eligible sectors"],
        "documents": ["Company Registration", "PAN Card", "GST Registration"]
    },
    {
        "name": "Export Promotion Capital Goods (EPCG) Scheme",
        "occupation": "Business Owner",
        "category": "Any",
        "income_limit": None,
        "overview": "Allows import of capital goods at zero customs duty for producing quality goods for exports.",
        "benefits": ["Zero customs duty on import of capital goods", "Boosts export competitiveness", "Technology upgradation support"],
        "eligibility": ["Exporters with valid Importer-Exporter Code (IEC)"],
        "documents": ["IEC Certificate", "GST Registration", "Export Plan"]
    },
    {
        "name": "Atmanirbhar Bharat Rojgar Yojana (ABRY)",
        "occupation": "Private Employee",
        "category": "Any",
        "income_limit": 15000,
        "overview": "Incentivizes employers to create new jobs and provide social security benefits to new employees by subsidizing EPF contributions.",
        "benefits": ["Government pays employee and employer EPF contributions for 2 years", "Encourages formal employment generation"],
        "eligibility": ["New employees with monthly wages less than ₹15,000 joining EPFO-registered establishments"],
        "documents": ["Aadhaar Card", "UAN Number", "Bank Account Details"]
    },
    {
        "name": "Rashtriya Swasthya Bima Yojana (RSBY)",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Health insurance scheme for BPL families and unorganized sector workers providing hospitalization coverage (now largely subsumed under PM-JAY).",
        "benefits": ["Cashless hospitalization coverage", "Coverage for pre-existing diseases", "Smart card-based access to empanelled hospitals"],
        "eligibility": ["BPL families and unorganized sector workers as per state notifications"],
        "documents": ["Aadhaar Card", "BPL Certificate", "RSBY Smart Card"]
    },
    {
        "name": "Pradhan Mantri Garib Kalyan Yojana (PMGKY)",
        "occupation": "Any",
        "category": "EWS",
        "income_limit": None,
        "overview": "Provides relief to poor and vulnerable sections through free food grains and direct benefit transfers during crisis periods.",
        "benefits": ["Free additional food grains through PDS", "Direct cash transfers to vulnerable groups"],
        "eligibility": ["BPL/EWS families holding valid ration cards"],
        "documents": ["Aadhaar Card", "Ration Card", "Bank Account Details"]
    },
    {
        "name": "Antyodaya Anna Yojana (AAY)",
        "occupation": "Any",
        "category": "EWS",
        "income_limit": None,
        "overview": "Provides highly subsidized food grains to the poorest of the poor families under the Public Distribution System.",
        "benefits": ["35 kg food grains per family per month at highly subsidized rates", "Priority access under PDS"],
        "eligibility": ["Poorest of the poor families identified by state governments"],
        "documents": ["Aadhaar Card", "AAY Ration Card"]
    },
    {
        "name": "One Nation One Ration Card (ONORC)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Allows migrant workers and their families to access subsidized food grains from any Fair Price Shop across India.",
        "benefits": ["Portability of ration card benefits across states", "Ensures food security for migrant workers"],
        "eligibility": ["All ration card holders under National Food Security Act"],
        "documents": ["Aadhaar Card", "Ration Card"]
    },
    {
        "name": "Pradhan Mantri Garib Kalyan Anna Yojana (PMGKAY)",
        "occupation": "Any",
        "category": "EWS",
        "income_limit": None,
        "overview": "Provides additional free food grains to NFSA beneficiaries to ensure food security during economic distress periods.",
        "benefits": ["Additional 5 kg free food grains per person per month", "Covers nearly 80 crore beneficiaries under NFSA"],
        "eligibility": ["Beneficiaries covered under National Food Security Act (NFSA)"],
        "documents": ["Aadhaar Card", "Ration Card"]
    },
    {
        "name": "Integrated Child Development Services (ICDS)",
        "occupation": "Pregnant Women",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides nutrition, health, and early education services to children under 6 years and pregnant/lactating mothers through Anganwadi centers.",
        "benefits": ["Supplementary nutrition for children and mothers", "Health check-ups and immunization referrals", "Pre-school non-formal education for children"],
        "eligibility": ["Pregnant women, lactating mothers, and children up to 6 years"],
        "documents": ["Aadhaar Card", "MCP Card"]
    },
    {
        "name": "Mission Shakti - Sambal and Samarthya",
        "occupation": "Any",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Umbrella scheme for women safety, security, and empowerment covering one-stop centers, helplines, and livelihood support.",
        "benefits": ["24x7 helpline and one-stop centers for women in distress", "Shelter homes for women in difficult circumstances", "Skill development and livelihood support"],
        "eligibility": ["All women, with special focus on women in vulnerable situations"],
        "documents": ["Aadhaar Card"]
    },
    {
        "name": "Working Women Hostel Scheme",
        "occupation": "Private Employee",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides safe and affordable accommodation to working women, especially those away from their home towns, with daycare facilities.",
        "benefits": ["Affordable hostel accommodation near workplace", "Daycare facility for children of working women"],
        "eligibility": ["Working women with income within prescribed limits, including trainees"],
        "documents": ["Aadhaar Card", "Employment Proof", "Income Certificate"]
    },
    {
        "name": "Mahila Shakti Kendra",
        "occupation": "Any",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Empowers rural women through community participation and provides convergent support services for skill development, employment, and digital literacy.",
        "benefits": ["Skill development and employment training", "Digital literacy programs", "Access to health, legal, and other government schemes"],
        "eligibility": ["Rural women, especially in aspirational districts"],
        "documents": ["Aadhaar Card"]
    },
    {
        "name": "Stand-Up India for Transgender Entrepreneurs",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Extends bank loan facilitation for setting up greenfield enterprises to transgender entrepreneurs with handholding support.",
        "benefits": ["Composite loans between ₹10 lakh and ₹1 crore", "Handholding support for application and credit linkage"],
        "eligibility": ["Transgender entrepreneurs above 18 years setting up new enterprises"],
        "documents": ["Aadhaar Card", "Business Plan", "Bank Account Details"]
    },
    {
        "name": "Garib Kalyan Rojgar Abhiyaan",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides employment and livelihood opportunities to returning migrant workers through infrastructure and rural development projects.",
        "benefits": ["Employment generation through 25 different infrastructure works", "Skill mapping of migrant workers for targeted job placement"],
        "eligibility": ["Returning migrant workers in identified districts"],
        "documents": ["Aadhaar Card", "Migration Proof", "Bank Account Details"]
    },
    {
        "name": "National Career Service (NCS) Portal",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Online platform connecting job seekers with employers and providing career counselling and skill development information.",
        "benefits": ["Free job matching and career counselling", "Access to job fairs and skill development programs", "Information on apprenticeships and internships"],
        "eligibility": ["All job seekers can register on the portal"],
        "documents": ["Aadhaar Card", "Educational Certificates"]
    },
    {
        "name": "Apprenticeship Promotion Scheme",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Promotes apprenticeship training in industries by sharing stipend cost with employers for first-year apprentices.",
        "benefits": ["Government shares 25% of prescribed stipend (up to a cap)", "Hands-on industry experience with certification"],
        "eligibility": ["Candidates aged 14-35 years engaged as apprentices in registered establishments"],
        "documents": ["Aadhaar Card", "Educational Certificates", "Apprenticeship Contract"]
    },
    {
        "name": "Skill India Digital Platform",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Unified digital platform offering skilling, education, employment, and entrepreneurship opportunities to youth.",
        "benefits": ["Access to free online courses and certifications", "Job and apprenticeship opportunities", "Career guidance and counselling"],
        "eligibility": ["All Indian youth seeking skill development and employment opportunities"],
        "documents": ["Aadhaar Card", "Mobile Number"]
    },
    {
        "name": "Digital India Land Records Modernization Programme (DILRMP)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Digitizes land records to provide farmers easy access to updated land ownership documents and reduce land disputes.",
        "benefits": ["Online access to land records and maps", "Reduced disputes through updated digital records", "Faster mutation processes"],
        "eligibility": ["Landowning farmers in states implementing the program"],
        "documents": ["Aadhaar Card", "Existing Land Records"]
    },
    {
        "name": "Kisan Rin Portal (KRP)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Digital platform for monitoring agricultural credit flow and ensuring farmers receive interest subvention benefits on crop loans.",
        "benefits": ["Transparent tracking of crop loan disbursement", "Ensures correct interest subvention is applied"],
        "eligibility": ["Farmers availing crop loans through banks"],
        "documents": ["Aadhaar Card", "KCC/Loan Account Details"]
    },
    {
        "name": "Agriculture Mechanization Custom Hiring Centres",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Establishes centers where farmers can rent agricultural machinery at affordable rates instead of purchasing expensive equipment.",
        "benefits": ["Access to modern farm machinery on rent", "Reduces capital investment burden on small farmers"],
        "eligibility": ["Small and marginal farmers in areas with Custom Hiring Centres"],
        "documents": ["Aadhaar Card", "Land Records"]
    },
    {
        "name": "Gramin Bhandaran Yojana (Rural Godown Scheme)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides subsidy for construction of rural godowns to enable farmers to store produce and avoid distress sales.",
        "benefits": ["Capital subsidy of 25-33% on godown construction cost", "Helps farmers avoid distress sale post-harvest"],
        "eligibility": ["Farmers, FPOs, and agri-entrepreneurs constructing storage facilities"],
        "documents": ["Aadhaar Card", "Land Records", "Project Proposal"]
    },
    {
        "name": "National Food Security Mission (NFSM)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to increase production of rice, wheat, pulses, and other crops through area expansion and productivity enhancement.",
        "benefits": ["Subsidy on quality seeds and farm inputs", "Demonstration of improved technologies", "Training and capacity building for farmers"],
        "eligibility": ["Farmers cultivating notified crops under the mission"],
        "documents": ["Aadhaar Card", "Land Records"]
    },
    {
        "name": "Krishi UDAN Scheme",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Facilitates air transportation of perishable agricultural produce to improve farmers' access to distant and export markets.",
        "benefits": ["Subsidized air freight for perishable goods", "Better market access for horticulture and fishery produce"],
        "eligibility": ["Farmers and exporters of perishable agricultural produce"],
        "documents": ["Aadhaar Card", "Produce Documentation"]
    },
    {
        "name": "Pradhan Mantri Annadata Aay SanraksHan Abhiyan (PM-AASHA)",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Ensures remunerative prices to farmers for their produce through price support, deficiency payment, and procurement schemes.",
        "benefits": ["Procurement at Minimum Support Price (MSP)", "Compensation for price difference under deficiency payment scheme"],
        "eligibility": ["Farmers selling notified crops during procurement season"],
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details"]
    },
    {
        "name": "Coaching Scheme for SC/ST/OBC/Minorities for Competitive Exams",
        "occupation": "Student",
        "category": "SC",
        "income_limit": 800000,
        "overview": "Provides free coaching to students from SC, ST, OBC, and minority communities for various competitive examinations.",
        "benefits": ["Free coaching for exams like UPSC, SSC, banking, and entrance tests", "Study material and mock test support"],
        "eligibility": ["Students from SC/ST/OBC/minority communities with family income within prescribed limits"],
        "documents": ["Aadhaar Card", "Caste/Community Certificate", "Income Certificate", "Educational Certificates"]
    },
    {
        "name": "Top Class Education Scheme for SC Students",
        "occupation": "Student",
        "category": "SC",
        "income_limit": 800000,
        "overview": "Provides full financial support to SC students for studying in identified top-class higher education institutions.",
        "benefits": ["Full tuition fee reimbursement at notified premier institutions", "Maintenance allowance for living expenses"],
        "eligibility": ["SC students admitted to notified institutes of excellence", "Family income up to ₹8 lakh per annum"],
        "documents": ["Aadhaar Card", "Caste Certificate", "Income Certificate", "Admission Proof"]
    },
    {
        "name": "Free Coaching for SC and OBC Students (Ministry of Social Justice)",
        "occupation": "Student",
        "category": "OBC",
        "income_limit": 800000,
        "overview": "Provides free coaching for SC and OBC students for entrance examinations to professional courses and recruitment exams.",
        "benefits": ["Free coaching classes for technical and competitive exams", "Stipend during coaching period"],
        "eligibility": ["SC/OBC students within prescribed income limits"],
        "documents": ["Aadhaar Card", "Caste Certificate", "Income Certificate"]
    },
    {
        "name": "Pre-Matric Scholarship for Children of Workers in Hazardous Occupations",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Supports education of children of workers engaged in hazardous occupations to prevent child labour and promote schooling.",
        "benefits": ["Monthly scholarship for school education", "Reduces dependency on child labour for family income"],
        "eligibility": ["Children of workers in identified hazardous occupations, studying in classes 1-10"],
        "documents": ["Aadhaar Card", "Parent's Employment/Occupation Proof", "School Enrollment Proof"]
    },
    {
        "name": "Mid-Day Meal Scheme (PM POSHAN)",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides free hot cooked meals to children studying in government and government-aided schools to improve nutrition and attendance.",
        "benefits": ["Free nutritious meal on all school working days", "Improves enrollment, attendance, and retention rates"],
        "eligibility": ["Students studying in government and government-aided schools (classes 1-8)"],
        "documents": ["School Enrollment Proof"]
    },
    {
        "name": "Samagra Shiksha Abhiyan",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Integrated scheme for school education covering pre-school to senior secondary level to ensure equitable and inclusive quality education.",
        "benefits": ["Free textbooks and uniforms for eligible students", "Infrastructure development in schools", "Support for digital education initiatives"],
        "eligibility": ["Students enrolled in government schools, with focus on disadvantaged groups"],
        "documents": ["Aadhaar Card", "School Enrollment Proof"]
    },
    {
        "name": "National Means-cum-Merit Scholarship Scheme (NMMSS)",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 350000,
        "overview": "Provides scholarships to meritorious students from economically weaker sections to reduce dropout rate at secondary stage.",
        "benefits": ["₹12,000 per annum scholarship for classes 9-12", "Direct transfer to student's bank account"],
        "eligibility": ["Students who cleared class 8 with minimum 55% marks", "Family income less than ₹3.5 lakh per annum"],
        "documents": ["Aadhaar Card", "Income Certificate", "Class 7/8 Marksheet", "Bank Account Details"]
    },
    {
        "name": "Kishore Vaigyanik Protsahan Yojana (KVPY)",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Encourages students with talent and aptitude for research to pursue careers in basic sciences through fellowships.",
        "benefits": ["Monthly fellowship for undergraduate and postgraduate studies in science", "Annual contingency grant for research expenses"],
        "eligibility": ["Students in class 11 onwards with strong aptitude for scientific research"],
        "documents": ["Aadhaar Card", "Academic Records", "Bank Account Details"]
    },
    {
        "name": "Begum Hazrat Mahal National Scholarship",
        "occupation": "Student",
        "category": "Any",
        "gender": "Female",
        "income_limit": 200000,
        "overview": "Provides scholarships to meritorious girl students from minority communities for studying in classes 9 to 12.",
        "benefits": ["Annual scholarship amount for educational expenses", "Encourages higher secondary education completion for minority girls"],
        "eligibility": ["Girl students from notified minority communities studying in classes 9-12", "Minimum 50% marks in previous examination", "Family income up to ₹2 lakh per annum"],
        "documents": ["Aadhaar Card", "Minority Community Certificate", "Income Certificate", "Previous Marksheet"]
    },
    {
        "name": "Ishan Uday Special Scholarship Scheme for North Eastern Region",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 450000,
        "overview": "Provides scholarships to students from North Eastern states for pursuing general degree level and professional courses.",
        "benefits": ["₹5,400 per month for general courses, higher for professional courses", "Covers tuition and other essential fees"],
        "eligibility": ["Students from North Eastern states admitted to recognized institutions", "Family income up to ₹4.5 lakh per annum"],
        "documents": ["Aadhaar Card", "Domicile Certificate", "Income Certificate", "Admission Proof"]
    },
    {
        "name": "Cycle Distribution Scheme for Girl Students",
        "occupation": "Student",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides bicycles to girl students transitioning to secondary school to reduce dropout rates and improve attendance.",
        "benefits": ["Free bicycle for commuting to school", "Reduces travel time and improves school attendance"],
        "eligibility": ["Girl students promoted to class 9 in government schools"],
        "documents": ["Aadhaar Card", "School Enrollment Proof"]
    },
    {
        "name": "Free Laptop/Tablet Distribution Scheme for Meritorious Students",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides laptops or tablets to meritorious students to support digital learning and bridge the digital divide.",
        "benefits": ["Free laptop/tablet for eligible meritorious students", "Promotes access to digital learning resources"],
        "eligibility": ["Students achieving merit criteria as per state notification (varies by state)"],
        "documents": ["Aadhaar Card", "Marksheet", "School/College Enrollment Proof"]
    },
    {
        "name": "Vidya Lakshmi Education Loan Portal",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Single-window platform for students to apply for education loans and scholarships from various banks and government schemes.",
        "benefits": ["Single application for multiple education loan providers", "Track application status online", "Access to information on scholarships"],
        "eligibility": ["Students seeking education loans for higher studies in India or abroad"],
        "documents": ["Aadhaar Card", "Admission Letter", "Income Certificate", "PAN Card"]
    },
    {
        "name": "Padho Pardesh Scheme (Interest Subsidy on Education Loans for Minorities)",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 600000,
        "overview": "Provides interest subsidy on education loans for students from minority communities pursuing higher studies abroad.",
        "benefits": ["Full interest subsidy during moratorium period of education loan", "Encourages overseas higher education for minority students"],
        "eligibility": ["Students from notified minority communities with admission to foreign institutions", "Family income up to ₹6 lakh per annum"],
        "documents": ["Aadhaar Card", "Minority Community Certificate", "Income Certificate", "Loan Sanction Letter", "Admission Letter"]
    },
    {
        "name": "Atal Innovation Mission - ATL (Atal Tinkering Labs)",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Establishes innovation labs in schools to cultivate curiosity, creativity, and innovation among young students.",
        "benefits": ["Access to tools and equipment for hands-on learning (robotics, IoT, 3D printing)", "Mentorship for innovative projects and ideas"],
        "eligibility": ["Students of schools selected for Atal Tinkering Lab setup"],
        "documents": ["School Enrollment Proof"]
    },
    {
        "name": "Rashtriya Madhyamik Shiksha Abhiyan (RMSA)",
        "occupation": "Student",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to enhance access to quality secondary education and improve enrollment for classes 9-12 (now part of Samagra Shiksha).",
        "benefits": ["Infrastructure improvement in secondary schools", "Additional classrooms, labs, and libraries", "Teacher training programs"],
        "eligibility": ["Students enrolled in government secondary schools"],
        "documents": ["School Enrollment Proof"]
    },
    {
        "name": "Nai Manzil Scheme",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides educational and skill training to minority youth who lack formal education or dropped out of school.",
        "benefits": ["Bridge education to mainstream school/college", "Skill training with certification", "Placement assistance"],
        "eligibility": ["Minority youth aged 17-35 years who are school dropouts or without formal education"],
        "documents": ["Aadhaar Card", "Minority Community Certificate"]
    },
    {
        "name": "Seekho Aur Kamao (Learn and Earn) Scheme",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides skill development training to minority youth to improve their employability in various trades.",
        "benefits": ["Free skill training in market-relevant trades", "Stipend during training period", "Placement support post-training"],
        "eligibility": ["Minority community youth aged 14-35 years"],
        "documents": ["Aadhaar Card", "Minority Community Certificate"]
    },
    {
        "name": "Hamari Dharti Hamara Parivar Scheme",
        "occupation": "Farmer",
        "category": "Any",
        "income_limit": None,
        "overview": "Promotes sustainable agriculture practices through awareness campaigns and farmer training on natural farming methods.",
        "benefits": ["Training on natural and chemical-free farming methods", "Reduced input costs through organic alternatives"],
        "eligibility": ["Farmers willing to adopt natural farming practices"],
        "documents": ["Aadhaar Card", "Land Records"]
    },
    {
        "name": "Pradhan Mantri Van Dhan Yojana",
        "occupation": "Self-Employed",
        "category": "ST",
        "income_limit": None,
        "overview": "Promotes value addition to minor forest produce collected by tribal gatherers through formation of Van Dhan Vikas Kendras.",
        "benefits": ["Training in value addition and processing of forest produce", "Marketing support through MFP centers", "Additional income for tribal collectors"],
        "eligibility": ["Tribal forest produce gatherers organized into Self Help Groups"],
        "documents": ["Aadhaar Card", "Tribe Certificate", "SHG Membership"]
    },
    {
        "name": "Minimum Support Price (MSP) for Minor Forest Produce Scheme",
        "occupation": "Self-Employed",
        "category": "ST",
        "income_limit": None,
        "overview": "Ensures fair price for minor forest produce collected by tribal gatherers to prevent distress sales to middlemen.",
        "benefits": ["Guaranteed minimum price for notified minor forest produce", "Procurement through state agencies/cooperatives"],
        "eligibility": ["Tribal gatherers of notified minor forest produce"],
        "documents": ["Aadhaar Card", "Tribe Certificate"]
    },
    {
        "name": "PM JANMAN (PM Janjati Adivasi Nyaya Maha Abhiyan)",
        "occupation": "Any",
        "category": "ST",
        "income_limit": None,
        "overview": "Aims to improve socio-economic conditions of Particularly Vulnerable Tribal Groups (PVTGs) through saturation of basic facilities.",
        "benefits": ["Pucca housing, road connectivity, and safe drinking water", "Healthcare and education facilities", "Livelihood support for PVTG households"],
        "eligibility": ["Members of Particularly Vulnerable Tribal Groups (PVTGs)"],
        "documents": ["Aadhaar Card", "Tribe Certificate", "PVTG Identification Proof"]
    },
    {
        "name": "Scheme for Development of Particularly Vulnerable Tribal Groups (PVTGs)",
        "occupation": "Any",
        "category": "ST",
        "income_limit": None,
        "overview": "Provides comprehensive development support to PVTGs including livelihood, health, education, and infrastructure development.",
        "benefits": ["Land-based and forest-based livelihood support", "Health camps and nutritional support", "Educational support including residential schools"],
        "eligibility": ["Members of notified Particularly Vulnerable Tribal Groups"],
        "documents": ["Aadhaar Card", "Tribe Certificate"]
    },
    {
        "name": "National Action for Mechanized Sanitation Ecosystem (NAMASTE)",
        "occupation": "Laborer",
        "category": "SC",
        "income_limit": None,
        "overview": "Aims to eliminate hazardous manual scavenging by providing safety gear, mechanization support, and alternative livelihoods to sanitation workers.",
        "benefits": ["Safety equipment and training for sanitation workers", "Capital subsidy for mechanized cleaning equipment", "Health insurance coverage under PM-JAY"],
        "eligibility": ["Sanitation workers and their families, particularly those engaged in manual scavenging"],
        "documents": ["Aadhaar Card", "Sanitation Worker Identification", "Bank Account Details"]
    },
    {
        "name": "Self Employment Scheme for Rehabilitation of Manual Scavengers (SRMS)",
        "occupation": "Self-Employed",
        "category": "SC",
        "income_limit": None,
        "overview": "Provides financial assistance and skill training to manual scavengers and their dependents for alternative self-employment.",
        "benefits": ["One-time cash assistance of ₹40,000", "Concessional loans for self-employment projects", "Skill training with monthly stipend"],
        "eligibility": ["Identified manual scavengers and their dependents"],
        "documents": ["Aadhaar Card", "Manual Scavenger Identification Certificate", "Bank Account Details"]
    },
    {
        "name": "Pradhan Mantri Anusuchit Jaati Abhyuday Yojana (PM-AJAY)",
        "occupation": "Any",
        "category": "SC",
        "income_limit": None,
        "overview": "Integrated scheme for socio-economic development of SC communities through skill development, infrastructure, and adarsh gram development.",
        "benefits": ["Development of model villages with SC majority population", "Skill development and income generation support", "Hostel facilities for SC students"],
        "eligibility": ["Members of Scheduled Caste communities, particularly in identified villages"],
        "documents": ["Aadhaar Card", "Caste Certificate"]
    },
    {
        "name": "Babu Jagjivan Ram Chhatrawas Yojana (Hostels for SC Students)",
        "occupation": "Student",
        "category": "SC",
        "income_limit": None,
        "overview": "Provides hostel facilities for SC students to enable them to pursue higher education without accommodation barriers.",
        "benefits": ["Subsidized hostel accommodation near educational institutions", "Mess and basic amenities at concessional rates"],
        "eligibility": ["SC students enrolled in higher education institutions, especially in urban areas"],
        "documents": ["Aadhaar Card", "Caste Certificate", "Admission Proof"]
    },
    {
        "name": "Scheme for Higher Education for ST Students (Top Class Education)",
        "occupation": "Student",
        "category": "ST",
        "income_limit": 600000,
        "overview": "Provides financial support to ST students for studying in identified premier higher education institutions.",
        "benefits": ["Tuition fee reimbursement at top-ranked institutions", "Maintenance allowance for living and study expenses"],
        "eligibility": ["ST students admitted to notified institutes of excellence", "Family income up to ₹6 lakh per annum"],
        "documents": ["Aadhaar Card", "Tribe Certificate", "Income Certificate", "Admission Proof"]
    },
    {
        "name": "Venture Capital Fund for ST (VCF-ST)",
        "occupation": "Business Owner",
        "category": "ST",
        "income_limit": None,
        "overview": "Provides equity and quasi-equity support to ST entrepreneurs to establish new ventures and expand existing businesses.",
        "benefits": ["Equity investment in viable ST-owned business ventures", "Mentoring and handholding for business growth"],
        "eligibility": ["ST entrepreneurs with majority ownership in the enterprise"],
        "documents": ["Aadhaar Card", "Tribe Certificate", "Business Plan", "Company Registration"]
    },
    {
        "name": "Scheme for Economic Empowerment of DNTs (SEED)",
        "occupation": "Any",
        "category": "OBC",
        "income_limit": 250000,
        "overview": "Provides educational, livelihood, health, and housing support to Denotified, Nomadic, and Semi-Nomadic Tribes (DNTs).",
        "benefits": ["Scholarships for DNT students", "Livelihood and skill development support", "Health insurance and housing assistance"],
        "eligibility": ["Members of Denotified, Nomadic, or Semi-Nomadic Tribes with family income up to ₹2.5 lakh"],
        "documents": ["Aadhaar Card", "Community Certificate", "Income Certificate"]
    },
    {
        "name": "OBC Pre-Matric Scholarship Scheme",
        "occupation": "Student",
        "category": "OBC",
        "income_limit": 250000,
        "overview": "Provides scholarships to OBC students studying in classes 9 and 10 to support continuation of education.",
        "benefits": ["Annual scholarship for tuition and incidental expenses", "Additional allowance for hostellers"],
        "eligibility": ["OBC students enrolled in class 9-10 with family income up to ₹2.5 lakh per annum"],
        "documents": ["Aadhaar Card", "OBC Certificate", "Income Certificate", "School Enrollment Proof"]
    },
    {
        "name": "Construction of Hostels for OBC Boys and Girls",
        "occupation": "Student",
        "category": "OBC",
        "income_limit": None,
        "overview": "Provides hostel accommodation for OBC students to facilitate access to education in areas away from their home.",
        "benefits": ["Subsidized hostel accommodation for OBC students", "Improves access to quality educational institutions"],
        "eligibility": ["OBC students enrolled in educational institutions with hostel facilities"],
        "documents": ["Aadhaar Card", "OBC Certificate", "Admission Proof"]
    },
    {
        "name": "Pradhan Mantri Daksh Scheme",
        "occupation": "Unemployed",
        "category": "OBC",
        "income_limit": None,
        "overview": "Provides skill development training to members of SC, OBC, EBC, DNT, and safai karamchari communities for better employment opportunities.",
        "benefits": ["Free skill training with certification", "Stipend during training period", "Placement linkage post-training"],
        "eligibility": ["Members of SC/OBC/EBC/DNT/Safai Karamchari communities aged 18-45 years"],
        "documents": ["Aadhaar Card", "Community Certificate", "Bank Account Details"]
    },
    {
        "name": "National Backward Classes Finance and Development Corporation (NBCFDC) Loan Scheme",
        "occupation": "Self-Employed",
        "category": "OBC",
        "income_limit": 300000,
        "overview": "Provides concessional loans to OBC individuals for self-employment and income-generating activities.",
        "benefits": ["Term loans at concessional interest rates for business setup", "Education loans for OBC students", "Skill training loans"],
        "eligibility": ["OBC individuals with family income below the prescribed limit"],
        "documents": ["Aadhaar Card", "OBC Certificate", "Income Certificate", "Business/Education Plan"]
    },
    {
        "name": "National Safai Karamcharis Finance and Development Corporation (NSKFDC) Scheme",
        "occupation": "Self-Employed",
        "category": "SC",
        "income_limit": None,
        "overview": "Provides financial assistance to safai karamcharis and their dependents for self-employment ventures and skill development.",
        "benefits": ["Concessional loans for self-employment activities", "Skill training with stipend", "Education loans for dependents"],
        "eligibility": ["Safai karamcharis, scavengers, and their dependents"],
        "documents": ["Aadhaar Card", "Occupation Certificate", "Bank Account Details"]
    },
    {
        "name": "Maulana Azad National Fellowship for Minority Students",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 600000,
        "overview": "Provides financial support to minority students pursuing M.Phil and PhD degrees in universities and research institutions.",
        "benefits": ["Monthly fellowship for M.Phil/PhD scholars", "Contingency grant for research-related expenses"],
        "eligibility": ["Students from notified minority communities pursuing M.Phil/PhD", "Family income up to ₹6 lakh per annum"],
        "documents": ["Aadhaar Card", "Minority Community Certificate", "Income Certificate", "Admission/Enrollment Proof"]
    },
    {
        "name": "Pre-Matric Scholarship for Minority Students",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 100000,
        "overview": "Provides scholarships to minority community students studying in classes 1 to 10 to reduce dropout rates.",
        "benefits": ["Annual scholarship covering admission fees and maintenance allowance", "Encourages continuation of school education"],
        "eligibility": ["Minority community students in classes 1-10 with family income up to ₹1 lakh per annum"],
        "documents": ["Aadhaar Card", "Minority Community Certificate", "Income Certificate", "School Enrollment Proof"]
    },
    {
        "name": "Jiyo Parsi Scheme",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to arrest the declining population of Parsis in India through financial and medical support for families.",
        "benefits": ["Financial assistance for fertility treatments", "Support for childcare and family welfare among Parsi community"],
        "eligibility": ["Married couples from the Parsi community"],
        "documents": ["Aadhaar Card", "Community Certificate", "Medical Records"]
    },
    {
        "name": "Hamari Dharohar Scheme",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Preserves and promotes the rich cultural heritage of minority communities in India through documentation and exhibitions.",
        "benefits": ["Support for cultural preservation projects", "Documentation of minority art, crafts, and heritage"],
        "eligibility": ["Organizations and individuals working on minority cultural heritage preservation"],
        "documents": ["Project Proposal", "Organization Registration"]
    },
    {
        "name": "Garib Kalyan Yojana for Urban Poor",
        "occupation": "Unemployed",
        "category": "EWS",
        "income_limit": None,
        "overview": "Provides livelihood and basic services support to urban poor and slum dwellers through skill training and self-employment assistance.",
        "benefits": ["Skill training for urban informal sector jobs", "Access to basic civic amenities in slum areas", "Self-employment credit linkage"],
        "eligibility": ["Urban poor identified through municipal surveys"],
        "documents": ["Aadhaar Card", "Income Certificate", "Residence Proof"]
    },
    {
        "name": "Deendayal Antyodaya Yojana - Self Help Group Bank Linkage",
        "occupation": "Self-Employed",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Facilitates bank credit linkage for Self Help Groups to enable members to access affordable credit for livelihood activities.",
        "benefits": ["Collateral-free loans to SHGs at concessional rates", "Interest subvention for prompt repayment"],
        "eligibility": ["Members of registered Self Help Groups, primarily women"],
        "documents": ["Aadhaar Card", "SHG Membership Certificate", "Bank Account Details"]
    },
    {
        "name": "Mahila E-Haat",
        "occupation": "Self-Employed",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Online marketing platform for women entrepreneurs and SHGs to showcase and sell their products directly to consumers.",
        "benefits": ["Free online platform to sell products nationwide", "No middlemen, direct access to buyers", "Increased visibility for women-made products"],
        "eligibility": ["Women entrepreneurs, SHGs, and NGOs working with women producers"],
        "documents": ["Aadhaar Card", "Bank Account Details", "Product Details"]
    },
    {
        "name": "Mahila Samman Savings Certificate",
        "occupation": "Any",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Small savings scheme exclusively for women and girls offering fixed interest rate for a 2-year tenure.",
        "benefits": ["Fixed attractive interest rate for 2-year deposit", "Partial withdrawal facility available"],
        "eligibility": ["Women and girls of any age (account opened by guardian for minors)"],
        "documents": ["Aadhaar Card", "Address Proof", "Photograph"]
    },
    {
        "name": "Working Women's Crèche Scheme (Palna)",
        "occupation": "Private Employee",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides daycare facilities for children of working women to enable workforce participation.",
        "benefits": ["Daycare facility for children aged 6 months to 6 years", "Nutritional support and basic healthcare monitoring for children"],
        "eligibility": ["Children of working mothers, including those in informal sector"],
        "documents": ["Aadhaar Card", "Employment Proof", "Birth Certificate of Child"]
    },
    {
        "name": "National Creche Scheme for Children of Working Mothers",
        "occupation": "Laborer",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides safe daycare and supplementary nutrition for children of working mothers from low-income families.",
        "benefits": ["Free daycare with nutrition and health check-ups", "Enables mothers to continue working without childcare concerns"],
        "eligibility": ["Children aged 6 months to 6 years of working mothers from economically weaker families"],
        "documents": ["Aadhaar Card", "Income Certificate", "Birth Certificate of Child"]
    },
    {
        "name": "Pradhan Mantri Ujjwal Bhavishya Yojana (PMUBY)",
        "occupation": "Pregnant Women",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Provides nutritional kits and health monitoring support to pregnant and lactating women in rural areas.",
        "benefits": ["Nutritional supplement kits during pregnancy and lactation", "Regular health monitoring through Anganwadi workers"],
        "eligibility": ["Pregnant and lactating women in rural and tribal areas"],
        "documents": ["Aadhaar Card", "MCP Card"]
    },
    {
        "name": "Anemia Mukt Bharat (AMB)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to reduce anemia prevalence among children, adolescents, pregnant women, and lactating mothers through iron supplementation.",
        "benefits": ["Free iron and folic acid supplementation", "Bi-annual deworming and anemia screening"],
        "eligibility": ["Children, adolescents, pregnant women, and lactating mothers"],
        "documents": ["Aadhaar Card (where applicable)"]
    },
    {
        "name": "Poshan Abhiyaan (National Nutrition Mission)",
        "occupation": "Pregnant Women",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Aims to improve nutritional outcomes for children, pregnant women, and lactating mothers through technology-enabled monitoring and convergence.",
        "benefits": ["Growth monitoring for children through digital tools", "Nutrition counselling for mothers", "Convergence with ICDS and health programs"],
        "eligibility": ["Pregnant women, lactating mothers, and children up to 6 years"],
        "documents": ["Aadhaar Card", "MCP Card"]
    },
    {
        "name": "Saksham Anganwadi and Poshan 2.0",
        "occupation": "Pregnant Women",
        "category": "Any",
        "gender": "Female",
        "income_limit": None,
        "overview": "Upgraded Anganwadi infrastructure scheme providing improved early childhood care, nutrition, and development services.",
        "benefits": ["Modernized Anganwadi centers with better facilities", "Improved supplementary nutrition quality", "Early childhood education resources"],
        "eligibility": ["Pregnant women, lactating mothers, and children up to 6 years registered at Anganwadi centers"],
        "documents": ["Aadhaar Card", "MCP Card"]
    },
    {
        "name": "Pradhan Mantri Bhartiya Janaushadhi Pariyojana (PMBJP)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides quality generic medicines at affordable prices through dedicated Janaushadhi Kendras across the country.",
        "benefits": ["Generic medicines at 50-90% lower prices than branded drugs", "Wide network of stores across India"],
        "eligibility": ["All citizens can purchase medicines from Janaushadhi Kendras"],
        "documents": ["None required for purchase"]
    },
    {
        "name": "PM-DevINE (Development Initiative for North East Region)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Funds infrastructure and social development projects in North Eastern states to address development gaps and promote livelihoods.",
        "benefits": ["Infrastructure projects in connectivity, health, and education", "Livelihood and entrepreneurship support for youth and women"],
        "eligibility": ["Residents of North Eastern states benefiting from funded projects"],
        "documents": ["Aadhaar Card", "Domicile Proof"]
    },
    {
        "name": "Aspirational Districts Programme",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Focuses on rapid transformation of underdeveloped districts through convergence of central and state schemes in health, education, and infrastructure.",
        "benefits": ["Accelerated implementation of welfare schemes in identified districts", "Improved access to health, education, and skill development"],
        "eligibility": ["Residents of identified Aspirational Districts"],
        "documents": ["Aadhaar Card", "Residence Proof"]
    },
    {
        "name": "Deen Dayal Upadhyay Antyodaya Parivar Yojana (Ration Card Scheme)",
        "occupation": "Any",
        "category": "EWS",
        "income_limit": None,
        "overview": "Identifies and provides ration cards to the poorest families to ensure access to subsidized food grains under PDS.",
        "benefits": ["Access to subsidized food grains through Fair Price Shops", "Identification card for availing other welfare benefits"],
        "eligibility": ["Families identified as below poverty line by state authorities"],
        "documents": ["Aadhaar Card", "Income Certificate", "Address Proof"]
    },
    {
        "name": "Aam Aadmi Bima Yojana (AABY)",
        "occupation": "Laborer",
        "category": "EWS",
        "income_limit": None,
        "overview": "Social security scheme providing life insurance cover to rural landless households and persons in identified vocational groups.",
        "benefits": ["Life insurance cover for natural and accidental death", "Additional disability cover", "Scholarship benefits for children of beneficiaries"],
        "eligibility": ["Head of family or earning member of rural landless households, aged 18-59 years"],
        "documents": ["Aadhaar Card", "Bank Account Details", "Landless Certificate"]
    },
    {
        "name": "Universal Account Number (UAN) Activation Drive",
        "occupation": "Private Employee",
        "category": "Any",
        "income_limit": None,
        "overview": "Ensures all EPF members have an activated Universal Account Number to easily track and transfer PF balances across jobs.",
        "benefits": ["Single PF account portable across employers", "Online access to PF balance and statements", "Simplified withdrawal and transfer process"],
        "eligibility": ["All EPF members"],
        "documents": ["Aadhaar Card", "PAN Card", "Bank Account Details"]
    },
    {
        "name": "Pradhan Mantri Rojgar Protsahan Yojana (PMRPY)",
        "occupation": "Private Employee",
        "category": "Any",
        "income_limit": 15000,
        "overview": "Incentivizes employers to generate new employment by reimbursing the employer's contribution to EPF for new employees.",
        "benefits": ["Government reimburses employer's 8.33% EPF contribution for new employees", "Encourages formalization of jobs"],
        "eligibility": ["New employees earning less than ₹15,000 per month registered with EPFO"],
        "documents": ["Aadhaar Card", "UAN Number", "Employment Proof"]
    },
    {
        "name": "Labour Welfare Fund Schemes (State-specific)",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "State-administered welfare funds providing financial assistance to registered workers for medical, educational, and housing needs.",
        "benefits": ["Medical assistance for workers and dependents", "Educational scholarships for workers' children", "Housing loan assistance"],
        "eligibility": ["Registered workers contributing to state labour welfare fund"],
        "documents": ["Aadhaar Card", "Labour Welfare Fund Registration", "Bank Account Details"]
    },
    {
        "name": "Domestic Workers Welfare Scheme",
        "occupation": "Laborer",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides social security registration and welfare benefits to domestic workers including health insurance and skill training.",
        "benefits": ["Registration under e-Shram for social security access", "Eligibility for health insurance under PM-JAY", "Skill upgradation training"],
        "eligibility": ["Domestic workers registered under e-Shram portal"],
        "documents": ["Aadhaar Card", "e-Shram Card", "Bank Account Details"]
    },
    {
        "name": "Gig and Platform Workers Social Security Scheme",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Extends social security benefits including health insurance and accident cover to gig and platform-based workers.",
        "benefits": ["Health insurance coverage under PM-JAY", "Accident insurance cover", "Access to PF and pension schemes through e-Shram linkage"],
        "eligibility": ["Workers engaged with aggregator platforms (delivery, ride-hailing, etc.) registered on e-Shram"],
        "documents": ["Aadhaar Card", "e-Shram Card", "Platform Work ID/Proof"]
    },
    {
        "name": "Pradhan Mantri Street Vendor Insurance Scheme",
        "occupation": "Self-Employed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides accident and life insurance coverage to street vendors registered under PM SVANidhi at nominal premium.",
        "benefits": ["Accidental death and disability cover", "Life insurance cover for registered vendors", "Low premium subsidized by government"],
        "eligibility": ["Street vendors registered under PM SVANidhi scheme"],
        "documents": ["Aadhaar Card", "Certificate of Vending", "Bank Account Details"]
    },
    {
        "name": "Income Tax Relief for Senior Citizens",
        "occupation": "Senior Citizen",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides higher basic exemption limits and additional deductions on income tax for senior and super senior citizens.",
        "benefits": ["Higher basic exemption limit on taxable income", "Additional deduction on medical insurance premium under Section 80D", "Exemption from advance tax for those without business income"],
        "eligibility": ["Resident individuals aged 60 years and above (higher benefits for 80+ years)"],
        "documents": ["Aadhaar Card", "PAN Card", "Age Proof"]
    },
    {
        "name": "Varishtha Pension Bima Yojana (VPBY)",
        "occupation": "Senior Citizen",
        "category": "Any",
        "income_limit": None,
        "overview": "Pension scheme for senior citizens providing assured returns through LIC on a lump-sum investment (predecessor to PMVVY).",
        "benefits": ["Assured monthly/quarterly/annual pension based on investment", "Loan facility against policy after 3 years"],
        "eligibility": ["Senior citizens aged 60 years and above"],
        "documents": ["Aadhaar Card", "Age Proof", "Bank Account Details"]
    },
    {
        "name": "Senior Citizen Welfare Fund",
        "occupation": "Senior Citizen",
        "category": "EWS",
        "income_limit": None,
        "overview": "Utilizes unclaimed deposits from small savings schemes and EPF to fund welfare programs for senior citizens.",
        "benefits": ["Funding for old age homes and day care centers", "Support for physiotherapy and mobility aids for elderly", "Helpline services for senior citizens"],
        "eligibility": ["Senior citizens accessing government-funded elderly care facilities"],
        "documents": ["Aadhaar Card", "Age Proof"]
    },
    {
        "name": "Integrated Programme for Senior Citizens (IPSrC)",
        "occupation": "Senior Citizen",
        "category": "EWS",
        "income_limit": None,
        "overview": "Provides basic amenities such as shelter, food, healthcare, and entertainment to indigent senior citizens through old age homes.",
        "benefits": ["Free shelter and food at old age homes", "Healthcare and recreational facilities for elderly", "Day care centers for senior citizens"],
        "eligibility": ["Indigent senior citizens without family support"],
        "documents": ["Aadhaar Card", "Age Proof", "Income Certificate"]
    },
    {
        "name": "Rashtriya Vridhajan Awas Yojana",
        "occupation": "Senior Citizen",
        "category": "EWS",
        "income_limit": None,
        "overview": "Provides housing assistance to destitute and homeless senior citizens through construction of old age shelters.",
        "benefits": ["Free shelter for homeless senior citizens", "Basic amenities including food and medical care"],
        "eligibility": ["Homeless senior citizens aged 60 years and above"],
        "documents": ["Aadhaar Card", "Age Proof"]
    },
    {
        "name": "Elderline (National Helpline for Senior Citizens)",
        "occupation": "Senior Citizen",
        "category": "Any",
        "income_limit": None,
        "overview": "Toll-free helpline providing information, guidance, and emotional support to senior citizens on issues like elder abuse and pension grievances.",
        "benefits": ["24x7 toll-free helpline support", "Guidance on legal aid and pension issues", "Referral to local support services"],
        "eligibility": ["All senior citizens can access the helpline"],
        "documents": ["None required"]
    },
    {
        "name": "Saksham Yojana for Persons with Disabilities (Employment)",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides skill training and employment support to persons with disabilities to enhance their workforce participation.",
        "benefits": ["Free skill training programs tailored for disabilities", "Job placement assistance and employer linkage"],
        "eligibility": ["Persons with disabilities (40% or more) seeking employment"],
        "documents": ["Aadhaar Card", "Disability Certificate"]
    },
    {
        "name": "Unique Disability ID (UDID) Scheme",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Creates a national database of persons with disabilities by issuing a unique disability identity card to streamline access to benefits.",
        "benefits": ["Single ID card valid across India for accessing disability benefits", "Simplifies application for multiple welfare schemes"],
        "eligibility": ["All persons with disabilities (40% or more as certified)"],
        "documents": ["Aadhaar Card", "Disability Certificate", "Address Proof"]
    },
    {
        "name": "Assistance to Disabled Persons for Purchase/Fitting of Aids and Appliances (ADIP)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides assistive devices to persons with disabilities to enhance their physical, social, and economic rehabilitation.",
        "benefits": ["Free or subsidized assistive devices (wheelchairs, hearing aids, prosthetics)", "Improves mobility and independence"],
        "eligibility": ["Persons with disabilities with family income within prescribed limits"],
        "documents": ["Aadhaar Card", "Disability Certificate", "Income Certificate"]
    },
    {
        "name": "Pradhan Mantri Jan Vikas Karyakram (PMJVK)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Develops socio-economic infrastructure in identified minority concentration areas to improve quality of life.",
        "benefits": ["Schools, hostels, and health facilities in minority concentration areas", "Skill development centers", "Improved basic infrastructure (roads, water, sanitation)"],
        "eligibility": ["Residents of identified Minority Concentration Areas/Blocks/Towns"],
        "documents": ["Aadhaar Card", "Residence Proof"]
    },
    {
        "name": "Direct Benefit Transfer (DBT) for LPG Subsidy (PAHAL)",
        "occupation": "Any",
        "category": "Any",
        "income_limit": None,
        "overview": "Transfers LPG cylinder subsidy directly to consumers' bank accounts to ensure transparent subsidy delivery.",
        "benefits": ["Direct subsidy credit to bank account on cylinder purchase", "Eliminates leakages in subsidy distribution"],
        "eligibility": ["LPG consumers with Aadhaar-linked bank accounts"],
        "documents": ["Aadhaar Card", "Bank Account Details", "LPG Consumer ID"]
    },
    {
        "name": "PM Gati Shakti - Skill Development for Logistics Sector",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Provides skill training for jobs in the logistics and infrastructure sector to support multi-modal connectivity projects.",
        "benefits": ["Skill training aligned with logistics sector job requirements", "Placement support in logistics and infrastructure projects"],
        "eligibility": ["Youth seeking employment in logistics, transport, and infrastructure sectors"],
        "documents": ["Aadhaar Card", "Educational Certificates"]
    },
    {
        "name": "PM Internship Scheme",
        "occupation": "Student",
        "category": "Any",
        "income_limit": 800000,
        "overview": "Provides internship opportunities to youth in top companies to enhance employability through real-world work exposure.",
        "benefits": ["12-month internship with monthly stipend of ₹5,000", "One-time grant of ₹6,000 for incidental expenses", "Exposure to real corporate work environment"],
        "eligibility": ["Youth aged 21-24 years, not employed full-time or in full-time education", "Family income not exceeding ₹8 lakh per annum"],
        "documents": ["Aadhaar Card", "Educational Certificates", "Income Certificate", "Bank Account Details"]
    },
    {
        "name": "Aatmanirbhar Bharat Skilled Workforce Scheme",
        "occupation": "Unemployed",
        "category": "Any",
        "income_limit": None,
        "overview": "Aims to create a skilled workforce aligned with industry demand across manufacturing and services sectors under self-reliant India initiative.",
        "benefits": ["Industry-aligned skill training programs", "Recognition of prior learning for experienced workers", "Certification boosting employability"],
        "eligibility": ["Youth and workers seeking upskilling or reskilling opportunities"],
        "documents": ["Aadhaar Card", "Educational/Experience Certificates"]
    },
]