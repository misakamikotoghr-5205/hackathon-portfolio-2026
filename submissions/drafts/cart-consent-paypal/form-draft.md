# Cart Consent — PayPal submission copy, 2026-11-10

Public [event](https://paypalaihackathon.devpost.com/) and [rules](https://paypalaihackathon.devpost.com/rules). **Event registration was verified on November 9.** The [public video](https://youtu.be/icz2WX1DXZ4) was published November 10 and lasts **138.8 seconds**. The submitted project includes the overview, Story, technology tags, public repository/video and original gallery/cover. Official final submission was verified at **2026-11-10 07:37:39.790 UTC** on the [public project page](https://devpost.com/software/cart-consent), which displayed **“Project submitted!”** and **“SUBMITTED TO PayPal AI Hackathon”**. This confirms entry receipt, not eligibility approval, judging results or a prize. This file preserves the project copy. The official public project page supplies the entry confirmation; no receipt number, confirmation email or judging result is claimed.

Deadline: **2026-11-12 12:00 PST = 20:00 UTC = November 13 04:00 Beijing**. Entrant eligibility and any final personal declarations must use the entrant's actual answers; no identity details are included here. Registering alone does not submit a project.

## Title / tagline

English: **Cart Consent**

Tagline: **An AI can propose a purchase. A changed basket needs a new human decision.**

中文：**Cart Consent · 购物篮变更再确认**

## English Devpost Story — paste-ready

### Inspiration

A shopping assistant may propose the right products and still hand over the wrong checkout: a quantity, delivery charge or address can change after someone says yes. A general “approved” flag does not show which basket was approved. Cart Consent makes that decision specific and reviewable.

### What it does

The working Python CLI and local JSON API bind approval to the exact catalog items, quantities, prices, currency, budget, shipping option and charge, recipient address, merchant and payment mode. A critical change invalidates approval. Separate agent and human HTTP capabilities let an agent propose or edit a basket, while only the human capability can approve its current fingerprint and request a checkout link. The ledger rechecks revision, catalog and approval after an upstream request, withholding a link if the approved state changed during the call.

### How we built it

The implementation uses Python's standard library, SQLite transactions, integer minor-unit amounts, SHA-256 snapshot fingerprints, expiring approvals and persisted request identities. The catalog owns prices and shipping charges; model output is restricted to known SKU/quantity selections and an explanation, then independently validated. The optional local Ollama planner has no approval or payment tools. Structured shipping-address fields are omitted from its prompt, although free-text goals are sent unchanged and must not contain sensitive information.

The payment adapter uses PayPal's official sandbox OAuth and Orders v2 endpoints. It requests a complete representation and checks the returned amount, items, shipping, merchant and snapshot identifiers before releasing an allowed sandbox approval URL. It implements neither production mode nor a capture endpoint.

### What actually ran

On November 10, a fresh local `qwen2.5:0.5b` proposal through Ollama 0.40.15 returned in **5.899 seconds**, selecting one fictional pen set. USD 8.99 plus USD 4.99 shipping totaled **USD 13.98**, below the USD 50.00 budget. The result remained an unapproved `DRAFT`. The developer reviewed the complete fictional snapshot and explicitly approved its exact fingerprint through the local CLI.

The real PayPal sandbox then returned **`PAYER_ACTION_REQUIRED`** for one unpaid order. The existing adapter validated the representation without a code change. An earlier attempt failed at OAuth HTTP 401 before any Orders request; duplicated private configuration was corrected while retaining the same cart, fingerprint, approval nonce and saved request ID. The successful checkout CLI invocation took 1.369 seconds. The raw success HTTP status was not recorded. A guarded subsequent checkout CLI call returned the cached existing order with zero network calls. That verifies local cached replay, not remote idempotency. A sanitized evidence record is included in the repository; credentials, account/order identifiers and approval URLs remain private.

This was a **developer-operated synthetic demonstration**, not authenticated real-buyer consent. The approval URL was not opened. No buyer login, checkout, authorization, capture, completed purchase or production payment occurred. `CAPTURE` is an order intent field, not evidence of an executed capture. The HTTP agent/human role tests are separate mock demonstrations. Earlier November 6 local-model evidence, including timeouts and an over-budget rejection, remains available rather than being replaced by the successful run.

### Challenges and limits

The difficult boundary is preserving the same reviewed state through edits, expiration, concurrent changes and ambiguous upstream failures. Saved attempt identities prevent blind retries with new keys. Local revocation blocks this application's future retrieval; it cannot cancel a remote URL already disclosed. The prototype assumes one local buyer ledger and does not establish multi-tenant identity, fraud prevention, real tax/shipping/address validation, model-quality performance or AP2 certification. Strict response matching may reject account responses with additional normalized fields; one successful run does not prove universal compatibility.

### Build disclosure and entry

Codex assisted design, coding, tests and documentation. Runtime AI is the explicitly configured local Ollama model; default rule-based mocks disclose `ai_used=false`. This is an original MIT-licensed implementation. PayPal Agent Toolkit and Google AP2 were reviewed as existing design/protocol comparisons; no copied code, schemas or assets are claimed. Approval-bound checkout already exists, so this is a focused consent gate rather than a new payment protocol.

The repository has runnable CLI/API instructions and a successful narrow AI/sandbox integration record. The [public English demonstration](https://youtu.be/icz2WX1DXZ4) is published at **138.8 seconds**. It combines edited sanitized evidence cards with an actual mock-mode native terminal shot, rather than continuous footage. Generic synthetic Aria narration and 25 English captions accompany the edit; full audio/video decoding passed, with no full manual listening claim. Official final submission was verified at **2026-11-10 07:37:39.790 UTC** on the [public project page](https://devpost.com/software/cart-consent), which displayed **“Project submitted!”** and **“SUBMITTED TO PayPal AI Hackathon”**. This confirms entry receipt, not eligibility approval, judging results or a prize.

## 中文摘要

购物智能体可以提出商品组合，批准必须对应人实际审阅的精确快照。Cart Consent 将商品、数量、价格、币种、预算、运费、地址、商户和支付模式绑定到指纹，关键字段变化或调用期间状态变化都会阻止旧批准释放链接。Python CLI/JSON API 已实现角色分离、持久化幂等和独立金额校验。11月10日真实本地 qwen2.5:0.5b 在5.899秒生成一件虚构笔套装建议，含运费总价13.98美元，低于50美元预算，初始仍未批准；开发者审阅后明确批准该指纹，真实PayPal沙箱返回PAYER_ACTION_REQUIRED。首次OAuth401在建单前发生，修正私密重复配置后保留原购物篮、批准及请求身份，只有一次远程建单。未打开买家链接、未登录买家、未结账或扣款。11月9日报名已核实，11月10日已公开138.8秒[演示视频](https://youtu.be/icz2WX1DXZ4)，为脱敏证据卡与真实mock终端画面的剪辑，不是连续录屏。作品已于2026年11月10日07:37:39.790 UTC完成正式提交，[官方公开项目页](https://devpost.com/software/cart-consent)显示“Project submitted!”及“SUBMITTED TO PayPal AI Hackathon”。这确认作品收件，不代表资格审核、评审或获奖；提交时源码为da95fd1bde83c608d72f57bd60aeb78a0eade44d。

## Technology / testing / reuse fields

- Built with: Python standard library, SQLite, HTTP JSON API, SHA-256, PayPal sandbox OAuth/Orders v2, local Ollama `/api/chat`, `qwen2.5:0.5b`. No vendor SDK or model weights are bundled.
- Run: follow the public README. The default CLI `demo` and HTTP role demo are synthetic mocks. Real sandbox configuration must be supplied privately by an authorized operator; no credentials or private ledger are distributed.
- Verification: twenty-three local tests are recorded in the portfolio. They are offline tests, distinct from the dated real integration evidence, and are not a security certification or model-quality benchmark.
- Source: https://github.com/misakamikotoghr-5205/cart-consent-paypal ; MIT.
- OSS comparisons: PayPal Agent Toolkit and Google AP2 at the pinned commits/licenses in `docs/landscape.md`, reviewed as comparisons without code reuse. External Ollama and the selected model retain their separate licenses.
- New work: independently created November 4–5, 2026, and advanced during the event window. No global novelty claim.

## Material mapping

| Required material | Current value / state |
| --- | --- |
| Features, tools and integration explanation | Story and technical fields above |
| Public licensed repository and instructions | Repository URL above; MIT; Python CLI and local API |
| Functional demo access | Runnable repository; no hosted interactive checkout is claimed |
| PayPal sandbox and meaningful AI usage | Actual November 10 fresh proposal → exact synthetic approval → unpaid sandbox order, sanitized evidence in `docs/evidence/sandbox-model-20261110.json` |
| Public YouTube video under three minutes | [Published November 10](https://youtu.be/icz2WX1DXZ4); 138.8 seconds; edited evidence cards + actual mock terminal shot; not continuous footage |
| Registration | Verified November 9; distinct from final project submission |
| Submitted materials | Overview, Story, technology tags, repository/video URLs, original gallery and cover |
| Official final entry | [Project submitted!](https://devpost.com/software/cart-consent), verified November 10 at 07:37:39.790 UTC; not eligibility approval or judging results |

Sponsor tools and sponsor-specific prizes are optional. Select only tools genuinely used. Do not substitute mock links for sandbox evidence, synthetic operator approval for authenticated buyer consent, or an entry draft for formal submission.
