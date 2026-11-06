# PayPal recording plan — 2:45 English, actual behavior only

This file is not a recording. Required final video: public YouTube, under three minutes, actual functioning project. Use fictional goods/addresses and keep every token, secret, account identifier and private ledger off screen. No buyer checkout, authorize or capture is needed to demonstrate this project's link-creation scope.

| Time | Demonstration | Narration |
|---|---|---|
| 0:00–0:20 | Title and DRAFT basket | “An AI can suggest a basket. It cannot decide what a person agreed to buy.” |
| 0:20–0:50 | Actually configured Ollama proposal, then validated known SKUs | “The model can choose only allowed catalog items and quantities. Its proposal is still unapproved.” If no model ran, label mock and do not claim this completes the AI requirement. |
| 0:50–1:20 | Human review snapshot, exact fingerprint approval; actual agent approval denial if performed | “The approval binds products, prices, currency, budget, shipping, address and merchant. Agent credentials cannot approve.” |
| 1:20–1:50 | Edit a fictional postcode or shipping option; try old fingerprint | “Changing this field invalidates the old approval. The stale request is rejected.” Show the actual error/audit field names. |
| 1:50–2:25 | Reapprove; only with authorized sandbox credentials, create one sandbox order | “This is PayPal's sandbox order creation, after human approval. No buyer payment is captured.” Show sanitized actual status, not secrets or an invented response. |
| 2:25–2:45 | README boundaries and repeat-request receipt | “Exact retries reuse the saved request identity. A local revocation cannot cancel an already disclosed remote URL; this app never captures.” |

Offline preparation from the project root: `python3 -m cart_consent --db var/recording-mock.sqlite3 demo`. This is explicitly mock consent and mock payment, and cannot stand in for the required real sandbox/AI technology demonstration. The configured model path and sandbox environment are documented in the project README and `docs/paypal-sandbox.md`; root must establish the actual accounts and authorized run before updating this description to past-tense success.

Actual local model evidence now exists at
`projects/cart-consent-paypal/docs/evidence/local-model-20261106.json`: a genuine
production-adapter `qwen2.5:0.5b` request accepted one pen set, total 1,398 minor
units including shipping, in 21.350 seconds. It was stored only as unapproved
`DRAFT`; no PayPal provider was called. Two timeouts and a prior over-budget
rejection are retained. This file is not a recording or sandbox proof; rerun the
actual model segment for the video, and disclose its narrow tested scope.

中文旁白要点：建议不等于同意；关键字段变化重新审阅；人和智能体权限分开；展示的真实沙箱只建订单链接，没有真实扣款。若远程步骤失败，保留失败事实，不能剪出虚假的成功链路。
