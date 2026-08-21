---
title: RX-8 Oil Nozzles, Premix & Clean Oil Feed
permalink: /ProjectPages/RX8/OMP/nozzles-premix/
description: >
  The system around the Series 1 RX-8 OMP — oil nozzle function and testing,
  what premix does and doesn't do, and clean oil feed conversions like the
  Sohn adapter, with the trade-offs of each.
---

The OMP doesn't work alone — metered oil only protects the engine if the nozzles, lines and the oil itself are right. This page covers the delivery end of the system, then the two big aftermarket topics: premixing two-stroke oil into the fuel, and clean oil feed conversions.

## Oil Nozzles

The Series 1 Renesis uses **two oil nozzles per rotor**, and because the Renesis breathes through side exhaust ports, Mazda angled these nozzles to inject oil directly toward the side housings — improving lubrication of the side housing and side seal area, which works harder on this engine than on peripheral-exhaust rotaries.

Each nozzle assembly includes a **one-way check valve** on the air-hose side, preventing reverse flow. The metered oil is injected, does its job at the seal interfaces, and is then burned as part of combustion — which is why oil level checks are part of normal RX-8 ownership.

### Testing & Symptoms

With a nozzle removed:

- It should **hold vacuum** applied from the air bleed side. A check valve that won't hold vacuum can allow reverse flow or air-lock the line.
- Oil should pass freely in the delivery direction.

Symptoms of a blocked nozzle are quiet but cumulative: that injection point simply stops being lubricated. There's no warning light for it — the pump and PCM are perfectly happy pushing oil at a dead end. On a high-mileage engine being serviced, vacuum-testing the nozzles while access is open is cheap insurance. Don't clear blockages by drilling; the orifice size is the metering. Solvent soak and compressed air only.

### Line Restrictions

The pipes and connector bolts between pump and nozzle have small internal drillings that varnish up on engines with long service neglect. Checks for this are covered in [diagnostics & testing](/ProjectPages/RX8/OMP/testing/).

## Premix — What It Does and Doesn't Do

"Premix" means adding two-stroke oil directly to the fuel tank, so a small amount of lubricant arrives at the seals with the fuel charge.

**What it does well:**
- Adds lubrication via the intake charge, reaching surfaces wetted by the fuel/air mixture — particularly the apex seal path.
- Acts as a **safety net**: if the OMP under-delivers or fails, premix keeps some lubricant arriving.
- Uses purpose-made two-stroke oil, which is formulated to burn cleanly (low ash), unlike crankcase oil.

**What it doesn't do:**
- It is **not targeted**. The OMP nozzles inject oil deliberately toward the side housings; premix distributes with the charge. The two are complementary, not interchangeable.
- It does **not repair a failed OMP**. A failed pump also means the engine's commanded, condition-dependent metering is gone — and the PCM's fail-safe behaviour (limp mode) exists for a reason. Running indefinitely on premix alone, with the metering system dead, is a risk decision, not a fix.

Community-reported premix ratios vary widely and are not treated here as manufacturer guidance. This car uses Renewable Lubricants Bio-Rotary Racing Premix; the [Sohn-adapter and premix page](/ProjectPages/RX8/sohn-adapter/#bio-rotary-oil-and-premix) converts the product's published application range. If you premix, measure the actual fuel added and record the dose rather than relying on a nominal tank quantity.

## Clean Oil Feed Conversions (Sohn-Style Adapters)

The stock system meters **engine sump oil** — whatever crankcase oil you run is what gets burned. Crankcase oils carry metallic detergent and anti-wear additive packages that leave **sulphated ash** when burned: carbon deposits, fouled plugs, and grief for seals and the catalyst over time.

A clean oil feed conversion (the Sohn adapter being the best-known) re-plumbs the OMP's **inlet** to draw from a small dedicated reservoir of two-stroke oil instead of the sump. The stock pump, control and nozzles all keep working exactly as designed — only the oil being metered changes.

The fitted system uses a [custom-designed Sohn adapter](/ProjectPages/RX8/sohn-adapter/), documented separately from general clean-oil-feed principles and from EnduraOMP.

**Benefits:**
- The engine burns clean, ashless oil formulated for total-loss lubrication, dramatically reducing deposit formation.
- Sump oil stays uncontaminated by its job description — it just lubricates bearings, so its condition and your choice of grade no longer have to compromise between "good crankcase oil" and "good burning oil".

**Trade-offs and obligations:**
- **You become the low-oil warning system.** The stock system can never run the metering circuit dry — the sump feeds it. With an external reservoir, an empty tank means no injection oil at all, and there is no factory warning for it. Checking and filling the reservoir becomes a hard maintenance discipline.
- More fittings and hose means more potential leak/air-ingestion points — inspect them as part of routine maintenance.
- Install quality matters: the feed must be reliable and air-free, and the reservoir mounted and routed so it can't chafe or starve under cornering.

This trade-off — better oil chemistry in exchange for the user carrying responsibility for the reservoir — is exactly the problem space my MEng project explored: [EnduraOMP](/ProjectPages/EnduraOMP/) combines the dedicated clean-oil reservoir concept with electronic metering, level sensing and a driver-visible gauge, so the system watches the tank rather than relying on the owner's memory.

## Maintenance After Modification

Whichever route you take, modifications to the lubrication system raise the inspection bar rather than lowering it:

- Verify oil consumption (or reservoir consumption) regularly — consumption is proof of delivery.
- Vacuum-test nozzles and inspect unions at service intervals.
- Keep premix discipline consistent if you rely on it; an unrecorded "did I dose this tank?" is how engines get hurt.
- After any line work, prime and leak-check exactly as you would after [pump servicing](/ProjectPages/RX8/OMP/servicing/).
