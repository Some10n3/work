const output = document.getElementById('result');
let currentExpression = '';
let memory = 0;

// Keyup event handler
document.addEventListener('keyup', (event) => {
    const key = event.key;
    
    // Check if the pressed key is a number or an operator
    if (!isNaN(key) || key === '+' || key === '-' || key === '*' || key === '/') {
        currentExpression += key;
        output.innerHTML = currentExpression;
    } else if (key === 'Enter' || key === '=') {
        try {
        // Try to evaluate the expression when Enter key is pressed
        const result = eval(currentExpression);
        output.innerHTML = result;
        currentExpression = result.toString(); // Store the result as the new expression
        } catch (error) {
        output.innerHTML = 'Error';
        currentExpression = ''; // Clear the expression in case of an error
        }
    } else if (key === 'Backspace') {
        // Handle backspace to remove the last character
        currentExpression = currentExpression.slice(0, -1);
        output.innerHTML = currentExpression;
    } else if (key === 'c' || key === 'C') {
        // Clear the expression when 'C' or 'c' is pressed
        currentExpression = '';
        output.innerHTML = '0';
    }
});

const buttons = document.querySelectorAll('td');

document.addEventListener('click', (event) => {
    const element = event.target;
    const key = element.id;

    switch (key){
        case 'Enter':
            try {
            // Try to evaluate the expression when Enter key is pressed
            const result = eval(currentExpression);
            output.innerHTML = result;
            currentExpression = result.toString(); // Store the result as the new expression
            } catch (error) {
                output.innerHTML = 'Error';
                currentExpression = ''; // Clear the expression in case of an error
            }
            break;
        case 'c':
            currentExpression = '';
            output.innerHTML = '0';
            break;
        case 'Backspace':
            // Handle backspace to remove the last character
            currentExpression = currentExpression.slice(0, -1);
            output.innerHTML = currentExpression;
            if (currentExpression === '') {
                output.innerHTML = '0';
            }
            break;
        //case when clicking numbers
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            if (currentExpression === '0'){
                currentExpression = '';
            }
            currentExpression += key;
            output.innerHTML = currentExpression;
            break;
        //case when clicking scientific operators
        case 'sin':
            currentExpression = Math.sin(currentExpression);
            output.innerHTML = currentExpression;
            break;
        case 'cos':
            currentExpression = Math.cos(currentExpression);
            output.innerHTML = currentExpression;
            break;
        case 'tan':
            currentExpression = Math.tan(currentExpression);
            output.innerHTML = currentExpression;
            break;
        case 'pi':
            currentExpression += Math.PI;
            output.innerHTML = currentExpression;
            break;
        case 'sqrt':
            currentExpression = Math.sqrt(currentExpression);
            output.innerHTML = currentExpression;
            break;
        case 'square':
            currentExpression = Math.pow(currentExpression, 2); 
            output.innerHTML = currentExpression;
            break;
        case '1/x':
            currentExpression = 1/currentExpression;
            output.innerHTML = currentExpression;
            break;
        case 'factorial':
            currentExpression = factorial(currentExpression);
            output.innerHTML = currentExpression;
            break;
        case 'mc':
            memory = 0;
            break;
        case 'mr':
            currentExpression = memory;
            output.innerHTML = currentExpression;
            break;
        case 'm+':
            if (memory === 0){
                memory = currentExpression;
                currentExpression = '';
                output.innerHTML = '0';
                break;
            }
            memory += currentExpression;
            currentExpression = '';
            output.innerHTML = '0';
            break;
        case 'm-':
            if (memory === 0){
                memory = -currentExpression;
                break;
            }
            memory -= currentExpression;
            currentExpression = '';
            output.innerHTML = '0';
            break;
        default:
            // Check if the pressed key is a number or an operator
            if (!isNaN(key) || key === '+' || key === '-' || key === '*' || key === '/') {
                currentExpression += key;
                output.innerHTML = currentExpression;
                if (currentExpression === '') {
                    currentExpression = '0';
                }
            }
    }
});

function factorial(n){
    if (n == 0 || n == 1){
        return 1;
    } else {
        return n * factorial(n-1);
    }
}