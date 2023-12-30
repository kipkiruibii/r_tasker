function updateDialCode() {
    var selectedCountry = document.getElementById("country").value;
    var dialCodes = {
    afghanistan: "+93",
    albania: "+355",
    algeria: "+213",
    andorra: "+376",
    angola: "+244",
    antiguaandbarbuda: "+1",
    argentina: "+54",
    armenia: "+374",
    australia: "+61",
    austria: "+43",
    azerbaijan: "+994",
    bahamas: "+1",
    bahrain: "+973",
    bangladesh: "+880",
    barbados: "+1",
    belarus: "+375",
    belgium: "+32",
    belize: "+501",
    benin: "+229",
    bhutan: "+975",
    bolivia: "+591",
    bosniaandherzegovina: "+387",
    botswana: "+267",
    brazil: "+55",
    brunei: "+673",
    bulgaria: "+359",
    burkinafaso: "+226",
    burundi: "+257",
    caboverde: "+238",
    cambodia: "+855",
    cameroon: "+237",
    canada: "+1",
    centralafricanrepublic: "+236",
    chad: "+235",
    chile: "+56",
    china: "+86",
    colombia: "+57",
    comoros: "+269",
    congo: "+242",
    costarica: "+506",
    cotedivoire: "+225",
    croatia: "+385",
    cuba: "+53",
    cyprus: "+357",
    czechrepublic: "+420",
    democraticrepublicofthecongo: "+243",
    denmark: "+45",
    djibouti: "+253",
    dominica: "+1",
    dominicanrepublic: "+1",
    ecuador: "+593",
    egypt: "+20",
    elsalvador: "+503",
    equatorialguinea: "+240",
    eritrea: "+291",
    estonia: "+372",
    eswatini: "+268",
    ethiopia: "+251",
    fiji: "+679",
    finland: "+358",
    france: "+33",
    gabon: "+241",
    gambia: "+220",
    georgia: "+995",
    germany: "+49",
    ghana: "+233",
    greece: "+30",
    grenada: "+1",
    guatemala: "+502",
    guinea: "+224",
    guineabissau: "+245",
    guyana: "+592",
    haiti: "+509",
    honduras: "+504",
    hungary: "+36",
    iceland: "+354",
    india: "+91",
    indonesia: "+62",
    iran: "+98",
    iraq: "+964",
    ireland: "+353",
    israel: "+972",
    italy: "+39",
    jamaica: "+1",
    japan: "+81",
    jordan: "+962",
    kazakhstan: "+7",
    kenya: "+254",
    kiribati: "+686",
    kuwait: "+965",
    kyrgyzstan: "+996",
    laos: "+856",
    latvia: "+371",
    lebanon: "+961",
    lesotho: "+266",
    liberia: "+231",
    libya: "+218",
    liechtenstein: "+423",
    lithuania: "+370",
    luxembourg: "+352",
    madagascar: "+261",
    malawi: "+265",
    malaysia: "+60",
    maldives: "+960",
    mali: "+223",
    malta: "+356",
    marshallislands: "+692",
    mauritania: "+222",
    mauritius: "+230",
    mexico: "+52",
    micronesia: "+691",
    moldova: "+373",
    monaco: "+377",
    mongolia: "+976",
    montenegro: "+382",
    morocco: "+212",
    mozambique: "+258",
    myanmar: "+95",
    namibia: "+264",
    nauru: "+674",
    nepal: "+977",
    netherlands: "+31",
    newzealand: "+64",
    nicaragua: "+505",
    niger: "+227",
    nigeria: "+234",
    northkorea: "+850",
    northmacedonia: "+389",
    norway: "+47",
    oman: "+968",
    pakistan: "+92",
    palau: "+680",
    palestinestate: "+970",
    panama: "+507",
    papuanewguinea: "+675",
    paraguay: "+595",
    peru: "+51",
    philippines: "+63",
    poland: "+48",
    portugal: "+351",
    qatar: "+974",
    romania: "+40",
    russia: "+7",
    rwanda: "+250",
    saintkittsandnevis: "+1",
    saintlucia: "+1",
    saintvincentandthegrenadines: "+1",
    samoa: "+685",
    sanmarino: "+378",
    saotomeandprincipe: "+239",
    saudiarabia: "+966",
    senegal: "+221",
    serbia: "+381",
    seychelles: "+248",
    sierraleone: "+232",
    singapore: "+65",
    slovakia: "+421",
    slovenia: "+386",
    solomonislands: "+677",
    somalia: "+252",
    southafrica: "+27",
    southkorea: "+82",
    southsudan: "+211",
    spain: "+34",
    srilanka: "+94",
    sudan: "+249",
    suriname: "+597",
    sweden: "+46",
    switzerland: "+41",
    syria: "+963",
    tajikistan: "+992",
    tanzania: "+255",
    thailand: "+66",
    timorleste: "+670",
    togo: "+228",
    tonga: "+676",
    trinidadandtobago: "+1",
    tunisia: "+216",
    turkey: "+90",
    turkmenistan: "+993",
    tuvalu: "+688",
    uganda: "+256",
    ukraine: "+380",
    unitedarabemirates: "+971",
    unitedkingdom: "+44",
    unitedstatesofamerica: "+1",
    uruguay: "+598",
    uzbekistan: "+998",
    vanuatu: "+678",
    venezuela: "+58",
    vietnam: "+84",
    yemen: "+967",
    zambia: "+260",
    zimbabwe: "+263"
    };

    // Update the dial code input field and the hidden input field
    //document.getElementById("dialCode").value = dialCodes[selectedCountry];
    alert(dialCodes[selectedCountry]);
    //document.getElementById("hiddenDialCode").value = dialCodes[selectedCountry];
}
function validateRegisterForm(){
    return true;

}