const form =
    document.getElementById("predictionForm");


const predictButton =
    document.getElementById("predictButton");


const loading =
    document.getElementById("loading");


const result =
    document.getElementById("result");


const errorBox =
    document.getElementById("error");


const predictionText =
    document.getElementById("predictionText");


const probabilityText =
    document.getElementById("probabilityText");



form.addEventListener(
    "submit",
    async function (event) {


        // Prevent page reload

        event.preventDefault();


        // Hide previous messages

        result.classList.add("hidden");

        errorBox.classList.add("hidden");


        // Show loading

        loading.classList.remove("hidden");

        predictButton.disabled = true;

        predictButton.innerText =
            "Predicting...";


        // --------------------------------------------------
        // Get Form Data
        // --------------------------------------------------

        const data = {

            gender:
                document.getElementById("gender").value,

            age:
                document.getElementById("age").value,

            degree:
                document.getElementById("degree").value,

            branch:
                document.getElementById("branch").value,

            cgpa:
                document.getElementById("cgpa").value,

            backlogs:
                document.getElementById("backlogs").value,

            internships:
                document.getElementById("internships").value,

            certifications:
                document.getElementById("certifications").value,

            coding_skills:
                document.getElementById("coding_skills").value,

            communication_skills:
                document.getElementById(
                    "communication_skills"
                ).value,

            aptitude_score:
                document.getElementById(
                    "aptitude_score"
                ).value,

            projects:
                document.getElementById(
                    "projects"
                ).value

        };


        console.log(
            "Sending Data:",
            data
        );


        try {


            // --------------------------------------------------
            // Send Data to Flask
            // --------------------------------------------------

            const response =
                await fetch(
                    "/predict",
                    {

                        method: "POST",

                        headers: {

                            "Content-Type":
                                "application/json"

                        },

                        body:
                            JSON.stringify(data)

                    }
                );


            const resultData =
                await response.json();


            console.log(
                "Server Response:",
                resultData
            );


            // --------------------------------------------------
            // Handle Response
            // --------------------------------------------------

            if (resultData.success) {


                predictionText.innerText =
                    resultData.prediction;


                if (
                    resultData.probability !== null &&
                    resultData.probability !== undefined
                ) {

                    probabilityText.innerText =
                        "Confidence: " +
                        resultData.probability.toFixed(2) +
                        "%";

                }

                else {

                    probabilityText.innerText =
                        "";

                }


                result.classList.remove(
                    "hidden"
                );


            }

            else {


                errorBox.innerText =
                    resultData.error ||
                    "Prediction failed.";

                errorBox.classList.remove(
                    "hidden"
                );

            }


        }

        catch (error) {


            console.error(error);


            errorBox.innerText =
                "Unable to connect to Flask server.";

            errorBox.classList.remove(
                "hidden"
            );


        }


        finally {


            // Hide loading

            loading.classList.add(
                "hidden"
            );


            // Enable button

            predictButton.disabled =
                false;

            predictButton.innerText =
                "Predict Placement";


        }

    }
);