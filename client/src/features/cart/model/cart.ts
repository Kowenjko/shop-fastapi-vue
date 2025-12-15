export interface CartI {
  [productId: number]: number
}

export interface CartItemI {
  product_id: number
  name: string
  price: number
  quantity: number
  subtotal: number
  image_url: string
}

export interface ResponseCartI {
  items: CartItemI[] | []
  total: number
  items_count: number
}

export interface AddToCartI {
  product_id: number
  quantity: number
  cart?: CartI
}
