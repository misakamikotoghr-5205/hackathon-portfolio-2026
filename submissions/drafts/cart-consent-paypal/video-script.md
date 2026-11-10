# PayPal published demonstration — 138.8 seconds

**Published November 10, 2026:** [Cart Consent | Exact Basket Approval + PayPal Sandbox](https://youtu.be/icz2WX1DXZ4), **138.8 seconds**. The event registration was verified November 9. Final project submission is still pending at Start project / CAPTCHA, awaiting current consent/action; there is no final project receipt.

The final cut is an edited walkthrough of sanitized evidence cards plus an actual mock-mode native terminal shot, not continuous footage. It uses generic synthetic Aria narration and **25 burned-in English captions**. The local upload source is **2,036,177 bytes**, SHA-256 `613781979f0f75434658069c0d2c528cd6e843a59114e69eb937bbe9a5c500f6`. Full audio/video decoding passed; full manual audio listening is not claimed. The table below is the original editorial outline, not measured final-cut timestamps or a verbatim transcript.

Required final video: public YouTube, under three minutes, actual functioning project. Use fictional goods and addresses. Keep tokens, secrets, merchant/order identifiers, approval URLs and the private ledger off screen. A saved-result walkthrough must say it is saved evidence rather than a continuous live terminal capture. Reuse the already recorded sandbox result instead of creating another remote order just for a shot.

| Time | Shot / evidence boundary | English narration |
| --- | --- | --- |
| 0:00–0:20 | Title, fictional catalog, consent problem | “An AI can suggest a basket. The problem is keeping an approval attached to exactly what was reviewed.” |
| 0:20–0:50 | Actual saved November 10 proposal: local `qwen2.5:0.5b`, `ai_used=true`, `DRAFT` | “This fresh local Qwen proposal took 5.899 seconds. One pen set costs eight dollars ninety-nine, plus four ninety-nine shipping: thirteen ninety-eight, below a fifty-dollar budget. The proposal is still unapproved.” |
| 0:50–1:20 | Sanitized snapshot and explicit CLI fingerprint approval | “For this fictional demonstration, the developer reviewed and approved the exact snapshot. This is not authenticated buyer consent. The separate human and agent HTTP capabilities are demonstrated with mocks.” |
| 1:20–1:50 | Separately labeled mock policy sequence; the final cut includes an actual mock-mode terminal shot | “In this local policy demonstration, changing a critical field invalidates approval. The old fingerprint cannot retrieve a link.” Show actual rejection and changed-field audit. Do not imply cancellation of an existing remote URL. |
| 1:50–2:25 | Sanitized actual November 10 sandbox response and saved request identity | “The real PayPal sandbox returned PAYER ACTION REQUIRED. An initial OAuth configuration error was corrected before the Orders request, retaining the same cart and request identity. One remote order was created. Its approval link was not opened.” |
| 2:25–2:45 | Limits and README reproduction route | “CAPTURE is the order's intent field. No capture was executed or implemented. There was no buyer checkout or production payment. Exact retries reuse the saved request identity; local revocation cannot cancel an already disclosed remote URL.” |

## Source and recording checklist

- Actual combined run: `projects/cart-consent-paypal/docs/evidence/sandbox-model-20261110.json`. Fresh model: **5.899 seconds**. Exact synthetic operator approval, OAuth success, one remote order, `PAYER_ACTION_REQUIRED`, strict adapter validation passed without code changes. Successful checkout CLI: **1.369 seconds**; success HTTP status unrecorded. The public record is sanitized operator-held evidence, not independent certification.
- A post-success checkout CLI probe, under a network guard, returned the same cached order with `replayed=true` and zero network calls. If shown, label this local cached replay; it is not a second remote order or a remote idempotency test.
- The initial OAuth HTTP 401 happened before any Orders request. Duplicated private configuration was corrected; the cart, fingerprint, approval nonce and persisted request ID remained the same. Do not narrate two remote order creations or hide this as an adapter repair.
- Historical November 6 model-only record: `projects/cart-consent-paypal/docs/evidence/local-model-20261106.json`. It preserves an earlier 21.350-second pen-set draft, two timeouts and a budget rejection. It made no payment-provider call and is not the source of the November 10 order.
- Default mock policy demo: `python3 -m cart_consent --db var/recording-mock.sqlite3 demo`; HTTP role demo: `scripts/api_demo.py`. Label these synthetic. The published cut contains an actual native terminal mock shot; do not relabel it as live model or sandbox footage. They do not prove real AI or remote payment integration.
- Disclose Codex assistance with design, implementation, tests and documentation. The configured local model only proposes catalog choices; it has no approval or payment authority.
- Do not claim authenticated buyer consent, completed purchase, AP2 certification, real address/tax/shipping validation, remote cancellation or a general model-quality result.
- Publication was verified November 10 at [https://youtu.be/icz2WX1DXZ4](https://youtu.be/icz2WX1DXZ4). Full audio/video decoding passed, with 25 English burned-in captions and a 138.8-second duration. Full manual listening is not claimed. Supply that exact case-sensitive URL to the project form after resolving the current Start project / CAPTCHA step; no formal project receipt exists.

中文核对：真实模型建议仍是未批准草稿；开发者操作虚构演示，非买家身份认证；相同快照明确批准后真实沙箱只建未支付订单；没有买家结账、授权或扣款；角色拒绝和变更拒绝如使用mock，必须与真实沙箱证据分开标注。
