// const validationErrorType = {};

/**
 * Validates a password based on length and complexity requirements.
 *
 * @param {string} password - The password to be validated.
 *
 * @returns {string} An error message indicating validation failure, or an empty string if validation passes.
 */
export function validatePassword(password) {
        const minLen = 6;
        const maxLen = 18;
        const passLen = password.length;

        if (passLen < minLen || passLen > maxLen) {
                return `La contraseña debe ser de almenos ${minLen} caracteres y maximo ${maxLen} caracteres.`;
        }

        const pattern = new RegExp(`^(?=.*[A-Z])(?=.*\\d).{${minLen},${maxLen}}$`);
        if (!password.match(pattern)) {
                return "contraseña debe contener una letra mayuscula y un numero.";
        }

        return "";
}

/**
 * Validates whether a selected date meets a minimum age requirement.
 *
 * @param {number} minAge - The minimum age in years.
 * @param {Date} selectedDate - The selected date to be validated.
 *
 * @returns {string} An error message indicating validation failure, or an empty string if validation passes.
 */
export function validateAgeByDate(minAge, selectedDate) {
        const currentDate = new Date();
        const minDate = new Date();

        minDate.setFullYear(currentDate.getFullYear() - minAge);

        if (selectedDate > currentDate) {
                return "Fecha Invalida";
        } else if (selectedDate > minDate) {
                return `Debe Ser Mayor De ${minAge} Años`;
        }

        return "";
}
