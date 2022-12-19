export const Routes = {
  // pages
  Register: { path: "./pages/Register" },
  LogIn: { path: "./pages/Login" },
  ForgotPassword: { path: "./pages/ForgotPassword" },
  Home: { path: "./pages/Home" },
  MovieMedia: { path: "./pages/MovieMedia" },
  AnalyticsDashboard: { path: "" },
  MovieHistory: { path: "" },
  PersonMessage: { path: "./pages/Message" },
  Settings: { path: "./pages/Settings" },
  LogOut: { path: "" },

  NotFound: { path: "./pages/404" }, // 404
  ServerError: { path: "./pages/500" }, // 500
  Exceptions: { path: "./pages/Exceptions" },

  // Analytics
  BestRating: { path: "./data/BestRating" },
  MovieTrending: { path: "./data/MovieTrending" },
  AnalyticsNotifications: { path: "./data/AnalyticsNotifications" },

  // Recommendations and Predictions
  ForYourPage: { path: "./data/ForYourPage" },
  YourRecommendations: { path: "./data/YourRecommendations" },
  ChartSelection: { path: "./data/ChartSelections" },
  SentimentAnalysis: { path: "./data/SentimentAnalysis" },

  //Addtional
  ProjectsInfo: { path: "./pages/ProjectsInfo" },
  DataInfo: { path: "./data/DataInfo" },
  StableDate: { path: "./data/DataInfo" }
};
