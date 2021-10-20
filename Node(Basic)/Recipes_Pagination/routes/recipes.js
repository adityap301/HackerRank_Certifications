var recipes = require('../recipes.json');
var router = require('express').Router();

router.get('/', (req, res) => {

  const page = req.query.page || 1;
  const limit = req.query.limit || 3;

  console.log("Page: ", page);
  console.log("Limit: ", limit);

  const selectedRecipes = recipes.slice(3*(page-1), 3*page);
  const limitedRecipes = selectedRecipes.slice(0, limit);
  // selectedRecipes = selectedRecipes.slice(0, limit+1);
  console.log(limitedRecipes);


  res.status(200).send(limitedRecipes);
});

module.exports = router;

