# 🚀 Senior SEO & Google Indexing Deployment Guide

This guide provides actionable instructions to verify and monitor **restoran.mirolimov.uz** in Google Search Console (GSC).

---

## 1. Google Search Console (GSC) Setup

### Step A: Property Type Selection
Always choose **URL Prefix** if you want to verify via HTML tag or file, OR **Domain** if you have DNS access (Recommended).

1. Go to [GSC Dashboard](https://search.google.com/search-console).
2. Click **Add Property**.
3. Select **Domain** and enter `restoran.mirolimov.uz`.

### Step B: DNS Verification (Professional Method)
1. Google will provide a **TXT record** (e.g., `google-site-verification=abc...`).
2. Log in to your DNS provider (Cloudflare, GoDaddy, etc.) for **mirolimov.uz**.
3. Add a new record:
   - **Type**: `TXT`
   - **Name**: `restoran` (or `@` if you're verifying the root, but for subdomain use `restoran`)
   - **Value**: The TXT string from Google.
4. Click **Verify** in GSC.

---

## 2. Sitemap Submission
Once verified, you must tell Google where your pages are.

1. Navigate to **Sitemaps** in the GSC sidebar.
2. Under "Add a new sitemap", type: `sitemap.xml`.
3. Click **Submit**.

> [!TIP]
> Your sitemap is dynamic: `https://restoran.mirolimov.uz/sitemap.xml`. It automatically updates when you add new products in the admin panel.

---

## 3. Fixing "Discovered - currently not indexed"
This usually happens if Google knows about the page but hasn't crawled it yet due to low "Crawl Budget" or perceived low quality.

**Fixes implemented:**
- **Internal Linking**: Added "Related Products" in `product_detail.html` to help bots travel between pages.
- **Canonical Tags**: Explicitly defined in `base.html` to prevent duplicate content flags.
- **Social Signals**: Added OG/Twitter tags to encourage external sharing, which triggers crawls.

---

## 4. Final SEO Checklist (For Every Deploy)

- [x] **SSL Active**: `SECURE_SSL_REDIRECT` is True.
- [x] **Robots.txt**: Exists at `/robots.txt` and points to sitemap.
- [x] **Slugs**: URLs use readable strings (e.g., `/product/lavash/`) instead of IDs.
- [x] **JSON-LD**: Validated via [Schema.org Validator](https://validator.schema.org/).
- [x] **Core Web Vitals**: Images use `loading="lazy"`.
- [x] **Caching**: `WHITENOISE_MAX_AGE` set to 1 year for static assets.

---

## 5. Rollback Plan
If you encounter 500 errors after `DEBUG=False`:
1. Check Railway logs: `railway logs`.
2. Ensure `ALLOWED_HOSTS` includes your exact domain.
3. Verify `DATABASE_URL` is correctly attached in Railway Variables.
