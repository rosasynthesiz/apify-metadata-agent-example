# Public HTML Metadata: agent usage example

Get static page metadata as structured JSON: title, description, canonical URL, Open Graph, Twitter Card tags and JSON-LD.

[Try the Apify Actor](https://apify.com/lightbarrer/public-html-metadata-private-test)

## Pricing
The current release has **no Actor service fee** and payment billing is OFF. Apify platform compute, transfer and storage charges may apply to the caller's account. This is not unlimited free hosting. A future paid release is not enabled.

## Tested example
Input: `{"urls":["https://example.com/"]}`.

Actual result: `status: "ok"`, `title: "Example Domain"`; metadata absent from the page remains null or empty. The dataset had one row and matched `OUTPUT.results` exactly. Billing was false and confirmed charge events were zero. Recorded run time was 2.493 seconds for this one-page self-test; this is not a speed guarantee or evidence of customer demand.

See [full input](examples/input.json), [actual OUTPUT](examples/output.json), [actual dataset](examples/dataset.json) and [MCP call sequence](examples/mcp-calls.json). These are recorded results, not a new run whenever the file is opened. The static fixture proof of OG/Twitter/JSON-LD extraction is separate from example.com's empty fields.

## Use from an MCP agent
1. Add the configuration in `mcp-config.json` to your MCP client. Sign in with your own Apify OAuth account. Never commit tokens.
2. Fetch Actor details and inspect its input and pricing.
3. Call the Actor with 1–3 public HTTPS URLs. Put run options in `callOptions`, not input: memory 128, timeout 60, maxTotalChargeUsd 0.01. Restart must remain OFF (default).
4. Use the returned run ID to check completion. Never repeat an ambiguous run submission.
5. Retrieve dataset items and the key-value store record with key `OUTPUT`. `call-actor` itself returns run/storage IDs rather than the extracted data. Counts can briefly lag after completion, so read the dataset before concluding that it is empty.
6. Check page `status`, `successful`, `unprocessed`, `billing_enabled` and `confirmed_events`.

### Copyable agent prompt
Use Apify MCP to fetch details of lightbarrer/public-html-metadata-private-test. Run it once on https://example.com/ with memory 128 MB, timeout 60 sec, maxTotalChargeUsd 0.01 and restart OFF. Wait for completion, retrieve dataset items and the OUTPUT record from the returned storage IDs. Report the actual title and metadata; verify billing_enabled false and confirmed_events 0. Stop on an ambiguous submission instead of starting another run.

## Limits
- 1–3 URLs, public HTTPS 443, static HTML only; maximum 1 MB response per page.
- No JavaScript rendering, login, proxies, linked-page crawling or anti-bot bypass.
- Empty fields are valid; JSON-LD warnings are not schema or factual validation.
- Escape scraped values before displaying HTML. Do not send private URLs or credentials.
- Primary results: run Storage → Key-value store → OUTPUT. Free release also provides a dataset copy for exports.
- Download records within your platform storage retention period.

## Offline evidence check
`python3 verify_example.py` checks the committed input, OUTPUT and dataset consistency without a token, network or credit use.

## Verification boundary
The live end-to-end test used the Codex Apify MCP connection, build 0.2.6 on 16 October 2026. A separate CLI client did not load Apify tools; compatibility with every client is not claimed. No customer adoption, revenue or uptime claim.

## References
- [Apify MCP](https://docs.apify.com/mcp)
- [Actor API](https://docs.apify.com/api/v2/actors-runs-post)

This repository contains usage examples and recorded test output; it does not contain the Actor runtime or credentials. No open-source license is specified.

## Reproduce the populated metadata demo

Use [fixture-input.json](examples/fixture-input.json) with the same bounded settings above. This synthetic HTTPBin HTML fixture contains known Open Graph, Twitter Card and Product JSON-LD fields. The recorded [fixture-output.json](examples/fixture-output.json) shows `MOTLEY Fixture`, `og:title: Known OG`, `twitter:card: summary` and the Product object. Its duplicate fragment is skipped. This is a controlled self-test, not customer demand or a claim about example.com content.

Example tasks: extract social card metadata from supplied URLs; export JSON-LD from public pages; collect CMS titles, descriptions and canonical URLs. Static HTML only, 1–3 URLs per run.
