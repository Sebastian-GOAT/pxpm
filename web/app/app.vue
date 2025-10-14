<template>
    <UApp>
        <NuxtLayout>
            <NuxtPage />
        </NuxtLayout>
    </UApp>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
@import "tailwindcss";
@import "@nuxt/ui";

:root {
    --primary: #1173D4;

    --bg: #F6F7F8;
    --fg: black;

    --bg-card: #1C252D; /* Change to light mode */
    --outline: #93aac5;
}

.dark {
    --bg: #101922;
    --fg: white;

    --bg-card: #1C252D;
    --outline: #3a434d;
}

@theme inline {
    --color-primary: var(--primary);

    --color-bg: var(--bg);
    --color-fg: var(--fg);

    --color-bg-card: var(--bg-card);
    --color-outline: var(--outline);
}

body {
    min-height: 100vh;
    background-color: var(--bg);
    color: var(--fg);
    font-family: "Inter", sans-serif;
}
</style>