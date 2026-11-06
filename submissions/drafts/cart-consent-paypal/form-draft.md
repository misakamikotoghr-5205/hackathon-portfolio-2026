# Cart Consent — PayPal draft, 2026-11-06

Public [event](https://paypalaihackathon.devpost.com/) and [rules](https://paypalaihackathon.devpost.com/rules). Join through the event's **Join hackathon** button, then its authenticated submission flow. No authenticated form was inspected here: the button redirects to Devpost registration. The following is ready content for the required materials, not a claim that every field label/character limit is known.

Deadline: **2026-11-12 12:00 PST = 20:00 UTC = November 13 04:00 Beijing**. Adult individual eligibility, local/account restrictions and actual entrant/team identity must be checked privately. Registering alone does not submit a project.

## Title / tagline

English: **Cart Consent — human approval that follows the exact basket**

Tagline: **An AI can propose a purchase. A changed basket needs a new human decision.**

中文：**Cart Consent · 购物篮变更再确认**

## English summary — paste-ready, current evidence

Cart Consent separates an AI shopping suggestion from a person's authority to create a checkout link. A fictional stationery basket is bound to its exact products, quantities, merchant-owned prices, currency, budget, shipping charge, recipient address, merchant and payment mode. Any critical change revokes the old approval. Separate agent and human API capabilities ensure that an agent can propose a basket but cannot approve it or request its payment link. The local ledger also rechecks approval after an upstream request, so an in-flight edit withholds the returned link.

The working Python CLI and JSON API use SQLite, integer minor-unit amounts, revision checks and persisted request IDs. Optional adapters implement the official PayPal sandbox OAuth/Orders contract and constrained local Ollama proposals. On November 6, the production planner/HTTP transport genuinely called local `qwen2.5:0.5b`: one short fictional request yielded a valid pen-set quantity of one in 21.350 seconds, costing 1,398 minor units including shipping against a 5,000 budget, and remained an unapproved `DRAFT`. The evidence retains the raw response, two timeouts and a prior budget rejection, rather than presenting one accepted output as a quality benchmark. No sandbox order creation, buyer checkout or capture has been performed. The default demo still labels its consent and payment links as synthetic. There is no production or capture endpoint.

The focused contribution is testable consent drift and role separation, rather than a new payment protocol. The code is public and MIT licensed. Actual sandbox and AI demonstration evidence, followed by an English public video, remain necessary before this candidate can claim to demonstrate the event's required technologies.

## 中文摘要

购物智能体可以提出商品组合，但不能替人批准。Cart Consent 把人工批准绑定到商品、数量、价格、币种、预算、运费、地址、商户和支付模式的精确快照；关键字段变化会撤销旧批准，调用期间发生变化也不会释放旧链接。Python CLI/JSON API 已实现权限分离、持久化幂等与金额校验。11月6日生产适配器真实调用本地 qwen2.5:0.5b，一次定向笔套装请求在21.350秒返回，1398分总价通过5000分预算校验，仍为未批准DRAFT；两次超时和一次超预算拒绝一并保留。PayPal沙箱仍未真实调用，不冒充已完成支付、完整演示或通用模型质量验证。

## Technology, differentiation and build process

- Built with: Python standard library, SQLite, HTTP JSON API, SHA-256 snapshots, official PayPal Orders v2 sandbox adapter, optional local Ollama `/api/chat` structured output. No vendor SDK/runtime/model weights are bundled.
- Difference: human capabilities, catalog-owned amounts, expiring exact approval, changed-field revocation, in-flight recheck and persisted retry identity. No AP2 mandate/signature certification, remote order cancellation guarantee, real tax/shipping/address validation or capture.
- Process: specify consent snapshot → implement transactional states and roles → bind amount/catalog/context → add sandbox and model adapters with configuration failure closed → test field changes, races, persistence and privacy. Twenty-three local tests are recorded in the portfolio; they are not remote PayPal evidence.
- AI disclosure: Codex assisted design, coding, tests and documentation. Runtime inference is optional; the real local model requests and their accepted/rejected/timed-out outcomes are recorded in `docs/evidence/local-model-20261106.json`. Rule-based mocks still explicitly report no AI. This narrow local probe is not a completed combined model/PayPal demonstration or recorded video.
- OSS disclosure: original implementation MIT. PayPal Agent Toolkit and Google AP2 were reviewed at pinned commits as Apache-2.0 design/protocol comparisons; no copied code, schemas or assets. Optional external Ollama is MIT, with each selected model's separate license to be checked.
- New work: independently created November 4–5, 2026, during the event window. Consent mechanisms already exist; no global novelty claim.

## Material mapping and remaining real evidence

| Required material from public rules | Honest value / state |
|---|---|
| Project features and functionality | Summary and technical sections above |
| Tools/model usage explanation | Actual `qwen2.5:0.5b` local request/response evidence; entrant review and recorded reproduction remain |
| Public open-source repository and runnable setup | https://github.com/misakamikotoghr-5205/cart-consent-paypal ; MIT and README instructions |
| Working demo access | Repository setup can satisfy access; no public hosted URL is claimed |
| PayPal sandbox + meaningful AI integration | Implemented adapters, actual combined demonstration still absent |
| Public YouTube video under 3 minutes | No video exists; use [video-script.md](video-script.md) only after recording actual behavior |
| Identity, team, rules agreement and any additional authenticated questions | Entrant/root supplies privately; no values invented here |

Sponsor tools and sponsor-specific prizes are optional. Do not select a sponsor award for a tool that was not genuinely used. Do not replace missing sandbox evidence with a mock link, or treat creating a Devpost draft as formal submission.
