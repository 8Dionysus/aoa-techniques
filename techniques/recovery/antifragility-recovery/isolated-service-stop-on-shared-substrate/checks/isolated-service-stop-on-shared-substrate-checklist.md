# Isolated Service Stop On Shared Substrate Checklist

Use this checklist to confirm that the bounded stop stayed smaller than full teardown and still produced explicit evidence.

- The target service was named explicitly before the stop.
- The shared substrate set was named explicitly before the stop.
- The stop handle affected only the target service.
- A post-stop check showed that the target service was actually down.
- A post-stop check showed that the shared substrate was still healthy enough for the next bounded step.
- The route preserved an explicit escalation seam to broader recovery if hidden coupling appeared.
