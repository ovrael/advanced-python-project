import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ImageToTextView from '../views/AiTools/ImageToTextView.vue'
import SpamDetectionView from '../views/AiTools/SpamDetectionView.vue'
import TextAnalysisView from '../views/AiTools/TextAnalysisView.vue'
import ImageAnalysisView from '../views/AiTools/ImageAnalysisView.vue'
import SpeechToTextView from '../views/AiTools/SpeechToTextView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView

    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/imageToText',
    name: 'imageToText',
    component: ImageToTextView
  },
  {
    path: '/spamDetection',
    name: 'spamDetection',
    component: SpamDetectionView
  },
  {
    path: '/textAnalysis',
    name: 'textAnalysis',
    component: TextAnalysisView
  },
  {
    path: '/imageAnalysis',
    name: 'imageAnalysis',
    component: ImageAnalysisView
  },
  {
    path: '/speechToText',
    name: 'speechToText',
    component: SpeechToTextView
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
