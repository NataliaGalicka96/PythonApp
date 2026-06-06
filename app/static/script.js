
document.addEventListener("DOMContentLoaded", () => {

    const saveButtons = document.querySelectorAll(".btn-save")

    const csrfToken =
        document.querySelector(
            'meta[name="csrf-token"]'
        ).content

    saveButtons.forEach(button => {
        //Iterujemy przez każdy przycisk
        //Wysyłam żądanie do endpointu @jobs_bp.route("/jobs/<int:id>/save", methods = ["POST"])


        button.addEventListener("click", async () => {

            const jobId = button.dataset.jobId // z html - data-job-id <button class="btn-save" data-job-id="{{offer.id}}">

            try {

                console.log("Jestem tutaj")
                console.log(jobId)

                const response = await fetch(`/jobs/${jobId}/save`, {
                    method: "POST",
                    headers: {
                        "Content-Type":
                            "application/json",

                        "X-CSRFToken":
                            csrfToken
                    }
                });

                const result = await response.json(); //Parsujemy odpowiedź jako json

                console.log(result)

                if (response.ok) {
                    if (result.saved) {
                        button.classList.add("saved")
                        button.innerHTML = "Zapisano"
                    } else {
                        button.classList.remove("saved")
                        button.innerHTML = "Zapisz"
                    }

                } else {
                    alert(result.error || "Wystąpił błąd podczas zapisywania ogłoszenia do ulubionych");
                }
            } catch (error) {
                console.error("Error liked offer:", error); // Logujemy błąd w konsoli
            }
        })

    });

    //OSBŁUGA OKNA MODALNEGO - APLIKOWANIE
    const modal =
        document.getElementById(
            "applyModal"
        )

    const closeModal =
        document.getElementById(
            "closeModal"
        )

    const applyButtons =
        document.querySelectorAll(
            ".btn-apply"
        )

    const modalJobTitle =
        document.getElementById(
            "modalJobTitle"
        )

    const modalJobId =
        document.getElementById(
            "modalJobId"
        )

    // OPEN MODAL

    applyButtons.forEach(button => {

        button.addEventListener(
            "click",
            () => {

                const jobId =
                    button.dataset.jobId

                const jobTitle =
                    button.dataset.jobTitle

                modal.classList.add(
                    "active"
                )

                modalJobTitle.innerText =
                    `Aplikuj — ${jobTitle}`

                modalJobId.value =
                    jobId

            }
        )

    })

    // CLOSE BUTTON

    closeModal.addEventListener(
        "click",
        () => {

            modal.classList.remove(
                "active"
            )

        }
    )

    // CLOSE ON BACKDROP

    modal.addEventListener(
        "click",
        (e) => {

            if (
                e.target === modal
            ) {

                modal.classList.remove(
                    "active"
                )

            }

        }
    )

})