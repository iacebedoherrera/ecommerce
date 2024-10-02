
async function paypalButton() {
    window.paypal.Buttons({
        style: {
            shape: "rect",
            layout: "vertical",
            color: "gold",
            label: "paypal",
        },
        async createOrder() {
            try {
                let products = localStorage.getItem('products')
                let amount = localStorage.getItem('amount')
                let backend_url = 'https://ecommerce-f8v1.onrender.com'
                const response = await fetch(backend_url + "/order/checkout", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        cart: products,
                        total_amount: amount
                    })
                });

                const orderData = await response.json();

                if (orderData.id) {
                    return orderData.id;
                }
                const errorDetail = orderData?.details?.[0];
                const errorMessage = errorDetail
                    ? `${errorDetail.issue} ${errorDetail.description} (${orderData.debug_id})`
                    : JSON.stringify(orderData);

                throw new Error(errorMessage);
            } catch (error) {
                console.error(error);
                // resultMessage(`Could not initiate PayPal Checkout...<br><br>${error}`);
            }
        },
        async onApprove(data, actions) {
            let backend_url = 'https://ecommerce-f8v1.onrender.com'
            try {
                const response = await fetch(backend_url + `/orders/${data.orderID}/capture`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                });

                const orderData = await response.json();
                // Three cases to handle:
                //   (1) Recoverable INSTRUMENT_DECLINED -> call actions.restart()
                //   (2) Other non-recoverable errors -> Show a failure message
                //   (3) Successful transaction -> Show confirmation or thank you message

                const errorDetail = orderData?.details?.[0];

                if (errorDetail?.issue === "INSTRUMENT_DECLINED") {
                    return actions.restart();
                } else if (errorDetail) {
                    throw new Error(`${errorDetail.description} (${orderData.debug_id})`);
                } else if (!orderData.purchase_units) {
                    throw new Error(JSON.stringify(orderData));
                } else {
                    const transaction =
                        orderData?.purchase_units?.[0]?.payments?.captures?.[0] ||
                        orderData?.purchase_units?.[0]?.payments?.authorizations?.[0];
                    //resultMessage(
                    //    `Transaction ${transaction.status}: ${transaction.id}<br>
                    //    <br>See console for all available details`
                    //);
                    console.log(
                        "Capture result",
                        orderData,
                        JSON.stringify(orderData, null, 2)
                    );
                    var jwt = document.cookie.replace(
                        /(?:(?:^|.*;\s*)jwt\s*\=\s*([^;]*).*$)|^.*$/,
                        "$1",
                    );
                    const products = localStorage.getItem('products');
                    const products_json = JSON.parse(products);
                    // Save the order in database
                    const response = await fetch(backend_url + "/order/save", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            token: jwt,
                            items: products_json
                        })
                    });

                    const responseJson = await response.json();
                    window.location.href = `/order_confirm/${responseJson.order_id}`;
                }
            } catch (error) {
                console.error(error);
                //resultMessage(
                //    `Sorry, your transaction could not be processed...<br><br>${error}`
                //);
            }
        }
    }).render("#paypal-button-container");
}