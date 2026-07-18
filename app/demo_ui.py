from fastapi.responses import HTMLResponse


def demo_ui_page():

    html = """
<!DOCTYPE html>
<html>
<head>

<title>Agentic Wallet Guardian v2</title>

<style>

body {
    font-family: Arial, sans-serif;
    background:#070b14;
    color:#e5e7eb;
    padding:30px;
}


h1 {
    text-align:center;
    margin:8px;
    font-size:26px;
    font-weight:600;
    letter-spacing:0.3px;
}

.subtitle {
    text-align:center;
    color:#94a3b8;
    margin-bottom:20px;
}


.section {

    background:#0f172a;
    border:1px solid #1e293b;
    border-radius:14px;
    padding:22px;
    margin:18px auto;
    max-width:1000px;

}


.pipeline {

    text-align:center;
    font-size:15px;
    padding:15px;
    color:#cbd5e1;

}


.trust {

    display:flex;
    justify-content:center;
    gap:15px;
    flex-wrap:wrap;

}


.trust-card {

    background:#0f172a;
    border-radius:10px;
    padding:12px;
    width:200px;
    text-align:center;

}


.results {

    display:flex;
    justify-content:center;
    gap:15px;
    flex-wrap:wrap;

}


.card {

    background:#111827;
    border:1px solid #1e293b;
    border-radius:14px;
    padding:20px;
    width:220px;
    text-align:center;

}


.allow {
border:2px solid #22c55e;
}


.warn {
border:2px solid #eab308;
}


.block {
border:2px solid #ef4444;
}


.decision {

font-size:25px;
font-weight:bold;

}


.power {

text-align:center;

}



.section h3 {

    color:#cbd5e1;
    font-size:16px;
    font-weight:600;
    letter-spacing:0.4px;
    margin-bottom:18px;

}

.card h3 {

    font-size:17px;
    font-weight:600;
    letter-spacing:0.5px;

}

.message {

    color:#94a3b8;
    font-size:14px;
    margin-top:12px;

}


</style>

</head>


<body>


<h1>
Agentic Wallet Guardian v2
</h1>


<div class="subtitle">
AI Security Layer for Autonomous Web3 Agents
</div>



<div class="section">

<h3>
Security Pipeline
</h3>

<div class="pipeline">

🤖 Request →
🔍 Wallet →
📜 Policy →
⭐ Reputation →
⚡ Fusion →
🛡 Decision

</div>

</div>




<div class="section">

<h3>
Agent Trust Layer
</h3>


<div class="trust">


<div class="trust-card">
🟢 Trusted Agent
<br>
100 / 100
<br>
TRUSTED
</div>


<div class="trust-card">
🟡 Unknown Agent
<br>
50 / 100
<br>
MONITOR
</div>


<div class="trust-card">
🔴 Drainer Agent
<br>
0 / 100
<br>
BLOCKED
</div>


</div>

</div>




<div class="section results">


<div class="card allow">

<h3>
🟢 SAFE AGENT
</h3>

Risk Score:
10/100

<p class="decision">
ALLOW
</p>

Transaction approved.

</div>



<div class="card warn">

<h3>
🟡 UNKNOWN AGENT
</h3>

Risk Score:
50/100

<p class="decision">
WARN
</p>

Review required.

</div>




<div class="card block">

<h3>
🔴 MALICIOUS AGENT
</h3>

Risk Score:
100/100

<p class="decision">
BLOCK
</p>

Threat detected.

</div>


</div>




<div class="section power">

<h3>
Powered By
</h3>

🧠 Agent Reputation Engine
&nbsp;&nbsp;
⚡ Risk Fusion Engine
&nbsp;&nbsp;
🔒 Guardian Policy Engine

</div>



</body>
</html>

"""

    return HTMLResponse(html)
