<template>
  <div class="grid md:grid-cols-4 gap-3 py-10 px-6">
    <div class="md:col-span-1 p-6 bg-teal-700 rounded-xl">  <!-- col-span full when in small screen -->
      <!-- w-full to fill the whole space in parent -->
      <div class="flex space-x-4">
        <input v-model="query" type="search" placeholder="Find a job..." class="w-full px-6 py-4 rounded-xl">
        <button @click="performSearch" class="px-6 py-4 bg-teal-900 text-white rounded-xl">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
               stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round"
                  d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"/>
          </svg>
        </button>
      </div>

      <hr class="my-6 opacity-30">

      <h3 class="mt-6 text-xl text-white">Categories</h3>

      <div class="mt-6 space-y-4">
        <p
            v-for="category in jobCategories"
            :key="category.id"
            @click="toggleCategory(category.id)"
            :class="{'bg-teal-900': selectedCategories.includes(category.id)}"
            class="py-4 px-6 text-white rounded-xl">
          {{ category.title }}
        </p>
      </div>
      {{ selectedCategories }}
    </div>

    <div class="md:col-span-3">
      <div class="space-y-4">
        <job v-for="job in jobs" :key="job.id" :job="job"/>
      </div>
    </div>
  </div>
</template>
<script setup>

let query = ''
let queryRef = ref('')
let {data: jobCategories} = await useFetch('http://localhost:8000/api/v1/jobs/categories')
let selectedCategories = ref([])
let {data: jobs} = await useFetch('http://localhost:8000/api/v1/jobs/', {
  query: {
    query: queryRef,
    categories: selectedCategories
  }
})

function performSearch() {
  queryRef.value = query
  console.log('searching for', query)
}

function toggleCategory(id) {
  const index = selectedCategories.value.indexOf(id)
  if (index === -1) {
    selectedCategories.value.push(id)
  } else {
    selectedCategories.value.splice(index, 1)
  }
}
</script>