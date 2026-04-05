(function () {
    const storageKey = "theme-preference";
    const root = document.documentElement;
    const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    const labelsByPreference = {
        auto: "Auto",
        light: "Light",
        dark: "Dark",
    };

    function getStoredPreference() {
        const storedPreference = window.localStorage.getItem(storageKey);
        if (
            storedPreference === "light" ||
            storedPreference === "dark" ||
            storedPreference === "auto"
        ) {
            return storedPreference;
        }

        return "auto";
    }

    function applyTheme(preference) {
        if (preference === "auto") {
            root.dataset.theme = "auto";
            return;
        }

        root.dataset.theme = preference;
    }

    function syncControls(preference) {
        const labels = document.querySelectorAll("[data-theme-current-label]");
        for (const label of labels) {
            label.textContent = labelsByPreference[preference];
        }

        const options = document.querySelectorAll("[data-theme-option]");
        for (const option of options) {
            if (!(option instanceof HTMLButtonElement)) {
                continue;
            }

            const isSelected = option.dataset.themeOption === preference;
            option.setAttribute("aria-pressed", isSelected ? "true" : "false");
        }
    }

    function updateTheme(preference) {
        applyTheme(preference);
        syncControls(preference);
    }

    function initializeTheme() {
        const preference = getStoredPreference();
        updateTheme(preference);

        const options = document.querySelectorAll("[data-theme-option]");
        for (const option of options) {
            option.addEventListener("click", (event) => {
                if (!(event.currentTarget instanceof HTMLButtonElement)) {
                    return;
                }

                const nextPreference = event.currentTarget.dataset.themeOption;
                if (
                    nextPreference !== "auto" &&
                    nextPreference !== "light" &&
                    nextPreference !== "dark"
                ) {
                    return;
                }

                window.localStorage.setItem(storageKey, nextPreference);
                updateTheme(nextPreference);

                const menu = event.currentTarget.closest("[data-theme-menu]");
                if (menu instanceof HTMLDetailsElement) {
                    menu.open = false;
                }
            });
        }

        mediaQuery.addEventListener("change", () => {
            if (getStoredPreference() === "auto") {
                updateTheme("auto");
            }
        });
    }

    window.themePreference = {
        applyTheme,
        getStoredPreference,
        initializeTheme,
    };

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initializeTheme, {
            once: true,
        });
    } else {
        initializeTheme();
    }
})();
