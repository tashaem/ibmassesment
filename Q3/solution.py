SELECT owned_id, owner_name FROM owner UNION COUNT(category_id) WHERE article.owner_id == owner.owner_id