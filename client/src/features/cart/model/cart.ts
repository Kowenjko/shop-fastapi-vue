export interface CartI {
  number: number
}

export interface ResponseCartI {
  items: [
    {
      product_id: number
      name: string
      price: number
      quantity: number
      subtotal: number
      image_url: string
    },
  ]
  total: number
  items_count: number
}

export interface AddToCartI {
  product_id: number
  quantity: number
  cart: CartI
}
